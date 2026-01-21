5.2. Contact Record

  


Requirements

Overview: The solution will use the standard AppHosting Contact records, which can be set to the specified Contact Types. 

  


Accessed via: The Contacts report 

  


Sections and Fields: The EZ Tally contact record will include standard AppHosting Contact fields, including name, address, phone number, and email, and it also will include some customizations. Note that all of the fields on the contact record for the EZ Tally should be the same as the standard contact record, with the exception of the following: 

  


  * "Customized for EZ Tally" section: This is a custom section that is visible for all contacts in the EZ Tally Solution, and will contain the following custom fields/links:



  


If Contact Type = Customer: 

  * View Bookings (link; opens the Bookings report with the Customer filter set to Contact Name; visible for users with the View Export Tallies and Bookings permission)
  * View Export Tallies by Booking (link; opens a screen with a prompt for Booking (drop list of Bookings for the Customer), which then opens the Export Tallies report with the Customer and Booking set accordingly; visible for users with the View Export Tallies and Bookings permission)



  


If Contact Type = Forester:

  * View Tracts (link; opens the All Tracts report with the Forester filter set to Contact Name; visible only for users with the Viiew All Yard Tallies and Tracts permission)



  


  


  *   Show Flat Payments Due

  *   Show Flat Payments Summary

  *   Show % Payments Due

  *   Show % Payments Summary

  


If Contact Type = Landowner: 

  * View Tracts (link; opens the All Tracts report with the Landowner filter set to Contact Name; visible only for users with the Edit and Delete Tracts permission)
  * View Yard Tallies (link; opens the Yard Tally report with the Landowner filter set to Contact Name; visible for users with the View Tracts, Yard Tallies, and Pulpwood Loads permission)
  * View Flat Payments Due (visible if the Contact is listed as a Landowner for one or more Flat-type Tracts; link; opens the Landowner Flat Payments Due Report, filtered to the corresponding Contact; visible for users with the View and Edit Financials permission)
  * View % Payments Due (visible if the Contact is listed as a Landowner for one or more Adjustable Tiered Percentages-type Tracts; link; opens the Landowner % Payments Due Report, filtered to the corresponding Contact; visible for users with the View and Edit Financials permission)
  * View Flat Payments Summary (visible if the Contact is listed as a Landowner for one or more Flat-type Tracts; link; opens the Landowner Flat Payments Summary Report, filtered to the corresponding Contact; visible for users with the View and Edit Financials permission)
  * View % Payments Summary (visible if the Contact is listed as a Landowner for one or more Adjustable Tiered Percentages-type Tracts; link; opens the Landowner % Payments Summary Report, filtered to the corresponding Contact; visible for users with the View and Edit Financials permission)



  


If Contact Type = Logger: 

  * View Yard Tallies (link; opens the Yard Tally report with the Logger filter set to Contact Name; visible for users with the View Tracts, Yard Tallies, and Pulpwood Loads permission)
  * View Logger Payments Due (link to the Logger Payments Due Report with the Payee filter set to Contact Name; visible for users with the View and Edit Financials permission)
  * View Logger Payments Summary (ink to the Logger Payments Summary Report with the Payee filter set to Contact Name; visible for users with the View and Edit Financials permission)



  


If Contact Type = Vendor:

  * View Yard Tallies (link; opens the Yard Tally report with the Vendor filter set to Contact Name; visible for users with the View Tracts, Yard Tallies, and Pulpwood Loads permission)
  * View Vendor Payments Due (link to the Vendor Payments Due Report with the Payee filter set to Contact Name; visible for users with the View and Edit Financials permission)
  * View Vendor Payments Summary (link to the Vendor Payments Summary Report with the Payee filter set to Contact Name; visible for users with the View and Edit Financials permission)



  


  * "AppHosting Settings" section: This is a standard section that is visible only if Contact Type = Employee, and contains the following standard field(s): 
    * User ID (drop list of User IDs)



  


  


Data Access: 

  * View and edit for all users
  * Delete only by users with the Delete Contact Records permission



  


Other Notes: 

  * Since the EZ Tally Solution is not using the Incidents or Invoices modules, those standard sections will be hidden on the Contact records.
  * Note that this record should have a name, date, and time stamp for Created and Last Modified.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1529895558](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1529895558)

  


Ellis Miller 12/14/2022: 

  


BID: 4 hours

[ ] Add report links with permissioning visibility

[ ] Override config macro for deleting: "A contact can be set as not active, but only administrators can delete a contact."
