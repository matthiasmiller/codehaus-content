5.3.6. Vehicle - Fees and Credits Section

  


Requirements

*Done. 

  


  * Fees and Credits section:
    * This vehicle is now inactive. Only Admins can make changes to Fees & Credits. (visible if Vehicle "Status" = "Inactive"; on-screen message in gray font) 



  


  * Fees and Credits (unlabeled embedded spreadsheet with the following:
    * Columns:
      * Client Name (required; drop list of active Client-type Contacts; with the following additional behaviors: 
        * defaults to the current "Owner" for the Vehicle;
        * editability: Admin only (in addition to the main "Row Editability" spec below))
      * Fee Date (required; date; with the following additional behaviors: 
        * defaults to the current date;
        * editability: Admin only (in addition to the main "Row Editability" spec below))
      * Coverage Type (required; drop list of "Coverage Types" list items; with the following additional behaviors: 
        * defaults to blank;
        * when set, the following other field(s) are affected:
          * "Fee Type" for the row: is cleared if previously set to a non-blank selection;
        * editability: Admin only (in addition to the main "Row Editability" spec below))
      * Fee Type (required; drop list of "Entry" (conditionally visible, see details) / "Premium"; with the following additional behaviors: 
        * defaults to blank;
        * clears if "Coverage Type" is cleared;
        * includes the following visibility conditions for the "Entry" option:
          * if "Coverage Type" = "Collision": "Entry" is included if Solution uses Collision Entry Fee;
          * if "Coverage Type" = "Cargo": "Entry" is included if Solution uses Cargo Entry Fee; 
        * editability: per the main "Row Editability" spec below)
      * Agent (required; drop list of active "In-State Agent"-type Contacts; with the following additional behaviors:
        * defaults to the current Agent of the current "Owner" for the Vehicle;
        * when set, the following other field(s) are affected:
          * "Fund" for the row: sets to the Fund for this Agent;  
        * editability: Admin only (in addition to the main "Row Editability" spec below))
      * Fund (required; drop list of active Funds; with the following additional behaviors: 
        * defaults to the Fund of the selected "Agent" for the row;
        * editability: Admin only (in addition to the main "Row Editability" spec below))
      * Invoice (read-only macro; when the row is invoiced, displays the corresponding "Invoice #")
      * Amount (required; number; 2 decimals; with the following additional details / behaviors: 
        * when this is manually changed to 0.00 from a non-blank value, the following field(s) are affected on change:
          * Billing Action: sets to "Dismiss"; 
        * when this is manually changed to a non-zero value, the following field(s) are affected on change:
          * Billing Action: sets to "Invoice"; 
        * editability: per the main "Row Editability" spec below)
      * Billing Action (with the following details / behaviors: 
        * drop list of "Invoice" / "Dismiss" (from the "Credit Options" simple list);
        * required; 
        * defaults to "Invoice";
        * if "Amount" is manually edited to 0.00 from another value, this auto-updates to "Dismiss", and if "Amount" is manually edited to a non-zero value, this auto-updates to "Invoice" \- see spec on "Amount" field; 
        * if "Billing Action" = "Invoice", the row will be included on an Invoice the next time an invoicing process is run that includes that client + vehicle combination; 
        * if "Billing Action" = "Dismiss", the row is disregarded by all invoicing processes and by the "Uninvoiced Fees & Credits" total on the Contact record (like the existing behavior for Credit rows set to "Dismiss"); 
        * if "Billing Action" = "Credit", the row is read-only for all users; note that this is not an active use case in the Solution, but is retained for historical items; 
        * editability:
          * interactively on the Vehicle screen: per the main "Row Editability" spec below;
          * via import: editable regardless of the status of the Invoice (this is to allow it to be set to "Dismiss" if the corresponding Invoice itemization row is deleted while the Invoice Status = "Draft" and then the Invoice Status is changed before the Invoice is saved);
        * is set to "Dismiss" via the "Dismiss Vehicle Rows From Deleted Invoice Rows" automatic process; if the Vehicle record is in Edit Mode when this happens, any unsaved changes will be lost and the user must refresh the page to continue working)
      * Status (auto-set and read-only; displays the current status of the linked Invoice)
      * View (link to open the Invoice; displays as "Link")
      * Start Date (required; date; with the following additional behaviors: 
        * defaults: 
          * defaults to the "Activation Date" or "Deactivation Date" for rows added via coverage activation / deactivation (see specs for "Activate Coverage Actions" and "Deactivate Coverage Actions"); 
          * defaults to blank for manually-added rows;
        * error on the field if changed when "Coverage Type" is blank: "Coverage type must be filled before start date."; 
        * error on the field if changed when "Fee Type" is blank: "Fee type must be filled before start date."; 
        * error on the field if "Fee Type" = "Premium" and "Start Date" is not a valid start date for any prior, current, or future period or the start date of the coverage: "Start date must be the current active coverage start date (<Coverage Start Date>) or upcoming period's start date or in any prior period."; 
        * error on the field if "Fee Type" = "Entry" and "Start Date" is after "Activation Date" for the Coverage Type: "Start date must be the active coverage activation date (<Coverage Start Date>) or in any prior period."; 
        * editability: per the main "Row Editability" spec below)
      * End Date (required and editable if Fee Type is "Premium"; date; with the following additional behaviors: 
        * default: 
          * defaults to the last day (6/30) of the Period Year for the "Start Date"; 
          * defaults to blank for manually-added rows; 
        * error on the field if set when "Start Date" is blank: "Start date must be filled before end date."; 
        * error on the field if "Start Date" and "End Date" are not in the same period: "Start date and end date must be in same period."; 
        * error on Save if "End Date" is prior to "Start Date": "End date cannot be before start date."; 
        * editability: if "Fee Type" = "Premium" (in addition to the main "Row Editability" spec below))
    * Automatically sorted by: Date
    * Buttons to add/remove rows:
      * Insert button: "+" (rows may be added by Admin users or the "Owner's Agent" to Vehicles with any active coverage)
      * Delete button: "-" (rows may be deleted by Admin users from Vehicles with any active coverage, if not linked with an Invoice)
    * Special Formatting: 
      * By default, rows are in black text. 
      * If "Client Name" for a row ≠ current "Owner", "Client Name" is displayed in maroon text and other columns for that row are displayed in gray text.
      * All that are linked to prior Owners are displayed in gray text.
    * Row Editability: 
      * for Admin users: rows are editable if the following criteria are met: 
        * "Invoice" for the row is blank or if "Billing Action" ≠ "Credit"; 
        * Admins can edit inactive vehicles; 
        * Admins can edit fees for all clients;
      * for non-Admin users rows are editable if the following criteria are met: 
        * "Invoice" for the row is blank or if "Billing Action" ≠ "Credit"; and
        * Vehicle "Status" = "Active"; and
        * "Client Name" for the row = a client of the Agent (note that this means that current Agents of prior owners can edit the row if the other criteria are met); 
      * for all other non-Admins: all rows are fully read-only; 
    * Other Notes: 
      * Note that when an Agent change happens for a client, the old agent is not able to edit anything (since the "Client Name" is not for their current client). 



  


  * "Previous owner <Full Name> has a credit/balance of $<positive or negative amount>." (label; visible to Admin users after the Vehicle has been transferred to a new owner, if the Prior Owner has any uninvoiced fees/credit related to the current Vehicle)  
  * Create Invoice (same visibility as the "Previous owner..." message above; located beside the message; button; prompts the user to save the record, then runs the "Create Invoice(s) Automatic Process" automatic process to create the Invoice)



  


  * Coverage History (button; opens a child screen with the "Vehicle Coverage History" embedded spreadsheet - see corresponding spec)



  


Development Specification

Change Requests: 

  * Tim Reitz 08/19/2025: [[[IN11314](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11316&)]] - ZWA Multi-State Feature - Umbrella Incident
  * Tim Reitz 08/26/2025: [[[IN10760](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10762&)]] - ZWA - Pre-ZWW - Processes - Add "Line Item Dismissal" Trigger / Process
  * Tim Reitz 08/26/2025: [[[IN9943](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9945&)]] - ZWA - Vehicle Record - Fees & Credits - Add "Dismiss" Option for Fees



  


  


TODO_: Tim Reitz 08/23/2025: Maroon color for some rows: I'm not sure what the purpose of this is/was. Maybe it was meant to display like this for manually-added rows that don't match the owner? (if yes, then we wouldn't necessarily want it to display in maroon for legitimate historical rows...)

  


TODO_CCI: Tim Reitz 08/04/2025: [Row Editability] What happens if the Agent changes, and the client's current agent is not the same as the one in the Agent column? Can the current agent edit the row? 

Sagar Sagar 12/10/2025: I believe here we updated the editability of the Fees and Credits row. As per this job - "[[[PC0180519](https://clientscope.invtools.com/Detail/View/2?RecordType=Holding&StringID=PC0180519&NumberID=0&State=XPSMmJcy76s& "https://clientscope.invtools.com/Detail/View/2?RecordType=Holding&StringID=PC0180519&NumberID=0&State=XPSMmJcy76s&")]] 

[[[IN11647](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11649&)]] - ZWA - Pre-ZWW - Vehicle Record - Update Record Editability for Non-Admins (T&M)

 agents can edit in row which has his name in Agent column.

  


  


Validation: 

  * Error on save: if Coverage Type is "Liability" and Fee Type is "Entry".



TODO_: Austin Priest 10/22/2024: It is not possible to bring about this validation because Entry fee type is not available if coverage type is liability and if the fee type is entry and you change the coverage type to liability the fee type clears. 

TODO_CCI: Tim Reitz 08/23/2025: Is this validation present in the code? If yes, do you see any problem with removing it? (I would add it to a CR).

Sagar Sagar 12/10/2025: Yes this is still present. I do not think we will ever be able to see this unless we import any vehicle with this discrepancy.
