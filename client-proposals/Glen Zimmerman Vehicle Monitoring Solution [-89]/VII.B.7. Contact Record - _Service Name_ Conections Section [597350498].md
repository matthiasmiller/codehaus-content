7.2.7. Contact Record - <Service Name> Conections Section

  


Requirements

*Done. (except for service name reference) 

  


  * <Service Name> Connections section (custom section): 



  


  * Church Affiliation (required; drop list of "Church Groups" list items and "Other"; with the following details / behaviors: 
    * for users with the "Edit lists" Permission, there is also the option to add a new item to the list; 
    * when changed from a non-blank value, the following field(s) are affected on the first subsequent Save: 
      * "Previous Church Affiliation": sets to the previous value of "Church Affiliation"; 
    * note that if this or "Other Church Affiliation" is changed from a non-blank value, the "Recently Changed Church Affiliations" notification is sent to certain users - see corresponding spec) 
  * Other Church Affiliation (visible and required if "Church Affiliation" = "Other"; plain text field; with the following details / behaviors: 
    * allows the user to enter an item not included in the list; 
    * when changed from a non-blank value, the following field(s) are affected on the first subsequent Save: 
      * "Previous Other Church Affiliation": sets to the previous value of "Other Church Affiliation") 



  


  * Previous Church Affiliation (hidden; auto-set and read-only list field; auto-sets to the previous "Church Affiliation" on the first Save after that field is changed) 
  * Previous Other Church Affiliation (hidden; auto-set and read-only plain text field; auto-sets to the previous "Other Church Affiliation" on the first Save after that field is changed)
  * Primary Contact (visible if the Contact is an organization; drop list of "Display Name" values for all individual Contacts; includes an ellipsis button to create a new Contact when blank, or to open the selected Contact)
  * Primary Contact For (visible if the Contact is an individual; read-only "virtual" embedded spreadsheet with the following:
    * Columns: 
      * Organization (displays the "Organization Name" of the linked Contact) 
      * View (link; displays as "Link"; opens the corresponding Account Reseller Contact record)
    * Automatically sorted by: "Organization Name" (alphabetically)
    * Buttons to add/remove rows: N/A
    * Shows 4 rows without scrolling
    * Other Notes: 
      * Automatically includes a row for each organization Contact record for which the individual is currently set as "Primary Contact")



  


Development Specification

Tim Reitz 01/19/2026: Better to put "Primary Contact" and "Primary Contact For" in the "<Service Name> Contact Details" section? Or keep them in a separate section to avoid that one too large?
