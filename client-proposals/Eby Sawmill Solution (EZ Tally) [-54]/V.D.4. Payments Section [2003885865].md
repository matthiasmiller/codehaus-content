5.4.4. Payments Section

  


Requirements

Payments section (visible only for Administrators; this section is laid out in a table-like format, with a row for each Payment type and a column for each field type):

  


"Rows":

  * Vendor (visible if Source = Vendor)
  * Logger (visible if Source = Tract)  
  * Landowner (visible if Source = Tract and the Purchase Type for the selected Tract = Adjustable Tiered Percentages)



  


"Columns":

  * Amount ($; number to 2 decimal places; auto-calculated and read-only; this is the amount that is added to the Payment record; amount is frozen on the first Save after the Confirmed checkbox is checked to prevent it from being updated if other changes are made on the Tally or in the Solution) 
    * For Vendor: displays the Total Value for the Tally; cleared on Save if Source is changed to Tract. 
    * For Logger: total Gross Board Feet for the Tally / 1000 * Logger Timber Rate on the Yard Tally ($/mbf); cleared on Save if Source is changed to Vendor, if the Payment is not paid. 
    * For Landowner: 1st Tier Landowner Share + 2nd Tier Landowner Share + 3rd Tier Landowner Share + 4th Tier Landowner Share + 5th Tier Landowner Share for this Tally; cleared on Save if Source is changed to Vendor, if the Payment is not paid. 
  * Payment ID (auto-set and read-only; displays as a link to open the corresponding Payment record; with the following behaviors: 
    * if an "Open Unpaid" Payment record exists for theType + Tract (when applicable) + Payee, this is set on Save after the Confirmed checkbox is checked, setting to that "Open Unpaid" Payment record; 
    * cleared on Save after the Confirmed checkbox is unchecked (see details with the Confirmed checkbox spec); 
    * cleared on Save if Source is changed, if the Payment is not paid; 
    * if no "Open Unpaid" Payment exists, set via the "Create Payment" link (see details below); 
    * validate against saving if the Payment ID was previously set and is now blank (to avoid having the item linked back to the same Payment in the event that the Payment is the "Open Unpaid" one) -- error message on Save: "Payment ID cannot be blank since it was previously set. Select a Payment or create & set a new one to continue."; 
    * validate against saving if attempting to link to a Paid Payment - error message on Save: "This item cannot be linked to the selected Payment, as it has been marked as Paid." ) 
  * Select Payment (button; displays as an ellipsis button immediately to the right of the Payment ID; visible in Edit Mode if the Yard Tally Status = Confirmed and (if the item is already linked to a Payment) if the Status of the linked Payment is not "Paid"; opens the "Select Payment Choice Report" as a child screen -- see corresponding spec) 
  * Create Payment (link; visible with the initial Save for new records, in the location of the Payment ID, if there is no "Open Unpaid" Payment record for the same Type + Tract (when applicable) + Payee; clicking this link runs the "Create and Link All Payments" background process to create a new Payment record and link the Yard Tally to it; note that after clicking the button, a manual refresh of the Yard Tally page is needed to allow further editing of the page and to display the new Payment ID)
  * Check # (auto-set and read-only; from the corresponding Payment record; wide enough for 6 digits)
  * Paid (checkbox; auto-set and read-only; from the corresponding Payment record)



Payment Date (auto-set and read-only; from the corresponding Payment record)

  * Payee (auto-set and read-only; displays the Payee for the corresponding Payment record when a Payment is linked; link to open the corresponding Contact's record; cleared on Save if Source is changed)



  


  


Select Payment Choice Report (open as a "child screen"; includes the following): 

  * Displays the following: 
    * The "Select Payment Choice Report" (see corresponding section of the proposal), showing unpaid Payments based on the selected filters and a row for "(none)"; 
    * New Payment (button; opens a new Payment record in a new tab with Payment Type, Payee, and Tract automatically filled, based on the information on the Yard Tally; note that after saving the new Payment, the user will need to return to the Yard Tally or Pulpwood Load record and click the "Refresh" button below to view the new Payment on the selection screen) 
    * "Refresh" button; 
    * "OK" button (links the item to the selected Payment record, or unlink the item if "(none)" is selected) 
    * "Cancel" button
  * Workflow: 
    * User opens the Choice Report. 
    * If the desired Payment record exists, the user selects it and clicks Continue to relink. 
    * If a new Payment record is needed, the user selects the "New Payment" button, goes to the new tab to set up the Payment, then returns to the Choice Report and clicks the "Refresh" button to display and select the new Payment. 
    * If the user wishes to completely unlink the record from any Payments, the user selects the blank line at the top of the Choice Report and clicks Continue to unlink.



  


Development Specification

Change Requests: 

  * Tim Reitz 08/19/2024: [[[IN10016](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10018&)]] - ZET - Tract Record - Adding More Tiers 
  * Tim Reitz 10/07/2024: [[[IN10236](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10238&)]] - ZET - Rework Payment Linking
  * 


  


  


CCI:

[ ] Call Niccolas's macros. 

Option 1: Have four rows. There will be two rows with a Landowner label, one for "Landowner Flat" and one for "Landowner Percent". These are shown conditionally based on whether Tract is Flat or Percent.

Option 2: Have 3 rows, pass in Landowner Flat or Landowner Percent conditionally.

BID: 2 HOUR

  


NIC:

[ ] Macros for YardTallyPaymentAmount( vPaymentType), etc

BID: 2 HOUR
