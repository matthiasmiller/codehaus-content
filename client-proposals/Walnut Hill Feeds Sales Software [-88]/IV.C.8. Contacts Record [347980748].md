4.3.8. Contacts Record

  


Requirements

Overview: The Solution includes the standard Silverloom Contacts record. It will have the standard fields, such as address, phone, and more.

  


It will have the following custom fields:

  * Dealer (checkbox; visible and enabled for Customer type)
  * Salesperson (droplist of Salespeople; visible and enabled for Customer type)
  * Commissions; visible and enabled based on user permissions; embedded spreadsheet of:
    * Year (#; sorted descending)
    * Goal (Tons) (number)
  * QuickBooks Contact (read-only; used for linking)
  * NG Customer (read-only; used for linking)



  


This will show links to:

  * Locations
  * Orders
  * Check-Ins



  


It will also show account balance.

  


Development Specification

NOTE: We need to make sure that we link NG Customer, QuickBooks Contact, and Silverloom Contacts. This will take time & thought.
