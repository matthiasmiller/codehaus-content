7.2.10. Contact Record - Invoices Section

  


Requirements

*Done.

  


  * Invoices section (standard; visible on all Contact Types; custom visibility: TBD; note that this would be visible but not used until the Invoices module & Subscription Management feature (Phase 2)): 



  


  * Invoices (standard; no label; read-only embedded spreadsheet showing Invoices for the Contact with "Status" ≠ "Canceled", with the following:
    * Columns: 
      * Invoice #
      * Date
      * Status
      * Amount
      * View (link to the Invoice record; displays as "Link")
    * Automatically sorted by: 
      * First by: "Status" ("Invoiced" / "Draft" / "Paid") 
      * Second by: "Date" (newest at the top)
    * Buttons to add/remove rows: N/A
    * Shows 4 rows without scrolling)
  * View All Invoices (standard; link; opens the "Invoices for Contact" report for the current Contact) 
  * Create Blank Invoice (standard; link; opens a blank new Invoice record for the current Contact) 
  * Statement (standard; link; opens a prompt screen to generate the standard "Statement" printout)



  


Development Specification

Tim Reitz 10/20/2025: [Phase 2] Consider how visibility should work for this. 

  * Visible only to "All Provider Roles", and have a custom link to an Invoices report in a custom section? 
  * Visible to the linked user and all "Upline Provider Roles" / "All Provider Roles"? Hide the "Create Blank Invoice" link from end users?


