5.9.3. User-Initiated Processes

  


Requirements

User-Initiated Processes: The Solution contains the following automatic processes that are initiated by a user action:

  


_. Activate New Membership: See spec in "Scheduled Processes" section. 

  


1\. Service Contact Set Paid Membership Start Date:

  * Description: Used to set the "Paid Membership Start" date on a Member's Contact record when they are added to a Growth Ring Group.
  * Prompts: 
    * __ 



TODO_VA: Tim Reitz 06/04/2025: Ask Jonathan about prompt details for these. 

  * Initiated:
    * When the "Continue" button is clicked on the Add Member child screen on the Growth Ring Group record. 
  * Action(s): 
    * Sets the Paid Membership Start date on the Contact record, based on the date that the member joined their first Growth Ring Group: If the Group Member Since date is the 1st of a month, this date is set to match; otherwise this date is set to the 1st of the following month. 
    * If the member does not have a renewal row in the Membership History embedded spreadsheet (i.e. if there is only one row), this also sets the Membership Year Start / Renewal date and the Next Renewal for the renewal / most recent row. 



  


2\. Deactivate Membership:

  * Description: Used to deactivate a membership. 
  * Prompts: 
    * __ 
  * Initiated:
    * When the "Deactivate Membership" button is clicked on a Contact record.
  * Action(s): 
    * Clear the Active Membership checkbox.
    * Delete any unpaid rows from the Membership History embedded spreadsheet. 
    * Remove the member from all Growth Ring Groups of which they are a member.
    * Set the Membership End Date to the current date.
    * Deactivate the linked User Profile if one is linked.



  


  


3\. Reactivate Membership:

  * Description: Used to reactivate a membership that was previously active and currently is inactive. 
  * Prompts: 
    * __  
  * Initiated:
    * When the "Reactivate Membership" button is clicked on a Contact record. 
  * Action(s): 
    * Clear the Membership End Date, 
    * Re-check the Active Membership checkbox.
    * Clear the Paid Membership Start date and reset it to (a) the current date if it is the first of a month or otherwise (b) the first date of the upcoming month, 
    * Set the Reactivation Date to the current date. 
    * Add a new row to the Membership History embedded spreadsheet, with Membership Year Start / Renewal date defaulted to the current date.  
    * Reactivate the linked User Profile if one is linked.
    * Create a new active User Profile and link it to the Contact if none is linked and "Online Member" = Yes.
    * Display the reactivation message.



  


  


4\. Create User Profile:

  * Description: Used to create a new User Profile for an Offline Member becoming an Online Member. 
  * Prompts: 
    * __ 
  * Initiated:
    * When the "Create User Profile for Member" button is clicked on a Contact record. 
  * Action(s): 
    * Create a new active User Profile for the Contact and link it to the Contact record. 



  


  


5\. Add Member to Growth Ring Group: 

  * Description: Used to link a member Contact with a Growth Ring Group record.
  * Prompts: 
    * __
  * Initiated:
    * When the "Continue" button is clicked on the Add Member child screen on the Growth Ring Group record.
  * Action(s): 
    * Adds a new row to the Growth Ring Group Members embedded spreadsheet on the Growth Ring record, with the Name field filled in.



  


  


6\. Add Default Branches: 

  * Description: Used to add the default list of Knowledge Tree Branches to a Member's list. 
  * Prompts: 
    * __ 
  * Initiated:
    * When the "Add Default Branches" button is clicked on a Knowledge Tree Entry record.
  * Action(s): 
    * Creates Knowledge Tree Branch records for the selected Member, one for each of the active Development Resource Categories in the Solution.



  


  


7\. Create Registrations from Info Meeting:

  * Description: Used to batch-create new Event Registration records for a Launch Meeting for registrants for the linked Info Meeting, with fields defaulted.
  * Prompts: 
    * __
  * Initiated:
    * When the "Create Registrations from Info Meeting" button is clicked on the Launch Meeting-type Event record.
  * Action(s): 
    * Looks at Event Registration records for the linked Info Meeting and finds any Contacts that match the following criteria:
      * Do not have an Event Registration record for the linked Launch Meeting. 
    * Creates a new Event Registration record for each of the Contacts that does not have one, with the following fields defaulted:
      * Event = "Launch Meeting" 
      * Registration Status = "Tentative" 
      * Attended = not checked
      * Lead Follow-up Completed = N/A (not included on the Launch Meeting type)
      * All other fields: Copied from the corresponding fields on the Event Registration record for the Info Meeting



  


8\. Create New Group (from Launch Meeting):

  * Description: Used to a new Growth Ring Group record from a Launch Meeting, with fields defaulted.
  * Prompts: 
    * __ 
  * Initiated:
    * When the "Create New Group" link is clicked on the Launch Meeting-type Event record.
  * Action(s): 
    * Creates a new Growth Ring Group record, with the following fields defaulted:
      * Growth Ring Group ID: Defaults to blank, but is required to save the new record 
      * Region: Sets to the Region set on the Info Meeting linked to the Launch Meeting 
      * Regional Rep: Sets based on the Region
      * Info Meeting: Sets to the Info Meeting ID for the Info Meeting linked to the Launch Meeting



  


  


9\. Create Event Registration: 

  * Description: Used to create a new Event Registration record from a Contact or Event record (or a menu option), with various fields defaulted based on prompts.
  * Prompts: 
    * Registrant Name (drop-list of all active individual Contacts; sets the "Registrant Name" field on the new Event Registration record)
    * Event (drop-list of all Event IDs; sets the "Event" field on the new Event Registration record) 
    * Bringing Guest (drop list of blank/Yes/No; defaults to blank; sets the corresponding field on the new Event Registration record) 
  * Initiated:
    * Via the "Add Event" link in the "Event Registration" section of the Contact record (the Contact is set on the prompt)
    * Via the "Register for Info Meeting" link in the "Lead Details" section of the Contact record (the Contact is set on the prompt)
    * Via the "Register for Launch Meeting" link in the "Lead Details" section of the Contact record (the Event and Contact name are set on the prompt)
    * Via the "Add Registrant" link in "Registration Details" section of the Event record (the Event is set on the prompt) 
    * Via the "Add Registrant" button on the "Event Registrations" report (the Event is set on the prompt screen)
    * Admin | Event Management | New Registration (menu option; all prompts default to blank, to be set manually) 
  * Action(s): 
    * Creates and opens a new Event Registration record based on the set prompts.



  


Development Specification

TODO_VA: Tim Reitz 07/10/2025: This could be broken down into sub-sections, one for each process (remove the numbering).

  


  


Change Requests:

  * Tim Reitz 06/28/2025: [[[IN9119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9121&)]] - ZSB - Add Events Feature (Info Meetings, etc.)
  * 


  


  


_EM: Tim Reitz 06/04/2025: Are the above actually user-initiated, or triggered? They weren't coded with the "Run Import" text (prior to our new list of words that can be used)

TODO_VA Ellis Miller 06/02/2025: Have Nic research.

  


TODO_: Note the following list of words that can be used in the button label text for manually triggering x30s: 

  * Confirm
  * Create
  * Delete
  * Import
  * Modify
  * Run
  * Send
  * Set
  * Update 



The button label must include one of these words. (See the following CLS page for additional details: [HS0000836](https://clientscope.invtools.com/Detail/View/2?RecordType=HelpDrafts&NumberID=-853&State=XPSMmJcy76s&_=X3eXw& "https://clientscope.invtools.com/Detail/View/2?RecordType=HelpDrafts&NumberID=-853&State=XPSMmJcy76s&_=X3eXw&") \- x30 Import Settings: Advanced Tab)
