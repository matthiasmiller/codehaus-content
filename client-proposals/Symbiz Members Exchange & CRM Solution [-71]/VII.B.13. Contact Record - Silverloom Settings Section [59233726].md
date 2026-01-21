7.2.13. Contact Record - Silverloom Settings Section

  


Requirements

The Contact record also includes the following custom fields in this standard section: 

  


  * Silverloom Settings standard section (custom: visible if Contact Type = Member; visible to Super Admins):
    * Is Super Admin (custom field; read-only checkbox; visible for Super Admins; automatically checked if the Contact is linked to a user profile with the "Edit Super Admin fields" permission enabled)
    * Is Regional Rep (custom field; read-only checkbox; visible for Super Admins; automatically checked if the Contact is selected as the Rep on one or more Region records)
    * Is Facilitator (custom field; read-only checkbox; visible for Super Admins; automatically checked if the Contact is selected as the Facilitator on one or more Growth Ring Group Records)
    * Is Standard Member (read-only checkbox; visible for Super Admins; automatically checked if the Active Membership checkbox is filled for the Contact)



  


  * Salesforce ID (custom hidden field; normally set via import; used to link records and preventing duplicate names on the data import) 



  


  * Symbuzz Extra Post Reviewer (custom field; checkbox; with the following details / behaviors: 
    * visible on Contact records belonging to Super Admins; 
    * visible to and editable by Super Admins; 
    * if checked, the user receives the Review Symbuzz Extra Posts user notification; 
    * note that multiple Contacts may have this checkbox checked at the same time \- warning on the first Save after checking the checkbox if there are multiples: "There is at least one other Super Admin set as a Symbuzz Extra Post Reviewer.") 
  * Receives Symbuzz Extra Monthly Reminder (custom field; checkbox; with the following details / behaviors:
    * visible on Contact records belonging to Super Admins; 
    * visible to and editable by Super Admins; 
    * if checked, the user receives the "Print Symbuzz Extra (Monthly)" user notification; 
    * note that multiple Contacts may have this checkbox checked at the same time \- warning on the first Save after checking the checkbox if there are multiples: "There is at least one other Super Admin set as a recipient of this notification.")
  * Receives Event Management Emails (custom field; checkbox; with the following details / behaviors:
    * visible on Contact records belonging to Super Admins; 
    * visible to and editable by Super Admins; 
    * if checked, the user receives the "Info Meeting Follow-up (Secondary)" and "Review Launch Meeting Registrations" emails (in addition to the main specified recipients); 
    * note that multiple Contacts may have this checkbox checked at the same time \- warning on the first Save after checking the checkbox if there are multiples: "There is at least one other Super Admin set as a recipient of this notification.") 



  


  * Other Notes: 
    * Note that up to all four of "role" checkboxes could be checked at the same time (i.e. in the event that a Super Admin is also a Regional Rep and Facilitator). 
      * The Solution looks at the highest-ranking checked checkbox to determine permissions / data access.



  


Development Specification

Change Requests:

  * Tim Reitz 02/16/2024: [[[IN9078](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9080&)]] - ZSB - User Groups - Pre-Deployment Changes
  * Tim Reitz 04/10/2024: [[[IN9550](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9552&)]] - ZSB - Contact & GR Goals - Items from Deployment walkthroughs
  * Tim Reitz 04/11/2024: [[[IN8960](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8962&)]] - ZSB - Add Features for Symbuzz Extra (prev. called Cross Network Forum)
  * Tim Reitz 06/04/2025: [[[IN9119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9121&)]] - ZSB - Add Events Feature (Info Meetings, etc.)


