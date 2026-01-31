12.3.5.1. Contact - Standard Sections and Fields

  


Requirements

Contact Record - Standard Sections & Fields (any customizations are noted as such in the spec): 

  


  * Active Contact (checkbox above the top section header; defaults to filled; note that by default, no validations are included) 



  


  * Contact section (standard section, may include custom fields):
    * Contact Type (required; standard field; drop list of of the following Contact Types; editable unless it is set to "Rental Company", or it is set to "Manufacturer" or "Dealer" and there are linked active contacts.):
      * Customer (individual or organization)
      * Rental Company (organization) 
        * Rental Company will not be displayed as an option in the Contact Types list on the Contact record. To create a new Rental Company go to Settings | Configuration | Configure Rental Companies and click the "New Rental Company" link in the top right.
      * Rental Rep (individual)
      * Manufacturer (organization) 
      * Manufacturer Rep (individual)
      * Dealer (organization)
      * Salesperson (individual)



Seth Miller 07/31/2025: TODO_Backlog: record name expression for each separate contact type

  * Organization (checkbox; defaults to not checked; uses to specify whether the the Contact is an organization or an individual; standard field) 
  * First Name (visible if the Contact is an individual; required; standard field) 
  * Middle (visible if the Contact is an individual; optional; standard field) 
  * Last Name (visible if the Contact is an individual; required; standard field) 
  * Display Name (visible if the Contact is an individual; if "Override Name" checkbox is not checked, this is auto-set and read-only, displaying the Contact's name in the Name Format selected in Silverloom Settings; if "Override Name" checkbox is checked, this becomes editable; standard field) 
  * Override Name (visible if the Contact is an individual; checkbox; defaults to not checked; checking this makes "Display Name" editable; standard field) 
  * Organization Name (visible if the Contact is an organization; required; standard field) 
  * Contact Tags (multi-select drop list; with the following items/behaviors:
    * Used to track subtypes for contacts
    * Multiple Tags can be selected for a contact
    * If multiple Tags are selected, they appear as a comma-delimited list when the drop list is closed
    * Users can create, edit, and delete Tags through the Lists menu option in the Advanced menu (there will not be a "\+ Add New Item" feature on the list on the detail screen).
    * The Contacts report will allow filtering by one or more Tags.



Sean Miller 07/25/2025: TODO_PERMISSIONS: Who should be able to edit Contact Tags?

  * Summary (optional; plain text field; standard field) 
  * Organization (visible if the Contact is an individual; allows the Contact to be linked to an organization; standard field) 



  


Contact Type| Organizations included in list| Required  
---|---|---  
Rental Rep| Rental Company| True  
Manufacturer Rep| Manufacturers| True  
Salesperson| Dealer| True  
Customer (if individual not organization)| NONE|   
  
  
  


  * Date of Birth (visible if the Contact is an individual; date field; standard field)
  * Gender (visible if the Contact is an individual; drop list of blank / Female / Male; standard field) 
  * Rental Company (list of active rental companies: more details in table below)

Contact Type| Visibility| Required| Validation  
---|---|---|---  
Manufacturer| True| True| error if changing rental company and there are dealers linked to the manufacturer  
Dealer| True| True|   
  
Customer| True| True|   
  
  
  * Manufacturers 
    * visible for dealer type contacts
    * not required
    * multi select list of active manufacturer type contacts for the dealers rental company
    * validation to ensure the linked manufacturers are within the same rental company



  


  * Linked Contact (visible on Rental Companies, Manufacturers, and Dealers; embedded spreadsheet displaying individuals linked to the organization)
    * Name 
      * displays the linked contact's name. 
      * Labeled as:
        * "Rental Rep" for Rental Companies
        * "Manufacturer Rep" for Manufacturers
        * "Salesperson" for Dealers
    * View link
    * Primary Email
    * Primary Phone



  


  * Website URL (visible for dealers and manufacturers)



  


  * Address section: 
    * "<" & ">" (visible if there are more than one address entered; buttons in the section heading; to cycle through the entered addresses) 
    * Type (optional; required if there are more than one address entered; drop list of Address Type list items, and the option to add a new item to the list) 
      * Address Type list comes with two items "Mailing" and "Physical", but can be added to
    * Address (optional; for "line 1"; plain text field) 
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
      * Automatically sorted by: (e.g. by date, etc, or N/A)
      * Buttons to insert/append/remove rows: "+" / "-" 
      * Show 12 rows without scrolling 
      * Other Notes: 
        * The first / top address is considered to be the "Primary" address. 



  


  * Phone section:
    * Phone Number (standard embedded spreadsheet; standard version can handle Canadian phone numbers since they use the same format as US numbers; standard also considers the top number to be the primary)



  


  * Email section:
    * Email (standard field & embedded spreadsheet; can track multiple email addresses, and one or more can be designated as "Primary")



  


  * Logo section (visible for all organization contacts)
    * Logo (a memo that allows adding a photo to be used in applicable places through the system)



  


  * Notes section 
    * "This record must be saved before creating a linked note." (label, visible for new unsaved records)
    * New Note (opens a new note record; populates the Type + Linked Record, visible if the record has been saved)
    * View Notes (report link; opens the My Notes report)
    * Notes (read-only memo that concats based on record Type + record ID, sorted in order of Note ID; newest first)



  


  * Footer: 
    * User ID (drop list of active User IDs that are not already linked to a Contact record)



  


Development Specification

Contact type and linking data structure

Contact Type| Is Organization| Can be linked to Organization*| Organization helper list| Rental Company list field| Other Linking  
---|---|---|---|---|---  
Customer| [ ] or [X] | [ ]|   
| [X]|   
  
Rental Company| [X]| [ ]|   
| [ ]|   
  
Rental Rep| [ ]| [X]| active Rental Companies| [ ]|   
  
Manufacturer| [X]| [ ]|   
| [X]|   
  
Manufacturer Rep| [ ]| [X]| active Manufacturers| [ ]|   
  
Dealer | [X]| [ ]|   
| [X]| can be linked to 0 or multiple manufacturers  
Salesperson| [ ]| [X]| active Dealers| [ ]|   
  
  
*NOTE: linking to organization is a 1 to 1 relationship.
