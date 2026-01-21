7.6.8. Device Record - Events Section

  


Requirements

*

  * Events section:
    * Device Events (no label; "virtual" read-only embedded spreadsheet of all Traccar Event records linked to the current Device; with the following:
      * Columns:
        * Account (read-only macro; displays the "Device Account" from the Traccar Event Record)
        * Event ID (read-only macro; displays the "Traccar Event ID" from the Traccar Event Record)
        * Event Type (read-only macro; displays the "Event Type" from the Traccar Event Record)
        * Device Primary Driver (read-only macro; displays the "Device Primary Driver" from the Traccar Event Record)
        * Override Driver (read-only macro; displays the "Override Driver" from the Traccar Event Record)
        * Device Primary Vehicle (read-only macro; displays the "Device Primary Vehicle" from the Traccar record)
        * Primary Vehicle Owner (read-only macro; displays the "Owner at Time of Event" from the Traccar Event Record) 
        * Override Vehicle (read-only macro; displays the "Override Vehicle" from the Traccar Event Record)
        * Event Location (link; displays as "Link"; opens the "Traccar Coordinates" location in Google Maps)
        * Event Date (read-only macro; displays the "Event Date" from the Traccar Event Record)
        * Event Time (read-only macro; displays the "Event Time" from the Traccar Event Record)
        * View / Edit Event (displays as "Link"; opens the corresponding Traccar Event record in Silverloom) 
    * Automatically sorted by:
      * First by: Event Date (latest at the top);
      * Second by: Event Time (latest at the top);
    * Buttons to add/remove rows: N/A (rows are automatically added, and not removed)
    * Shows __ rows without scrolling



TODO_GZ: Tim Reitz 09/12/2025: Any idea how many Events will be happening on a daily / weekly basis?

  * Row Visibility:



TODO_GZ: Tim Reitz 01/14/2026: Is it fine for all providers to see all events for each others' clients? Or should only uplines be able to see Events? 

TODO_: Tim Reitz 01/14/2026: If we need to restrict it to uplines, this row visibility spec would be needed. 

  * Rows are visible to current "Upline Provider Roles" users for the "Account" on the row:
    * Note that in the future, additional visibility conditions could be added, to allow end users to see Device Events in the End User Portal, based on "Account", "Primary Driver", and "Primary Vehicle Owner". 


  * Other Notes: 
    * N/A 



  


  


_VA: Tim Reitz 12/18/2025: Consider a warning / alert when the Device is plugged into a different Vehicle - to prompt the provider to change the Primary Vehicle if needed.

Tim Reitz 01/13/2026: This presumably would be based on Event records for the Device -- whenever an Event is registered with a VIN other than the "Primary Vehicle" VIN. 

However, I'm not sure if Traccar logs the VIN with the Event -- we need to look into this. 

Does Traccar log the VIN for Events / Notifications?

TODO_JB (research):  Tim Reitz 01/16/2026: Same question as early regarding logging VINs. The client also would like to have a notification of some sort when an OBD logs a different VIN that the linked "Primary Vehicle" VIN for that Device in Silverloom. But I realized that I'm not specifically seeing VIN details in Traccar, so I'd like some deeper digging on that.

  


Development Specification

TODO_MOCKUPS: Tim Reitz 01/14/2026: I've updated this RG spec.
