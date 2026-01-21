7.2.3. Contact Record - Membership Details Section

  


Requirements

  * Membership Details custom section (visible if Contact Type = Member; visible to the corresponding Member, the Member's Regional Rep, and all Super Admins; editable for the Member's Regional Rep and all Super Admins, with some fields restricted to Super Admin only): 



  


Membership status information:

  * Membership Status (status displays in the section heading; automatic and read-only, based on various fields - see the corresponding section of this proposal)



  


Membership activation:

  * Membership Stage (optional; drop list of Membership Stages)
  * Paid Membership Start (date; includes the following behaviors:) 
    * used to track the start of the member's paid membership, which can be different from the date that membership was initially activated if the member had to wait to join a group;
    * can be manually edited in certain circumstances if a date other than the default if desired;
      * editable and required if the member is part of a Growth Ring Group 
      * editable and optional if the Active Membership checkbox is checked but the member is not part of a Growth Ring Group; 
      * when editable interactively, it is editable for Super Admin only;
    * editable via import for Regional Reps (to allow setting the date when a Rep adds a new member to a Growth Ring Group, via the "Service Contact Set Paid Membership Start Date" background process); 
    * must be the first day of a month - validation error message on the field: "This date must be the first day of a month.";
    * set based on the date that the member joined their first Growth Ring Group: if the date they were added to the group is the 1st of a month, this date is set to match, otherwise this date is set to the 1st of the following month;
    * this date is stored here so that future changes to the Group Member Since date don't inadvertently change the Paid Membership Start date
    * includes no validations against past or future dates; 
    * cannot be cleared manually - error message on field: "This date cannot be cleared manually. To deactivate the membership, use the Deactivate Membership button." (note that this date does not clear when the Deactivate Membership button is clicked, but it could easily be done if desired))
  * Initial Invoice Sent (checkbox + date; editable macro for the Invoice Sent date field for the first row on the Membership History embedded spreadsheet; editability & validations match the corresponding field on the embedded spreadsheet; when checked when there are no rows, the initial row is added and the corresponding date field there is set to match; if unchecked, it simply clears the corresponding date on the row (does not automatically remove the row) 
  * Initial Payment Received (checkbox + date; editable macro for the Invoice Sent date field for the first row on the Membership History embedded spreadsheet; editability & validations match the corresponding field on the embedded spreadsheet, with the exception that the macro becomes read-only when a second row/year is added to the embedded spreadsheet; when checked for the first time, it makes the Activate Membership button visible - see corresponding details)
  * Confidentiality Agreement (checkbox + date; date defaults to current date when the checkbox is filled and clears when the checkbox is cleared; both editable only by Super Admin; warning on Save for Super Admin if the Initial Payment Received checkbox has been filled but this one is blank: "Initial payment has been marked as received but the confidentiality agreement has not been marked as signed."; remains editable; note that eventually there could be a customization to store digital copies of these agreements via the Solution)
  * Active Membership (checkbox; not editable interactively; filled for the first time via the Activate Membership button; cleared via the Deactivate Membership button; can be re-filled via the Reactivate Membership button) 
  * Membership Activation Date & Time (hidden date field + time field; auto-set and read-only; defaults to the date and time that the Active Membership checkbox was checked; uses US Eastern Time)
  * Activate Membership (button; with the following behaviors:
    * visible only for Super Admins if all of the following are true:  
      * Initial Payment Received checkbox is checked (meaning the contact has paid the initial membership fee), 
      * Active Membership checkbox is not checked (meaning the contact does not currently have an active membership), 
      * Renewal Payment Received checkbox for the top row of the embedded spreadsheet is not checked (mainly relates to reactivation),
      * Membership End Date is blank (meaning the contact has never had a membership previously); 
    * clicking this button prompts the user to save the current Contact record if there are unsaved changed, then once saved this runs the Activate New Membership background process to do the following: 1. Fill the Active Membership checkbox, 2. Activate the linked User Profile, if one is linked and inactive, 3. Create a new active User Profile and link it to the Contact if none is linked and "Online Member" is set to "Yes")
  * Note in green text on screen: "Paid Membership Start date is set when the member joins a Growth Ring Group." (visible if the Active Membership checkbox is checked and the member is not part of a Group and the Paid Membership Start field is empty and Reactivation Date is blank)



  


Membership renewal:

  * Renewal Date (date; editable macro for the Membership Year Start / Renewal field for renewal rows on the Membership History embedded spreadsheet; visible if there is more than one row; displays the date from the top (latest) non-initial row on the embedded spreadsheet; editability & validations match the corresponding field on the embedded spreadsheet) 
  * Renewal Invoice Sent (checkbox + date; editable macro for the Invoice Sent Date field for renewal rows on the Membership History embedded spreadsheet; displays the date from top (latest) non-initial row on the embedded spreadsheet; editability & validations match the corresponding field on the embedded spreadsheet) 
  * Renewal Payment Received (checkbox + date; editable macro for the Payment Received Date field for renewal rows on the Membership History embedded spreadsheet; displays the date from top (latest) non-initial row on the embedded spreadsheet; editability & validations match the corresponding field on the embedded spreadsheet) 
  * Next Renewal Date (date; editable macro for the Next Renewal Date field on the Membership History embedded spreadsheet; displays the date from top (latest) row on the embedded spreadsheet, initial or otherwise; editability & validations match the corresponding field on the embedded spreadsheet)
  * Membership History (button; opens the Membership History child screen - see corresponding spec) 



  


  


Membership History Child Screen: Contains the following: 

  * Membership History (embedded spreadsheet, with one row for each year of membership for the contact; editable only by Super Admin; with the following:  
    * Columns: 
      * Membership Year Start / Renewal (date; with the following behaviors: 
        * for the initial row: 
          * defaults to the 1st date of the current month & year when the row is added;
          * not editable interactively; 
          * sets to match the Paid Membership Start date when that field is set (via the Add Member to Group background process when the contact is added to a Growth Ring Group); 
          * updates to match any changes made to Paid Membership Start while there is only 1 row; once there is a second row this field stops updating; 
        * for subsequent/renewal rows: 
          * when a row is added, defaults to match the previous row's Next Renewal Date and is editable; 
          * while editable, updates to match any changes made to the previous row's Next Renewal Date; 
          * required while editable; 
          * editable until Payment Received Date for the same row is set, at which point it becomes read-only; 
        * for all rows: 
          * defaults to the 1st date of the month & year of whatever date is entered (this makes this field to always be set to the 1st of a month without needing a validation message);
          * while editable, cannot be before the Paid Membership Start date for the member - validation error message on the field: "This date cannot be before the Paid Membership Start date."; 
          * if payment has not been marked received for the row, this date cannot be before another Membership Year Start / Renewal date on the embedded spreadsheet - validation error message on the field: "This date cannot be before other Membership Year Start / Renewal dates."; 
          * cannot be the same as another Membership Year Start / Renewal date - validation error message on the field: "There is already another membership year with the same date for this member."; 
          * there cannot be more than one unpaid row - validation error message on the field: "There are multiple unpaid rows. Previous row(s) must be marked as paid before new rows can be saved.")
      * Invoice Sent Date (date; with the following behaviors:
        * for the initial row: 
          * defaults to the current date when the row is added (when the "Initial Invoice Sent" checkbox is checked); 
          * clears if the "Initial Invoice Sent" checkbox is unchecked; 
          * editable if there are 0 or 1 rows on the embedded spreadsheet and "Payment Received Date" for the same row is not set; 
          * becomes read-only when "Payment Received Date" for the same row is set; 
        * for subsequent/renewal rows: 
          * defaults to blank when the row is added; 
          * cannot be set if the Payment Received Date for the initial row is not filled - validation error message on the field: "Initial Payment Received must be set before marking the renewal invoice as sent.";
          * sets to the current date when the "Renewal Invoice Sent" checkbox is checked and clears if the checkbox is unchecked; 
          * becomes read-only when the Payment Received Date for the same row is set (i.e. when "Renewal Payment Received" checkbox is checked), and becomes editable again if that field is cleared; 
        * for all rows: 
          * N/A) 
      * Payment Received Date (date; with the following behaviors: 
        * for the initial row: 
          * defaults to blank and read-only when the row is added; 
          * sets to the current date when the "Initial Payment Received" checkbox is checked and clears if the checkbox is unchecked; 
        * for subsequent/renewal rows: 
          * defaults to blank and read-only when the row is added; 
          * cannot be set if the Invoice Sent Date for the same row is not filled - validation error message on the field: "Renewal Invoice Sent must be set before marking the renewal payment as received."; 
          * sets to the current date when the "Renewal Payment Received" checkbox is checked and clears if the checkbox is unchecked;
        * for all rows: 
          * becomes editable when there is an Invoice Sent Date set for the same row (i.e. when the "Initial Invoice Sent" or "Renewal Invoice Sent" checkbox is checked); 
          * does not become read-only as long as the Invoice Sent Date for the same row is set, to allow for "undoing" changes in the future; 
          * required if there is a subsequent row on the embedded spreadsheet) 
      * Next Renewal Date (date; with the following behaviors: 
        * for the initial row: 
          * defaults to blank and read-only when the row is added; 
          * sets to 1 year after the same row's Membership Year Start / Renewal date when that field is set; 
        * for subsequent/renewal rows: 
          * when a row is added, defaults to 1 year after the same row's Membership Year Start / Renewal date; 
        * for all rows: 
          * only the top/latest row is editable, and becomes editable and required when the Membership Year Start / Renewal date for the row is set, so that it can be edited to a later date to extend a membership, i.e. for a "grace period"; 
          * while editable, updates to match any changes made to the Membership Year / Start / Renewal date; 
          * becomes read-only again when the row is no longer the top/latest row; 
          * when manually edited, defaults to the 1st date of the month & year of whatever date is entered (this makes this field to always be set to the 1st of a month without needing a validation message);
          * if payment has not been marked received for the row, this date cannot be on or before any Membership Year Start / Renewal date on the embedded spreadsheet - validation error message on the field: "The Next Renewal Date cannot be on or before a Membership Year Start / Renewal date."; 
          * When this date is within 1 month of the current date, it is caught by the Annual Renewal Due background process that runs monthly on the first of the month (see details in the corresponding section of the proposal) and does the following: 
            * 1\. Add a new row the the Membership History embedded spreadsheet, 
    * Automatically sorted by: Membership Year Start / Renewal date (blank at the top, then latest set date) 
    * Show 6 rows without scrolling
    * Other Notes:
      * Adding rows: 
        * The first row is normally added when the "Initial Invoice Sent" checkbox is checked. See details in the corresponding spec. 
        * Subsequent rows for renewals of ongoing memberships are added via the automatic Annual Renewal Due background process, 30 days before the Next Renewal Date. See details in the corresponding spec. 
        * When a deactivated membership is reactivated, a row is added via the Reactivate Membership background process (when the Reactivate Membership button is clicked). See details in the corresponding spec. 
        * Rows can be manually added, but this must be done with caution. 



  


Membership deactivation:

  * Membership End Date (date; visible, set and required for members who have had an active membership deactivated, so it only can be set via the Deactivate Membership button - see details in the spec for the button; once set, this can be edited manually if a date other than the default is desired; if set, it must be a date on or before the current date - validation error messages on the field: "This date must be in the past.") 
  * Deactivate Membership (button; with the following behaviors: 
    * visible only for Super Admins if all of the following are true:  
      * Active Membership checkbox is checked (meaning the contact currently has an active membership); 
    * clicking this button prompts the user to save the current Contact record if there are unsaved changed, then once saved this runs the Deactivate Membership background process to: 
      * 1\. Clear the Active Membership checkbox, 
      * 2\. Delete any unpaid rows from the Membership History embedded spreadsheet, 
      * 3\. Remove the member from all Growth Ring Groups of which they are a member, 
      * 4\. Set the Membership End Date to the current date, 
      * 5\. Deactivate the linked User Profile if one is linked; 
    * error if the contact is a Facilitator and/or Regional Rep: "Facilitators and Regional Reps cannot have their memberships deactivated. To deactivate this membership, first change the member to not be a Facilitator and/or Regional Rep.")



  


Membership reactivation:

  * Reactivate Membership (button; with the following behaviors: 
    * visible only for Super Admins if all of the following are true:  
      * Active Membership checkbox is not checked (meaning the contact is not an active member), 
      * Membership End Date is filled (meaning the contact previously was an active member),
    * clicking this button prompts the user to save the current Contact record if there are unsaved changes, then once saved this runs the Reactivate Membership background process to: 
      * 1\. Clear the Membership End Date, 
      * 2\. Re-check the Active Membership checkbox, 
      * 3\. Clear the Paid Membership Start date and reset it to (a) the current date if it is the first of a month or otherwise (b) the first date of the upcoming month, 
      * 4\. Set the Reactivation Date to the current date. 
      * 5\. Add a new row to the Membership History embedded spreadsheet, with Membership Year Start / Renewal date defaulted to the current date and Next Renewal Date set to 1 year from the current date, 
      * 6\. Reactivate the linked User Profile if one is linked, 
      * 7\. Create a new active User Profile and link it to the Contact if none is linked and "Online Member" = Yes, 
      * 8\. Display the reactivation message mentioned below.)
  * Reactivation Date (hidden field; set via the Reactivate Membership background process) 
  * Reactivation message in green text on screen after the Reactivate Membership button has been clicked: "Please review and confirm that the renewal dates and payments are correct, and edit if needed. Add the member to a Growth Ring Group to fully activate the membership and to clear this message." (visible if the Active Membership checkbox is checked and the Member is not part of a Growth Ring Group and and the Paid Membership Start field is set and Reactivation Date is set; message made visible by clicking the Reactivate Membership button; hidden when the member is part of a Group) 



  


Additional details:

  * Account Name (optional; drop list of Organization-type Contacts; filters down as you type; an ellipsis button to the right of this field allows for creating a new Organization if the field is blank (opens a new Contact record, with Type defaulted to Organization), or for opening the selected Organization if one is selected; warning on save if blank: "Account name is blank.")
  * Online Member (required; drop list of Yes/No/blank; defaults to blank; to be manually set to "Yes" for members who will access the Solution online, and otherwise to "No"; error message on save if blank: ""Online Member" in the Membership Details section is a required field.") 
  * User Profile (visible if "Online Member" = "Yes"; required if the "Active Membership" checkbox is checked; drop list of active User Profiles that aren't already linked to a Contact record, with the following additional behaviors: 
    * note that all support- and system-related User Profiles on this drop list are visible only for support users (i.e. users who have the "CCI_" prefix in their User ID); these are hidden here from non-support users (i.e. users who do not have the "CCI_" prefix in their User ID) to avoid confusion & mistakes, but they are still visible in the User/Group Administration report;
    * note that this field normally is set via a background process when the "Activate Membership" button is clicked; 
    * if this field is blank and the Active Membership checkbox is checked, show a warning on Save for users that can edit it: "This member does not have a User Profile linked to their Contact record."; 
    * if this field is blank when required, show an error on Save with the same wording; 
    * on the first Save after a User Profile is set, the Solution automatically sends the Members Exchange Welcome Email to the Contact's primary email address)
  * Create User Profile (button; visible if "Active Membership" checkbox is checked and "Online Member" = Yes and there is no User Profile selected on the "User Profile" drop list; visible only to Regional Reps and Super Admins; clicking this button runs the "Create User Profile" background process to create a new active User Profile and link it to the Contact record)
    * (Note that this is located in the Membership Details section, to the right of the "User Profile" drop list, in the place of the "Manage User Profile" link since that will be hidden if this button is visible) 
  * Manage User Profile (visible if there is a User Profile selected; visible only to Regional Reps and Super Admins; link to open the User Profile record for the selected user profile)
  * View Growth Ring Goals (link to open the My Growth Ring Goals Report report, filtered to the current Member; see details in the corresponding section of the proposal)
  * Print Blank Life Goals Worksheet (link; generates a PDF for the Life Goals Worksheet with no fields filled) 
  * Print My Life Goals (link; generates a PDF of the Life Goals Worksheet with fields filled) 



  


Additional automation notes: 

  * There is a nightly Sync Contacts and User Profiles background process to keep the Contact and User Profile in sync.
  * The Activate New Membership background process also runs nightly to automatically activate memberships for all Contacts that have the Activate Membership button visible (this helps prevent members from getting "lost" once their payment has been marked as received). 
  * The Sync Contacts and Growth Ring Groups background process runs nightly to automatically removes Contacts with inactive memberships from Growth Ring Groups and upcoming Growth Ring Group Meetings.
  *  See the corresponding section of the proposal for additional details on all of the background processes.



  


  * Additional Validation: 
    * Warning on Save if "Active Membership" checkbox is checked and "Online Member" = Yes and there is no User Profile selected on the "User Profile" drop list: "This Member has been changed from an offline member to an online member, but they are lacking a User Profile. Click the "Create User Profile for Member" button." 



  


Other Notes:

  * If a membership is deactivated, the Contact record itself will remain active by default, and all of the member's existing information will be retained.



  


Development Specification

TODO_VA: Tim Reitz 07/10/2025: This should be broken down into sub-sections, based on the bolded sections in this memo. 

  


  


Change Requests: 

  * Tim Reitz 02/16/2024: [[[IN9178](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9180&)]] - ZSB - Background Processes - Changes Due to User Group Adjustments
  * Tim Reitz 03/13/2024: Adding this section - [[[IN9344](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9346&)]] - ZSB - Misc. Minor Changes & Bugs (01/23/24)
  * Tim Reitz 04/04/2024: [[[IN9075](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9077&)]] - ZSB - Contact - Membership Details - Changes to Account Name Field
  * Tim Reitz 04/04/2024: [[[IN8909](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8911&)]] - ZSB - Contacts / User Profiles - Creating User Profile for Active Members who Become Online Members
  * Tim Reitz 04/04/2024: [[[IN9502](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9504&)]] - ZSB - Contact Record - Membership Details Section - User Profile - Editability / Visibility
  * Tim Reitz 04/04/2024: [[[IN9518](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9520&)]] - ZSB - Contact Record - Membership Buttons
  * Tim Reitz 04/04/2024: [[[IN9581](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9583&)]] - ZSB - Contact Record - (Simplified) Clean up Renewal Process & Fields: Main Job
  * Tim Reitz 04/09/2024: [[[IN9565](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9567&)]] - ZSB - Contact Record - Clarify Visibility & Editability
  * Tim Reitz 04/10/2024: [[[IN9550](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9552&)]] - ZSB - Contact & GR Goals - Items from Deployment walkthroughs
  * Tim Reitz 07/20/2024: [[[IN9836](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9838&)]] - ZSB - Dashboard - Add Scrolling News Feed
  * Tim Reitz 07/20/2024: [[[IN9728](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9730&)]] - ZSB - Various Cleanup Changes #2 (prev. "April 2024 (batch 1)")
  * Tim Reitz 12/16/2024: [[[IN10462](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10464&)]] - ZSB - Error: Scheduled Task Alert for Sync Contacts and User Profiles
  * Ben Reitz 10/08/2025: [[[IN12047](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12049&)]] - ZSB - Contact record - Add "Membership Stage" fielding
  * 


  


  


Ellis Miller 05/05/2023: 

[ ] some validation 

[ ] x30s to modify user profiles

[ ] OnChange buttons

  


  


BID: 1.5 days

  


  


DONE_CCI: Tim Reitz 05/18/2023: Per Ellis, consider User Profile linking if Contact is Active and User Profile is Inactive. Jonathan Bergen 09/13/2023: This is covered by current functionality.

  


Paid Membership Start date: Tim Reitz 05/23/2023:  Per Ellis: 

Dev Spec: * The paid membership start is an editable expression that is calculated from the first Group Member Since date. We use an expression so that it is immediately displayed after the user is added to the group. We also have a stored underlying field so that we can snapshot the date. We fill in the field if the admin edits the date and we'll also fill it in with a nightly process -- an x30 that goes through and if there is no stored date, but there is a calculated date, we copy the calculated date into the underlying stored date.

The calculated value will be copied into the underlying field if the underlying field is blank. This happens at the first edit to the contact after the group join or in a process that runs each night.

  


DONE_IDD: Tim Reitz 07/13/2023: Add the background processes to the new section

  


DONE_CCI: Tim Reitz 07/14/2023:  See the "Background Processes" section of this proposal for information about the scheduled tasks. I'm leaving it here grayed out for now.

Dev spec for the automation: (can be run both as needed for activation/deactivation/reactivation) and/or as a nightly process).

\- Helper Report (for x30) of contacts with Contact Name, User ID, and Membership End Date

\- x30list: one User-level to deactivate Users if the Contact's Membership Status is not Active, and one Growth Ring Group-level x30 that removes all Contacts without an Active Membership from the Group.

Tim Reitz 05/09/2023: Per Ellis, distinguish between support users and unlinked member users.

\- x30 to create missing User Profiles or update existing ones 

  


  


Spec for the Contact / User Profile Linking background process (might need some tweaking):

For each contact:

[ ] Set User ID (from contact if specified, otherwise, firstname.lastname.contactid)

[ ] First Name (from contact)

[ ] Last Name (from contact)

[ ] Email Address (from contact)

[ ] Quick Login (set to true) 

[ ] User Disabled (based on active/inactive membership)

[ ] User Group (hardcoded based on list item)

DONE_MM: Tim Reitz 06/28/2023: I think this is the x30?? Either way, we should make sure that the details for setting the Username and other details on the User Profile are clear where we've specced out that background process. 

Tim Reitz 06/29/2023: Yes. 

DONE_MM: Tim Reitz 06/29/2023: Right that the automatic process for creating the User Profile should also create their temporary PW and set the "change password next login" checkbox?

DONE_IDD: Tim Reitz 06/29/2023: 

\- Set Quck Login 

\- Allow users to reset their own passwords (see [[[W0202](https://zch.apphosting.zone/Detail/Edit/2?RecordType=WikiPages&NumberID=-203&)]] - Using Username / Password for AppHosting Login) 

\- Include the pw reset link in the welcome email (e.g. [https://SUBDOMAIN.apphosting.zone/ResetPassword](https://SUBDOMAIN.apphosting.zone/ResetPassword) )

  


Spec for the Deactivation background process (might need some tweaking):

[ ] Automatic process runs in the middle of the night after the End Date 

[ ] Member's Growth Ring Goals: only send emails for goals of active members

[ ] Member's Knowledge Tree Branches: let these live on and get lost

[ ] Member's Development Resource Reviews: let these live on

[ ] Member's Knowledge Tree Entries: let these live on and get lost

[ ] Member's Knowledge Tree Record: let these live on and get lost

[ ] GR Group Meetings that the Member is part of: remove from meetings that haven't happened yet

  


  


Spec for the Reactivation background process (might need some tweaking):

[ ] Member's Contact record: manually reset the Start Date

[ ] Member's User Profile: via the Update Now button on the Contact record

[ ] Add Member to a GR Group: manually 

[ ] Member's Growth Ring Goals: start up with the Group

[ ] All other records: should be as they were when the member left
