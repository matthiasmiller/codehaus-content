27.3. Delivery Ticket - Auto-Add Freight Rows to Other Line Items

Sean Miller 04/29/2025: Moved to [[[IN11420](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11422&)]] - ZGW - Delivery Ticket - Auto-Add Freight Rows to Other Line Items

  


  


From the Member Financials section of the Delivery Ticket record: We had specced this out to automatically add a row for Freight to the Other Line Items table if the "Include Freight..." checkbox is checked (otherwise the user would manually do calculations and add a row if needed). We're now splitting this out as an optional add-on to help give more opportunities to reduce cost.

  


Estimated Cost: $300-400 to auto-add rows vs. always adding the rows manually 

  


Spec:

  * Include Freight in Member Payment (visible if "Buyer Paying Freight $" ≠ zero; checkbox; with the following special behaviors:  
    * defaults to checked when visible; 
    * if checked, when the "Buyer's PO #" is selected, an editable row is added to the "Other Line Items" embedded spreadsheet with the following auto-set: 
      * Type: "Freight"; 
      * Amount: <Buyer Paying Freight $>; 
      * Date: <current date>; 
      * Description: "Freight from Buyer"; 
    * this includes the "Buyer Paying Freight $" in the "Total Other Line Items $", and therefore also the "Buyer Invoice $"; 
    * if manually unchecked, the row in the table is deleted; 
    * workflow explanations: 
      * If GW is not brokering the freight, this stays checked and the "Buyer Paying Freight $" is included in the "Other Line Items" table, and handled just like (and along with) the lumber funds (no special handling for fees for just the freight);
      * If GW is brokering the freight, this gets manually unchecked, and the "Buyer Paying Freight $" is not included in the "Other Line Items" table. GW would manually handle the calculations outside of the Solution, then add the appropriate value back in as a line item on the "Other Line Items" table, which then adds it back to the Member Payment.)


