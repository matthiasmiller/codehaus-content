5.4.9.1. Process: Create Registrations from Info Meeting

  


Requirements

*Documented 

  


Tim Reitz 06/05/2025: This looks like a "User-Initiated" automatic process. 

  


Overview: This is a process used to batch-create new Event Registration records for a Launch Meeting for registrants for the linked Info Meeting, with fields defaulted.

  


Interfaced:

  * Via the "Create Registrations from Info Meeting" button on the Launch Meeting-type Event record.



  


Action(s): 

  * Looks at Event Registration records for the linked Info Meeting and finds any Contacts that match the following criteria:
    * Do not have an Event Registration record for the linked Launch Meeting. 
  * Creates a new Event Registration record for each of the Contacts that does not have one, with the following fields defaulted:
    * Event = "Launch Meeting" 
    * Registration Status = "Tentative" 
    * Attended = not checked
    * Lead Follow-up Completed = N/A (not included on the Launch Meeting type)
    * All other fields: Copied from the corresponding fields on the Event Registration record for the Info Meeting



  


Scheduled Task Command: N/A

  


Development Specification

Ellis Miller 06/21/2024:

[ ] "Std Launch Meeting Create Missing Registrations.x30" with required LaunchMeetingID ask prompt.

[ ] Header Validation Error if NOT EventField( AskLaunchMeetingID, EventIsLaunchMeeting): "This is not a valid launch meeting ID: " \+ AskLaunchMeetingID

[ ] Header Validation Error if no linked Info Meeting for AskLaunchMeetingID.

[ ] Uses input "Std Launch Meeting Find Missing Registrations.r20" that takes AskLaunchMeetingID, it will subset to all registrations for locLinkedInfoMeetingID (the info meeting linked from the AskLaunchMeeting) that don't have a corresponding LaunchMeetingID. The report just needs a single column for the Contact Name.

[ ] The x30 can then simply create new records for each line in the input report.

Bid: 4 hours
