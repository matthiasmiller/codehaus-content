7.2.8. Contact Record - <Service Name> Contact Details Section

*Done. (except for service name) 

  


  * <Service Name> Contact Details section (custom section):



  


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


