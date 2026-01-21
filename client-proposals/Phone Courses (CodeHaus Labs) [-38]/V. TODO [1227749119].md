5\. TODO

[https://www.twilio.com/blog/2013/10/test-your-webhooks-locally-with-ngrok.html](https://www.twilio.com/blog/2013/10/test-your-webhooks-locally-with-ngrok.html)

[ ] Fix TODO references in subsets, etc

Directory:

[ ] Validate against duplicate codes and courses on a directory.

[ ] Validate email onn signup and account

[ ] Validate that active courses have entries

[ ] Validate that inactive courses aren't referenced in directories

[ ] Validate against selecting inactive courses through the menu

[ ] Make sure we handle Free courses 

Directory type show vs course Timestamp on intro for offset Time zone and rg of dates and times Hmac uploader to public s3 Internal downloader starting at offset Out of band calls - give an option to get callback at the scheduled time

• The next call will be on Monday, 1pm Mountain Time. • Add a field for colloquial time zone name

Tests

• Phone directory without...???

Test design:

Open to send directions by FAX

frame# = ms * framerate / 1000 byte# = frame# * ch * samplewidth

bytespersecond = channels * samplewidth * framerate length_ms = 1000 * bytes / bps

Could do scheduling software where you record yourself a message, then have it call back at a date and time with the reminder

Welcome to the CodeHaus Training library.

To get started, what is the best way to send you course materials? 1. For email, press 1. 2. For fax, press 2 3. For customer support, press 3. 4. To request course materials, press 4. ->>> then, they enter the code < ==> Enter your fax number --- sends the fax >>> Please enter the 6-digit code from the fax you just received

Your fax number has been confirmed..

When they start the course, send the course materials immediately.

Need to 

  * -> will take them back to 
  * for account options
  * For a course directory, press 1


  * To add an email address, press 1
  * To add a fax number, press 2
  * For customer support, press 3



Send the course materials one time....

To access your

Here is an example for Tim.

The ONLY way we will use SES is on user-initiated actions.

  * To sign up, they will email SES at "subscribe@_______" (or something similar), which will automatically generate a code and email them back.
  * All other emails will be sent when they a) the first time they start listening to a new "course" on their phone, and b) when they specifically request course materials to be sent to them
  * I expect them to get an SES email once a month, at the most.
  * These emails will be stored in a database.
  * Each outbound email will include unsubscribe instructions to email "unsubscribe@_______". (This is because our target market do not have Internet access, but they do have email. When we receive an email from this address, we will deactivate this email in the inbox. EXAMPLE WORDING: To unsubscribe, please send any email to [unsubscribe@codehaus.academy](mailto:unsubscribe@codehaus.academy). If you can no longer send emails from this account, please email [support@codehaus.com](mailto:support@codehaus.com) with the email you would like to unsubscribe.
  * The email record will have multiple flags for:



unsubscribed

temporary bounce

permanent bounce

complaint

  * Each of these will be flagged on the email record. Emails will be considered inactive/unusable if any of these flags are set. The temporary bounce will allow a manual override to clear it. All of these flags will be cleared when receiving a new request. (Of course, these flags may be immediately set if the response bounces, etc.)



We will also monitor emails to the automated email addresses to check for user requests.

For example, in response to the subscribe:

Subject: Your CodeHaus.Academy Account Body: Thank you for setting up your email for your CodeHaus.Academy account.

To activate your email, call (PHONE), select (MENU OPTION), and enter the following code: 123-456

If you have any questions, please reach us at [support@codehaus.com](mailto:support@codehaus.com) or call us at (719) 888-2424.

Thank you!

(UNSUBSCRIBE FOOTER)

....and then...

Subject: CodeHaus.Academy course materials Body: Thank you for taking the (COURSE NAME)!

You can find the course materials attached to this email as a PDF.

To listen to this course, please call (PHONE), select (MENU OPTION).

If you have any questions, please reach us at [support@codehaus.com](mailto:support@codehaus.com) or call us at (719) 888-2424

Thank you!

(UNSUBSCRIBE FOOTER)

We don't have an active app or website, because we will be advertising this in print media. Our company website is codehaus.com, and my LinkedIn profile is matthiasmiller.com

What else would be helpful to know about this?
