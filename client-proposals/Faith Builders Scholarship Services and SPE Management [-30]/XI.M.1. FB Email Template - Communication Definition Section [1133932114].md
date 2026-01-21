11.13.1. FB Email Template - Communication Definition Section

Communication Definition section:

  * Name (uneditable)
  * Department (required; drop list of "FBSS" and "FBSPE"; defaults to blank; the "From" email address sets for emails based on this selection)
  * Level (required; drop list of the following list items:
    * Contact
    * Member Applications
    * SPE Approval) 
  * Evaluate Template from Email Record (checkbox)



  


Validations:

_TR Austin Priest 10/04/2024: It is not possible to cause these validations since when you change the level the body and subject clear and if you check the Evaluate Template from Email Record checkbox the body and subject also clear. Maybe should note those behaviors above instead.

TODO_NM: Tim Reitz 02/24/2025: Could you take a look at this? 

  * Error on save:
    * If Evaluate Template from Email Record is not checked and Level has been changed without clearing Subject and Body.
    * If Evaluate Template from Email Record is checked without clearing Subject and Body.


