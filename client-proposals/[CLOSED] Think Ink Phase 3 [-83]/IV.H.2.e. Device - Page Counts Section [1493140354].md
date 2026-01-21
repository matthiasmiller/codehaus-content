4.8.2.5. Device - Page Counts Section

Note that for Phase 3, all page counts are to be collected and entered manually. Support for syncing/imports is to be included in Phase 4.

  


  * Page Counts section (visible if Type is or previously was "Customer Printer" or "Leased Printer" and if the Managed checkbox is or previously was checked)
    * Page Count Collection Type (required; drop list of Manual, Automatic)
    * Last Page Count Reminder (Phase 4; visible if Collection Type = Manual; date; auto-filled and read-only; date of the last Request or Reminder sent for this Device; see the corresponding sections of the proposal for details about Page Count Request and Reminders)
    * Page Counts Notes (memo field; can attach documents)



  


  * Average Black Usage (auto-fill and read-only; average number of black pages per month for this Managed Device; see Other Notes for more details)
  * Average Color Usage (auto-fill and read-only; average number of color pages per month for this Managed Device; see Other Notes for more details)
  * Manual Print Count Instructions (read-only memo; displays the contents of the Print Count Instructions memo on the selected Model) 



  


  * Page Counts (embedded spreadsheet with the following: 
    * Columns: 
      * Customer (auto-set and read-only; sets to the current Customer on the Device)
      * Meter Read Date (required; default to the current date when a row is added; editable even after an invoice has been linked to the row)
      * Source (required; defaults to Manual for Phase 3) 
        * Phase 4: drop list of Page Count Source items; defaults to blank for manually-added rows.
      * Current Black Meter Count (required; number field with no decimals; defaults to blank)
      * Black Pages Used (auto-filled and read-only; calculated from this row's Current Black Meter Count minus the previous row's Current Black Meter Count)
      * Black Pages Overage (auto-set and required; calculated from the Black Pages Used for the current row minus the Included Black Pages for the Device; this can be edited manually to adjust/override how much the customer is billed in a given billing cycle; editable until there is an Invoice linked to the row)
      * Black Overage $ (auto-set and read-only; calculated from the Black Pages Overage for this row times the Black Overage $ for the Device)
      *       * Current Color Meter Count (editable and required if Print Type = Color for the Device's Model; number field with no decimals; defaults to blank)
      * Color Pages Used (auto-filled and read-only; calculated from this row's Current Color Meter Count minus the previous row's Current Color Meter Count) 
      * Color Pages Overage (auto-set and required if Print Type = Color for the Device's Model; calculated from the Color Pages Used for the current row minus the Included Color Pages for the Device; editable until there is an Invoice linked to the row; this can be edited manually to adjust/override how much the customer is billed in a given billing cycle)
      * Color Overage $ (auto-set and read-only; calculated from the Color Pages Overage for this row times the Color Overage $ for the Device)
      * Notes for Invoice (optional plain text field; defaults to blank; editable until there is an Invoice linked to the row; used for documenting any notes to be included in the Invoice line item)
      * Invoice # (Phase 3: optional; plain text field; manually filled with an invoice number)
        * Phase 4: To be auto-set when an invoice is linked to the row
      * Invoice Status (Phase 3: blank)
        * Phase 4: auto-set and read-only; displays the Status of the corresponding Invoice 
      * View (Phase 4; displays "Link" if there is a linked invoice for the fee; opens the corresponding invoice) 
    * Automatically sorted by: Meter Read Date (most recent at top)
    * Buttons to manually add and remove rows ("+" and "-")
      * Warning on Save if a row has been removed: "You have removed one or more rows from the Page Counts table. If you do not wish to continue, refresh the page to cancel changes." 
      * Phase 4: Design to be determined. 
    * Show 10 rows without scrolling
    * Other Notes:
      * If the Customer changes for the Device, rows for previous Customers display in gray. 



  


TODO_IDD: They need to track the initial page count (like if it's a used printer at a new location). Preference between an auto row on the RG when a Customer is set that requires the count fields, or separate fields on the record? I'm thinking auto row, but there would be nuances...

Matthias Miller 05/19/2022: By definition, the first row can never be billed, so....I think we just assume that. And we never bill it out.

TODO_EM: Tim Reitz 08/31/2023: Thoughts on this?

\- Auto include a row on creation that requires the user to set a starting count (normally would be 0 unless a used printer), and have the first row not be billed.

\- Have a separate field to set the starting page count?

  


  


  * Other Notes:
    * For calculating Average Print Counts: 



Matthias Miller 05/10/2022: My proposal:

  * Find latest meter count
  * Find earliest meter count >= 1 year ago
  * Calculate the # of months based on method above
  * Result = NumPages / NumMonths
  * This would be updated when adding a new row. It might be slightly more accurate to do earliest >= a year prior to latest page count, better handling seasonal items. The short question is -- how concerned



_IDD: Review this proposal and make sure we still like it. Also, there's a broken sentence at the end of the comment above. 

Tim Reitz 08/31/2023: Updated:

  * Find the latest Invoiced meter count
  * Find the earliest meter count
  * Calculate the number of months (using TI's standard of 28 days per month), rounded to the nearest whole number
  * Calculate the number of pages per month



TODO_EM: Tim Reitz 08/31/2023: thoughts on this?

TODO_JM: Tim Reitz 08/31/2023: thoughts on this?
