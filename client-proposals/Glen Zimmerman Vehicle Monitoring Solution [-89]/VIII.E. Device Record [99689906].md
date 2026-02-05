8.5. Device Record

  


Requirements

*Done. 

  


Overview: This is a custom record type, used to track a Device. A Device can be linked to only one Account, one Primary Driver, and one Primary Vehicle at a time. 

  


Accessed via:

  * Devices reports
  * Providers | Devices | New Device (opens a new Device record) 
  * Administrators | Device Management | New Device (opens a new Device record) 



  


Sections and Fields: The sections and fields for this record are specced out in sub-sections below.

  


Data Access: 

  * Visibility: Visible to all users, with some sections / fields hidden:
    * All users with the "Full Access" Permission can view everything. 
    * The "Assigned Reseller" (when applicable) and "Upline Provider Roles" for the linked Account can view almost everything. 
    * Other users can view the main record, with various things hidden. 
  * Editability:
    * For new, unsaved records: Editable for all users; 
    * For saved records: 
      * All users with the "Full Access" Permission" can edit everything. 
      * The "Assigned Reseller" (when applicable) and "Upline Provider Roles" users for the linked Account can edit everything. 
      * Note that this could be changed in Phase 2 or at some other point in the future, to allow other providers some limited editing. 



  


Special Considerations: 

  * Copy Record: Disallow
  * Delete Record: Allow if "Device Status" = "Decommissioned" and no linked Events information exists.
  * Merge Record: Disallow



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.  
  * Unless otherwise noted, all fields that become hidden for any reason retain their values. If they should be cleared, that is noted specifically in the field specs.
  * Heading color (custom): This record type uses a light green color for section headings.
  * Main workflows / channels for obtaining OBD Devices:
    * Standard: The main office orders a batch, enters them into Silverloom (not synced to Traccar yet), and keeps them in "General Inventory". When a Reseller or Group Admin requests some devices, the main office selects the devices, set the "Assigned Reseller" in Silverloom, and ship them off.
      * Main office can add Devices via the "New Device" option on the "Administrators" menu.
        * Optional add-on / future feature: Main office can batch-add Devices via the "New Devices Batch Entry" new records report (see corresponding spec)
      * Main office can assign Devices to a Reseller individually by opening the Device record or in a batch via the "Assign Devices to Reseller" report (see corresponding spec)
      * Resellers can select from their assigned Devices via the "Available Devices" report (see corresponding spec)
    * Reseller-Initiated: A Reseller or Group Admin purchases devices on their own and enters them into Silverloom, at which point "Assigned Reseller" is required. These remain as reseller inventory until linked with an Account.
      * This is done via the "New Device" options in various places: 
        * on the "Providers" menu, 
        * on the main "Devices" reports, 
        * on the "Available Devices" report.
    * Group Admin-Facilitated: A Group Admin has their own inventory (with "Assigned Reseller" set to themselves) and provides a device to a person, who takes it to a Reseller. In this case, the Group Admin should change the "Account Reseller" at hand-off to the person, to allow the Reseller to edit / set it up, and for traceability .
      * This functions like the "Reseller-Initiated" approach.
    * End User-Initiated (rarely happens): A person buys their own device and brings it to a Reseller or Group Admin for setup. 
      * The goal would be to avoid this approach, but if it happens, it would function like the "Reseller-initiated" or "Group Admin-Facilitated" approaches.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=1724244723#gid=1724244723](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=1724244723#gid=1724244723)
