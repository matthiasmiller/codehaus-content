6.9.2.1. Agreement - Agreement Details Section

  * Agreement Details section: 
    * Status (required; drop list of Agreement Statuses; defaults to Pending for new records; error on save if Status = Inactive and there are any Active linked Devices: "Agreement cannot be made Inactive because there is one or more active linked Devices. Deactivate or remove the Device(s) or change the Agreement Status."; see the following details:)
      * Pending: Used during setup, etc.; Agreements with this Status are not included in the invoicing process or page count requests, etc.; if an Agreement has this Status for more than a week, the "Agreements Pending for Over 1 Week" notification is set - see details in the corresponding section of the proposal.
      * Active: Used for active, ongoing Agreements.
      * Inactive: Used for Agreements that have been ended by Think Ink or the customer; to set and Agreement to this Status, all linked devices must be deactivated / unlinked, but unpaid invoices are allowed to continue.
    * Agreement ID (hidden; auto-number; unique identifier for the Agreement, since the Agreement Name is not always unique)



TODO_EM: Tim Reitz 08/03/2023: The client would like the Agreement to have a number that is visible to the customer. Number + decimal that advances with each revision. It's fine to only do one revision per day. 

Idea: change the Agreement ID to be visible and handle this (or continue to hide the base ID and display the ID + Revision #): 

  * Agreement ID (auto-number; starts at 0001 and counts up; unique identifier for the Agreement, since the Agreement Name is not always unique) 
  * separate field for revision number: 2 digits, starting at 00, gets combined with the Agreement ID for visible places.



  


  * Agreement Name (auto-set and read-only; displays the selected Customer's name and the first line of the selected Location Address, in the following format "<CustomerName> \- <StreetAddress>"; automatically updates if the corresponding fields are changed) 



  


  * Customer (required; drop list of all Customer-type contacts; after the initial save, this can only be edited by Admins; warn on Save if changed: "You are about to change the Customer. Are you sure you want to continue?")



  


  * New Customer (Phase 4; to be included once the Solution includes the Accounting module and is no longer syncing with Classic Accounting; link; visible if no Customer is selected; opens a new blank Customer-type Contact record)
  * View/Edit Customer (visible if a Customer is selected; link to open the selected Customer record)



  


  * Billing Group Nickname (required; plain text field; used for reference purposes; validate against duplicates for the same Customer - error message on Save: "This Billing Group Nickname is already being used for this Customer."; no validation against duplicates across Customers) 
  * Agreement Sales Rep (required; drop list of Employee contacts; defaults to the current user for new records; note that this is not linked to the Sales Rep on the Region or the Customer record)



  


  * Agreement Creation Date (date; required; tracks the original start date of the Agreement; default to the current date when the record is created; does not update when the Agreement is revised; warning on Save if changed: "You are about to change the Agreement Creation Date (previously <MM/DD/YYYY>).")



TODO_JM: Tim Reitz 09/12/2023: Do you want this as a separate field? If not, we have the "Created" info at the bottom of the screen that we can always look at.

  * Effective Start Date (date; auto-set and read-only; tracks the start date of the initial version and subsequen renewals; sets to the Agreement Creation Date date when the record is created, then sets to the actual date when the Agreement is renewed; does not update when the Agreement is revised with non-renewal revisions)



TODO_JM:Tim Reitz 09/19/2023: Do you want 2 or 3 date fields? 

  * 3: 
    * Agreement Creation Date 
    * Effective Start Date (tracks renewals) 
    * Current Revision Date (tracks all revisions)
  * 2: 
    * Agreement Creation Date 
    * Current Revision Date (tracks all revisions)



  


  * Current Revision Date (date; auto-set and read-only; updates each time a revision is applied to the Agreement; see the Agreement Revisions notes for more details)



  


  * Current Revision Date (date; auto-set and read-only; tracks the date that the most recent revision was made to the Agreement or one of its linked Devices; defaults to blank when the Agreement record is created and cannot equal the Agreement Creation Date; is updated to the current date when a revision is made; see the Agreement Revisions notes for more details) 
  * ??Current Revision Number (



TODO_IDD: Tim Reitz 09/12/2023: If needed (see Agreement ID)

  * ??Revision Reasons (auto-set and read-only; comma-separated list of the Revision Reasons for the most recent revision) 



TODO_EM: Tim Reitz 10/03/2023: Thoughts on doing this? (We're doing the same type of thing for the Needs Review checkbox on the Device). This would make it easy for a user to see at a glance a summary of what has changed (and to be able to pass it along to the Customer).

  


  * Agreement Length ____ Months (____



TODO_JM: how should this work?

  * Agreement Renewal Due Date (auto-set and read-only; calculated from the Effective Start Date and the number of months in Agreement Length; Agreements are included in the Agreements Needing Renewal alert & report when this date is in the past or within the next two months)



TODO_JM: Tim Reitz 09/12/2023: Do you want the renewals to always happen at the end / beginning of a month? If so, how should handle situations where they actually are renewed late (part way into the following month)?

  * Months Remaining (auto-calculated and read-only; months between the current date and the Agreement Renewal Due Date; rounds to the nearest 1 decimal place; displays as a negative number in red text if the Agreement Renewal Due Date is in the past)
    * Note: use the following formula: "NumDays / 365.25 * 12" (rounded to 1 decimal place at the end). This takes leap year into account, and prevents skew for a 1-year contract. 



  


  * Renew Agreement (button; runs the Renew Agreement background process - see details in the corresponding section of the proposal)



TODO_IDD: Tim Reitz 09/12/2023: review / finish and move to the Background Processes section:

Renew Agreement background process:

  * Schedule: 
    * When the "Renew Agreement" button on the Agreement record is clicked. 
  * Actions: 
    * TODO_IDD: Ben Reitz 10/03/2023: Make sure that the dates, including the Renewal Due Date, are handled correctly
    * Runs the Agreement Revision background process
    * Send the Updated Agreement Notice Email to the Customer



  


Agreement Revision background process:

  * Schedule:
    * On Save whenever a change constituting a revision has been made to an Agreement record or a linked Device record. 
  * Actions:
    * Set the Current Revision Date to the current date if not already set to the current date
    * Set the Current Revision Number to the next sequential digit if it has not already been updated on the current date (this prevents multiple separate revision numbers on the same date)



TODO_IDD: Ben Reitz 10/03/2023: Remove from here if we remove it from the detail screen.

  * Save the record (other details will update automatically)
  * TODO_JM: Ben Reitz 10/03/2023: Should it generate an invoice right away or will it be picked up on the next regular invoice? (Phase 4 item)
  * A database trigger kicks off the PDF generation and saves the new PDF in the Shared folder (one sub-folder for each Agreement)



TODO_EM: Tim Reitz 09/19/2023: What spec do we need for this?

  * Sends the Updated Agreement Notice Email



TODO_JM: Ben Reitz 09/19/2023: Do you want any kind of email to go to the customer or to the sales rep when this happens? Our current spec for this email says that it is manually sent. Do you prefer to have it go out manually or automatically?

  


  * Agreement End Date (required if Status = Inactive; defaults to the current date when the Status is set to Inactive)



TODO_JM: how to cancel / end an Agreement? (probably a button that runs a background process to make sure all devices are inactive / removed, sets the End Date, and generates a final invoice / gives the option to generate it)

TODO_EM: Ben Reitz 10/03/2023: What would be the approximate price difference for a button with an x30 versus a simple checkbox with validations?

  


  * Agreement Text (read-only memo; contents are pulled from the Manage Service Agreement memo in AppHosting.Zone Settings; this is printed on the Managed Service Agreement printout) 
  * Agreement Special Terms (editable memo; contents of this memo are included in Section B of the Managed Service Agreement printout)
  * Print Agreement (PDF) (link; opens a PDF in a new tab; see the corresponding section in this proposal)
  * Print Agreement (Word) (link; downloads the document; see the corresponding section in this proposal; can be used if manual editing of an agreement is desired -- the final agreement could be uploaded to the Notes memo for documentation)
  * Agreement Folder (link; 



TODO_EM: Ben Reitz 09/19/2023: what spec do we need for this?

  * Internal Notes (memo; used for internal documentation purposes; not included on the printout)
  * Send Renewal Notice Email (button/link; sends the Upcoming Agreement Renewal Notice Email to the customer; see the corresponding section of the proposal)



TODO_JM: Tim Reitz 09/21/2023: Here is a manual link; the email spec says that it's automated - which do you want?

  * Send Updated Agreement Notice Email (button/link; sends the Updated Agreement Notice Email; see the corresponding section of the proposal)


