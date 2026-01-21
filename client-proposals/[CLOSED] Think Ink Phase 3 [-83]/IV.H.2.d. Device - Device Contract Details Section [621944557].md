4.8.2.4. Device - Device Contract Details Section

  * Device Contract Details section (visible if the "Managed" checkbox is or previously was checked):
    * Agreement Start Date (auto-set and read-only; displays the date that the Device was added to the Managed Service Agreement; when the Device is linked to an Agreement, this sets to the Effective Start Date on the Agreement if there is no Current Revision Date, otherwise sets to the Current Revision Date; does not update if the Current Revision Date changes on the Agreement) 



  


  * Monthly Service Plan (required; drop list of the Monthly Service Plan options for the selected Model; warning on Save if changed: "The Monthly Service Plan for this Device has been changed.")



  


  * Prepay (visible if Printer = Yes on the Device Model; checkbox; defaults to unchecked; if checked, additional fields become visible and the main Monthly Base Price $ field is hidden; if unchecked, the additional fields are hidden and the main Monthly Base Price $ field is visible)
  * Prepay Monthly Base Price $ (visible and required if the Prepay checkbox is filled; number field to 2 decimals; defaults to the Prepay Discounted Price for the selected Monthly Service Plan; this is the calculated price per month for the prepay contract, used to adjust / calculate the Prepay Annual Price; error on Save if blank: "Prepay Monthly Base Price $ is required.") 
  * Prepay Annual Price $ (visible if the Prepay checkbox is filled; auto-set and read-only; this is the Prepay Monthly Base Price * 12)
  * Prepay Start Date (visible and required if the Prepay checkbox is checked; date field; defaults to the nearest 1/4 month (1st, 8th, 15th, or 22nd) in the future when the Prepay checkbox is checked; ___)
  * Prepay End Date (visible and required if the Prepay checkbox is checked; date field; defaults to ___; warning on Save if changed from one date to another: "The Prepay End Date has been changed, which could result in data discrepancies.") 



DONE_JM: Ben Reitz 09/21/2023: What should this default to?

TODO_IDD:Ben Reitz 09/21/2023: From client: It should always end at the end of a month and start whatever date the agreement starts rounded to .25 months. Start date should round ahead to the closest .25 months to start.

Tim Reitz 10/03/2023: Summary: The Prepay Start Date would be the nearest 1/4 of the month (1st, 8th, 15th, or 22nd) from the current date. It would end (or be renewed) with the linked Agreement. This means that the first "year" of prepay would actually almost never be a full year. Then when the Agreement renews, the Prepay year would also renew, and from there one the Agreement year and the Prepay year would run together.

TODO_EM: Tim Reitz 10/03/2023: See notes below about using an account credit approach instead.

TODO_IDD / TODO_JM: Ben Reitz 09/21/2023: Consider calling this "Prepay Renewal Date" to make it more consistent with the terminology on the Agreement (where the End Date is actually the date that the Agreement was terminated).

  * Create Prepay Invoice (Phase 4; visible if the Prepay checkbox is filled; opens a new Invoice for the Customer with a line item for the Prepay Annual Price or the prepay price until the end date, as applicable) 



TODO_EM: Tim Reitz 09/21/2023: Are you fine with this design for prepay? 

  


DONE_JM:  How does the prepay cycle of 1 year line up with the Managed Service Agreement cycle of 1 year? Should they line up to start and end at the same time, or do we allow a new 1-year prepay plan to start at any point?

TODO_IDD: Ben Reitz 09/21/2023: From client: I think they should end at the same time as all agreements are to be 12 months. The agreement would only restart if there was a big enough change that it would also affect the prepay $ amount.

A question on this: Would it simplify things a lot if we rethought the prepay and would just invoice for the total prepay amount and only apply it to account credit and then apply this to their invoices till it’s used up instead of trying to calculate it all out automatically. Let me know what your thoughts are here.

Tim Reitz 10/03/2023: I could see that simplifying things a bit, but we would also need to build out handling for account credits. We definitely pursue this option if you would like, though I'd probably suggest we defer that to a later stage and take a very simplified approach to the prepay for now (such as handling all prepay pricing outside of the software and simply setting the Monthly price to $0.00 if the "Prepay" checkbox is checked for a printer).

TODO_EM: Tim Reitz 10/03/2023: Thoughts on this?

  


  * Monthly Base Price $ (required; number field to 2 decimals; defaults to the default Monthly Base Price for the selected Monthly Service Plan, or 0.00 if the Prepay checkbox is checked; editable to allow overriding the default if desired; this is the monthly fee for the device; error on Save if blank: "Monthly Base Price $ is required."; Phase 4: this value is included on the monthly invoice)



  


  * Included Black Pages (visible and required if Printer = Yes on the Device Model; number field to 0 decimals; defaults to the default Included Black Pages for the selected Monthly Service Plan; editable to allow overriding the default if desired; this is the included black pages per billing cycle) 
  * Black Overage $ (visible and required if Printer = Yes on the Device Model; number field to 3 decimals; defaults to the default Black Overage $ for the selected Monthly Service Plan; editable to allow overriding the default if desired; this is the price per black page if the customer uses more than the Included quantity) 



  


  * Included Color Pages (visible and required if Printer = Yes on the Device Model and if Print Type = Color on the Device Model; number field to 0 decimals; defaults to the default Included Color Pages for the selected Monthly Service Plan; editable to allow overriding the default if desired; this is the included color pages per billing cycle) 
  * Color Overage $ (visible and required if Printer = Yes on the Device Model and if Print Type = Color on the Device Model; number field to 3 decimals; defaults to the default Color Overage $ for the selected Monthly Service Plan; editable to allow overriding the default if desired; this is the price per color page if the customer uses more than the Included quantity) 



  


  * Base Charge Itemization (for tracking fees; used for invoice itemization; embedded spreadsheet with the following:) 



TODO_IDD: update once we work on Managed Service Agreement details. 

TODO_EM: Tim Reitz 08/10/2023: should this be on the Device or on the Agreement? I'm thinking probably the Agreement, to keep all of the billing there. 

  * Columns: 
    * Fee Date (auto-filled with the date the row is created; editable by admin if Invoice # is still blank)



TODO_IDD: Tim Reitz 08/10/2023: how are we adding the rows? 

TODO_EM: Tim Reitz 08/29/2023: Thoughts on a background process (kicked off either manually, or automatically on X day) that runs and looks for all Devices that need to be billed in this upcoming billing cycle and adds rows to this RG?

  * Billing Cycle (Months) (auto-set and read-only; displays the number of months that corresponds to the selected Base Charge Billing Frequency on the Managed Service Agreement)
  * Amount (auto-filled from the current Monthly Base Price $; editable by admin if Invoice # is blank, in the event that overriding the base charge for a specific month is desired)
  * Invoice # (Phase 3: optional; plain text field; manually filled with an invoice number)
    * Phase 4: To be auto-set when an invoice is linked to the row
  * Invoice Status (Phase 3: blank)
    * Phase 4: auto-set and read-only; displays the Status of the corresponding Invoice 
  * View (Phase 4; displays "Link" if there is a linked invoice for the fee; opens the corresponding invoice) 


  * Automatically sorted by: Fee Date (most recent at top)
  * Buttons to add and remove rows (Phase 3: "+" and "-"; rows cannot be removed if they are linked to an invoice; Phase 4 behavior to be determined)
  * Show 8 rows without scrolling


