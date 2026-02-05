24.12. Users: Allow Group Admins & Primary Reseller Reps to Set Up Users

  


Requirements

*Done. 

  


In Phase 1, only Master Administrators can set up Silverloom users. 

  


In the future, additional coding would could be done to build a feature that would allow Group Admins and Reseller Admins to set up Silverloom users, probably via an automatic process.

  


Development Specification

Tim Reitz 01/15/2026: Request submission -- prompts for the necessary fields, sends a notification to the Master Administrators, who can open a report to view the request and click a button to set up the User Profile. 

  * Technical notes: 
    * RG (hidden?) on the Contact record of the person making the request, with all of the fields as columns + "Request Date" \+ "Approved" (list of Approved / Denied / blank) + "Approved By"; 
    * Report Alert for Master Administrators 
    * Report would show all blank & denied; 
    * Button on the report would run an x30list to set up the User Profiles and set the fields on the RG. 
    * Nic is thinking this could be $1K-2K (don't necessarily share with client)


