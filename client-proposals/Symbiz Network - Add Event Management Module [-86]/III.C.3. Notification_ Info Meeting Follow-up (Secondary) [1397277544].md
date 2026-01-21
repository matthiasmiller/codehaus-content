3.3.3. Notification: Info Meeting Follow-up (Secondary)

  


Requirements

*Documented 

  


Name: Info Meeting Follow-up (Secondary)

Record Type: Event (with Type = Info Meeting)

Date: 21 calendar days after the Event Date of an Info Meeting with Status other than Canceled, if there is at least one linked Event Registration record with the "Lead Follow-up Completed" checkbox not checked

Trigger / Scheduled Task Details: Scheduled task that runs Monday-Friday at 7:00 am ET

Scheduled Task: "Send Info Meeting Follow-up Emails (Primary & Secondary)" 

Format: Email

Send To: The Info Meeting Presenter for the Info Meeting and all Super Admins who have the "Receives Event Management Emails" checkbox checked on their Contact record. 

Subject / Message:

Subject: Info Meeting Follow-up Needed (Secondary)

Message: Hello, <Contact FirstName>, 

  


There are leads from the <Event Name> Info Meeting on <Event Date> that still need a follow-up.

  


Link to to the Info Meeting Event record: <link>

  


Leads needing follow-up: 

<embedded report of the Leads report, with the "Info Meeting" filter = the corresponding Info Meeting and the "Follow-up Completed" filter = "No">

  


View report: <link to Leads report, with the same filters set as the embedded reported above>

  


Development Specification

Ellis Miller 06/20/2024:

  


Name: Info Meeting Follow-up (secondary)

  * Cloned from above:
  * Merge at event level also checks EventRegistrationsByEventNdxFindField( EventID, True, NOT EventRegistrationFollowedUp) to checks whether any registrations still need followup
  * Email also goes to all SuperAdmins (Concat through all contacts looking for super-admins). 
    * Tim Reitz 06/22/2024: Note: Not literally all SuperAdmins -- only those who have the "Receives Event Management Emails" checkbox checked on their Contact record. Note that this is like the "Receives Symbuzz Extra Monthly Reminder" checkbox that determines which SuperAdmins receive the "Print Symbuzz Extra (Monthly)" notification. 



4 Hours
