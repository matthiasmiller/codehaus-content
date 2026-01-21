5.2.1. Contact - Contact Section

  * Contact section (standard section, with custom behaviors and custom fields):
    * Active Contact (checkbox; located above the top section header; defaults to checked; 
      * custom: visible only for non-client Contact Types; 
      * custom: note that the status for client contacts is displayed in the Contact Details section)



  


  * "Transfer all high-risk driver fees and claims for <Contact LastName, FirstName Middle>" (custom item; message in red font; visible after the first Save for a new Client-type Contact record created from a Household Driver of an existing Client; visible until the "Transfer" button is clicked - see corresponding spec)
  * Transfer (custom item; button; with the following details / behaviors:
    * visible after the first Save for a new Client-type Contact record created from a Household Driver of an existing Client;
    * visible until clicked;
    * clicking this button runs the "Transfer Fee & Remove Driver from Contact" Automatic Process (see corresponding spec);
    * note that after this process runs, the page needs to be refreshed) 
  * Contact Type (required; drop list of Contact Types; standard field; see below for custom validations for this field: 
    * Error on change if changed and the client has more No-Charge Vehicles than the new Contact Type allows: "This client has more No-Charge vehicles than the Client Individual Contact Type allows. Reduce the number of No-Charge vehicles before changing the client's Contact Type."
    * Error on Save if changed to a non-client type and the Contact has any uninvoiced Contact ("High-Risk Driver") fees: "You cannot change this client to a non-client type contact because this client has uninvoiced fees."
    * Error on Save if changed to a non-client type and the Contact has any unpaid Contact ("High-Risk Driver") fees: "You cannot change this client to a non-client type contact because this client has unpaid invoices."
    * Error on the field if changed to a non-client type and the Contact has one or more active Vehicles: "You cannot change this client to a non-client type contact because this client has one or more active vehicle(s)."
    * Error on the field if changed to a non-client type and the Contact has any uninvoiced Vehicle Fees: "You cannot change this client to a non-client type contact because this client has uninvoiced fees."
    * Error on the field if changed to a non-client type and the Contact has any unpaid invoices: "You cannot change this client to a non-client type contact because this client has unpaid invoices."
    * Error on the field if changed to a non-client type and the Contact is marked as "Snoozed": " You cannot change this client to a non-client type contact because this client is snoozed."
    * Error on the field if changed to a non-agent type and the Contact has any active clients: "You cannot change this In-State Agent to another contact type because this agent has active clients."



TODO_BR: Tim Reitz 12/10/2025: This validation is not working correctly - let's write up a CR to have it fixed to match the spec. 

While we're at it, let's double check the other custom validations on the Contact Type field here, to see if any of the others are malfunctioning. 

  * Warning on Save if changed to a non-agent type and the Contact is a "Checkbook Holder" for a Fund: "You are about to change the Contact Type for this In-State Agent who is the checkbook holder for the following Fund: <FundName>. Deactivate the Fund after making this change.") 



  


  * Organization (checkbox; defaults to not checked; uses to specify whether the the Contact is an organization or an individual; standard field)
  * First Name (visible if the Contact is an individual; required; standard field) 
  * Middle (visible if the Contact is an individual; optional; standard field) 
  * Last Name (visible if the Contact is an individual; required; standard field) 
  * Display Name (visible if the Contact is an individual; if "Override Name" checkbox is not checked, this is auto-set and read-only, displaying the Contact's name in the Name Format selected in Silverloom Settings; if "Override Name" checkbox is checked, this becomes editable; standard field)
  * Override Name (visible if the Contact is an individual; checkbox; defaults to not checked; checking this makes "Display Name" editable; standard field)
  * Congregation (custom field; required; drop list of Congregations; defaults to blank)
  * Organization Name (visible if the Contact is an organization; required; standard field) 
  * Organization (visible if the Contact is an individual; embedded spreadsheet that allows the Contact to be linked to multiple organizations/businesses; standard field)
  * Date of Birth (visible if the Contact is an individual; date field; standard field)
  * Gender (visible if the Contact is an individual; drop list of blank / Female / Male; standard field) 



  


  


Other Notes: 

  * The following standard field(s) are hidden in this Solution: 
    * Summary (optional; plain text field; standard field)


