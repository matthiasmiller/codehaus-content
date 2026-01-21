7.6.6. Device Record - Latest Position Section

TODO_VA: Tim Reitz 01/13/2026: This needs a lot of work. 

  


  * Latest Position section (visible to the linked "Primary Driver" user and all uplines):



Tim Reitz 09/15/2025: It looks like this is simply displaying details from the most recent "Traccar Position record" for the Device. 

Tim Reitz 09/15/2025: Would this essentially be real-time, where a user could watch it tick along? Or only current as of the last time that the page was opened/refreshed? 

Tim Reitz 09/15/2025: Actually, see the next set of questions about records / RGs / periodic syncing. 

TODO_JB: Tim Reitz 12/08/2025: Consider this more once we have more data / details from Traccar / JB. [see the Traccar Position sync record]

  


HLD note: Do we want to turn off activity history for the latest position? Or do we want an RG that keeps up to X hours of history? Or do we want to keep full history?

Tim Reitz 07/23/2025: Also the following: In the in-depth design, consider whether we want to store latest position, all positions, positions for N days, etc

TODO_: Tim Reitz 07/23/2025: How frequently is "Latest Position" being updated? (I'm assuming the concern here is for the amount of data that would end up being stored by activity history here)

  


  * Traccar Position ID (read-only macro; displays the ID for the most recent Traccar Position record for the Device, based on the "__" field)



TODO_: Tim Reitz 09/15/2025: There are 3 different date/time fields on the Position record - which one to use?

  * VIN / Vehicle (read-only macro; displays __



TODO_: Tim Reitz 07/23/2025: Update here and in Events RG once we have the field specced on the Vehicle record.

Tim Reitz 09/15/2025: It doesn't appear that the Traccar Position actually tracks VIN. So we'd have to deduct this based on the linked Primary Vehicle.

  * VIN Owner (read-only macro; displays the current "Owner" of the Vehicle as of the time that the row is added; this is stored so that Event data is only available to the person who owned the Vehicle at the time of tracking)
  * Traccar Driver ID (read-only macro; displays __



HLD note: Save the Traccar Driver ID for attempted driver matching with Traccar

TODO_: Tim Reitz 09/15/2025: It doesn't appear that the Traccar Position actually tracks Driver either. So we'd have to deduct this based on the linked Primary Driver for the Device.

  * Date (read-only macro; displays __
  * Time (read-only macro; displays __



TODO_: Tim Reitz 09/15/2025: Split apart the date/time field into 2, or just display them as 1?

  * Latitude (read-only macro; number; 6 decimals; may be positive or negative; displays the "Latitude" from the Traccar Position record)
  * Longitude (read-only macro; number; 6 decimals; may be positive or negative; displays the "Longitude" from the Traccar Position record)
  * Speed (read-only macro; number; 2 decimals; displays the "Speed" from the Traccar Position record)
  * View Position History (link; opens ___



TODO_: Tim Reitz 09/15/2025: Possibly a link to a report in Traccar, with data passed in, if we can do that.
