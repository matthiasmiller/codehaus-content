5.4. Claim Record

  


Requirements

*Done. 

  


Overview: This is a custom record type, used to track Claims for Vehicle-related accidents or incidents. Claim records are used to track Vehicle and Owner/Driver details, accident/incident details, settlements, and payouts.

  


Accessed via:

  * All Claims Report 
  * My Client Claims Report 
  * Home | Claims | New Claim (opens a new blank Claim record, with the default fields set) 
  * "View / Create Claims" link on Vehicle records (opens a filtered version of the Claims report) 



  


Sections and Fields: See the following sub-sections of this living spec. 

  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (User ID, date, and time stamp) 
  * Last Modified: (User ID, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: The Claim record is visible to the following:
    * All admin users
    * Current agent for the "Client" on the Claim record (this is the "Current Agent") 
    * Current agent for the "Originating Owner" on the Claim record (this is the "Orig. Owner Agent")
    * Current checkbook holder for the "Originating Fund" on the Claim record
  * Editability: The Claim record is editable for the following:
    * All Admin users
    * Current agent for the "Client" on the Claim record (this is the "Current Agent") 
    * Current checkbook holder for the "Originating Fund" on the Claim record 



  


Special Considerations: 

  * Copy Record: Disallowed.
  * Delete Record: Allowed for Admin users, with no limitations. 
  * Merge Record: Disallowed.



  


Other Notes: 

  * N/A



  


Development Specification

Change Requests: 

  * See sub-sections for changes specific to those sections/fields.



  


Other Notes:

  * Some old Claim IDs were generated using a previous numbering convention:
    * Client number
    * Numeric ID of the claim
    * Accident date
    * The agent code from the client's agent.



TODO_VA: Tim Reitz 08/15/2025: This is PA-specific. Probably move to a special section in the ZWA living spec, once we split things apart.
