3.3.3.3. Vehicle - Fees and Credits Section

  


Requirements

*Documented. Tim Reitz 08/19/2025

  


Make the following changes (changes noted with blue and strike-through): 

  


Fees and Credits section: Make changes to the below column in the "Fees & Credits" embedded spreadsheet:

  


  * Fee Type (required; drop list of "Entry" (conditionally visible, see details) / "Premium"; defaults to blank; clears if "Coverage Type" is cleared; with the following additional behaviors: 
    * includes the following visibility conditions for the "Entry" option:
      * if "Coverage Type" = "Collision": "Entry" is included if Solution uses Collision Entry Fee;
      * if "Coverage Type" = "Cargo": "Entry" is included if Solution uses Cargo Entry Fee) 
    * for Admin users: fully editable until the row is linked with an Invoice or after save if "Credit Action" is set to "Credit", at which point it becomes read-only; 
    * for non-Admin users: auto-set and read-only)



  


Note that the full spec is no longer included here, since there are lot of changes happening to this Fees & Credits section in various Change Requests, and since there are some updates happening to the living spec along the way, so it seems less complicated for this to include only the column that is receiving changes in this project.

  


Development Specification

Tim Reitz 03/18/2025: Note that there are many other changes happening to the Fees & Credits RG specced in other "Pre-ZWI" CR(s). Those changes mainly affect the "Credit Action" column and other misc. things, so there shouldn't be conflict between those changes and these changes to the "Fee Type" column, but I wanted to mention it here. 

  


Ellis Miller 09/05/2024: 

  


2 Hours

[ ] Change VehicleFeesFeeTypeList to Fee Type so that we conditionally show Entry based on the Vehicle's setting
