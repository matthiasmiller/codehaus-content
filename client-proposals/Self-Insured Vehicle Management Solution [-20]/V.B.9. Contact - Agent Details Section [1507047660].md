5.2.9. Contact - Agent Details Section

*Done. 

  


  * Agent Details section (custom section; visible if the selected Contact Type = "In-State Agent"; fields editable for Admin users only): 



  


  * Checkbook Holder (visible if the agent is set as the "Checkbook Holder" for a Fund record; link; opens the Fund record; prompts the user to save the current record before opening) 
  * Generate Agent Code (button; visible for Admin users if "Agent Code" is blank; sets "Agent Code" to the first three characters of the Contact's last name plus the first two characters of the Contact's first name, e.g. if the Contact's name is "John Smith", this sets to "SMIJO")
  * Agent Code (editable if the Contact is active; required; with the following details / behaviors: 
    * allows letters, numbers, and special characters;
    * auto-capitalizes any letters entered as lower case;
    * validates against duplicate Agent Codes: error message on Save: "Duplicate agent codes are not allowed. (Field: Agent Code)"; 
    * validates that this must be 5 characters long: error message on Save: "Agent code should be 5 characters long. (Field: Agent Code)")
  * Agent Fund (drop list of active Funds; editable if the client is active; with the following details / behaviors:
    *  validates that the linked Fund must be active: error message on Save: "Fund associated to this agent is not active. (Field: Agent Fund)"; 
    * cannot be cleared if "Contact Type" = "In-State Agent" and this field has been set: "Existing fund name cannot be blanked out.") 
  * "This agent can not have clients linked unless a fund is specified." (on-screen message in red text; visible if Contact Type = "In-State Agent" and Agent Fund is blank, or if the "Suppress all validations" System Switch is turned on)


