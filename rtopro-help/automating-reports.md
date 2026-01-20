# http://www.rtopro.com/help/automating-reports.htm

# Automating Reports

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Automating Reports

|  [](web_invoice___request_for_paym.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](glossary.md "Next Topic")  
---|---  
  
You can automate reports with RTO Pro from a command line. The reports you can automate will be increased over time, currently only the Payment/Transaction report and Customer Listing Report can be automated.

This feature can be used to save report options for easy recall later also without automating the report.

When you automate a report it will save a PDF copy of the report in the path you specify or in your local RTOwin\Reports folder. You can also optionally specify to email a copy of the PDF file.

From the report screen click on the "Report Save Options" menu item at the top left (if you don't see this then the report you have open does not support this feature yet).

![report save options](hmfile_hash_1de93a31.png)

You can load a saved report or save the options for the current report screen you have open.

To automate a report the options are explained below:

Below is an example command line to automate running of a report.

C:\RTOwin\RTO-win.exe -automatereport 8,C:\RTOwin\Reports\,test@gmail.com

The section in red is the path to the RTO Pro exe, edit this as needed for your installation.

The section in green is the command so RTO Pro knows you are wanting to automate a report, this must be passed exactly as shown.

The "8" is the ID of the report to run, this is required, you can see the ID of saved reports on the Saved Report Screen(click load saved report from the menu displayed above).

The "C:\RTOwin\Reports\" is the path you want the PDF of the report saved. This is optional and the file will be saved in the local RTOwin\reports folder if not passed.

The "[test@gmail.com](mailto:test@gmail.com)" is the email you want to email the report to. This is optional, the report does not have to be emailed. You must have your email account set up in RTO Pro for this to work.

Below are a couple more sample command lines

C:\RTOwin\RTO-win.exe -automatereport 10

This will be saved to default folder, not emailed.

C:\RTOwin\RTO-win.exe -automatereport 8,,test@gmail.com

This will be saved to default folder, emailed to test@gmail.com

From the Saved Reports screen you can click on the command line information at the bottom of the screen to have the command line copied to your clipboard, then you can edit it as needed.
