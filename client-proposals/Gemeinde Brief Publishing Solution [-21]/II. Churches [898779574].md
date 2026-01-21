2\. Churches

  


Requirements

Most of the records are associated with specific churches. Each church record has:

  


  * Church # - This is the identifying code for the church. It will either be a number (14) or a number and letter (21C). We do not require special validation. When sorting, sort first by the numeric value, then by the letter. (Alternatively, you can simple left-pad the Church # with 0's for sorting.)
  * Church Name - Required
  * Schedule - Required; list of:
    * A
    * B
  * Reporter Contact
    * Name
    * Address
    * City
    * State
    * Zip Code
    * Phone No
    * Fax No



  


When you delete a church, it should delete all the associated magazine entries. Add a prompt before deleting, and delete all related magazine entries.

  


Any Publication Date in the system should be a drop-down list (fields and ask prompts), with entries as "October 30, 2019" (actual publication date). Show entries for alternating weeks. The publication date should default to the next publication date until the day before publication, when the default publication date automatically jumps 2 weeks into the future. For example:

  * On Monday, October 28, 2019, the default publication date should be October 30, 2019.
  * On Tuesday, October 29, 2019, the default publication date should be November 13, 2019.



  


Development Specification

Matthias Miller 06/12/2020: 

  * Goals for July:
    * Schedule call on or after 15th
    * Have design finished by 27th
    * End of July, have the design to you..



  


Matthias Miller 06/12/2020: 

High level of urgency:

  * Software is in really bad shape right now
  * Design the whole thing, then develop what they have now


