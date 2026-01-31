11.0.2. Leads by Info Meeting Report

  


Requirements

Tim Reitz 07/01/2024: This section was archived because we have added spec notes to the places that would have had a report like this, basing it directly on filters rather than calling it by a new report name. 

  


  


Add the following new report: 

  


This is the Leads report, filtered to a selected Info Meeting.

  


This is accessed from:

  * Admin | Lead Management | Leads by Info Meeting
  * The "Info Meeting Follow-up (Secondary)" email notification



  


Title: Leads for <Info Meeting Name> Info Meeting 

  


The following filters are set to something other than their default:

  * Info Meeting = _
    * Admin | Lead Management | Leads by Info Meeting: N/A (defaults to blank)
    * "Info Meeting Follow-up (Secondary)" email notification: The Info Meeting for which the notification is running.
  * Follow-up Completed = __
    * Admin | Lead Management | Leads by Info Meeting: N/A (defaults to blank)
    * "Info Meeting Follow-up (Secondary)" email notification: "No"



  


Ellis Miller 06/20/2024: _VA: Need required ask prompt for Info Meeting. Need ask prompt for lead status or needing follow up or something so that emails can only show the ones that need follow-up. 

_JB: Tim Reitz 06/27/2024: Do you know why the Info Meeting ask prompt would need to be required?

Tim Reitz 06/28/2024: Jonathan doesn't see why it would need to be required. But let's leave a note in the Dev Spec for the devs to ask Ellis?

  


_JB: Tim Reitz 06/27/2024: We want different defaults for the filters at different times: 

  * menu: blank
  * email: filled in (Info Meeting based on the Event, Follow-up always "No") 



Do we need two separate versions of this?

  


_VA Tim Reitz 06/28/2024: We probably should do away with this section. 

[X] Add the spec for the menu item to the Leads report spec ("Accessed from"), 

[X] and the spec for the emailed version with the email. 

Tim Reitz 07/01/2024: This has been done, so I'm archiving this section. 

  


  


Other Notes: 

  * N/A



  


Development Specification

Mockup: Not needed

TODO_CCI: Tim Reitz 05/28/2024: Please send us screenshots of the report once you have it coded so we can review it prior to testing. Thanks!
