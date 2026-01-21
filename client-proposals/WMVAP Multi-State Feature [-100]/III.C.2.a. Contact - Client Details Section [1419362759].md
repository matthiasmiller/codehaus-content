3.3.2.1. Contact - Client Details Section

  


Requirements

*Documented. Tim Reitz 08/19/2025

  


Make the following changes (full spec included here, with changes noted with blue and strike-through): 

  


Client Details section (custom section; visible if the Selected Contact Type has "Client?" set to "Yes"; fields editable by Admin users only):

  * Member Policy # (visible based on the "Contact Policy Number" System Switch evaluating to a non-blank value; auto-set and read-only; displays the member-specific Policy # in the format as described in the "Policy #" section of the proposal / living spec)
  * Entry Date (date; auto-set and read-only)
  * Status (auto-set and read-only)



Status options:

  * Inactive - if Inactive As Of date is not blank
  * Snoozed - if Snoozed Until date is not blank
  * Active - if inactive and snoozed dates are blank


  * Snoozed Until (checkbox and date; adding/removing a date checks/unchecks the checkbox; visible if Inactive As Of is blank; date is required if the checkbox is checked)
  * Deactivation Reason (uneditable; displays the latest deactivation reason from the client's vehicles; visible if Inactive As Of is not blank)
  * Update Reason (link to the most recently deactivated vehicle for the client; visible if Deactivation Reason is not blank; prompts the user to save the record before opening)
  * Inactive As Of (checkbox and date; adding/removing a date checks/unchecks the checkbox)
  * Client's Agent (drop-list of active In-State agents with specified fund contacts; required)
  * Client's Agent Fund (auto-set and read-only)
  * Prior Agent & Date Changed (auto-set and read-only)
  * Print Agent Change Notice (PDF link; visible for admin for 24 hours after the agent has been changed)



  


  * Print New Member Card (checkbox; visible if the "New Member Card" memo field in Silverloom Settings is not blank)
  * Print Card (report link; visible if Print New Member Card is checked and it has been less than 24 hours since the card was printed; prompts the user to save the record before opening)
  * Printed On (date; visible if Print New Member Card is checked and it has been more than 24 hours since the card was printed)



  


  * View 1 Client Claim(s) (link to Claims report) (visible to the client's agent, the agent's fund holder, and all admins; visible if there is more than one client claim; prompts the user to save the record before opening)



  


Validations:

  * Snoozing / Snoozed Contacts:
    * Error on change: If the "Snoozed Until" checkbox is checked and the client has one or more uninvoiced fees or credits.
      * Error Message: "This client has uninvoiced fees or credits and therefore it cannot be snoozed."
    * Error on save: If the "Snoozed Until" checkbox is checked and the client has one or more active vehicles.
      * Error Message: "This contact cannot be snoozed because one or more active vehicles are associated with it."
    * Error on save: If the "Snoozed Until" checkbox is checked and the client has one or more unpaid invoices.
      * Error Message: "This client has unpaid invoices and therefore it cannot be snoozed." 
    * Warning on save: If the "Snoozed Until" checkbox is checked and the Snoozed Until date is in the past. 
      * Warning Message: "This client is snoozed with a past-due snoozed until date. (Field: Snoozed Until)"



  


  * Inactivating / Inactive Contacts:
    * Error on change: if the Inactive as Of date is in the future.
      * Error Message: "Inactive as of date cannot be a future date."
    * Error on change: If the "Inactive as Of" checkbox is checked and the client has one or more uninvoiced fees or credits.
      * Error Message: "This client has uninvoiced fees or credits and therefore it cannot be deactivated."
    * Error on save: If the "Inactive as Of" checkbox is checked and the client has one or more active vehicles. 
      * Error Message: "This client has one or more active vehicles and therefore it cannot be deactivated. (Field: ContactInactiveDate)"
    * Error on save: If the "Inactive as Of" checkbox is checked and the client has one or more unpaid invoices.
      * Error Message: "This client has unpaid invoices and therefore it cannot be deactivated. (Field: ContactInactiveDate)"
    * Error on save: If the "Inactive as Of" checkbox is checked  (after having been saved as not checked) and the Contact Type is inactive.
      * Error Message: "This contact cannot be activated because its contact type is inactive. (Field: ContactInactiveDate)"
    * Error on save: If the "Inactive as Of" checkbox is checked, the Contact Type = Agent, and the agent has one or more active clients.
      * Error Message: "This agent cannot be deactivated because one or more active clients are associated with it. (Field: ContactInactiveDate)"
    * Error on save: If the client's Inactive as Of date is before the the date of their last vehicle's deactivation.
      * Error Message: "The client cannot be deactivated before the date of their last vehicle's deactivation. (Field: ContactInactiveDate)"
    * Error on save: If the "Inactive as Of" checkbox is checked and the client is a Primary Contact for an active client organization.
      * Error Message: "This individual is the Primary Contact of an active client organization and therefore cannot be deactivated. (Field: ContactInactiveDate)"
    * Warning on save: If the "Inactive as Of" checkbox is checked and the client is a Checkbook Holder for an active Fund.
      * Warning Message: "You are about to deactivate the contact record of this In-State Agent who is the checkbook holder for the following Fund: <FundName>. Deactivate the Fund after making this change. (Field: ContactInactiveDate)"



  


  * Other:
    * Warning on save: If the client's selected agent is not active or does not have any Fund.
      * Warning Message: "Client's agent is either not active or does not have any fund. (Field: Client's Agent)"
    * Warning on save: If the client is not inactive or snoozed and the "Print New Member Card" checkbox is not checked.
      * Warning Message: "Print new member card has not been checked for this contact. (Field: Print New Member Card)"



  


Development Specification

Ellis Miller 09/05/2024: 

  


2 Hours

[ ] In ZWI, we will want to set the ContactPolicyNumber to something like "SI" \+ PadWithZeros the ContactNum. See Deployment settings for exact format. For testing purposes, you could fill in temporarily into ContactPolicyNumber if the switches job isn't coded yet.

[ ] Only show Member Policy # if this evaluates to non-blank.

[ ] Only show Print New Member Card if memo is blank.

Tim Reitz 05/06/2025: This should be "...if memo is not blank."
