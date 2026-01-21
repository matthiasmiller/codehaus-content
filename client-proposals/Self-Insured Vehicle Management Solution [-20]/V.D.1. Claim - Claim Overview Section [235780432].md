5.4.1. Claim - Claim Overview Section

  


Requirements

  * Claim Overview section:
    * Client (required; with the following details / behaviors:
      * for Admin users: drop list of all (active, snoozed, and inactive) Clients; always editable;
      * for non-Admin users: drop list of active non-snoozed Clients; only editable on new records (i.e. if the record has not yet been saved for the first time); 
      * when set, the following field(s) are affected: 
        * "Vehicle": clears if previously set; 
        * "Driver": sets to the Client; 
        * "Originating Agent": sets to the Client's current Agent; 
        * "Originating Fund": sets to the "Agent Fund" of the Client's current Agent)
    * Internal Claim ID (__



TODO_VA: Tim Reitz 12/24/2025: This is the hidden numeric field used in the "Claim ID". Sequential auto-number. 

  * Claim ID (auto-set and read-only; unique identifier for the record; with the following details / behaviors:
    * set at the first Save of the record, and does not change if "Client" is subsequently changed; 
    * set based on the "Client ID" for the "Client" and the numeric ID of the Claim, in the following format: "<Client ID> \- "Numeric Claim ID>")



TODO_CCI1: Tim Reitz 09/15/2025: Does the ID change when a Claim is transferred to a new household member Contact (via the "Transfer Fee & Remove Driver from Contact" x30)? 

Sagar Sagar 12/15/2025: No, this does not happen. The import process only updates the Client, Driver fields.

  


  * Vehicle (required; with the following details / behaviors: 
    * for Admin users: drop list of active Vehicles for the selected Client; always editable;
    * for non-Admin users: drop list of active Vehicles for the selected Client; editable only on new records (i.e. if the record has not yet been saved); 
    * when the record is not in Edit Mode, displays as a link to the corresponding Vehicle record)
  * View (visible in Edit Mode; link to open the Vehicle record)
  * Year (read-only macro; displays the "Year" from the selected Vehicle record)
  * Make (read-only macro; displays the "Make" from the selected Vehicle record)
  * Model (read-only macro; displays the "Model" from the selected Vehicle record)
  * VIN / Serial # (read-only macro; displays the "VIN" or "Serial #" from the selected Vehicle record)
  * License Plate # (read-only macro; displays the "License Plate" from the selected Vehicle record)



  


  * Originating Owner (auto-set and read-only; list field for Contacts; with the following details / behaviors: 
    * visible if the Claim has been transferred to a new Client (via the "Transfer all high-risk driver fees and claims for <Name>" button on a new Contact record created from a Household Driver for an existing Client), and if the new "Client" on the Claim is not the same as the Owner of the Vehicle at the time that the Claim was created; 
    * sets to the name of the Owner of the Vehicle at the time that the Claim was created) 
  * Orig. Owner Agent (conditionally visible; read-only macro; dynamically displays the current Agent for the "Originating Owner") 



  


  * Driver (required; editable if "Client" is not blank; drop list of "Household Drivers" for the Client (which includes the Client themselves) and an option for "(Other/Non-household Driver)") 
  * "Stored Claim Driver ID": __;



TODO_CCI1: Tim Reitz 08/22/2025: You mentioned this one in the x30 spec recently. Could you give a brief summary of this field? 

Sagar Sagar 12/15/2025: 

  * Stored Claim Driver ID (hidden, stored ID field for household driver, when we update claim or driver or vehicle, we update stored driver ID)



  


  * "Stored Claim Driver Name": __; 



TODO_CCI1: Tim Reitz 08/22/2025: You mentioned this one in the x30 spec recently. Could you give a brief summary of this field? 

Sagar Sagar 12/15/2025: 

  * Stored Claim Driver Name (hidden, stored name field for household driver, when we update claim or vehicle, we update stored driver name)



  


  * Name (visible and required if "Driver" = "(Other/Non-household Driver)"; plain text)
  * Driver DOB (macro; with the following details / behaviors: 
    * if "Driver" = "Client": read-only; displays the "Date of Birth" from the Client's Contact record; 
    * if "Driver" = a Household Driver: read-only; displays the "Date of Birth" for the selected Household Driver, from the Client's Contact record; 
    * if "Driver" = "(Other/Non-household Driver)": editable; warning on Save if blank) 



  


  * Current Agent (read-only macro; displays the current Agent for the selected Client) 
  * Originating Agent (drop list of active "In-State Agent"-type Contacts with Funds; with the following details / behaviors: 
    * when "Client" is set, auto-sets and does not change unless manually edited or unless "Client" is changed; 
    * for Admin users: editable if "Client" is not blank; 
    * for non-Admin users: read-only) 
  * Originating Fund (drop-list of active Funds; with the following details / behaviors: 
    * when "Client" is set, auto-sets and does not change unless manually edited or unless "Client" is changed; 
    * for Admin users: editable if "Client" is not blank; 
    * for non-Admin users: read-only) 



  


  * Coverage (label for the following three read-only checkboxes)  
  * Liability (read-only macro; checkbox; displays as checked if the Vehicle currently has active Liability coverage) 
  * <Alternate text for Collision - Short label> (read-only macro; checkbox; displays as checked if the Vehicle currently has active <Collision> coverage)
  * Cargo (read-only macro; checkbox; displays as checked if the Vehicle currently has active Cargo coverage)



  


Development Specification

TODO_: Tim Reitz 08/15/2025: Should the vehicle details be stored fields instead of macros? Esp. License Plate, as that would normally change when a Vehicle is transferred (or could go away when a vehicle is sold/deactivated). 

  


TODO_: Tim Reitz 08/15/2025: For the "Coverage" checkbox macros: Let's consider changing these to be stored fields that set when "Vehicle" is set. It doesn't seem like it's very helpful to display the current coverage situation of the vehicle (i.e. if the vehicle has been sold or deactivated, etc.). 

  


TODO_CCI: Tim Reitz 08/15/2025: Minor question about the "Driver DOB" macro: When "Driver" = "Client", does this macro display the Date of Birth from the detail screen, or from the Household Drivers RG? 

Sagar Sagar 12/13/2025: When Driver = Client, it shows client's DOB, otherwise Household Driver's DOB from the RG.

  


TODO_CCI: Tim Reitz 08/15/2025: Is there a hidden field that is set by the "Driver DOB" macro when it is editable? 

Sagar Sagar 12/13/2025: Yes, with the same label. When you select "Other/Non-household Driver" in Driver field, then it becomes visible. Either the macro is visible for client or household driver, or the field is visible for unsaved other driver.

  


TODO_CCI: Tim Reitz 08/15/2025: What is the conditional visibility for "Orig. Owner Agent"? Thanks! 

Sagar Sagar 12/13/2025: If there is no Originating Owner or Originating Owner and Client are not same.

  


  


Change Requests: 

  * [[[IN5695](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-5697&)]] - ZWA - Changes to Claim IDs \-- simplified ID
  * Tim Reitz 09/30/2024: [[[IN10221](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10223&)]] - ZWA - Claims - Clarify Claim Client vs. Originating Owner & Corresponding Agents


