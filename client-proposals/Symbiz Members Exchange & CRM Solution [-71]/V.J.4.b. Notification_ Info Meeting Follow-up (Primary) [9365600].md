5.10.4.2. Notification: Info Meeting Follow-up (Primary)

  


Requirements

Name: Info Meeting Follow-up (Primary)

Record Type: Event (with Type = Info Meeting)

Date: 14 calendar days after the Event Date of an Info Meeting with Status other than Canceled

Trigger / Scheduled Task Details: Scheduled task that runs Monday-Friday at 7:00 am ET.

Scheduled Task: "Send Info Meeting Follow-up Emails (Primary & Secondary)"

Format: Email 

Send To: The Info Meeting Presenter for the Info Meeting 

Subject / Message:

Subject: Info Meeting Follow-up Needed

Message: Hello, <Contact FirstName>, 

  


It's time for your 2-week follow-up with the leads from the <Event Name> Info Meeting on <Event Date>: <Link to Event record>

  


Leads from this Info Meeting: 

<embedded report of the Leads report, with the "Info Meeting" filter = the corresponding Info Meeting>

  


View report: <link to Leads report, with the same filters set as the embedded reported above>

  


Development Specification

Change Requests:

  * Tim Reitz 06/04/2025: Added in [[[IN9119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9121&)]] - ZSB - Add Events Feature (Info Meetings, etc.)


