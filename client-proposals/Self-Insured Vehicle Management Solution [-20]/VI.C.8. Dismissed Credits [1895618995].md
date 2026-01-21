6.3.8. Dismissed Credits

  


Requirements

*Done. 

  


Overview: This is a custom report of dismissed Vehicle fees (specifically, all items from the Vehicle "Fees and Credits" embedded spreadsheets with "Billing Action" = "Dismiss").

  


Accessed from: Admin | Exception Reports | Dismissed Credits (opens a prompt screen with the filters)

  


Title: "Dismissed Credits"

  


Preface: N/A

  


Columns: 

  * Date
  * Client Name
  * Vehicle Name (link to the Vehicle record)
  * Amount (total rows display sum)



  


Row-Specific Buttons: N/A

  


Grouped by: Agent (displayed as "<Agent Name>")

  


Sorted by: Fee Date (latest at the top)

  


Filters: 

  * Start Date (date; defaults to blank = all)
  * End Date (date; defaults to the current date)



  


Buttons: N/A

  


Menu Visibility: Admin

  


Other Notes:

  * N/A



  


Development Specification

TODO_VA: (priority CR): TODO_CR: Tim Reitz 08/27/2025: I think we want to make some changes to reflect the fact that this includes all (positive, negative, and zero-dollar) items: 

[ ] Change this report name / title to "Dismissed Fees & Refunds" or something like that

[ ] Change the "Amount" column from "Abs( VehicleFeesInvoiceAmount)" to "VehicleFeesInvoiceAmount", so that it shows negative amounts (or have separate columns for postive (fee) and negative (refund/credit) items)

[ ] If we do separate columns for Amount, maybe also include a new column for "Type" that displays Fee/Refund/Credit
