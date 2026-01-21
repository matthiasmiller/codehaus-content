11.2.1. Contact - Contact Section

Contact section (standard): 

  * Active Contact (checkbox; defaults to filled)
  * This contact is inactive as of (date; becomes visible when Active Contact is unchecked; defaults to the current date)
  * Contact Type (required; drop list of active Contact Types) 
  * Organization (checkbox)
  * Display Name (read-only; contact name + ID number)



Tim Reitz 04/24/2025: We apparently hide the standard "Display Name" and "Override Name" fields, and have a custom macro for this. Let's document this. 

  * Name (visible and required if the Organization checkbox is filled)
  * First Name (visible and required if the Organization checkbox is cleared)
  * Middle Name (visible if the Organization checkbox is cleared)
  * Last Name (visible and required if the Organization checkbox is cleared)
  * Organization (visible if the Organization checkbox is cleared; drop list of all Active Organizations)
  * Date of Birth (date; visible if the Organization checkbox is cleared)
  * Gender (visible if the Organization checkbox is cleared; drop list of Genders)



  


Additional behaviors:

  * The organization checkbox editability is dependent upon Contact Type:
    * If the selected Contact Type supports the Organization Entity Type, it can be filled. 
    * If the selected Contact Type defaults to the Organization Entity Type, it will default to being filled and will be uneditable.
    * If the selected Contact Type support both Individual and Organization Entity Types, it will be editable and can be either cleared or filled.
    * If the selected Contact Type does not support Organization Entity Types, it will default to being cleared and will not be editable.



  


Validation:

  * Error on save: if there is no primary related contact, the record is not being modified in import, and contact type is Scholarship Organization or contact type is Business and Eligible for SPE is checked.
    * Error Message: "A primary contact is required for this contact."


