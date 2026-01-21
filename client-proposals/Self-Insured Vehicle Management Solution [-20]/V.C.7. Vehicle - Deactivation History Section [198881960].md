5.3.7. Vehicle - Deactivation History Section

  


Requirements

*Done. 

  


  * Deactivation History section:
    * "The following client(s) have invoices and/or fees and/or refunds that need to be resolved before client deactivation: <Client 1 Name>, <Client 2 Name>, <Client 3 Name>." (on-screen message in red text and warning on Save; visible if any client Contact on the embedded spreadsheet meets all of the following conditions:
      * there is a row for the client in the Deactivation History embedded spreadsheet with a "Client Deactivation Reason" set and 
      * the client does not have any active Vehicles and 
      * one or more of the following are true for the client's Contact record: 
        * there are unpaid Invoiced invoices
        * there are any Draft invoices 
        * there are uninvoiced Vehicle fees 
        * there are uninvoiced Vehicle Refunds 
        * there are uninvoiced past HRD fees 



  


  * Vehicle Deactivation (no label; embedded spreadsheet with the following; visible if there are any rows on it; a row is automatically added whenever the last active coverage for a Vehicle is deactivated:
    * Columns:
      * Date (auto-set and read-only; date; required; defaults to the current date)
      * Owner (auto-set and read-only; required; defaults to the "Owner" for whom the Vehicle is being deactivated)
      * Vehicle Deactivation Reason (required; drop list of "Vehicle Deactivation Reasons" list items)
      * Vehicle Deactivation Reason (Other) (plain text; editable and required for both admins and agents if "Vehicle Deactivation Reason" = "Other (must specify)")
      * Client Deactivation Reason (drop list of active "Client Deactivation Reason" records; with the following details / behaviors: 
        * editable when deactivating the client's last active Vehicle or for Admin users if not blank; 
        * required when deactivating or transferring the client's last active Vehicle or for Admin users if not blank; 
        * when set, the following field(s) are affected: 
          * "Client Deactivation Reason (Other)": clears; 
        * error on change if cleared: "An existing client deactivation reason cannot be blank.")
      * Client Deactivation Reason (Other) (plain text; with the following details / behaviors: 
        * editable and required for both admins and agents if the selected "Client Deactivation Reason" has the "Requires Clarification" field checked)
    * Automatically sorted by: Date
    * Buttons to add and delete rows: "+" / "-" 
      * These buttons are visible only for Admin users) 
    * Visibility / Editability Notes:
      * Admins can always edit all editable fields on the rows.
      * "Owner's Agent" can edit the editable fields until the record is saved for the first time after the row is added.
      * Agents can never edit already-saved rows.
    * Other Notes: 
      * N/A)



  


Development Specification

TODO_CCI: Tim Reitz 08/15/2025: Could you review this section's spec and see if it looks correct? And could you provide specifics on which Agents can edit the rows before Save (I'm not sure if it's only "Owner's Agent", or if there are any other conditions)? Thanks!

Sagar Sagar 12/11/2025: Yes the spec looks correct. We need to update a little more. There is one hidden field. I am trying to write it.

  * Deactivation Agent Can Edit Row (hidden field, defines the editability of the row, initially false, when we are adding a row in the deactivation history RG, we make it true, edit the row and save the record, and after saving, the row becomes non-editable again)



  


 And that is owner's agent you are talking about. Before saving the record, the owner's agent can add the deactivation reason and client deactivation reason (when applicable). 

  


Let me know if you have questions regarding this.

  


  


Change Requests:

  * Tim Reitz 08/23/2025: [[[IN9912](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9914&)]] - ZWA - Pre-ZWW - Contact & Vehicle Records - Additional Validation for Client Deactivation
  * Tim Reitz 08/23/2025: [[[IN11799](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11801&)]] - ZWA - Deactivation History RG Client Deactivation Reason False Requirement


