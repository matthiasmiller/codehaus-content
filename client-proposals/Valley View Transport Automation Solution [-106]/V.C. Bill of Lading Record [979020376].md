5.3. Bill of Lading Record

  


Requirements

Overview: This is a custom record type, used to track Bills of Lading. Note that this record is read-only. This read-only record is imported from DispatchTrack that represents a truck's full load manifest, organized by drop sequence with associated order numbers. This serves as the master reference for pullers and loaders to know which orders go on which truck and in what delivery sequence.

  


Accessed via: Bills of Lading report

  


Sections and Fields: 

  * DispatchTrack ID (i.e. "107-5326")
  * Start of Week (date)
  * Drops (embedded spreadsheet of the following:
    * #
    * Notes
    * Order #
    * reverse sorted by #)



  


  * Record History section: 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: TBD
  * Editability: TBD



  


Special Considerations: 

  * Copy Record: TBD
  * Delete Record: TBD
  * Merge Record: TBD



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.  
  * Unless otherwise noted, all fields that become hidden for any reason (based on other fields, user permissions, etc.) retain their values. If they should be cleared, that is noted specifically in the field specs, with a "clear if hidden" or similar note.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1Eo-qztGoXmt5e6q_S9lNygvSc33VJAABb9K33xWXpvQ/edit?gid=765578549#gid=765578549](https://docs.google.com/spreadsheets/d/1Eo-qztGoXmt5e6q_S9lNygvSc33VJAABb9K33xWXpvQ/edit?gid=765578549#gid=765578549)
