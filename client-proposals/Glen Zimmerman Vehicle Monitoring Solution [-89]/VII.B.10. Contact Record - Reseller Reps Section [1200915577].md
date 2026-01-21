7.2.10. Contact Record - Reseller Reps Section

*Done. 

  


  * Reseller Reps section (custom section; visible if the Contact is an Organization and the "Is Account Reseller" checkbox is checked; editable for the linked "Reseller Admin" user(s) selected in this section and for users with the "Full Access" Permission): 



  


  * Reseller Reps (no label; embedded spreadsheet with the following: 
    * Columns: 
      * Name (required; drop list of "Display Name" values for all active individual Contacts in the Solution; with the following detail(s) / behavior(s): 
        * error on the field if multiple rows exist with duplicate "Name" selections for the same Reseller: "This Contact is already a Rep for this Reseller.") 
      * Reseller Admin (checkbox; defaults to not checked; with the following details / behaviors:
        * error on Save if no row is marked as Reseller Admin: "At least one Reseller Admin is required."; 
        * note that multiple Reseller Admins are allowed)
      * View (link to open the selected Contact record; displays as "Link")
    * Automatically sorted by:
      * First by: "Reseller Admin" (row(s) with "Reseller Admin" checked at the top)
      * Second by: Name (alphabetically)
    * Buttons to add/remove rows: "Add" / "Remove" (buttons are visible to users who can edit the embedded spreadsheet / section) 
    * Shows 8 rows without scrolling
    * Other Notes: 
      * On the first Save after a new row is added, the "Set User Group Based on User Role" triggered background process runs - see corresponding spec)


