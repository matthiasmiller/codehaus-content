5.2.6. Contact - Client Details Section

  


Requirements

*Done. 

  


  * Client Details section (custom section; visible if the Selected "Contact Type" for the Contact has "Client?" set to "Yes"; fields editable by Admin users only):
    * Member Policy # (visible based on the "Contact Policy Number" System Switch evaluating to a non-blank value; auto-set and read-only; displays the member-specific Policy # in the format as described in the "Policy #" section of the proposal / living spec)
    * Entry Date (read-only macro; date; displays the date that the Contact record was created)
    * Status (read-only macro; with the following details / behaviors:
      *  displays "Client Status" list items, based on the following logic:
        * "Inactive": if "Inactive As Of" date is not blank;
        * "Snoozed": if "Snoozed Until" date is not blank;
        * "Active": if both "Inactive As Of" and "Snoozed Until" dates are blank)
    * Snoozed Until (visible if "Inactive As Of" is blank; checkbox and date, which toggle; date is required if the checkbox is checked; with the following validations:
      * error on the field if the "Snoozed Until" checkbox is checked and the client has one or more uninvoiced fees or credits: "This client has uninvoiced fees or credits and therefore cannot be snoozed.";
      * error on Save if the "Snoozed Until" checkbox is checked and the client has one or more active Vehicles: "This contact cannot be snoozed because there are one or more associated active vehicles.";
      * error on Save if the "Snoozed Until" checkbox is checked and the client has one or more unpaid invoices: "This client has unpaid invoices and therefore cannot be snoozed."; 
      * warning on Save if the "Snoozed Until" checkbox is checked and the "Snoozed Until" date is in the past: "This client is snoozed with a past-due snoozed until date. ")



  


  * Deactivation Reason (visible if "Inactive As Of" is not blank; read-only macro; displays the latest deactivation reason for the client (from Vehicle records))
  * Update Reason (link visible if "Deactivation Reason" is not blank; link; prompts the user to save the record before opening, then opens the most recently-deactivated Vehicle for the client) 
  * Inactive As Of (checkbox and date, which toggle; with the following validations:
    * error on the field if the "Inactive as Of" date is in the future: "Inactive as of date cannot be a future date.";
    * error on the field if the "Inactive as Of" checkbox is checked and the client has one or more uninvoiced fees or credits: "This client has uninvoiced fees or credits and therefore cannot be deactivated.";
    * error on Save if the "Inactive as Of" checkbox is checked and the client has one or more active Vehicles: "This client has one or more active vehicles and therefore cannot be deactivated.";
    * error on Save if the "Inactive as Of" checkbox is checked and the client has one or more unpaid Invoices: "This client has unpaid invoices and therefore cannot be deactivated.";
    * error  on Save if the "Inactive as Of" checkbox is checked after having been saved as not checked and the selected "Contact Type" is inactive: "This contact cannot be activated because the selected Contact Type is inactive.";
    * error on Save if the "Inactive as Of" checkbox is checked and the "Contact Type = "Agent" and the Agent has one or more active clients: "This agent cannot be deactivated because there are one or more associated active clients."; 
    * error on Save if "Inactive as Of" checkbox is checked and the client has one or more Invoices with "Status" = "Draft": "This client has one or more draft invoices and therefore cannot be deactivated.";
    * error on Save if the client's "Inactive as Of" date is before the date of their last Vehicle's deactivation: "The client cannot be deactivated before the date of their last vehicle's deactivation.";
    * error on Save if the "Inactive as Of" checkbox is checked and the client is a Primary Contact for an active client organization: "This individual is the Primary Contact of an active client organization and therefore cannot be deactivated.";
    * warning on Save if the "Inactive as Of" checkbox is checked and the client is a "Checkbook Holder" for an active Fund: "You are about to deactivate the contact record of this In-State Agent who is the checkbook holder for the following Fund: <Fund Name>. Deactivate the Fund after making this change.") 



  


  * Client's Agent (required; drop-list of active "In-State Agent"-type Contacts with a specified Fund; with the following details / behaviors: 
    * warning on Save if the selected "Agent" is not active or does not have any Fund: "Client's agent is either not active or does not have any fund."; 
    * error on on the field if changed and the client has one or more uninvoiced fees or credits: "This client has one or more uninvoiced fees or credits and therefore the Agent cannot be changed."; 
    * error on on the field if and the client has one or more unpaid Invoices: "This client has one or more unpaid invoices and therefore the Agent cannot be changed."; 
    * error on the field if changed and the client has one or more Invoices with Status" = "Draft": "This client has one or more draft invoices and therefore the Agent cannot be changed."
  * Client's Agent Fund (read-only macro; displays the current Agent's "Agent Fund")
  * Prior Agent & Date Changed (read-only macro; displays the client's prior Agent (if applicable) and the date on which the Agent was changed to the current Agent)
  * Print Agent Change Notice (visible for Admin users for 24 hours after the Agent has been changed; link; generates the "Agent Change Notice" printout - see corresponding spec)



  


  * Print New Member Card (checkbox; visible if the "New Member Card" memo field in Silverloom Settings is not blank; warning on Save if "Status" = "Active" and the "Print New Member Card" checkbox is not checked: "Print new member card has not been checked for this contact.")
  * Print Card (report link; visible if "Print New Member Card" is checked and it has been less than 24 hours since the card was printed; prompts the user to save the record before opening)
  * Printed On (date; visible if "Print New Member Card" is checked and it has been more than 24 hours since the card was printed)



  


  * View <#> Client Claim(s) (visible if there are any Claim records with "Client" = the current Contact; with the following details / behaviors: 
    * visible to the "Client's Agent" user, the "Checkbook Holder" user for the Agent's current Fund, and all Admin users; 
    * link; 
    * "#" displays the number of corresponding Claims; 
    * prompts the user to save the current record, then opens the "Claims for Client" report for the current Contact - see corresponding spec)



  


Development Specification

Change Requests: 

  * Tim Reitz 08/19/2025: [[[IN11314](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11316&)]] - ZWA Multi-State Feature - Umbrella Incident
  * Tim Reitz 08/23/2025: [[[IN9912](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9914&)]] - ZWA - Pre-ZWW - Contact & Vehicle Records - Additional Validation for Client Deactivation
  * Tim Reitz 08/23/2025: [[[IN11239](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11241&)]] - ZWA - Pre-ZWW - Contact - Client Details Section - Clean up Validations
  * Tim Reitz 08/26/2025: [[[IN10683](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10685&)]] - ZWA - Pre-ZWW - Contact Record - Add Invoice-Related Validations for Changing a Client's Agent
  * 


  


  


TODO_CR: Tim Reitz 08/25/2025: I feel like we could improve the "Print New Member Card" feature (it seems unnecessary to have to wait 24 hours for the Printed On date to appear, etc. 

  


TODO_CCI: Tim Reitz 08/25/2025: Question about "Entry Date" (ContactEntryDate): The description for this macro says "Imported contact entry date", but I'm thinking that it applies to records created in the system (not imported) as well. Is that correct? Would it be good to update the macro description to something like "Contact record creation date", or something similar?

Sagar Sagar 12/10/2025: Yes you are correct. This applies for both of type records. Yes I think we can consider to change the description so that it stays out of confusion. One correction is that, its a field, not macro. I have highlighted in your comment.
