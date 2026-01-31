6.2. Traccar Event Types List

_GZ: Tim Reitz 07/23/2025: Is this something that you would add to, or is it static? (or maybe you don't know?) 

Tim Reitz 07/24/2025: Client thinks that these are "baked-in" types that Traccar reports on. He thinks that these are the ones that they had identified as "important". 

I'm thinking this list could be added via import. 

Tim Reitz 01/15/2026: Probably not add via import, actually. We probably want to hard-code which Types are brought in by the import, based on this list. 

  


DONE_JB (research): Tim Reitz 12/30/2025: What are the Event Types in Traccar? [full list]

_VA: Jonathan Bergen 01/21/2026: The list below is correct ([https://www.traccar.org/events/](https://www.traccar.org/events/))

Tim Reitz 01/22/2026: See the link for explanations of each Type. 

  * Alarm



Tim Reitz 01/22/2026: Yes. 

  


  * Command result



TODO_JB (research): Tim Reitz 01/22/2026: I don't think we need this one in Silverloom, but do you think differently? 

  * Device inactive



Tim Reitz 01/22/2026: Yes. 

  * Device moving



Tim Reitz 01/23/2026: Not sure - this could proliferate a lot of data in Silverloom, but also could be useful. 

TODO_JB (research): Tim Reitz 01/29/2026: Thoughts on this? 

  * Device stopped



Tim Reitz 01/23/2026: Not sure - this could proliferate a lot of data in Silverloom, but also could be useful. 

TODO_JB (research): Tim Reitz 01/29/2026: Same as above: Thoughts on this? 

  * Driver changed



TODO_JB (research): Tim Reitz 01/22/2026: I don't think we need this one in Silverloom since users wouldn't be editing interactively in Traccar, but do you think differently? 

  * Fuel drop



TODO_GZ: Tim Reitz 01/22/2026: Tracks a sharp fuel drop. Needed? 

Tim Reitz 01/23/2026: See email "Questions related to Traccar events in Silverloom". 

  * Fuel increase



TODO_GZ: Tim Reitz 01/22/2026: Needed? 

  * Geofence entered



Tim Reitz 01/22/2026: Yes. 

  * Geofence exited



Tim Reitz 01/22/2026: Yes. 

  * Ignition off



TODO_GZ: Tim Reitz 01/22/2026: Needed? 

  * Ignition on



TODO_GZ: Tim Reitz 01/22/2026: Needed? 

  * Maintenance required



TODO_JB (research): Tim Reitz 01/22/2026: I'm thinking this is related to the Traccar "Maintenance" feature, and would not be needed at this point. But does it actually correspond to the vehicle's "check engine" light coming on? 

  * Media



TODO_JB (research): Tim Reitz 01/22/2026: I don't think we need this one in Silverloom, but do you think differently? 

  * Queued command sent 



TODO_JB (research): Tim Reitz 01/22/2026: Not seeing this one on the Traccar list that you linked to above. Thoughts on whether you would want it in Silverloom for anything? 

  * Speed limit exceeded



TODO_JB (research): Tim Reitz 01/22/2026: What is the "speedLimit" attribute? 

  * Status offline



Tim Reitz 01/22/2026: Yes. 

  * Status online



Tim Reitz 01/22/2026: Yes. 

  * Status unknown



Tim Reitz 01/22/2026: Yes. 

  * Text message received



TODO_JB (research): Tim Reitz 01/22/2026: Not seeing this one on the Traccar list that you linked to above. Thoughts on whether you would want it in Silverloom for anything? 

  


_VA: Tim Reitz 07/24/2025: To consider: We might filter down the Events that we actually bring into the Silverloom database -- which ones are actually useful / helpful to the Account Managers & Drivers?

  


  


\--------

*. 

  


Overview: This is a custom non-editable simple list used to track types of Traccar Events. 

  


It includes the following items: 

  * Alarm
  * Command result
  * Device inactive
  * Device moving
  * Device stopped
  * Driver changed
  * Fuel drop
  * Fuel increase
  * Geofence entered
  * Geofence exited
  * Ignition off
  * Ignition on
  * Maintenance required
  * Media
  * Queued command sent
  * Speed limit exceeded
  * Status offline
  * Status online
  * Status unknown
  * Text message received



  


This list is universal for all users.

  


Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

  


This list will be set up by CodeCrafters as part of the main development. If changes need to be made to this list, it will require some coding work.
