5.1.3. Proposal Note Record

  


Requirements

Overview: The Proposal Note record is a custom record, and is used to configure default text for the Proposal Notes feature on Proposals.

  


Accessed via: Configure Proposal Notes report

  


Sections and Fields: 

  * Proposal Note section:
    * Active (checkbox; defaults to checked)
    * Note Text (required; plain text; validate against duplicates)
    * Sort Order (required; number; 0 decimals; used to determine the sequence in which Proposal Note items are displayed, i.e. on the selection drop list on the Proposal record; in the case of duplicate "Sort Order" numbers, secondary sorting is done based on the "Note Text")



  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access: All users can view and edit

  


Special Considerations:

  * Copy Record: N/A (disallowed)
  * Delete Record: Allow deletion until the record has been referenced by another record, then disallow. 
  * Merge Record: N/A (disallowed)



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=513170788#gid=513170788](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=513170788#gid=513170788)

  


Ellis Miller 06/10/2025: 

[ ] Simple lookup record with one additional field.

2 Hours
