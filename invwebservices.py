import base64
import json
import sys
import time
import urllib

if sys.version_info >= (3,):
    from http.client import HTTPConnection, HTTPSConnection
    from urllib.parse import quote, urlencode, urlparse, urlunparse
else:
    from httplib import HTTPConnection, HTTPSConnection
    from urllib import quote, urlencode
    from urlparse import urlparse, urlunparse

class CommandResponse(object):
    """
        An object that contains the response data from a web service call.
        
        Members:
            messages        An array of messages. May be empty.

            warnings        An array of warnings. May be empty.

            content         The response data from the command.
                            Will be None if the command doesn't return data.

            content_type    The MIME type of the command response data.
                            Will be None if the command doesn't return data.

            filename        The proposed file name for the command response data.
                            Will be None if the command doesn't return data.
                            For reports this will be the report's output file name.

            command_desc    A description of the command that was run.
                            Useful for log messages.
                            Example: GET http://host/services/v2/report.r20?Format=Text
    """
    def __init__(self, messages, warnings, output, output_content_type,
                 output_filename, command_desc):
        self.messages = messages
        self.warnings = warnings
        self.content = output
        self.content_type = output_content_type
        self.filename = output_filename
        self.command_desc = command_desc

class CommandError(Exception):
    """
        The exception that will be raised if the web service encounters an error.

        Members:
            errors          A list of errors

            command_desc    A description of the comand that was run.

            response        An instance of CommandResponse. This will be None
                            if the server could not be contacted, or if the response
                            could not be parsed. It is useful for some commands
                            that can return messages and warnings along with a fatal
                            error.

    """

    def __init__(self, errors, command_desc, status_code, response=None):
        self.errors = errors
        self.command_desc = command_desc
        self.status_code = status_code
        self.response = response;
        super(CommandError, self).__init__(str(self))

    def __str__(self):
        return '\n'.join(self.errors)

    def get_verbose_info(self):
        log_info = ['Encountered an error while running %s:' % self.command_desc]
        log_info.extend(['Error: ' + e for e in self.errors])

        if self.response:
            log_info.extend(['Warning: ' + w for w in self.response.warnings])
            log_info.extend(['Message: ' + m for m in self.response.messages])

        return '\n'.join(log_info)


class ServiceUnavailableError(CommandError):
    """ The exception that will be raised if the web service encounters a 503 response
        and either is not configured to retry or has exceeded its retry attempts.
    """
    pass


class Client(object):
    def __init__(self, server, username=None, password=None, ssl_context=None,
                 key_file=None, cert_file=None, retry_on_503=False,
                 impersonate_user=None):
        """
            key_file and cert_file are deprecated. Please use the ssl_context instead.
        """
        self._scheme, self._hostname = urlparse(server, 'http')[:2]
        self._username = username
        self._password = password
        self._ssl_context = ssl_context
        self._key_file = key_file
        self._cert_file = cert_file
        self._retry_on_503 = retry_on_503
        self._impersonate_user = impersonate_user

    def get(self, command, definition=None, options=None):
         return self._call('GET', command, definition, options, None)
        
    def post(self, command, definition=None, options=None, post_data=None):
         return self._call('POST', command, definition, options, post_data)

    def _call(self, method, command, definition, options, post_data):
        url_path = '/Services/v2/%s/' % command
        if definition:
            definition = definition.replace('\\', '/')
            definition = definition.replace('MainDir::/', '')
            definition = definition.lstrip('/')
            url_path += quote(definition)

        query_parms = dict(options or {})
        query_parms['MessageFormat'] = 'JSON'

        for key, value in query_parms.items():
            if value is None:
                query_parms[key] = ''

        retry_intervals = [15, 30, 60, 120, 300, 600, 15 * 60, 15 * 60]
        while True:

            if self._scheme == 'https':
                options = {
                    'context': self._ssl_context,
                    'key_file': self._key_file,
                    'cert_file': self._cert_file
                }
                # Filter out default values. We do this because in older
                # versions of python context isn't a valid parameter.
                options = {k: v for (k, v) in options.items() if v is not None}
                connection = HTTPSConnection(self._hostname, **options)
            else:
                connection = HTTPConnection(self._hostname)

            headers = {}
            if self._username:
                credentials = self._username + ':' + self._password
                auth_value = base64.b64encode(credentials.encode('ascii')).decode('ascii')
                headers['Authorization'] = 'Basic %s' % auth_value

            if self._impersonate_user:
                headers['X-Impersonate-User'] = self._impersonate_user

            query = urlencode(query_parms)

            connection.request(method, '%s?%s' % (url_path, query),
                               body=post_data, headers=headers)
            response = connection.getresponse()

            status = response.status
            raw_data = response.read()

            response.close()

            command_desc = '%s %s' % (method, urlunparse((
                self._scheme,
                self._hostname,
                url_path,
                '',
                query,
                ''
            )))

            if status not in (200, 500, 503):
                raise CommandError(['Unexpected status code: %i' % status],
                                   command_desc, status)

            if status == 503:
                if self._retry_on_503 and retry_intervals:
                    time.sleep(retry_intervals.pop(0))
                    continue

                raise ServiceUnavailableError(['Temporarily Unavailable.'], command_desc, status)

            data = {}
            try:
                data = json.loads(raw_data.decode('ascii'))
            except ValueError:
                raise CommandError(['Could not parse response: %s' % raw_data],
                                   command_desc, status)
            content = data.get('content', None)
            if content and data.get('base64Encoded', False):
                content = base64.b64decode(content)

            ret = CommandResponse(data.get('messages', []),
                                       data.get('warnings', []),
                                       content,
                                       data.get('contentType', None),
                                       data.get('fileName', None),
                                       command_desc)

            # We will never return an error with a 200.
            if status == 500:
                errors = data.get('errors', ['An unknown error occurred.'])
                raise CommandError(errors, command_desc, status, response=ret)

            return ret
