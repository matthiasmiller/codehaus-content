5.3.11. Proposal - Customer Acceptance Section

  


Requirements

  * Customer Acceptance section (note editability in Limited Editing Mode for fields in this section - see specs below; note that some items in this section are visible even if "Ready to Send to Customer" is not checked): 
    * Proposal Date (date; with the following details / behaviors:
      * visible and editable and required if the "Ready to Send to Customer" checkbox is checked; 
      * editable in Limited Editing Mode; 
      * auto-sets to the current date when the "Ready to Send to Customer" checkbox is checked, and clears if that checkbox is unchecked (see corresponding spec);
      * when edited, the following field(s) are affected on change:
        * "Proposal Valid Through": set to the date calculated from "Proposal Date" \+ the current "Number of Days for Valid Proposal" in Silverloom Settings (see corresponding specs);  
      * when cleared, the following field(s) are affected on change:
        * "Proposal Valid Through": cleared) 
    * Proposal Valid Through (stored date field; with the following details / behaviors: 
      * visible if "Ready to Send to Customer" is checked; 
      * auto-set and read-only; 
      * editable in Limited Editing Mode; 
      * stores and displays the date that the pricing expires for the Proposal, based on the "Proposal Date" and the "Number of Days for Valid Proposal" setting in Silverloom Settings;
      * this is a stored field rather than a macro because it should not change for existing Proposals if the setting is changed in Silverloom Settings)
    * "The Proposal Valid Through date is in the past. Consider setting Proposal Result to "Archived" or "Lost"." (on-screen message in orange font; visible if "Ready to Send to Customer" is checked and "Proposal Valid Through" date is in the past and "Proposal Result" = blank) 



  


  * Sent to Customer (checkbox + date, which toggle; with the following details / behaviors: 
    * visible and editable only if "Ready to Send to Customer" is checked (to prevent sending the Proposal prematurely); 
    * editable in Limited Editing Mode; 
    * when checked, the date sets to the current date; 
    * automatically checked by the "Print / Email Proposal" checkbox; 
    * can be manually checked / unchecked, even after it has been automatically checked;
    * used for Status and tracking purposes) 



  


  * Open eSignature Service (link; visible if "Sent to Customer" is checked; opens the eSignature provider used by Leacock Paving, based on the URL set in the "Proposal eSignature URL" System Switch (see corresponding spec))
  * Proposal Signed (checkbox + date, which toggle; visible if "Sent to Customer" is checked; editable in Limited Editing Mode; any user can set this to document when the signature was received) 



  


  * Initial Follow-Up Due (visible if the "Ready to Send to Customer" checkbox is checked; read-only macro; date; with the following details / behaviors:
    * dynamically displays the date 2 weeks from the "Proposal Date" date; 
    * note that the "Proposals Needing Follow-Up" report alert runs 2 days before and the day after this date, if "Status" = "Follow-Up Needed" \- see corresponding report alert spec) 
  * Initial Follow-Up Complete (visible if the "Ready to Send to Customer" checkbox is checked; checkbox + date, which toggle; with the following details / behaviors:
    * editable if "Sent to Customer" is checked; 
    * editable in Limited Editing Mode; 
    * to be checked manually; used to track the completion of the initial follow-up with the customer, and for Status and notification purposes) 



  


  * Secondary Follow-Up Due (visible if the "Ready to Send to Customer" checkbox is checked; read-only macro; date; with the following details / behaviors:
    * dynamically displays the date 4 weeks from the "Initial Follow-Up Due" date; 
    * note that the "Proposals Needing Follow-Up" report alert runs 2 days before and the day after this date, if "Status" = "Follow-Up Needed" \- see corresponding report alert spec) 
  * Secondary Follow-Up Complete (visible if the "Ready to Send to Customer" checkbox is checked; checkbox + date, which toggle; with the following details / behaviors:
    * editable if "Sent to Customer" is checked;
    * editable in Limited Editing Mode; 
    * to be checked manually; used to track the completion of the secondary follow-up with the customer, and for Status and notification purposes)



  


  * Proposal Result (drop list of "Proposal Results" list items; with the following behaviors / details:
    * editable, including in Limited Editing Mode, unless "Job Scheduled" checkbox is checked, at which point it becomes read-only;
    * optional if "Initial Follow-Up Complete" and/or "Secondary Follow-Up Complete" checkboxes are not checked; 
    * required if both "Initial Follow-Up Complete" and "Secondary Follow-Up Complete" are checked - error on Save: "Proposal Result is required since both follow-ups are complete. Set it to "Pending" if no decision from customer yet."; 
    * when edited, the following fields are affected:
      * "Proposal Result Date":
        * if "Proposal Result" is set to any non-blank value: sets to the current date;
        * if "Proposal Result" is set from non-blank to blank: clears;
      * "Group Awarded" in the Groups embedded spreadsheet:
        * if "Proposal Result" is set to "Awarded": is checked for all rows on the Groups embedded spreadsheet that have "Opt / Alt" = blank (i.e., all Groups for "Standard" Sections are automatically marked as as awarded, and the user should manually uncheck the checkbox for any that should not be included, and the user should manually mark any awarded "Option" and/or "Alternate" Groups as awarded); 
        * if "Proposal Result" is changed from "Awarded" to anything else (including blank): is unchecked for all rows on the Groups embedded spreadsheet (and therefore "Group Awarded Date" and "Group Target Start" are also cleared for all);
      * "Group Awarded Date" in the Groups embedded spreadsheet:  
        * if "Proposal Result" is set to "Awarded": sets to the current date for all rows that have "Opt / Alt" = blank;
        * if "Proposal Result" is changed from "Awarded" to anything else (including blank): clears for all rows on the Groups embedded spreadsheet;
      * "Job Target Start Comments": if "Proposal Result" is changed from "Awarded" to anything else (including blank): clears; 
    * also, when set to "Awarded":
      * on the first Save after this is set to "Awarded", the "Set Proposal Results for Other Proposals in Family" automatic process is run (see corresponding spec); 
        * note that this process sets this field on other non-Change Order Proposals in the same "proposal family" to "Lost" or "Awarded"; 
      * on the first Save after this is set to "Awarded", the "Job Awarded" email: is sent via the "Send Job Awarded Email" automatic process (see the corresponding specs);
      * "All Standard Groups have been marked as awarded..." on-screen message becomes visible (see corresponding spec); 
    * includes the following additional validations:
      * validate against setting to "Awarded" if "Sent to Customer" is not checked - error on the field: "Cannot be set to "Awarded" because "Sent to Customer" is not checked.";
      * warning on the field if changed from "Awarded" to anything else: ""Group Awarded" and "Group Target Start" have been cleared for all Groups. To undo, please refresh the page."; 
      * warning on the first Save after this is set to "Awarded": "Please confirm that all awarded Groups are marked correctly ("Group Awarded" checkbox)."; 
      * warning on the field when set to "Awarded" if "Proposal Valid Through" date is in the past: "The Proposal Valid Through date is in the past."; 
      * validate against multiple Proposal records with "Proposal Type" = "Original " or "Revised" that have a matching "Numeric ID" portion of the "Proposal #" from being marked as "Awarded" \- error on the field "There is already a Proposal in the same Proposal family that has been marked as Awarded (#<Proposal #>)." 
        * note that this validation does not apply to "Change Order"-type Proposals, as multiple of those may be awarded, in addition to the main Proposal for the "family")



  


  * Proposal Result Date (visible and required if "Proposal Result" ≠ blank; date; with the following details / behaviors: 
    * editable in Limited Editing Mode; 
    * auto-sets to the current date when "Proposal Result" is set, and clears if "Proposal Result" is cleared; 
    * note that this field is not included in the Power App) 
  * "All Standard Groups have been marked as awarded. Review & uncheck "Group Awarded" for any that aren't actually awarded by the Customer.



Also, mark "Opt / Alt" Groups as awarded if needed." (on-screen message in orange font; visible until the first Save after "Proposal Result" is set to "Awarded")

  


  * Job Target Start Comments (visible and required if "Proposal Result" = "Awarded"; wide plain text field; with the following details / behaviors:
    * editable in Limited Editing Mode; 
    * to be manually set by the Sales Rep to note when the Customer would like the job to be done, as an indicator to the Scheduler; 
    * when set / edited, "Group Target Start" is set to the same contents for all rows on the Groups embedded spreadsheet that meet all of the following conditions: 
      * "Group Target Start" is blank; 
      * "Group Awarded" is checked; 
      * "Group Scheduled Start Date" is blank; 
    * warning on the field if edited when non-blank: "Groups that already have "Group Target Start" comments will not be updated."; 
    * note that when this is cleared, "Group Target Start" for the Groups embedded spreadsheet are not cleared, to allow different comments on different rows, and since "Group Target Start" is cleared anyway when "Group Awarded" is unchecked);
    * is not cleared when hidden (i.e. if "Proposal Result" is changed to something else from "Awarded"); this retains the entered information for the event that the Proposal is later marked as Awarded again);
    * note that this field is not included in the Power App) 
  * Entered into QuickBooks (visible if "Proposal Result" = "Awarded"; editable in Limited Editing Mode; checkbox + date, which toggle)



  


Development Specification

Ellis Miller 06/19/2025: Standard fields and behaviors as described.

  


[ ] Trigger email on Awarded. handled separately

[ ] "validate against multiple Proposal records" awarded -- Nic will give you a macro: ProposalFamilyAwardedNumber( vProposalNumber) \-- this will return the proposal number that is awarded (if any). Make sure it is blank or is our own number. Otherwise give an error.

  


BID: 1 DAY

  


\----------------

TODO_: Tim Reitz 06/24/2025: Proposal Result Date: Per Ellis, we could change the label to "Awarded Date" if awarded. See spec that we could add: 

  * if "Proposal Result" = "Awarded", this field label displays as "Awarded Date"; 



However, there aren't many places where having a separate label for awarded Proposals actually seems helpful. If anything, it seems like it could make things more confusing. I'm leaving it out for now, but we could add it back in at some point if needed.
