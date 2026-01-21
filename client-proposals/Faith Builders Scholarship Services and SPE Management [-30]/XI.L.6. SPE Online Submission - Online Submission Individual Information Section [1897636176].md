11.12.6. SPE Online Submission - Online Submission Individual Information Section

Online Submission Individual Information (visible for individuals):

  * SSN (number; auto-formats; displays in green text if it matches the value from the Linked Member Contact; visibility & editability based on the following requirements: 
    * if field is blank: visible and editable for all users until the first save after the field has been filled; after the first save, this field becomes read-only, displaying only the last 4 digits; 
    * if field is not blank: for users with the "Can view saved sensitive data" permission: an ellipsis button is displayed next to the last 4 digits, to view/edit the full number)



  


Validation:

  * Error: if SSN is not 9 digits long or contains any other characters than digits and dashes.
    * Error Message if does not contain 9 digits: "The SSN should be 9 digits long."
    * Error Message if contains other characters: "Please enter a valid SSN."



  


Additional Notes:

  * Text value for the field is displayed in green if it matches values from the Linked Member Contact.
  * Note that the full SSN is not tracked in Activity History, but the "last 4" is tracked.


