5.1.2. Lead Source Record

  


Requirements

Overview: The Lead Source record is a simple custom record, and is used to track the source of leads / projects. 

  


Accessed via: Configure Lead Sources Report

  


Sections and Fields: 

  * Lead Source section:
    * Active (checkbox; defaults to checked)
    * Name (required; plain text field; validate against duplicates; read-only for Silverloom-supplied records)



  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to all users
  * Editability: Editable for all users 



  


Special Considerations:  

  * Copy Record: N/A (disallowed)
  * Delete Record: Allow deletion until the record has been referenced by another record, then disallow. 
  * Merge Record: N/A (disallowed)



  


Other Notes:

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked. 
  * The Solution includes one or more "Silverloom-supplied" Lead Source records that have hard-coded Names. This is reserved only for items that seem especially important, and other items can be added by users. The following items are included as Silverloom-supplied records:
    * "Previous Customer" (Explanation: This lead source is used for times when a lead has been a customer of Leacock Paving in the past.)
    * "Referral" (Explanation: This lead source is used for times when a lead has been referred to Leacock by another party (another customer, etc.).)
    * "Other" (Explanation: This lead source is used for times when the a lead gives a reason that isn't on the Lead Sources list, especially one that isn't worth adding to the list.)
  * Additional Lead Sources (beyond the "Silverloom-supplied" items) may be imported at deployment of Phase 1, and/or may be manually added. Note that for imported Proposals to match correctly, items must be included that correspond to the imported data - details to be handled in the Data Migration section of this design proposal.
    * Examples of additional Lead Sources:
      * Lancaster Business Directory
      * Craigslist
      * Facebook
      * Online
      * From previous job
      * Seen us around
      * Local
      * Yard Sign
      * Neighbor
      * WDAC Radio
      * Neighbors
      * Knows the sales person
      * Knew of us
      * Knows the owner
      * Seen Trucks
      * Seen guys on the job



  


Development Specification

Ellis Miller 06/10/2025:

[ ] Simple lookup record with 3 standard items.

2 hours

  


Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1456517693#gid=1456517693](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1456517693#gid=1456517693)
