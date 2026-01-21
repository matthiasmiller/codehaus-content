5.2.1. Contact - Standard Sections & Fields

  


Requirements

Contact Record - Standard Sections & Fields (any customizations are noted as such in the spec): 

  


  * Active Contact (checkbox above the top section header; defaults to filled; note that by default, no validations are included) 
    * Note: No custom validations are included. For Phase 1, there is not much happening on the Contact records, and deactivating a Contact should not have much or any impact on the function of the software, so any Contact may be deactivated without warning or error.



  


  * Contact section (standard section, may include custom fields):
    * Contact Type (required; drop list of Contact Types; standard field; 
      * custom behavior: a Contact may have multiple Contact Types assigned to it, meaning that if paving is done for an employee, or an "Other" contact requests an estimate, additional Types can be added to the Contact to handle this; this is based on the "Show multiple contact types" System Switch;
      * custom behavior: validate that "Employee" is not in the "Additional Contact Types" embedded spreadsheet: error message on Save: ""Employee" should be the primary Contact Type, not an additional contact type."; note that this is to facilitate excluding the street address from the Display Name for Employee-type Contacts - see the "Display Name" spec) 
    * Additional Contact Types (ellipsis button (no text label); standard feature; custom behavior: visible in this Solution; opens a child screen with the following: 
      * "Select Additional Contact Types" embedded spreadsheet with the following columns: 
        * checkbox to select additional Contact Types; 
        * Type (displays the Contact Type name; always displays one row for each active Contact Type except the one selected in the main "Contact Type" field); 
      * ellipsis button to open another child screen, with a "Stored Additional Contact Types" embedded spreadsheet with the following: 
        * Columns: 
          * Addl Type (drop list of all Contact Types; note that rows are added here automatically when the checkboxes are checked on the "Select Additional Contact Types" embedded spreadsheet) 
        * Buttons: 
          * Insert Row 
          * Append Row 
          * Delete Row) 
    * Is Organization (label displays as just "Organization"; checkbox; defaults to not checked; used to specify whether the the Contact is an organization or an individual; standard field) 
    * First Name (visible if the Contact is an individual; required; standard field; when edited, the "Display Name" is updated accordingly) 
    * Middle (visible if the Contact is an individual; optional; standard field; when edited, the "Display Name" is updated accordingly) 
    * Last Name (visible if the Contact is an individual; required; standard field; when edited, the "Display Name" is updated accordingly) 
    * Display Name (customized read-only field; with the following details / behaviors:
      * if "Employee" is included as a Contact Type: displays the Contact's name, in the following format: "<Display Name, based on the "Name Format" selection in Silverloom Settings>"; 
      * otherwise (if "Employee" is not included as a Contact Type): displays the Contact's name and line 1 of the Primary address for the Contact, in the following format: "<Display Name, based on the "Name Format" selection in Silverloom Settings> ("Address")"; 
      * examples: "Smith, John (123 Some St.)" or "ABC Builders (321 Some Road)";
      * this is the unique identifier for the Contact record, with validation against Contacts with identical Display Names; 
      * note that this allows for distinguishing Contacts with matching names; however, the same contact could theoretically be entered multiple times if any included data is not identical (i.e. including/lacking Middle name, spelling "Road" vs. "Rd" in the Address, etc.);  
      * note that for non-Customer-type Contacts, this would not include the address if none is entered, since address is not required for Contacts of other types; 
      * the displayed details are updated automatically when the source fields are edited - see corresponding specs) 
    * Short Display Name (standard; hidden read-only macro; with the following details / behaviors:
      * dynamically displays the following:
        * if "Organization" checkbox is checked: displays the following: "<Organization Name>";
        * if "Organization" checkbox is not checked: displays the following: "<First Name> <Last Name>";
      * to be used on printouts and as the Job Contact on Proposals where "(Use Customer as Job Contact)" is selected)



  


  * Organization Name (visible if the Contact is an organization; required; standard field) 
  * Summary (optional; plain text field; standard field) 
  * Organization (visible if the Contact is an individual; embedded spreadsheet that allows the Contact to be linked to multiple organizations/businesses; standard field)



  


  * Address section: 
    * "<" & ">" (visible if there are more than one address entered; buttons in the section heading; to cycle through the entered addresses) 
    * Type (optional; visible and editable if there are more than one address entered; drop list of Address Type list items, and the option to add a new item to the list) 
    * Address (optional; for "line 1"; plain text field;
      * custom behavior: when edited for the Primary address, the "Display Name" is updated on the subsequent Save, if "Employee" is not included as a Contact Type)
    * Address 2 (unlabeled field; optional; for "line 2"; plain text field) 
    * City (optional; plain text field) 
    * State (unlabeled field; optional; drop list of US state & territory abbreviations) 
    * Zip (unlabeled field; optional; plain text field) 
    * Google Maps (link; visible if at least one of the address-related fields has data entered; opens the entered address in Google Maps) 
    * Export Address (link; visible if at least one of the address-related fields has data entered; opens a prompt screen to export the address (i.e. for printing on an envelope)) 
    * View All (button; opens the "View All Addresses Child Screen" \- see spec below) 
    * New (button; adds a new address item)  
    * Delete (visible if there are more than one address entered; button; deletes the currently-visible address) 



  


  * View All Addresses Child Screen: 
    * Embedded spreadsheet with the following: 
      * Columns: 
        * Type (column always visible; otherwise the same as the corresponding field on the main screen) 
        * Address (same as the corresponding field on the main screen)
        * Address2 (same as the corresponding field on the main screen)
        * City (same as the corresponding field on the main screen) 
        * State (same as the corresponding field on the main screen) 
        * Zip (same as the corresponding field on the main screen) 
        * Country (same as the corresponding field on the main screen)
        * Export (link; displays as "Link"; same behavior as the "Export Address" link on the main screen) 
      * Automatically sorted by: N/A (rows remain in the order in which they were entered)
      * Buttons to insert/append/remove rows: "✚" / "🞭"
      * Buttons to move rows up and down (up/down arrows) 
      * Show 12 rows without scrolling
      * Other Notes:
        * The first / top address is considered to be the "Primary" address. 
        * Custom validation: At least one address is required for each Customer-type Contact: validation error on Save if "Customer" is included as a Contact Type and no address is specified: "Customers must have at least one address." 
      * "The first address is considered primary." (informational message in gray text, below the embedded spreadsheet on the child screen)



  


  * Phone section:
    * Phone Number (standard embedded spreadsheet; standard version can handle Canadian phone numbers since they use the same format as US numbers; standard also considers the top number to be the primary) 



  


  * Email section:
    * Email (standard field & embedded spreadsheet; can track multiple email addresses, and one or more can be designated as "Primary")



  


  * Notes section 
    * Notes (standard memo) 



  


Other Notes: 

  * The following entire standard section(s) with all included fields are hidden (custom) in this Solution: 
    * Executive Notes section / memo
  * The following individual standard field(s) are hidden (custom) in this Solution: 
    * Display Name
    * Override Name
    * Date of Birth
    * Gender



  


Development Specification

TODO_VA: Tim Reitz 10/08/2025: At some point (maybe once initial coding (and maybe deployment is done?), let's split these standard Contact record sections out into separate Proposal rows (like we're doing for the Vehicle Tracking IDD Proposal). 

  


  


Ellis Miller 06/10/2025: 

  


[ ] Reminder: Make sure that all references to ContactType use the ContactOfType macro so that it works with additional types.

  


[ ] Default Contact Type -- Override CustomContacts_DefaultType to return ValidatedListSTring("Customer")

1 Hour

  


[ ] Custom validation for address for customers. Add a Validate Record in the client catalog.

1 Hour

  


[ ] Override existing system switches as noted to hide the various fields.

1 Hour

  


[ ] Display Name / Short Display Name SEPARATE JOB FOR NICCOLAS (1 Day)

[ ] I think set CustomContacts_ShowDisplayNameRO to true

[ ] Maybe override ContactDefaultLookupName and ContactDefaultDisplayName

[ ] Consider whether we want to document anywhere various systems and how they override names. 

  


  


  


Tim Reitz 01/28/2025: Wrote up [[[IN11088](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11090&)]] - CORE - Contacts - Add Sorting to Addresses & Phone RGs, to improve the ability to set a Primary Address & Primary Phone.

_PRICING: Tim Reitz 04/21/2025: Let's work on this at some point (as we wind down design?).

Ellis Miller 06/19/2025: _VA: Let's do this after acceptance. I've included some margin for it.

_EM: Tim Reitz 07/07/2025: How would you like to approach this now? 

Tim Reitz 10/24/2025: This has been coded and tested. 

  


  


_EM: Tim Reitz 06/19/2025: Let's also look at doing this after acceptance: [[[IN11617](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11619&)]] - CORE - Contacts: Improvements for Interaction Between "Contact Type" & "Additional Contact Types".

Tim Reitz 06/24/2025: I would love to also see some additional improvements to the feature (generally reducing the cumbersome & hacky feeling/look that it currently has). 

\- Why the 2 layers of RGs? 

-

Tim Reitz 10/24/2025: This has been coded.
