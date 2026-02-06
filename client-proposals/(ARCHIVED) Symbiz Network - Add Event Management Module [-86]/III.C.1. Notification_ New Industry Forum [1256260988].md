3.3.1. Notification: New Industry Forum

  


Requirements

*Documented 

  


Name: New Industry Forum 

(Note that this is a replica of and replaces the existing "New Industry-Specific Meeting" notification for General Meetings.)

Record Type: Event (with Type = Industry Forum)

Date: Date that a relevant Industry is selected on a scheduled Industry Forum-type Event, or date that an Industry matching a scheduled Industry Forum-type Event is selected on the Contact record.

Trigger / Scheduled Task Details: On save, if one of the following criteria is met: 

  * A relevant Industry is selected on a scheduled Industry Forum-type Event, or 
  * An Industry matching a scheduled Industry Forum-type Event is selected on the Contact record.



Scheduled Task: N/A

Format: Member's choice

Send To: All Members in the selected industry(ies) who have the notification enabled

Subject / Message:

In-App (real-time notification):

An Industry Forum has been scheduled for your industry. View details here. (opens the Master Events report, with the "Event" filter set to the corresponding Event record and the "Event Type" filter set to "Industry Forum) 

  


Email:

Subject: New Industry Forum Scheduled

Message: Hello, <Member FirstName>, 

  


An Industry Forum has been scheduled for your industry. Here is the information:

Focus: <Event Focus> (visible if an Event Focus has been set)

Date: <mm/dd/yyyy>

Time: <h:mm AM/PM> 

Time Zone: <Time Zone> 

Description: <Event Description> 

Industry: <Industry(ies), comma separated if multiple)> 

Virtual Event: <Yes/No>

Meeting Link: <link> (visible if "Event Format" = "Virtual" or "Hybrid")

Dial-In Number: <Dial-In Number> (visible if "Event Format" = "Virtual" or Hybrid")

Dial-In Meeting ID: <Dial-In Meeting ID> (visible if "Event Format" = "Virtual" or Hybrid")

Dial-In Passcode: <Dial-In Passcode> (visible if "Event Format" = "Virtual" or Hybrid")

In-Person Event: <Yes/No>

Location: <Location> (visible if "Event Format" = "In-Person" or "Hybrid")

Address: <full address> (visible if "Event Format" = "In-Person" or "Hybrid")

Link to Event record: <link>

  


Development Specification

Tim Reitz 01/23/2025: Note that this is displayed as a single notification on the Contact record, but on the User Profile record ("Notification Preferences" section/RG), this is displayed as two separate items: 

  * New Industry Forum (New Event created)
  * New Industry Forum (Industry added to Contact) 



See conversation in [[PC0168781]] for further details. 

  


Change Requests: 

  * Tim Reitz 03/29/2025: [[[IN11109](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11111&)]] - ZSB - Event Email Notifications - Include call-in info 
  * 


  


  


Ellis Miller 06/20/2024:

  


Name: New Industry Forum 

  * Email: Clone what we had for the old General Meetings
  * In-App: Clone what we had for the old General Meetings



4 Hours
