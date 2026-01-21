5.3.7.1. Proposal Itemization Section - Sections Embedded Spreadsheet

  


Requirements

  * Sections (embedded spreadsheet with the following: 
    * Columns: 
      * Section Row ID (with the following behaviors / details:
        * hidden column; 
        * auto-set and read-only; editable via import; 
        * numeric; 
        * unique identifier for the row; 
        * note that for Proposal Sections imported from the existing Power App solution, this will be set to the "Power App Quote Section ID" from the imported data) 
      * Section Name (required; drop list of "Default Sections" list items and the option to add a single-use custom entry; validate against duplicates for the same Proposal) 
      * Section Inclusion Type (required; drop list of "Section Inclusion Types" list items; with the following details / behaviors: 
        * defaults to "Standard";
        * this determines how Groups in the Section will be handled in the Proposal prior to "Proposal Result" being set to "Awarded" \- see spec for "Total Proposal Price $", Proposal Printout, etc.)  
      * Opt / Alt # (editable and required if "Section Inclusion Type" for the row = "Option" or "Alternate"; number; 0 decimals; see Glossary explanations for "Standard" / "Option" / "Alternate" Sections) 
    * Automatically sorted by: N/A (rows remain in the sequence in which they are entered)
    * Buttons to add/remove rows: "✚" / "🞭"
      * Both buttons visible if "Ready to Send to Customer" is not checked, with the following additional condition(s): 
        * "🞭" is hidden if the selected Section is referenced on any rows on the Groups embedded spreadsheet; this is to prevent deletion of a Section if it is being used for any Groups.
    * Show 5 rows without scrolling
    * Other Notes: 
      * If a Section Name is edited here, it will automatically be updated on any rows in the "Groups" embedded spreadsheet where it is referenced.
    * Additional Validations:
      * Warning on Save if any of the Sections are not referenced on at least one row on the "Groups" embedded spreadsheet: "Section <Section Name> is not used on any Groups and will not be included in the printout.")



  


Development Specification

Ellis Miller 06/17/2025:

Simple RG:

[ ] Section Name: String field with a helper list of standard section names with option to add something else. AddToListLabel should be "Use Custom Section Name"

[ ] "If a Section Name is edited here, it will be updated on any rows in the "Groups" embedded spreadsheet where it is referenced." \-- you can do this by storing the Section Row ID in the Groups RG.

BID: 3 HOURS

  


Tim Reitz 04/03/2025: Note that we [might] will be importing Section IDs for records imported records from the Power App.
