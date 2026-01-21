5.3.3.2. Customer & Job Information Section - Main Fields

  


Requirements

  * Customer (required; with the following details / behaviors:
    * drop list all active Contacts (displaying the "Display Name"); 
      * note that this includes more than only Customer-type Contacts, to allow for easily setting up a Proposal record for another Contact who is already in the database, i.e. employee or referring party; however, there is a validation on Save to ensure that the selected Contact has "Customer" as a Contact Type - see below spec;
    * when set / changed, the following other fields are affected:
      * "Job Contact": auto-sets to blank unless there is only one Job Contact on the Customer's Contact record, in which case it sets to that Job Contact - see corresponding spec; 
      * "Sales Rep": if any other Proposal records exist for the same Customer, auto-sets to the "Sales Rep" on the most recent one, regardless of that Proposal's Status - see corresponding spec; 
      * "Lead Information Required" checkbox: if any other Proposal records exist for the same Customer, automatically unchecks - see corresponding spec; 
      * "Lead Source": if any other Proposal records exist for the same Customer, auto-sets to "Previous Customer" - see corresponding spec);
    * error on Save if the selected Contact does not have "Customer" included as a "Contact Type": "Customer: Selected contact is not a customer. Open the Contact record and select "Customer" as an additional Contact Type.";
    * warning on the field if changed at any point after the initial Save: "Changing the Customer affects Proposal details.")



  


  * Previous Customer (read-only macro; checkbox; with the following details / behaviors:
    * underlying name is "Has Other Proposal", to allow for clear identification, and easy changing of the label in the future if separate tracking is desired for "Previous Lead" (this) vs. "Previous Customer";
    * displays as checked if any other Proposal records exist with "Customer" = the currently-selected Contact) 
  * New Customer (visible if "Customer" is blank; link; with the following details / behaviors: 
    * opens a new Contact record with "Contact Type" = "Customer"; 
    * user note: if a person/company who is not an existing Customer calls, the user should click this link, enter the basic (required) details on the new Contact record and save it, then come back to the new Proposal record and select the new Contact from the Customer drop list) 
  * View/Edit Customer (visible if "Customer" is not blank; link; same location as the "New Customer" link; opens the selected Contact record) 
  * Customer Address (read-only macro; displays the Primary address for the Customer, in the standard multi-line format without the addressee name) 
  * Customer Phone (read-only macro; displays the primary (top) phone number from the selected Customer's Contact record) 
  * Customer Email (read-only macro; displays the top Primary email address from the selected Customer's Contact record; displays as a link to open a new email with the email address defaulted) 
  * Preferred Contact Method (read-only macro; displays the contents of the "Preferred Contact Method" field on the selected Customer's Contact record) 



  


  * Job Type (required; drop list of Job Types list items; with the following details / behaviors:
    * if set to "Commercial" or "Sports Construction", the following field(s) are affected: 
      * "Lead Information Required" checkbox: automatically unchecked - see corresponding spec) 
  * Sales Rep (required; drop list of active Employee-type Contacts with the "Is Sales Rep" checkbox checked (displaying the "Display Name"); with the following details / behaviors: 
    * if any other Proposal records exist for the same Customer: auto-sets to the "Sales Rep" on the most recent one, regardless of that Proposal's Status, when the Customer is set - see the "Customer" field spec; 
    * if no other Proposals exist for the same Customer, this is set manually by the person receiving the lead; 
    * editable in limited editing mode) 



  


  * Job Name (plain text; with the following details / behaviors: 
    * if blank when the record is saved (meaning that it will never be saved blank):
      * if the Customer is an individual: sets to "<Customer "First Name"> <Customer "Last Name">"; 
      * if the Customer is an organization: set to "<Customer "Name">"; 
    * editable in limited editing mode) 



  


  * View Lead Information (visible after the initial Save for the record, which is also when the Lead Information section & fields are hidden via the "View / Edit Lead Information on Main Screen" checkbox; button; opens the "View Lead Information" child screen - see corresponding child screen spec)
  * Print Lead Information Sheet (visible after the initial Save for the record; link; opens the Lead Information Sheet Printout PDF for the current record in a new tab, to view, download, or print)



  


Development Specification

Ellis Miller 06/17/2025: 

[ ] Customer field:

[ ] Active contacts helper list

[ ] Job Contact - look up from the contact record

[ ] SalesRep - create a ProposalsByClientAndID.ndx ProposalsByClientAndIDLastField( BinString(Client)+"...", ProposalSalesRep)

[ ] Previous Customer - ClientHasOtherProposal(vClient, vOurID) macro that checks  ProposalsByClientAndIDFindField( BinString(Client)+"...", True, ProposalID <> OurID). Be sure to handle unsaved record correctly.

[ ] Lead Info Required - NOT ClientHasOtherProposal

[ ] Lead Source -- use ClientHasOtherProposal

[ ] error on save for customer type

[ ] Warning on change if not NewRecord.

4 Hours

  


[ ] New Customer link - use "Std Autopush New Contact.r20"

[ ] View/Edit Customer - "Std Autopush Open Contact.r20"

[ ] Customer Address - readonly macro ProposalCustomerAddress

[ ] ProposalCustomerPhone

[ ] ProposalCustomerEmail

[ ] ProposalCustomerPrefContactMethod

2 Hours

  


[ ] Job Type with behaviors

[ ] Sales Rep - use ActiveSalesReps that filters ActiveContactsByType("Employee") AND IsSalesRep

[ ] JobName - use ContactDisplayName

1 Hour

  


[ ] View Lead Information - child screen spec separately

[ ] Print Lead Info Sheet - link. Visible: Not NewRecord

1 Hour

  


\----------------
