# https://rtopro.com/help/automate-daily-management-repo.htm

# Automate Daily Management Report

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** »No topics above this level« 

# Automate Daily Management Report

# 

|  [](welcome_welcome_1.md "Parent Chapter")  
---|---  
  
You can automate the Daily Management Report by command line. The report can be emailed as a PDF or HTML attachment. You can automate this report using Windows Task Scheduler. Please note for this to work you have to have your outgoing email service setup in RTO Pro.

Below are the command line options

Example command line

c:\RTOwin\rtowin.exe -automate 1,pdf,sales@rtopro.com,test@rtopro.com

Definitions

1 = store number, required for Central Server, for non Central Server this can be passed as 0 or any number, for non Central Server this value is ignored, but there must be a value passed.

pdf = attach as a PDF file, "html" can also be used in this spot.

sales@rtopro.com,test@rtopro.com = these are the email address(es) to email the report to. It can be 1 email address or multiple.

For example to send the report as an HTML file to only 1 email address the command line is below

c:\RTOwin\rtowin.exe -automate 1,html,sales@rtopro.com
