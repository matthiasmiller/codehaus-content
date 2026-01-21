11.2.13. Contact - EITC Section

  


Requirements

EITC section (visible if the "EITC" checkbox in the Contact Details section is checked):

  * Entity Type (drop-list of BusinessEntityTypes)
  * NAICS (Bus. Code) (number)
  * Incorporated In PA (checkbox)
  * FEIN (auto-formats)
  * Registered in PA (checkbox)
  * PA Revenue # (optional; plain text; if not blank, may not be more than 10 digits long and may not contain characters other than numbers and dashes)
  * Pass-through Entity (checkbox)
  * Municipality (plain text)
  * Enterprise Type (RG; drop-list of BusinessEnterpriseTypes)
  * Tax Year End Month (drop-list of months)
  * Tax Year End Day (number; must be a valid day of the month)
  * CEO First (uneditable; displays the first name of the first contact in the Related Contacts RG with CEO checked, if no such rows are found, returns the hidden CEO First Name field from the merge)
  * CEO Last (uneditable; displays the last name of the first contact in the Related Contacts RG with CEO checked, if no such rows are found, returns the hidden CEO Last Name field from the merge)
  * CEO Title (uneditable; displays the Title of the first contact in the Related Contacts RG with CEO checked, if no such rows are found, returns the hidden CEO Title field from the merge)
  * Contact First (uneditable; displays the first name of the primary related contact if there is one, otherwise displays the hidden Contact First Name from the merge)
  * Contact Last (uneditable; displays the last name of the primary related contact if there is one, otherwise displays the hidden Contact Last Name from the merge)
  * Contact Title (uneditable; displays the Title of the primary related contact row if there is one, otherwise displays the hidden Contact Title from the merge)



  


Validation:

  * Error on change: if FEIN does not contain exactly nine digits.
    * Error Message: "The FEIN should be 9 digits long."
  * Error on change: if FEIN contains any characters other than digits or dashes.
    * Error Message: "Invalid FEIN."
  * Error on change: if PA Revenue # contains any characters other than digits or dashes.
    * Error Message: "Please enter a valid PA Revenue #."
  * Error on change: if PA Revenue # contains more than ten digits.
    * Error Message: "The PA Revenue # should not be more than 10 digits long."



  


  


TODO_JK: Tim Reitz 10/01/2024: (found by Austin) We have 2 fields that seem to be the same:

  * Member Details section (section is visible if Eligible for SPE is checked): PA Revenue ID (number; visible and required if Contact Type = "Business" and the selected Entity Type = "LLC - filing as S Corp", "S Corp", or "C Corp"; must be 10 digits long and normally should begin with a "1") 



  


  * EITC section (section is visible if the "EITC" checkbox in the Contact Details section is checked): PA Revenue # (optional; plain text; if not blank, may not be more than 10 digits long and may not contain characters other than numbers and dashes)



  


Are these duplicates? They have almost the same name, and very similar validations, but aren't identical. 

Also, it is possible to have just one or the other visible, or both visible at the same time for a Business:

  * Just the first: If "Eligible for SPE" is checked and Entity Type  = "LLC - filing as S Corp", "S Corp", or "C Corp". 
  * Just the second: If "EITC" checkbox is checked.  
  * Both: if both sets of conditions above are true.



  


Development Specification

TODO_NM: Change to > and update parameter order.

Validate:If( Length( KeepOnlyDigits( ContactBusinessPARevenueNum)) <= 10

           , ""

           , "ERRORONCHANGE:The PA Revenue # should not be more than 10 digits long."

           )
