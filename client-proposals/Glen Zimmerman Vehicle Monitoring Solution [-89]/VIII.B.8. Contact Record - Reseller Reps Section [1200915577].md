8.2.8. Contact Record - Reseller Reps Section

*. 

  


TODO_VA: Tim Reitz 02/04/2026: Rework design on this RG, now that it would be a virtual RG of Traccar User sync records. 

  


  * Reseller Reps section (custom section; visible if the Contact is an Organization and the "Is Account Reseller" checkbox is checked; editable for the linked "Reseller Admin" user(s) selected in this section and for users with the "Full Access" Permission): 



  


  * Reseller Reps (no label; embedded spreadsheet with the following: 
    * Columns: 
      * Name (required; drop list of "Display Name" values for all active Contacts with the "Is Reseller Rep" checkbox checked; with the following detail(s) / behavior(s): 
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
      * N/A



  


  * Contact a Master Administrator to request a login for a new Rep, or to request deactivation of a Rep's login. (on-screen message in green font; visible to the "Reseller Admin" user(s) for the Contact)


