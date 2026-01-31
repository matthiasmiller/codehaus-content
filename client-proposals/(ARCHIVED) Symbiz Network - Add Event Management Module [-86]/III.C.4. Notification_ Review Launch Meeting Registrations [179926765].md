3.3.4. Notification: Review Launch Meeting Registrations

  


Requirements

*Documented 

  


Name: Review Launch Meeting Registrations

Record Type: Event (with Type = "Launch Meeting" and Event Status = "Tentative" or "Scheduled")

Date: 14 calendar days before the Event Date 

Trigger / Scheduled Task Details: Scheduled task that runs Monday-Friday at 7:00 am ET

Scheduled Task: "Send Review Launch Meeting Registration Email"

Format: Email 

Send To: The Symbiz Presenter for the Launch Meeting and  all Super Admins who have the "Receives Event Management Emails" checkbox checked on their Contact record. 

Subject / Message:

Subject: Review Launch Meeting Registrations

Message: Hello, <Contact FirstName>, 

  


It's time to review the registration list for the <Event Name> Launch Meeting scheduled for <Event Date>: <link to the Launch Meeting Event record>.

  


Please make sure that all interested leads from the associated Info Meeting are included.

  


Info Meeting registration: <link to the Event Registrations Report, with the Event filter = the Info Meeting that is linked to the corresponding Launch Meeting>

  


Current Launch Meeting registration: <link to the Event Registrations Report, with the Event filter = the corresponding Launch Meeting>

  


Development Specification

Ellis Miller 06/20/2024:

  


Name: Review Launch Meeting Registrations

  * Merge at event level as defined in record type
  * Uses SuperAdminEmails macro from above Secondary followup



4 Hours

  


  


_VA: Seth Miller 12/05/2024: Is this supposed to only include scheduled or also tentative meetings? The notes in the Background Processes say to include tentative but here it does not.

Tim Reitz 12/05/2024: For now, let's include Tentative both places. I've updated the spec here in the proposal. However, we're not fully confident in this. Currently the Registration record allows you to select an Event with any status, but it doesn't make a lot of sense to register someone for a Tentative or Canceled Event.
