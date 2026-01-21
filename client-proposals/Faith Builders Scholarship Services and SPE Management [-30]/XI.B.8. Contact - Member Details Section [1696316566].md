11.2.8. Contact - Member Details Section

  


Requirements

Member Details section (visible if Eligible for SPE is checked):

  * Entity Type (drop-list; visible and required if Contact Type = "Business")
  * EIN (number; visible and required if Contact Type = "Business"; auto-formats)
  * PA Revenue ID (number; visible and required if Contact Type = "Business" and if the selected Entity Type = "LLC - filing as S Corp", "S Corp", or "C Corp"; must be 10 digits long and normally should begin with a "1")
  * Owner SSN (number; auto-formats; visible and required for businesses if the selected Entity Type is "Single Member LLC"; must be 9 digits long; visibility & editability based on the following requirements: 
    * if field is blank: visible for all users until the first save after the field has been filled; after the first save, this field becomes read-only, displaying only the last 4 digits; 
    * if field is not blank: for users with the "Can view saved sensitive data" permission: an ellipsis button is displayed next to the last 4 digits, to view/edit the full number)
  * SSN (number; auto-formats; visible and required if Contact Type = Individual; visibility & editability based on the following requirements: 
    * if field is blank: visible and editable for all users until the first save after the field has been filled; after the first save, this field becomes read-only, displaying only the last 4 digits; 
    * if field is not blank: for users with the "Can view saved sensitive data" permission: an ellipsis button is displayed next to the last 4 digits, to view/edit the full number)



  


Validation:

  * Error: if the EIN is not 9 digits long.
    * Error Message: "The EIN should be 9 digits long."
  * Error: if the EIN contains any characters other than digits and dashes.
    * Error Message: "Invalid EIN."
  * Error on save: if the PA Revenue ID is not ten digits long.
    * Error Message: "The Revenue ID should be 10 digits long. (Field: PA Revenue ID)"
  * Warning on save: if the PA Revenue ID does not begin with a 1.
    * Warning Message: "The first digit should usually be a 1 (Field: PA Revenue ID)"
  * Error: if the Owner SSN is not 9 digits long.
    * Error Message: "The SSN should be 9 digits long."
  * Error: if the Owner SSN contains any characters other than digits and dashes.
    * Error Message: "Please enter a valid SSN."
  * Warning on save: if the Owner SSN is changed.
    * Warning Message: "Owner SSN has been changed. (Field: Owner SSN)"
  * Error: if the SSN is not 9 digits long.
    * Error Message: "The SSN should be 9 digits long."
  * Error: if the SSN contains any characters other than digits and dashes.
    * Error Message: "Please enter a valid SSN."
  * Warning on save: if the SSN is changed.
    * Warning Message: "SSN has been changed. (Field: SSN)"



  


Other Notes: 

  * Note that the full SSN is not tracked in Activity History, but the "last 4" is tracked.



  


Development Specification

TODO_NM: WSGIEvaluate... and WSGIValidation... macros should use Ifs.
