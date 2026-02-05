8.5.6. Device Record - Latest Position Section

  


Requirements

  * Latest Position section (visible to "Upline Provider Roles" users for the linked Account):
    * Traccar Position ID (hidden; read-only macro; data synced from Traccar; displays the ID for the most recent Traccar Position sync record for the linked Traccar Device sync record, based on the "__" field)



DONE_JB (research): Tim Reitz 09/15/2025: There are 3 different date/time fields on the Position record - which one to use to determine the latest (and to display the position date & time below)?

Jonathan Bergen 02/02/2026: We'll use the serverTime. This datetime is in UTC.

  * VIN / Vehicle (read-only macro; data synced from Traccar; displays __



TODO_VA (later): Tim Reitz 07/23/2025: Update here and in Events RG once we have the field specced on the Vehicle record.

Tim Reitz 09/15/2025: It doesn't appear that the Traccar Position actually tracks VIN. So we'd have to deduct this based on the linked Primary Vehicle.

  * VIN Owner (read-only macro; displays the current "Owner" of the Vehicle as of the time that the row is added; this is stored so that Event data is only available to the person who owned the Vehicle at the time of tracking)



TODO_VA (later): Tim Reitz 01/31/2026: Update here once we have details about the VIN for the Position.

  * Traccar Driver ID (read-only macro; data synced from Traccar; displays __



HLD note: Save the Traccar Driver ID for attempted driver matching with Traccar

Tim Reitz 09/15/2025: It doesn't appear that the Traccar Position actually tracks Driver either. So we'd have to deduct this based on the linked Primary Driver for the Device.

DONE_JB (research): Tim Reitz 01/31/2026: Does the Traccar Position track an associated Driver?

Jonathan Bergen 02/02/2026: I don't think so, and I don't see how it would be able to say which driver is using it.

If not, we'll probably just skip this item here (we're tracking it on the Event record).

  * Date (read-only macro; data synced from Traccar; displays the date from the "__" field on the "Latest Position" record)
  * Time (read-only macro; data synced from Traccar; displays the time from the "__" field on the "Latest Position" record)



TODO_VA (later): Tim Reitz 01/31/2026: Finish specs once we know which Time field we're looking at

  * Coordinates (read-only macro; data synced from Traccar; displays the coordinates from the "Latest Position" record, as a link to open the location in Google Maps)
  * Speed (read-only macro; data synced from Traccar; number; 2 decimals; displays the "Speed" from the "Latest Position" record)
  * View Position History (link; opens the "Traccar Positions by Device" report, filtered to the current Device ID)



  


Development Specification

Tim Reitz 01/31/2026: We could consider merging this into the "Traccar Device Details" section.
