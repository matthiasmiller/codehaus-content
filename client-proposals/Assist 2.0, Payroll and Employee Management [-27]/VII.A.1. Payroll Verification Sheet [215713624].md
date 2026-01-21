7.1.1. Payroll Verification Sheet

  


Requirements

The Owner Payroll Verification Report will include a verification sheet that can be faxed back to confirm that the payroll numbers are correct. If no corrections are needed, the production manager can fax back the verification sheet to confirm.

  


This page can include a checklist of items the builder must check, verify, and initial. This will be configurable list that Burkholder Management can manage.

  


If corrections are required, the requested changes will be sent back to Burkholder Management. Burkholder Management can either send an updated report, or simply approve the payroll after making the changes.

  


Development Specification

Nate Kilcrease 01/15/2021: Is this a company-specific checklist? What would this look like?

Matthias Miller 01/22/2021: This is the setting in "Payroll Report Verification Checklist". Nothing more to do, besides that.

  


NOTE: The current model for verification reports are like this:

  * Here's a special transmission with a template export to run. Stick these boxes on the page. When they fax it back in, run this x30.



  


When the verification is submitted, we would add an entry to a hidden RG on the company indicating which items were verified. We would warn against (but still allow) changing time cards or building times after the payroll was verified.

  


The profitability report can be generated via a special transmission using the x30. To send the email to the accountant, we will either enhance the special transmission to allow sending , or set up a trigger that runs whenever verification is complete.

  


Use AppHosting.zone settings for the Production & Payroll Verification Checklist
