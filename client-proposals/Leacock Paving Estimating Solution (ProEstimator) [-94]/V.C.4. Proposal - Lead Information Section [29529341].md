5.3.4. Proposal - Lead Information Section

  


Requirements

  * Lead Information section (visible if "View / Edit Lead Information on Main Screen" checkbox is checked; note that the checkbox is automatically unchecked after every Save, including the initial Save, for the Proposal record, which means that this section is hidden accordingly; however, all of the fields in this section can be viewed by clicking the "View Lead Information" button, which opens a child screen with the details in a read-only format as well as the aforementioned "View / Edit Lead Information on Main Screen" checkbox) 



  


  * "Lead Information will be hidden on Save, and can be accessed via the "View Lead Information" button." (on-screen message in gray font, located below the section header; to help the user anticipate that the section will disappear) 



  


  * Left side: 
    * Lead Source (drop list of active Lead Source record Names; with the following details / behaviors:
      * if "Previous Customer" checkbox is checked (i.e. if any other Proposal records exist for the same Customer - see corresponding spec):
        * read-only;
        * is auto-set to "Previous Customer" when "Customer" is set;
      * if "Previous Customer" checkbox is not checked:
        * editable; 
        * required if "Lead Information Required" is checked, otherwise optional; 
      * note that Lead Source records can be added to this list via import) 
    * Referring Party (visible if "Lead Source" = "Referral"; with the following details / behaviors:
      * drop list of all Contacts (displaying the "Display Name"); 
      * warning on Save if visible and blank: "Referring Party is blank." (note that this is to allow the user to leave notes in "Lead Source Note" to follow up on later, if they don't want to take the time to set up a new Contact while receiving the lead); 
      * note that an optional add-on is mentioned at the end of this document, for a feature that would provide tracking and reporting for the referral gift cards that are sent to referring parties) 
    * New Referring Party Contact (visible if "Referring Party" is visible and blank; with the following details / behaviors:
      * link;
      * opens a new Contact record with "Contact Type" = "Other Individual"; 
      * user note: if the referring party is not an existing Contact, the user should click this link, enter the basic (required) details on the new Contact record and save it, then come back to the new Proposal record and select the new Contact from the "Referring Party" drop list;
      * also note that a address is not required for non-Customer-type Contacts, which enables the user to set up the referring party Contact without an address, if the lead doesn't know the address, and the address could be pursued when it comes time to send gift cards)
    * View / Edit Referring Party Contact (visible if "Referring Party" is visible and not blank, in the same location as the "New Referring Party Contact"; link; opens the selected Contact record) 
    * Referring Party Address (read-only macro; with the following details / behaviors: 
      * visible if "Lead Source" = "Referral"; 
      * dynamically displays the full Primary address for the selected "Referring Party" Contact, in the standard multi-line format without the addressee name, or is blank if there is none)
    * Lead Source Note (plain text field; with the following details / behaviors: 
      * visible for all "Lead Source" selections; 
      * required if "Lead Source" = "Other", otherwise optional) 



  


  * Paved Before (checkbox)
  * Pavement Age (plain text field; with the following details / behaviors: 
    * visible and required if "Paved Before?" is checked)
  * Pavement Condition (plain text field; with the following details / behaviors: 
    * visible and required if "Paved Before?" is checked; 
    * this is used for documenting notes about the condition of any existing pavement; 
    * note that existing "Cracks/Potholes" field entries are to be migrated to this field at deployment) 
  * Stone Base Good (checkbox; visible if "Paved Before?" is not checked;) 
  * Have Drawings (checkbox) 
  * Grading Required (checkbox; visible if "Paved Before?" is not checked) 
  * Ideal Project Timeframe (drop list of Project Timeframes list items; with the following details / behaviors: 
    * required if "Lead Information Required" is checked, otherwise optional) 
  * Decision Process (multi-select drop list of "Decision Processes" list items; at least one selection is required if "Lead Information Required" is checked, otherwise is optional) 
  * Decision Process Note (plain text field; with the following details / behaviors: 
    * visible and required if "Other" is selected in "Decision Process"; 
    * this is used for entering clarifying notes about the "Other" selection) 
  * Additional Lead Notes (optional; memo)



  


  * Right side: 
    * Lead Information Required (editable checkbox; with the following details / behaviors:
      * defaults to checked for new blank Proposals;
      * when checked, certain Lead Information fields are required - see corresponding specs; 
      * is automatically unchecked by any of the following:
        * when "Job Type" is set to "Commercial" or "Sports Construction" \- see corresponding spec;
        * when "Customer" is set, if any other Proposal records exist for the same Customer - see corresponding spec;
        * when the "Change Order" or "Duplicate Proposal" buttons are clicked - see "Copy Action Details" spec;
      * can be manually unchecked if needed) 
    * Received Date (required; date; defaults to the current date for new blank Proposals) 
    * Received By (required; drop list of all active Employee-type Contacts; defaults to the current user creating the record for new blank Proposals)
    * Appointment Date (optional; date field; warning on the initial Save for the record if blank: "Appointment info is missing.") 
    * Appointment Time (required if "Appointment Date" is not blank, otherwise optional; time field; when blank, shows a gray hint in edit mode if blank: "e.g. 9:30 AM")
      * For these "Appointment" fields: Consider skipping the warnings for "Change Order"-type Proposals.



  


Development Specification

Ellis Miller 06/17/2025: 

[ ] Simple, but lots of fields.

[ ] Lead Source: CanAddToList: InImport

[ ] Need a hidden DecisionProcess RG to support the multi-select list. See other examples like that.

[ ] Received Date: Just use OnInit:Today

[ ] Appointment Time

[ ] See other places where we have Time macros

[ ] Use PlaceHolder: behavior for the gray hint

4 Hours
