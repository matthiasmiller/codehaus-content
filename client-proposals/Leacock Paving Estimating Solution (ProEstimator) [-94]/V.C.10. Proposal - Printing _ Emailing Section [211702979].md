5.3.10. Proposal - Printing / Emailing Section

  


Requirements

  * Printing / Emailing section:
    * Draft Proposal PDF (link; visible if "Ready to Send to Customer" checkbox is not checked; if there are any unsaved changes for the current screen, prompts/requires the user to save the record, then opens the Proposal Printout for the current Proposal, to view, download, or print; see printout spec for more details) 



  


  * Print / Email Proposal (checkbox; visible if "Ready to Send to Customer" checkbox is checked; with the following details / behaviors: 
    * editable in Limited Editing Mode; 
    * becomes hidden as soon as it is checked (replaced by the "Proposal PDF" link); 
    * when checked, the following field(s) are affected: 
      * "Sent to Customer" checkbox: set to checked; 
    * note that this checkbox is used so that the "Sent" date can be set; in the future this could be automated more as the Silverloom Business Suite gains more capabilities for interleaving changes) 



  


  * Proposal PDF (link; visible if "Print / Email Proposal" checkbox is checked (in the location of that checkbox); if there are any unsaved changes for the current screen, prompts/requires the user to save the record, then opens the Proposal Printout for the current Proposal, to view, download, or print; see printout spec for more details) 



  


  * Proposal + Customer Letter PDF (link; visible if "Print / Email Proposal" is checked; if there are any unsaved changes for the current screen, prompts/requires the user to save the record, then opens the Proposal + Customer Letter Printout for the current Proposal in a new tab, to view, download, or print; see printout spec for more details)



  


  * Send Proposal Email (link; visible if "Print / Email Proposal" is checked; if there are any unsaved changes for the current screen, prompts/requires the user to save the record, then opens the "Proposal Email to Customer" Email, using the mailto: feature; see email spec for more details) 



  


  * Work Order PDF (Complete) (link; visible if "Proposal Result" = "Awarded"; if there are any unsaved changes for the current screen, prompts/requires the user to save the record, then opens the Work Order Printout, to view, download, or print; see printout spec for more details)
  * Work Order PDF (Partial) (link; visible if "Proposal Result" = "Awarded"; if there are any unsaved changes for the current screen, prompts/requires the user to save the record, then opens a prompt screen with a "Select Groups to Print" multi-select drop list of all "Awarded" Groups in the Proposal, with none selected by default; the user selects the desired items, then clicks "Continue" to generate the Work Order Printout based on the selected Group(s); see printout spec for more details) 
  * Send Work Order Email (link; visible if "Proposal Result" = "Awarded"; if there are any unsaved changes for the current screen, prompts/requires the user to save the record, then opens the "Work Order Email" Email, via the mailto feature; see email spec for more details)



  


Development Specification

Ellis Miller 06/18/2025: 

  


BID 4 HOURS
