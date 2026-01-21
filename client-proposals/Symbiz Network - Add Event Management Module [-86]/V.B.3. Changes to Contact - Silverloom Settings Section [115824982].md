5.2.3. Changes to Contact - Silverloom Settings Section

  


Requirements

*Documented 

  


Make the following changes to the existing custom Silverloom Settings section of the Contact record (changes indicated with blue / strike-through):

  


The Contact record also will include the following custom fields in this standard section: 

  


  * Silverloom Settings section (visible if Contact Type = Member; visible to Super Admins):
    * Is Super Admin (read-only checkbox; visible for Super Admins; automatically checked if the Contact is linked to a user profile with the "Edit Super Admin fields" permission enabled)
    * Is Regional Rep (read-only checkbox; visible for Super Admins; automatically checked if the Contact is selected as the Rep on one or more Region records)
    * Is Facilitator (read-only checkbox; visible for Super Admins; automatically checked if the Contact is selected as the Facilitator on one or more Growth Ring Group Records)
    * Is Standard Member (read-only checkbox; visible for Super Admins; automatically checked if the Active Membership checkbox is filled for the Contact)
    * Salesforce ID (hidden field; normally set via import; used to link records and preventing duplicate names on the data import)
    * Symbuzz Extra Post Reviewer (checkbox; visible on Contact records belonging to Super Admins; visible to and editable by Super Admins; if checked, the user receives the Review Symbuzz Extra Posts user notification; note that multiple Contacts may have this checkbox checked at the same time - warning on the first Save after checking the checkbox if there are multiples: "There is at least one other Super Admin set as a Symbuzz Extra Post Reviewer.") 
    * Receives Symbuzz Extra Monthly Reminder (checkbox; visible on Contact records belonging to Super Admins; visible and editable by Super Admins; if checked, the user receives the Print Symbuzz Extra (Monthly) user notification; note that multiple Contacts may have this checkbox checked at the same time - warning on the first Save after checking the checkbox if there are multiples: "There is at least one other Super Admin set as a recipient of this notification.")
    * Receives Event Management Emails (checkbox; visible on Contact records belonging to Super Admins; visible and editable by Super Admins; if checked, the user receives the "Info Meeting Follow-up (Secondary)" and "Review Launch Meeting Registrations" emails (in addition to the main specified recipients); note that multiple Contacts may have this checkbox checked at the same time - warning on the first Save after checking the checkbox if there are multiples: "There is at least one other Super Admin set as a recipient of this notification.") 



  


  * Other Notes: 
    * Note that up to all four of these checkboxes could be filled at the same time (i.e. in the event that a Super Admin is also a Regional Rep and Facilitator). 
    * The Solution looks at the highest-ranking filled checkbox to determine permissions / data access.



  


Development Specification

Tim Reitz 06/25/2024: Note: This was not added to the mockup, but it should be located below the "Receives Symbuzz Extra..." checkbox.
