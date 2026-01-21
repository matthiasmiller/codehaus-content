4.1. Customer Referrals Report

  


Requirements

This is a report on Sales Orders showing all referred customers, corresponding sale dates, and referring parties. This report would be used to see all referrals and to print referral letters (either in batches or individually).

  


This would be accessed from:

  * The Financial menu
  * The Customer Referrals Letter Notification (monthly alert) 
  * The Referring Party's contact record 



  


Title: Customer Referrals Report

  


Columns: 

  * Referred Customer
  * Referring Party
  * Sales Order (link to record)
  * Sale Date
  * Referral Letter Print Date
  * Referral Payment Amount (with totals) 



  


Grouped by: Unprinted / Printed (items with a Referral Letter Printed date at the bottom; items with no Referral Letter Printed date at the top), then by Standard Referrals / Dealer Referrals (Standard on top, Dealer on bottom) 

  


Sorted by: Sale Date (most recent at the top), then Referred Customer

  


Filters: 

  * Referred Customer (list of all Customer type contacts; filters down as you type)
  * Referring Party (list of all Contacts; filters down as you type)



  


Buttons: 

  * Prepare Documents
  * Print Referral Letters (prompt for date, defaulting to today)
    * Generates a PDF file with letters on separate pages for each Sales Order that has no Referral Letter Printed date and that has a non-Dealer Referring Party; opens or downloads the PDF based on your browser settings
    * Note that these letters can be printed for all Referring Parties or for just one Referring Party, depending on which version of the report is opened.
  * Print Dealer Reports (prompt for date, defaulting to today)
    * The PDF contains reports on separate pages for each Dealer that is a Referring Party on at least one Sales Order that has no Referral Letter Printed date; the printed report reflects the Customer Referrals Report
    * Opens or downloads the PDF based on your browser settings



  


Data Access: 

  * Visible only for Full Admins and Secretary



  


Other Notes: N/A

  


*Done.

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=829387963](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=829387963)

  


TODO_CCI: Ellis, could you confirm that we can do the Print Dealer Reports feature OK? Matthias is thinking an Excel merge that gets generated as a PDF.

  


TODO_CCI: Use a shared macro to control visibility in all these places.
