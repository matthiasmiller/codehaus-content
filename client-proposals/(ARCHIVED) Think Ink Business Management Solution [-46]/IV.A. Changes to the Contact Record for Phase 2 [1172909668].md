4.1. Changes to the Contact Record for Phase 2

  


Requirements

TODO_CH: Tim Reitz 02/16/2023: Merge into the main Contacts section above. 

  


The following custom fields will be added to the Contacts record to facilitate the syncing process:

  


In the Classic Accounting Notes section: Add the following fields:

  * CA Sales Rep ID (read-only; stores the 36-character Sales Rep ID from Classic Accounting as a list field. For Customers, this is the default sales rep. For Employee, this is the Sales Rep ID that identifies this employee.)
  * Classic Accounting Modify Date (read-only)
  * Classic Accounting Modify Time (read-only)



  


In the Addresses section: Add the following columns to the existing Address table:

  * Classic Accounting ID (number)
  * Classic Accounting Modify Date
  * Classic Accounting Modify Time



  


Development Specification

Ellis Miller 09/22/2022: Not sure the address fields even need to be visible. One option is to only show them in the MRG.
