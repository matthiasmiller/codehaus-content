4.6. Background Processes

  


Requirements

The Solution includes the following background processes (also called "scheduled tasks"). These are configured at deployment by CH/CCI.

  


  


  


Replace Device Under Warranty background process (used to quickly create a new Device Record when a Device is replaced under warranty)

  * Schedule:
    * When the Continue button is clicked on the Replace Under Warranty child screen.
  * Actions:
    * Create a copy of the Device record (not following the standard copy rules):
      * Set the Status to "Active"
      * Clear the Serial # field and set to the new Device Serial #
      * Clear the Page Counts embedded spreadsheet
      * Clear the Device ID
      * Clear the Install Date and set to the new Install Date
      * Clear the Base Charge Itemization embedded spreadsheet
      * Clear the Needs Review checkbox (if checked)
      * (If a new Initial Invoice Number is specified on the child screen) Clear the Initial Invoice Number and set to the new Invoice Number
      * Display a note beside Install Date: "Provided as a replacement under warranty."
      * TODO_IDD: review all the fields
    * Change the old Device's status to "End of Life"
    * Open the new record automatically.



  


Prepay Plans Ending Soon (used to __ TODO_IDD): 

  * Schedule: 
    * TODO_IDD
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
