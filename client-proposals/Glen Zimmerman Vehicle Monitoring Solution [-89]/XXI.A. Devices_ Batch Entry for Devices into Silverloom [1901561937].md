24.5. Devices: Batch Entry for Devices into Silverloom

  


Requirements

*Done. 

  


Overview: This is a special report used to batch-enter OBD Devices into Silverloom after the <Service Name> main office has purchased a batch. 

  


Accessed from: Administrators | Device Management | New Devices Batch Entry (opens the report directly, bypassing any filters) 

  


Title: "New Devices Batch Entry"

  


New Records Details:

  * Source Record Type: N/A
  * Source Record Subset: N/A
  * Source Repeating List: N/A 
  * New Record Fields and Values:
    * Device Type (defaults to "OBD-II") 
    * Device ID (editable; required) 
    * SIM Card ICCID (editable) 
  * New Record Match On (unique identifying fields): "Device ID"



  


Columns: See the items and descriptions under "New Record Fields and Values" above.

  


Grouped by: N/A

  


Sorted by: N/A

  


Filters: 

  * N/A



  


Buttons: 

  * Finish (clicking this button creates and saves a new record for each row with data, and takes the user to the default follow-up screen that shows the number of records saved) 



  


Other Notes: 

  * N/A



  


Development Specification

Tim Reitz 01/20/2026: Per Nic, would require some research, but likely would be 4-8 hours to build one and make sure it's working correctly. 

  


Finish" button: (internal note that we can set a redirect post-save - e.g. to a report, show the default screen (i.e. # of records saved, etc.), or show a custom stock message) 

  


(Internal note: New Record Match On should be a list of fields that uniquely identify the record, to avoid creating new records that duplicate one that already exists in the database.)

  


Sample in testzch: [https://testzch.apphosting.zone/Reports/Standard/Designer/Std_Create?Asks=AskType%3D%22Field%22%2CAskParentID%3D7.00&State=Tr1GcI4u7tA](https://testzch.apphosting.zone/Reports/Standard/Designer/Std_Create?Asks=AskType%3D%22Field%22%2CAskParentID%3D7.00&State=Tr1GcI4u7tA) .
