11.12.4. SPE Online Submission - Online Submission Business Information Section

Online Submission Business Information (visible for businesses):

  * Business Name (plain text)
  * EIN (auto-formats with dashes)
  * Entity Type (drop-list of entity types)
  * Owner SSN (number; auto-formats; displays in green text if it matches the value from the Linked Member Contact; visibility & editability based on the following requirements: 
    * if field is blank: visible and editable for all users until the first save after the field has been filled; after the first save, this field becomes read-only, displaying only the last 4 digits; 
    * if field is not blank: for users with the "Can view saved sensitive data" permission: an ellipsis button is displayed next to the last 4 digits, to view/edit the full number)
  * PA Revenue ID



  


Validation:

  * Error: if EIN is not 9 digits long or contains any other characters than digits and dashes.
    * Error Message if does not contain 9 digits: "The EIN should be 9 digits long."
    * Error Message if contains other characters: "Invalid EIN."
  * Error: if SSN is not 9 digits long or contains any other characters than digits and dashes. 
    * Error Message if does not contain 9 digits: "The SSN should be 9 digits long."
    * Error Message if contains other characters: "Please enter a valid SSN."



  


Additional Notes:

  * Text values for all fields are displayed in green if they match values from the Linked Member Contact.
  * Note that the full SSN is not tracked in Activity History, but the "last 4" is tracked.


