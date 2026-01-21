16.2.1. Weight Entry

  


Requirements

This feature is used to assign weights to animals. The details on how this will work would be worked out during in-depth design.

  


Development Specification

TODO_IDD: 

  * Option 1:
    * Have an editable report of all dogs:
      * Serial (read-only)
      * Date (editable)
      * Weight (editable)
      * Person (default to current user?)



  


  * Option 2:
    * Same thing, but with a button for "Find Dog" that prompts for:
      * Serial (list of active dogs)
      * Date (editable)
      * Weight (editable)
      * Person (list of employees)
      * This would simply be another way of updating the row in the report. The user would have to click the button, enter the weight, click continue, then click the button again to enter the next one.



  


  * Option 3:
    * Create a Mass Weight Entry record
      * ID (autonumber)
      * Applied (checkbox; read-only)
      * Embedded spreadsheet of (editable if not applied):
        * Serial (list of active dogs)
        * Date (editable)
        * Weight (editable)
        * Person (list of employees)
      * Apply button
        * Requires saving the record, then runs a process to:
          * Copy all the weights to the respective animals
          * Flag the record as "Applied", making it read-only
      * Consider:
        * Validation against edit collisions



  


  * Option 4: TODO_ - Do we need to do mass actions / dosages? If not, it would be brilliant if we could keep these on a per-animal basis, or even have a way to edit a single litter at a time, but edit dosages on a per-animal basis.


