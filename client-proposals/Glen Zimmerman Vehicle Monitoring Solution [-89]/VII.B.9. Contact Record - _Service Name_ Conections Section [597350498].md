7.2.9. Contact Record - <Service Name> Conections Section

  


Requirements

*Done. (except for service name reference) 

  


  * <Service Name> Connections section (custom section): 



  


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

  


TODO_VA: Tim Reitz 01/19/2026: The following are noted in History as RGs that I was deciding to switch to report links:

  * Admin for Account Group(s)
  * Primary Driver for Device(s)
  * Account Manager for Account(s)
  * Account Manager for Devices 
  * Linked Drivers for Account(s)



Did I do that?
