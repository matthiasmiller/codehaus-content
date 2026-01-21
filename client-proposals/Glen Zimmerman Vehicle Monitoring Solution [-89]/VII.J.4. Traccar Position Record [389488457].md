7.10.4. Traccar Position Record

  


Requirements

TODO_JB (research): Tim Reitz 09/17/2025: Are we doing this as a record, or an RG on the Silverloom Device record? or not storing it at all in Silverloom (due to quantity / space concerns)? [see conversation below] 

  


Tim Reitz 09/15/2025: Are we going to be creating a record for every single Position? Or maybe a record with an RG instead? (though do RGs eventually get slow with hundreds of thousands or millions of rows?) Or, does our API connection with Traccar just pull the "most recent" Position every X minutes to display here / to store it on a linked record? (and users would need to go to Traccar for full reporting)

Tim Reitz 09/15/2025: Per Nic, it seems scary to report on an RG with millions of rows. Likely would be best to slow things down and pull from Traccar every 3 minutes, then give the user a link to reporting in Traccar. 

TODO_JB: Tim Reitz 12/08/2025: Consider this more once we have more data / details from Traccar / JB. 

  


TODO_JB (research): Tim Reitz 09/18/2025: We need to find out how long Traccar retains data -- do they dump it after a certain point? If so, Glen would probably want to pull certain important/critical data out and store it in Silverloom. 

  


Overview: This is a custom record type, used to store information about "__" from Traccar. This is a "sync record", not editable interactively in Silverloom.

TODO_:

  


Accessed via: __

TODO_:

  


Sections and Fields: TODO_:

  * Traccar Position Details section: 
    * ID (auto-set and read-only interactively; number; no decimals; corresponds to the __ in Traccar)
    * Device ID (auto-set and read-only interactively; number; no decimals; corresponds to the __ in Traccar; link to the corresponding __ record in Silverloom



TODO_: Traccar Device Record or "Device" record?

  * Protocol (auto-set and read-only interactively; plain text field; corresponds to the __ in Traccar)
  * Device Time (auto-set and read-only interactively; UTC date & time in the ISO 8601 format (i.e. "2019-08-24T14:15:22Z"); corresponds to the __ in Traccar)
  * Fix Time (auto-set and read-only interactively; UTC date & time in the ISO 8601 format (i.e. "2019-08-24T14:15:22Z"); corresponds to the __ in Traccar)
  * Server Time (auto-set and read-only interactively; UTC date & time in the ISO 8601 format (i.e. "2019-08-24T14:15:22Z"); corresponds to the __ in Traccar)
  * Outdated (auto-set and read-only interactively; __ field; corresponds to the __ in Traccar)
  * Valid (auto-set and read-only interactively; __ field; corresponds to the __ in Traccar)
  * Latitude (auto-set and read-only interactively; number; 6 decimals; corresponds to the __ in Traccar)
  * Longitude (auto-set and read-only interactively; number; 6 decimals; corresponds to the __ in Traccar)
  * Altitude (auto-set and read-only interactively; number; __ decimals; corresponds to the __ in Traccar)
  * Speed (auto-set and read-only interactively; number; 2 decimals; corresponds to the __ in Traccar)
  * Course (auto-set and read-only interactively; __ field; corresponds to the __ in Traccar)
  * Address (auto-set and read-only interactively; plain text field; corresponds to the __ in Traccar)
  * Network (auto-set and read-only interactively; __ field; corresponds to the __ in Traccar)
  * Geofence IDs (auto-set and read-only interactively; __ field; corresponds to the __ in Traccar)



TODO_: comma-separated list? link(s) to the corresponding Traccar Geofence Records in Silverloom?

  * Attributes (auto-set and read-only interactively; __ field; corresponds to the __ in Traccar)



  


  * Record History section (visible to __): TODO_: 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (link to open the report for the record)



  


Data Access: TODO_:  

  * Visibility: __
  * Editability: __



  


Special Considerations:

  * Copy Record: Disallowed
  * Delete Record: Disallowed
  * Merge Record: Disallowed



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


Development Specification

Mockup: N/A

  


Tim Reitz 09/15/2025: The "Route" report in Traccar appears to display data from Position records: [https://x6rildfvs.traccar.com/reports/route](https://x6rildfvs.traccar.com/reports/route).
