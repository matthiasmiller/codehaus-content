3.1. Changes to Data Access Controls

  


Requirements

*Documented 

  


Make the following changes to Data Access Controls (changes indicated with blue / strike-through):

  


Record| Org. Roles That Can View| Org. Roles That Can Edit  
---|---|---  
Event Type| Everyone| N/A (not editable in the Solution)  
Event|   
  
|   
  
With Event Visibility = Public| Everyone (with additional visibility restrictions based on Event Status, and some sections/fields restricted to only Regional Reps and Super Admins)| Regional Reps and Super Admins  
With Event Visibility = All Members| Everyone (with additional visibility restrictions based on Event Status, and some sections/fields restricted to only Regional Reps and Super Admins)| Regional Reps and Super Admins  
  
With Event Visibility = Invitation Only| Members with an Event Registration record for the Event and all their uplines (with additional visibility restrictions based on Event Status, and some sections/fields restricted to only Regional Reps and Super Admins)| Regional Reps and Super Admins  
Event Registration|   
|   
  
Linked to an Event with Event Visibility = Public| Everyone (basic details only; with additional visibility restrictions based on individual sections/fields; more details visible to the Member whose name is in the Registrant Name field & uplines; all details visible to Regional Reps and Super Admins)| Regional Reps and Super Admins  
Linked to an Event with Event Visibility = All Members| Everyone (basic details only; with additional visibility restrictions based on individual sections/fields; more details visible to the Member whose name is in the Registrant Name field & uplines; all details visible to Regional Reps and Super Admins)| Regional Reps and Super Admins  
Linked to an Event with Event Visibility = Invitation Only  
| Member whose name is in the Name field & all uplines (with additional visibility restrictions based on individual sections/fields; all details visible to Regional Reps and Super Admins) | Regional Reps and Super Admins  
  
  


  


Development Specification

Ellis Miller 06/20/2024:

  * Restricted Records:
    * Events: Create an EventIsVisibleToUser
      * if Status is tentative, then UserIsRegionalRepOrSuperAdmin, 
      * if Event Visibility = Invitation Only, then Invitees and uplines:



UserIsRegionalRepOrSuperAdmin OR HasRG( EventInvitees, CurrentUserIsContactOrContactUpline( EventInviteeContact))

  * Event Registration:
    * Use EventIsVisibleToUser



Seth Miller 12/14/2024: This has changed. We no longer actually restrict the event registration record. We hide as much information as possible and the only way a user should be able to get to a record they shouldn't be able to see is through manipulating links. We removed the restriction because of concerns the complicated logic could lead to infinite recursion in the future (event reg depending on event which depends on event reg for visibility)

  


Limit activity history to UserIsRegionalRepOrSuperAdmin

  


3 hours.
