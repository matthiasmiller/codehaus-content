3.4.1. Silverloom Settings - Contact Settings Section

  


Requirements

  * Contact Settings section (standard): 
    * Name Format (required; 
      * drop list of the following items: 
        * FirstName LastName
        * FirstName MiddleName LastName
        * LastName, FirstName
        * LastName, FirstName MiddleName; 
      * Leacock Paving custom note: This will be set to "LastName, FirstName MiddleName" upon deployment (no coding needed); 
      * Leacock Paving custom note: On all printouts, names are displayed in the "First Name LastName" format, based on the "Short Display Name" for the Contact record.)  
    * Apply Changes (button; clicking this after changing the selection in "Name Format" applies the change to existing Contacts in the Solution) 
    * "You must apply changes to update existing contacts. Overridden contact names will remain unchanged." (on-screen message in gray font)



  


Development Specification

Ellis Miller 06/06/2025:

[ ] NOTE: We encourage devs to set the name format as clients will "Last Name, First Name Middle Name"
