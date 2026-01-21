7.2.6. Contact - GemWood Internal Section

  


Requirements

The Contact record also includes the following custom section and fields: 

  


  * GemWood Internal section (visible if "Contact Type" = "Internal"):
    * View Internal Fee Payouts for Contact (link; visible to users with the "Manage Financials" Permission; opens the "Internal Fee Payouts by Contact" report, filtered to the current Contact)



  


  * Other Validations: 
    * Warning on Save, with the following details: 
      *  if the Contact is selected on the "Internal Fee Payouts Configuration" embedded spreadsheet in Silverloom Settings and one of the following is true: "Contact Type" ≠ "Internal" or "Active" checkbox is not checked;  
      * message: "This contact has been deactivated or changed from "Internal" to another Type, and needs to be removed from the Internal Fee Payouts Configuration in Silverloom Settings."; 
      * note that the purpose of this warning is to alert the user that a Contact listed on the "Internal Fee Payouts Configuration" embedded spreadsheet in Silverloom Settings has been deactivated or has been changed to a different Contact Type, and therefore needs to be removed from the configuration to prevent it from receiving further internal fee payouts.)



  


Development Specification

BID: 2 HOURS
