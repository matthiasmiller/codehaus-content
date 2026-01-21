6\. Quickbooks reports

  


Requirements

The system will allow access to a set of Quickbooks reports. These reports will be updated every night.

  


Initially, the following reports will be supported:

  * Yearly P&L Short Form
  * Weekly P&L Detail
  * Monthly P&L Short Form
  * Monthly P&L Short Form Comparison
  * Yearly P&L Short Form Comparison



  


More reports can be added at a later point. Adding new reports will need to involve AppHosting.zone.

  


USER SPECIFICATION

Because the Quickbooks files are maintained on an accountant's computer, the software will include a program that runs overnight daily. It will extract the specified reports out of Quickbooks, and save them where they can be retrieved by fax. Each company file will need to be configured in the software, along with the destination location in the phone menu.

  


The report extract will connect to Quickbooks, retrieve the data in XML format, then convert the XML to HTML and then to PDF. This will happen on the server, so that formats can be updated without the need to install a new version of the software on the accountant's computer.

  


This program will require that Quickbooks be closed overnight. We will need to work with the accountant to ensure that this happens consistently. If Quickbooks is not closed, the software will not be able to extract the reports that night. The program will provide the accountant with an interface to manually run the reports in cases where the scheduled nightly run failed or other unexpected cases.

  


In case of failure, administrators will be notified via fax or email. The list of people notified can be configured as desired. This will be done with a server-side process that looks for all Quickbooks reports, and makes sure that they have been updated in the expected time interval. If any have not, it will send out notifications. The notifications will include a list of reports that have not been updated.

  


When any of these reports are accessed via the phone menu or fax cover sheet, the software will automatically recognize the user based on Caller ID and select report corresponding to that user's company.

  


Development Specification

Py2exe daemon running on accountant's computer. Kicked off with Windows scheduled task. Generates the reports, then uploads to the server.

  


Report names:

  * ProfitAndLossStandard
  * ProfitAndLossPrevYearComparison



  


Report parameters:

  * Report type (summary vs detail)
  * Date range type
  * Target location (document ID)



  


We'll need to specify these settings in a config file. That allows the program to avoid needing access to the database itself, only to the wsgi that uploads the documents.

  


Does the uploader send up XML that we convert server-side, or the PDF? I think that we send up XML, so that we can tweak formatting without needing to get the accountant to install a new version of the uploader.

  


Config.ini to hold username/password. Account unique to accountant.

  


What about an updater mechanism?

  


This requires an entrypoint that takes the XML, turns it into HTML, then uses weasyprint (or something like it) to turn it from HTML into PDF.

  


[http://weasyprint.org/](http://weasyprint.org/)

  


20 hours?
