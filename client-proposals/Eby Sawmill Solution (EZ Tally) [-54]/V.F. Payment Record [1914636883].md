5.6. Payment Record

  


Requirements

Overview: The Payment record is used to track individual payments to Landowners, Loggers, and Vendors.

  


Accessed via: 

  * Payments Due reports
  * Payment Summary reports
  * Links in other records
  * Find Payment (menu option in the General section of the Financial menu; opens a screen that prompts for Payment ID) 



  


Sections and Fields: 

  * Payment section: 
    * Status (auto-set and read-only; 
      * "Open Unpaid" if Check # is blank and there are no newer (based on the sequential payment number) Paid or Unpaid Payment records for the same Type + Tract + Payee; 
      * "Locked Unpaid" if Check # is blank and there are newer (based on the sequential payment number) Paid or Unpaid Payment records for the same Type + Tract + Payee; or
      * "Paid" if Check # is filled)
    * Payment ID (auto-set and read-only; unique identifier; uses a sequential payment number + Payment Type Code + Tract ID (or "X" if not linked to a Tract) + Contact ID; e.g. "00001.3.13.34")
    * Payment Type (required; editable if Status is not Paid (i.e., "Check #" is blank); drop list of the Payment Type record names; initially set to: Landowner Flat, Landowner %, Logger, Vendor)
    * Tract (visible and required if Payment Type = Landowner Flat, Landowner %, or Logger; editable if Payment Status is not Paid (i.e., "Check #" is blank); drop list of all Tracts where Status is not Archived; filters down as you type; Validate that the Tract Type matches the Payment Type)
    * Payee (required; editable if Status is not Paid (i.e., "Check #" is blank); drop list of all active Contacts; filters down as you type; filtered according to Payment Type + Tract (as applicable):)
      * If Payment Type = Landowner Flat, show Landowners for selected Tract and default to the Primary Landowner
      * If Payment Type = Landowner %, show Landowners for selected Tract and default to the Primary Landowner
      * If Payment Type = Logger, show Loggers for the selected Tract; if there is only one, default to that one, otherwise default to blank
      * If Payment Type = Vendor, show all Vendors and default to blank



  


  * Flat Payment Subtype (visible and required if Payment Type = Landowner Flat; editable if Status = "Open Unpaid" or "Locked Unpaid"; for reference only; drop list of the options from the Flat Payment Subtypes list - see "Lists" section of the proposal)
  * Flat Payment Due Date (visible and required if Payment Type = Landowner Flat; date; editable if Status = "Open Unpaid" or "Locked Unpaid"; defaults to the current date)



  


  * Itemization (link; opens the Payment Summary report, filtered to the corresponding Payment ID) 
  * Itemization Snapshot (button; visible if Type = Landowner %, Logger, or Vendor and if Status = Paid; clicking the button opens the Itemization Snapshot child screen (see spec below), displaying a table with a snapshot of calculations as of the time that the Payment was marked Paid; the purpose of this is to provide an explanation of the calculations in the event that numbers change due to tiers being adjusted, etc.) 



  


  * Amount Paid (visible if "Payment Type" = "Landowner %"; read-only macro; with the following details / behaviors: 
    * number; 2 decimals; 
    * displays the following: 
      * if "Payment Status" = "Open Unpaid" or "Locked Unpaid": displays the absolute value of all "Down Payment" amounts included on the Payment (to show the total as a positive amount already paid to the Payee);
      * if "Payment Status" = "Paid": displays the sum of the following, which is the total amount that has been paid to the Landowner for the Payment record, both previously (Down Payment(s)) and on the check for the Payment record itself: 
        * absolute value of all "Down Payment" amounts included on the Payment (to include them as positive amounts to the Payee); 
        * "Check Amount") 



  


  * Calculated Amount (number to 2 decimal places; may be negative; see conditional details:
    * If "Payment Type" = "Landowner %": read-only macro; dynamically displays the sum of the following:
      * all "Landowner Amounts" from Yard Tallies included on / linked to this Payment; 
      * all Landowner amounts for each Pulpwood Load included on / linked to this Payment: <Landowner Pulpwood Rate on the Tract> * <Pulpwood Tons>; 
      * Down Payment Amount(s) included on / linked to this Payment (Amount * -1 to handle positive or negative amounts entered on the Tract); 
      * Expense Withholding Amount(s) included on / linked to this Payment (Amount * -1 to handle positive or negative amounts entered on the Tract); 
    * If "Payment Type" = "Logger": read-only macro; dynamically displays the sum of the following: 
      * Logger Amounts for Yard Tallies included on / linked to this Payment; 
      * Logger amounts for each Pulpwood Load included on / linked to this Payment: Logger Pulpwood Rate on the Tract * Pulpwood Tons; 
    * If "Payment Type" = "Vendor": read-only macro; dynamically displays the sum of the Total Values for Yard Tallies included on / linked to this Payment) 
  * Flat Payment Amount (visible if "Payment Type" = "Landowner Flat"; editable and required if "Status" = "Open Unpaid" or "Locked Unpaid"; number to 2 decimal places; may be negative) 



  


  * Check # (required if Payment Date or Check Amount is filled - see validation note below; number field; wide enough to show 6 digits; when filed, auto-fills Check Amount to the Calculated Amount or Flat Payment Amount (as applicable) and auto-fills Payment Date to the current date)
  * Check Amount (required if Check # or Payment Date is filled - see validation note below; number to 2 decimal places; red message displays beside this field if it does not match the Calculated Amount / Flat Payment Amount: "Check Amount does not match <the Calculated Amount / the Flat Payment Amount>. Review itemization and update Check Amount as needed.", auto-fills as mentioned in Check # spec) 



  


  * Notes (optional; plain text)



  


  * Payment Date (required if Check # or Check Amount is filled - see validation note below; auto-fills as mentioned in Check # spec; editable; cannot be set to a future date - error on Save validation message: "Payment Date cannot be set to a future date.") 



  


  * Email Payment Summary (link; visible if Payment Type = Landowner % or Logger; opens a new tab to send the Payment Summary email for the corresponding Payment, with the appropriate fields defaulted; see details in the corresponding section of the proposal)
  * Payment Summary PDF (link; opens the Payment Summary PDF for the Payment)



  


  


  * Itemization Snapshot child screen (includes: 
    * Memo; read-only; displays a table with the following (for a visual, see the sample table at the bottom of this section): 
      * Columns: 
        * Explanation (displays a brief explanation of what the row includes) 
        * Type (displays the source of the item: Yard Tally, Pulpwood Load, Down Payment, or Expense Withholding)
          * Includes a total row at the bottom in bold: "Total" (to designate the total row for the Amount column) 
        * ID (displays the ID of the item:)
          * For Yard Tally or Pulpwood Load, this displays the record ID; 
          * For Down Payment, this displays the DP Date; 
          * For Expense Withholding, this displays the EW Date) 
        * Amount (number to 2 decimals; displays the dollar amount for the item:) 
          * For "Landowner - Yard Tally": <Yard Tally Landowner Amount>
          * For "Landowner - Pulpwood Load": <Pulpwood Load Landowner Amount>
          * For "Landowner Down Payment": -<Down Payment Amount> (note that this displays as negative, since income is being counted against it) 
          * For "Landowner Expense Withholding": -<Expense Withholding Amount> (note that this displays as negative, since income is being counted against it)
          * For "Logger Tally": <Yard Tally Logger Amount>
          * For "Logger - Pulpwood Load": <Pulpwood Load Logger Amount>
          * For "Vendor Yard Tally": <Yard Tally Vendor Amount>
          * This column includes a total row at the bottom in bold: <Sum of Amounts>
        * Details (displays a text version/explanation of the calculations for the amount:
          * For "Landowner - Yard Tally": includes the following: 
            * <1st Tier Log Value macro label>: $<1st Tier Log Value macro value> x <1st Tier Landowner Share macro label> = $<1st Tier Landowner Share macro value>
            * <2nd Tier Log Value macro label>: $<2nd Tier Log Value macro value> x <2nd Tier Landowner Share macro label> = $<2nd Tier Landowner Share macro value>
            * <3rd Tier Log Value macro label>: $<3rd Tier Log Value macro value> x <3rd Tier Landowner Share macro label> = $<3rd Tier Landowner Share macro value>
            * <4th Tier Log Value macro label>: $<4th Tier Log Value macro value> x <4th Tier Landowner Share macro label> = $<4th Tier Landowner Share macro value>
            * <5th Tier Log Value macro label>: $<5th Tier Log Value macro value> x <5th Tier Landowner Share macro label> = $<5th Tier Landowner Share macro value>
            * Total Net Board Feet: <Total Net Board Feet macro value>
          * For "Landowner - Pulpwood Load": <Tons> tons * $<Landowner Pulpwood Rate>
          * For "Landowner Down Payment": N/A
          * For "Landowner Expense Withholding": N/A
          * For "Logger Tally": includes the following: 
            * Total Gross Board Feet: <Yard Tally Total Gross Board Feet> 
            * Logger Rate: $<Logger Timber Rate> 
          * For "Logger - Pulpwood Load": <Tons> tons * $<Logger Pulpwood Rate>
          * For "Vendor Yard Tally": Total Net Board Feet: <Yard Tally Total Net Board Feet>
      * Other Notes: 
        * One row for each individual item included on the Payment. 
        * The memo will be populated (and the Itemization Snapshot button displayed) when Check # is first entered. 
        * Changes to Check # will not refresh the snapshot immediately, as it is cleared on Save if Check # is blanked out and the record is saved. 
    * "Close" button, to close the child screen



  


  


Additional Validation(s): 

  * Validation error on Save if any but not all of the following are specified: Check #, Check Amount, Payment Date: ""Check #, Check Amount, and Payment Date are all required for processed payments."



  


Data Access:

  * View, edit, and delete: Users with the View and Edit Financials permission



  


Special Considerations:

  * Copy Record: Disallow copying 
  * Delete Record: Prevent deletion if Status = Paid: "This record cannot be deleted because the Status is Paid."
    * Note that a user can clear the Check # field to revert the status, then delete. 
    * Note that if a user deletes an unpaid Payment, the Solution automatically unlinks / removes the Payment ID from all places it is referenced (i.e. Yard Tallies, Pulpwood Loads, & Tracts), and the newly unlinked records will be linked to another Payment record the next time the "Create and Link All Payments" background process is run (or the next time the "Create and Link Single Payment" background process is run, if run with matching parameters).
  * Merge Record: Disallow merging 



  


Other Notes:

  * Summary of what can be included on the various Types: 
    * Landowner Flat: None (amount is always manually set) 
    * Landowner %: Any or all of the following: 
      * One or more Yard Tallies (Landowner Amount) 
      * One or more Pulpwood Loads (Landowner amount)
      * One or more Down Payment line items 
      * One or more Expense Withholding line items 
    * Logger: Any or all of the following: 
      * One or more Yard Tallies (Logger Amount)  
      * One or more Pulpwood Loads (Logger amount) 
    * Vendor: 
      * One or more Yard Tallies (Vendor Amount) 
  * Manually linking / unlinking: 
    * For auto-linking: Always auto-link to the "Open Unpaid" Payment (never auto-link to a "Paid" or "Locked Unpaid" Payment); this means that items will always be linked to the newest / most recently-created Payment record. Note that this applies to all items that are linked to Payments: Yard Tallies, Pulpwood Loads, Down Payments, and Expense Withholding items. 
    * For manual linking: Yard Tallies and Pulpwood Loads can be linked manually to either "Open Unpaid" or "Locked Unpaid" Payments. 
  * For Landowner Flat payments, the date-based and harvest-based payments would be handled with the Due Date. Date-based payments can be set up in advance for a certain amount, and a reminder will alert the admin when they come due. Harvest-based payments can be set up when the forester alerts the admin that a payment is due.
  * Note that if a Landowner or a Logger is due payment for more than one Tract, those will be handled on separate Payment records (one Payment record per Payee per Tract).
  * Payment Amount on reports will be an expression that displays the "Check Amount" for Paid payments and either "Calculated Amount" or "Flat Payment Amount" for unpaid payments.  
  * Note that this record should have a name, date, and time stamp for Created and Last Modified.
  * Visual example of the Itemization Snapshot table: 

Explanation| Type| ID| Amount| Details  
---|---|---|---|---  
Landowner - Yard TallyDetails show the tally summary from yard tally.| Yard Tally (Landowner %)| <Yard Tally ID> | <Yard Tally Landowner Amount>| 

  * <1st Tier Log Value macro label>: $<1st Tier Log Value macro value> x <1st Tier Landowner Share macro label> = $<1st Tier Landowner Share macro value>
  * <2nd Tier Log Value macro label>: $<2nd Tier Log Value macro value> x <2nd Tier Landowner Share macro label> = $<2nd Tier Landowner Share macro value>
  * <3rd Tier Log Value macro label>: $<3rd Tier Log Value macro value> x <3rd Tier Landowner Share macro label> = $<3rd Tier Landowner Share macro value>
  * Total Net Board Feet: <Total Net Board Feet macro value>

  
Landowner - Pulpwood Load| Pulpwood Load|  <Pulpwood Load ID>| <Pulpwood Load Landowner Amount>| <Tons> tons * $<Landowner Pulpwood Rate>  
Landowner Down Payment| Down Payment| <DP Date>| -<Down Payment Amount>|   
  
Landowner Expense Withholding| Expense Withholding| <EW Date>| -<Expense Withholding Amount>|   
  
Logger Tally| Yard Tally (Logger)| <Yard Tally ID>| <Yard Tally Logger Amount>| 

  * Total Gross Board Feet: <Yard Tally Total Gross Board Feet> 
  * Logger Rate: $<Logger Timber Rate> 

  
Logger - Pulpwood Load| Pulpwood Load| <Pulpwood Load ID>| <Pulpwood Load Logger Amount>| <Tons> tons * $<Logger Pulpwood Rate>  
Vendor Tally| Yard Tally (Vendor)| <Yard Tally ID> | <Yard Tally Vendor Amount>| Total Net Board Feet: <Yard Tally Total Net Board Feet>  
  
| Total|   
| <Sum of Amounts>|   
  
  
  


  


Development Specification

Change Requests: 

  * Tim Reitz 08/19/2024: [[[IN10016](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10018&)]] - ZET - Tract Record - Adding More Tiers 
  * Tim Reitz 10/07/2024: [[[IN10236](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10238&)]] - ZET - Rework Payment Linking
  * Tim Reitz 10/04/2025: [[[IN11651](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11653&)]] - ZET - Landowner % Payments - Add Down Payment Info
  * 


  


  


  


Mockup: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=2067530284](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=2067530284)

  


[ ] Disallow merging payments

  


Assigning the Payment ID:

  * Use the following format: Autonumber Payment ID + "." \+ Type ID + "." \+ Tract ID + "." \+ Contact ID
    * e.g. 00001.0.13.34
  * We are adding a Type ID and Tract ID so that we don't rely on list numbers. We already have Payment ID and Contact ID.



  


  * Notes:
    * Add a system switch for MaxPaymentID
    * Store the payment number in a PaymentIDNum hidden field.
    * Add a field change expression to payments to update MaxPaymentID based on the first part of the ID
    * Assume that Tract and Contact will only use user-owned list numbers (i.e. use ListString(Contacts, -Value("13")))
    * Add a macro that creates a new ID, using MaxPaymentID+1 for the first number.
    * Use "X" for Tract ID if there is no Tract associated with the payment (i.e. if Payment Type = Vendor).



  


Note: No validation needed against duplicate check #'s

  


Find Payment: menu option in the General section of the Financial menu; opens the ask prompt page for the Payments report, with Search by Payment ID checkbox checked so as to only prompt for Payment ID. 

  


  


  


BID - CCI

[ ] Basic Screen -- 4 HOUR

[ ] Add payment ID (set on save)    4 HOURS

[ ] Add auto-incrementing payment number

[ ] Format the payment ID as shown above

[ ] Clear payment ID and ID Num On Copy

[ ] Filtering on tract (requires an ActiveTracts.ndx with list numbers for active tracts) -- 1 HOUR

[ ] Filtering contacts (4 different ways)  \-- 4 HOURS

[ ] Tying in Niccolas's pricing formulas

BID: 2 Days

  


BID -- NICCOLAS -- 8 HOURS

[ ] Formulas to calculate Landowner % payment Amount

[ ] Formulas to calculate Logger

[ ] Formulas to calculate Vendor

  


Total: 3 Days
