7.2.1. Contact Record - Contact Section

  


Requirements

*. 

  


  * Contact section (standard; note that one or more fields in this section have special restrictions): 



  


  * Active Contact (standard field; checkbox; defaults to checked; with the following additional details / behaviors:
    * custom editability: editable only for users with the "Full Access" Permission;
    * includes the following custom validations:
      * validate against deactivating the Contact if "Is Master Administrator" is checked - error on the field: "Contact is a Master Administrator and cannot be deactivated."; 
      * validate against deactivating the Contact if included on the "Group Admins" embedded spreadsheet for any active Account Groups - error on the field: "Contact is a Group Admin for one or more active Groups and cannot be deactivated.";
      * validate against deactivating the Contact if set as the "Account Reseller" for any active Accounts - error on the field: "Contact is an Account Reseller for one or more active Accounts and cannot be deactivated."; 
      * give a warning if the Contact is a "Reseller Rep" for any "Account Resellers" (i.e. if the "Is Reseller Rep" checkbox is checked) - warning on Save: "Contact is a Reseller Rep. Confirm that it is safe to deactivate."; 
      * validate against deactivating the Contact if the "Is Account Manager" checkbox is checked - error on the field: "Contact is an Account Manager for one or more active active Accounts and cannot be deactivated."; 
      * validate against deactivating the Contact if the "Is Driver" checkbox is checked - error on Save: "Contact is a Driver on one or more active Accounts and cannot be deactivated.")
  * This contact is inactive as of [   ] (standard; visible if "Active Contact" is not checked; on-screen message in gray font + editable date field; date toggles with "Active Contact" checkbox, defaulting to the current date when the checkbox is unchecked) 



  


  * Contact Type (standard; required; drop list of Contact Types; with the following details / behaviors:  
    * custom editability:
      * before the initial Save: editable for all users;
      * after the initial Save: editable only for users with the "Full Access" Permission;
    * custom behavior: defaults to "Individual") 
  * Is Organization (standard field; label displays as just "Organization"; checkbox; defaults to not checked; used to specify whether the the Contact is an organization or an individual) 



  


  * First Name (standard field; visible if the Contact is an individual; required; cleared if "Contact Type" is changed to one that is an organization) 
  * Middle (standard field; visible if the Contact is an individual; optional; cleared if "Contact Type" is changed to one that is an organization) 
  * Last Name (standard field; visible if the Contact is an individual; required; cleared if "Contact Type" is changed to one that is an organization) 



TODO_NM: Tim Reitz 01/30/2026: What happens to the following when the Contact's name is changed?: 

\- Name on the "Provider Traccar Logins" RG 

\- Name on the "Account Members" RG 

\- Names on the Traccar User sync record 

These matter because they get synced to Traccar (specifically the sync record), so I just wanted to make sure we're accounting for how to handle name changes when they happen (which probably won't be very frequently, so let's try to go simple for Phase 1 if special handling is needed). 

  * Display Name (standard; visible if the Contact is an individual; macro; with the following details / behaviors: 
    * custom behavior: read-only;
    * displays the contents of the "Contact Name" hidden field)
  * Contact Name (standard field; hidden; with the following details / behaviors: 
    * must be unique, as this is the unique identifier for the record; 
    * by default, 
      * if the Contact is an individual: auto-sets from "First Name", "Middle", and "Last Name", in the "Name Format" selected on the Silverloom Settings page; 
      * if the Contact is an organization: auto-sets from "Organization Name"; 
    * custom behavior: always includes line 1 of the Primary address for the Contact, inside parentheses; 
      * examples: "Smith, John (123 Some St.)" or "ABC Builders (321 Some Road)"; 
      * note that this allows for distinguishing Contacts with matching names; however, the same contact could theoretically be entered multiple times if any included data is not identical (i.e. including/lacking Middle name, spelling "Road" vs. "Rd" in the Address, etc.); 
    * cleared if "Contact Type" is changed to one that is an organization) 



  


  * Organization Name (standard; plain text field; visible if the Contact is an organization; required; cleared if "Contact Type" is changed to one that is an individual) 
  * Short Display Name (standard; hidden read-only macro; with the following details / behaviors: 
    * dynamically displays the following:
      * if "Organization" checkbox is checked: displays the following: "<Organization Name>";
      * if "Organization" checkbox is not checked: displays the following: "<First Name> <Last Name>";
    * to be used in places such as printouts and emails, where the address should not be included in the displayed name) 



  


  * Summary (standard field; optional; plain text field) 



  


  * Date of Birth (standard field; visible if the Contact is an individual; date field; with the following: 
    * custom behavior: warning on Save if visible and blank: "Date of Birth is blank.";
    * custom behavior: required if any of the "Role" checkboxes are checked - error on Save: "Date of Birth is required because this Contact is a provider and/or end user.") 
  * Age (custom; visible if the Contact is an individual; read-only macro; number; 1 decimal place; displays the age of the Contact, based on the "Date of Birth" and the current date, rounded down to the nearest 1 decimal place; note that this is rounded down so that "19.96" is rounded to "19.9" instead of "20.0") 
  * Gender (standard field; visible if the Contact is an individual; drop list of blank / Female / Male; with the following: 
    * custom behavior: warning on Save if visible and blank: "Gender is blank.";
    * custom behavior: required if any of the "Role" checkboxes are checked - error on Save: "Gender is required because this Contact is a provider and/or end user.") 
  * New Contact for Household Member (custom; visible if the Contact is an individual; link; opens a new Contact record, with "Last Name" and any/all Addresses defaulted based on the Contact from which the link was clicked)



  


Development Specification

TODO_: Tim Reitz 10/01/2025: Update standard sections/fields to match the Snippet, once that is updated/finalized: [https://zch.apphosting.zone/Detail/Edit/2?RecordType=Snippets&NumberID=-53&State=ctLVLwm53iQ&](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Snippets&NumberID=-53&State=ctLVLwm53iQ&)

  


  


  


Contact Type: 

Tim Reitz 12/22/2025: Custom editability: Per Nic, we just need to override CustomContacts_CanEditPrimaryType.
