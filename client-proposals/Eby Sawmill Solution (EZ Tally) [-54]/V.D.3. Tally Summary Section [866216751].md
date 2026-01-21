5.4.3. Tally Summary Section

  


Requirements

Tally Summary section:

  * Confirmed (checkbox + date and time + user name; with the following behaviors: 
    * checking the checkbox auto-fills the date/time and username, which are read-only;
    * the Tally can be "unconfirmed" by unchecking the checkbox; note unchecking the checkbox also clears the date/time and username; 
    * to link the Yard Tally with Payment records: 
      * if there is an "Open Unpaid" Payment record for a payee (Logger, Landowner, Vendor): Set on Save after the Confirmed checkbox is checked, setting to the "Open Unpaid" Payment record for the corresponding Type + Tract (when applicable) + Payee. 
      * If there is not an "Open Unpaid" Payment record for a payee: The Payment is created and linked via the "Create and Link All Payments" background process run from the "Create Payment" button here on the Yard Tally or the "Create Missing Payments" button on the Payments Due reports. Note that the "Confirm" button on the Yard App also runs this background process when it is clicked, so this button on the Yard Tally record should almost never be needed.;
    * to unlink the Yard Tally from a Payment record: happens on Save after the "Confirmed" checkbox is unchecked; 
    * cannot be checked if there are no logs entered in the Logs table - error message on the field: "This Yard Tally cannot be confirmed because there are no logs on it."; 
    * checkbox becomes read-only if one or more linked Payment record has a Status of Paid)
  * Print Yard Tally Summary (link; opens the Yard Tally Summary Printout (Vendor or Tract) in a new tab; see printout details in the corresponding section of the proposal)
  * Email Yard Tally Summary (visible if Source = Vendor and Status is Confirmed or Closed; link; opens a new tab to send the Vendor Yard Tally Summary email, with the appropriate fields defaulted; see details in the corresponding section of the proposal; email can be sent via import and by users with the "Edit Open/Confirmed Yard Tallies" permission, even when the Status = Closed)



  


  * Logger Timber Rate (visible for Source = Tract; auto-set and read-only; displays the Logger Timber Rate from the selected Tract for the selected Logger; value is copied in when the Logger is selected on the Yard Tally; this value does not change if edited on the Tract, but does change if the Logger is changed on the Yard Tally; cleared on Save if Source is changed to Vendor) 
  * 1st Tier Board Footage (visible for Source = Tract if the Purchase Type for the Tract = Adjustable Tiered Percentages; label displays the following from the corresponding tier from the Adjustable Tiered Percentages table on the Tract record: "<Min Price> & greater - BF", e.g. "100 & greater - BF"; field shows the total BF for all logs with a Price within the 1st Tier; auto-calculated and read-only; number with no decimal places) 
  * 1st Tier Log Value (visible for Source = Tract if the Purchase Type for the Tract = Adjustable Tiered Percentages; label displays the following from the corresponding tier from the Adjustable Tiered Percentages table on the Tract record: "<Min Price> & greater - $", e.g. "100 & greater - $"; field shows the total of Log Values for all logs with a Price within the 1st tier; auto-calculated and read-only; number to 2 decimal places) 
  * 1st Tier Landowner Share (visible for Source = Tract if the Purchase Type for the Tract = Adjustable Tiered Percentages; label displays corresponding percentage for the tier from the Adjustable Tiered Percentages table on the Tract record, e.g. "60%"; field shows the corresponding % of the 1st Tier Log Value; auto-calculated and read-only; number to 2 decimal places) 
  * 2nd Tier Board Footage (visible for Source = Tract if the Purchase Type for the Tract = Adjustable Tiered Percentages; label displays the following from the corresponding tier from the Adjustable Tiered Percentages table on the Tract record: "<Min Price> to <Max Price> \- BF", e.g. "50 to 99 - BF"; field shows the total BF for all logs with a Price within the 2nd Tier; auto-calculated and read-only; number with no decimal places) 
  * 2nd Tier Log Value (visible for Source = Tract if the Purchase Type for the Tract = Adjustable Tiered Percentages; label displays the following from the corresponding tier from the Adjustable Tiered Percentages table on the Tract record: "<Min Price> to <Max Price> \- $", e.g. "50 to 99 - BF"; field shows the total of Log Values for logs with a Price within the 2nd tier; auto-calculated and read-only; number to 2 decimal places) 
  * 2nd Tier Landowner Share (visible for Source = Tract if the Purchase Type for the Tract = Adjustable Tiered Percentages; label displays corresponding percentage for the tier from the Adjustable Tiered Percentages table on the Tract record, e.g. "40%"; field shows the corresponding % of the 2nd Tier Log Value; auto-calculated and read-only; number to 2 decimal places)
  * 3rd Tier Board Footage (visible for Source = Tract if the Purchase Type for the Tract = Adjustable Tiered Percentages; label displays the following from the corresponding tier from the Adjustable Tiered Percentages table on the Tract record: "<Min Price> to <Max Price> \- $", e.g. "20 to 49 - BF"; field shows the total BF for all logs with a Price within the 3rd Tier; auto-calculated and read-only; number with no decimal places) 
  * 3rd Tier Log Value (visible for Source = Tract if the Purchase Type for the Tract = Adjustable Tiered Percentages; label displays the following from the corresponding tier from the Adjustable Tiered Percentages table on the Tract record: "<Min Price> to <Max Price> \- $", e.g. "20 to 49 - BF"; field shows the total of Log Values for logs with a Price within the 3rd tier; auto-calculated and read-only; number to 2 decimal places) 
  * 3rd Tier Landowner Share (visible for Source = Tract if the Purchase Type for the Tract = Adjustable Tiered Percentages; label displays corresponding percentage for the tier from the Adjustable Tiered Percentages table on the Tract record, e.g. "30%"; field shows the corresponding % of the 3rd Tier Log Value; auto-calculated and read-only; number to 2 decimal places)
  * 4th Tier Board Footage (visible for Source = Tract if the Purchase Type for the Tract = Adjustable Tiered Percentages; label displays the following from the corresponding tier from the Adjustable Tiered Percentages table on the Tract record: "<Min Price> to <Max Price> \- $", e.g. "10 to 19 - BF"; field shows the total BF for all logs with a Price within the 4th Tier; auto-calculated and read-only; number with no decimal places) 
  * 4th Tier Log Value (visible for Source = Tract if the Purchase Type for the Tract = Adjustable Tiered Percentages; label displays the following from the corresponding tier from the Adjustable Tiered Percentages table on the Tract record: "<Min Price> to <Max Price> \- $", e.g. "10 to 19 - BF"; field shows the total of Log Values for logs with a Price within the 4th tier; auto-calculated and read-only; number to 2 decimal places) 
  * 4th Tier Landowner Share (visible for Source = Tract if the Purchase Type for the Tract = Adjustable Tiered Percentages; label displays corresponding percentage for the tier from the Adjustable Tiered Percentages table on the Tract record, e.g. "20%"; field shows the corresponding % of the 4th Tier Log Value; auto-calculated and read-only; number to 2 decimal places)
  * 5th Tier Board Footage (visible for Source = Tract if the Purchase Type for the Tract = Adjustable Tiered Percentages; label displays the following from the corresponding tier from the Adjustable Tiered Percentages table on the Tract record: "<Max Price> & less - BF", e.g. "9 & less - BF"; field shows the total BF for all logs with a Price within the 5th Tier; auto-calculated and read-only; number with no decimal places) 
  * 5th Tier Log Value (visible for Source = Tract if the Purchase Type for the Tract = Adjustable Tiered Percentages; label displays the following from the corresponding tier from the Adjustable Tiered Percentages table on the Tract record: "<Max Price> & less - $", e.g. "9 & less - BF"; field shows the total of Log Values for logs with a Price within the 5th tier; auto-calculated and read-only; number to 2 decimal places) 
  * 5th Tier Landowner Share (visible for Source = Tract if the Purchase Type for the Tract = Adjustable Tiered Percentages; label displays corresponding percentage for the tier from the Adjustable Tiered Percentages table on the Tract record, e.g. "10%"; field shows the corresponding % of the 5th Tier Log Value; auto-calculated and read-only; number to 2 decimal places)



  


  * Total Gross BF (auto-calculated and read-only; number with no decimals; sum of all Gross Board Feet for the Tally) 
  * Total Net BF (auto-calculated and read-only; number with no decimals; sum of all Net Board Feet for the Tally)  
  * Total Value (auto-set and read-only; sum of Log Values for the Tally; number to 2 decimal places)



  


Other Notes: 

  * A log should not count toward the total calculations until it is completely entered (if it is counted as 0 as soon as log entry begins, it skews the calculations until the log is complete).



  


Development Specification

Change Requests: 

  * Austin Priest 10/02/2023: [[[IN8692](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8694&)]] - ZET - Yard Tally Record - Confirmed checkbox becomes read-only when linked Payment is Paid
  * Tim Reitz 08/19/2024: [[[IN10016](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10018&)]] - ZET - Tract Record - Adding More Tiers 
  * Tim Reitz 10/07/2024: [[[IN10236](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10238&)]] - ZET - Rework Payment Linking
  * 


  


  


CCI:

[ ] Confirmed Date/Time/User are non-editable fields set by OnChange statements

[ ] Macros

BID: 1 HOUR

  


NIC:

[ ] YardTallyBoardFeet(vTierNum)

[ ] YardTallyLogValue( vTierNum)

[ ] YardTallyLandownerShare (vTierNum)

[ ] YardTallyGrossBoardFeet

[ ] YardTallyNetBoardFeet

[ ] YardTallyTotalValue

BID: 2 HOURS
