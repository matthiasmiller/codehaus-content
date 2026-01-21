5.10.4.4. Notification: Review Launch Meeting Registrations

  


Requirements

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

Change Requests:

  * Tim Reitz 06/04/2025: Added in [[[IN9119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9121&)]] - ZSB - Add Events Feature (Info Meetings, etc.)


