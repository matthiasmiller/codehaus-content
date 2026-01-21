6.6. Background Processes

  


Requirements

The Solution includes the following background processes (also called "scheduled tasks"). These are configured at deployment by CH/CCI.

  


Agreements Pending Over 1 Week (used to set the report alert to remind users of Managed Service Agreements that have had the status of "Pending" for over a week):

  * Schedule:
    * Nightly at 2:00am 
  * Actions:
    * Finds all Managed Service Agreements that have had the status of Pending for more than a week. 
    * Sets the Agreements Pending Over 1 Week report alert (see corresponding section of the proposal).



  


Agreements Needing Renewal (used to set the report alert to remind Sales Reps users of Managed Service Agreements that need to be renewed):

  * Schedule:
    * On the 1st of every month at 2:00am 
  * Actions:
    * Finds all Manage Service Agreement records that have at least one Printer Device on them and have the Agreement Renewal Due Date within two months of the current date.
    * Sets the Agreements Needing Renewal report alert (see corresponding section of the proposal).



  


Renew Agreement (used to manually mark Managed Service Agreement records): 

  * Schedule: 
    * When the "Renew Agreement" button is clicked on an Agreement record
  * Actions: 
    * TODO_IDD



  


Sample (TODO): 

  * Schedule: 
    * TODO
  * Actions: 
    * TODO



  


Development Specification

  * Commands: 



TODO_ : Tim Reitz 09/07/2023: include the commands here.

  


TODO_IDD: Tim Reitz 11/22/2023: Add note in deployment incident to set them up.
