11.2.12. Contact - Postcards Section

  


Requirements

Postcards section (visible if "Postcard" checkbox is checked):

  * Use Different Name And Address (checkbox; controls editability for name and address fields in the section)
  * Name (defaults to Name for businesses, or First + Middle + Last name for individuals)
  * Address (defaults to the contact's address) 
  * Logo (memo)
  * Community Message (memo)



  


Validation:

  * Error: if Anonymous Donor and Use Different Name and Address are both checked.
    * Error Message: "Post card details cannot be overridden for anonymous contacts. (Field: Anonymous Donor)"



  


Development Specification

TODO_NM: use title case in label for ContactPostcardOverrideDefaults ("And" should not be capitalized).
