5.2.8. Contact - Household Drivers Section

*Done. 

  


  * Household Drivers section (custom section: visible if the selected "Contact Type" for the record has "Client?" = "Yes"): 
    * Household Drivers (no label; embedded spreadsheet with the following:
      * Columns: 
        * First Name (plain text; required - error message on Save: "Household Driver First Name is a required field.")
        * Middle Name (plain text)
        * Last Name (plain text; required - error message on Save: "Household Driver Last Name is a required field."; defaults to the last name on the current record)
        * Date of Birth (date; required - error message on Save: "Date of Birth is not specified for one or more household driver(s).")
        * Notes (plain text)
      * Automatically sorted by: N/A
      * Buttons to add/remove rows: "✚" / "🞭"
        * Drivers cannot be deleted if set as the "Primary Driver" for any active Vehicle ("🞭" button is hidden).
        * No rows can be added before the Contact record has been saved for the first time ("✚" button is hidden).
      * Show 4 rows without scrolling
      * Other Notes:
        * A read-only row is automatically added, with "First Name" and "Last Name" defaulted the Contact's name. This row cannot be deleted.
    * "* First row is for client and can neither be deleted nor edited." (on-screen message) 
    * "* Drivers cannot be deleted if assigned as the Primary Driver for any active vehicle." (on-screen message)


