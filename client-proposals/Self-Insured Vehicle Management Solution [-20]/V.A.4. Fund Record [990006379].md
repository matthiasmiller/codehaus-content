5.1.4. Fund Record

*Done. 

  


Overview: This is a custom record type, used to store fund information.

  


Note that a "Fund" corresponds to a checking account primarily managed by a single person, called the "Checkbook Holder" (could also be called a "Fund Manager"). One or multiple agents can operate under / out of a given Fund.

  


Accessed via: Advanced | Configuration | Configure Funds

  


Sections and Fields: 

  * Checkbook Holder (required; drop list of active In-State Agents; with the following details / behaviors:
    * when changed, the following field(s) are affected:
      * "Fund Name": set to the Checkbook Holder's "Agent Code" plus "FUND"; 
    * error on save: if the Checkbook Holder is already assigned to an active Fund: "<FundCheckbookHolder> already has an active fund and therefore cannot be linked to this one. (Field: Checkbook Holder)"; 
    * error on save: if the Fund is deactivated and is set as the Agent Fund for an active In-State Agent: "This fund cannot be deactivated because it is set as the Agent Fund for the following active In-State Agent(s): <comma-separated list of Agents> (Field: Active)")
  * Active (checkbox; defaults to checked; error on save: if the Fund is active and the checkbook holder is not an active agent: "The checkbook holder is not an active agent. (Field: Checkbook Holder)")
  * Fund Name (editable; initially set when the "Checkbook Holder" is set - see corresponding spec ) 



  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (User ID, date, and time stamp) 
  * Last Modified: (User ID, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access:

  * View, edit and delete: Admin



  


Special Considerations: 

  * Copy Record: Allowed
  * Delete Record: Allowed when not active
  * Merge Record: Allowed



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.


