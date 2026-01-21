7.4.2. Delivery Ticket - Documentation Section

  


Requirements

  * Documentation section: 
    * Attached Documents (unlabeled read-only memo; includes a table with the following: 
      * column headers in bold font: 
        * "Delivery Ticket" 
        * "Buyer Grade Report"; 
      * a cell for each attached document (if a document is attached), in its corresponding column, 
        * displaying the following text as a link to open the corresponding file: 
          * for the first uploaded file of each type: "View Delivery Ticket" / "View Buyer Grade Report" 
          * for subsequent uploaded files of each type: "View Delivery Ticket <#>" / "View Buyer Grade Report <#>, note that "#" should start with 2; 
        * if multiple files are included in one of the columns, they display in the same sequence as the corresponding file upload embedded spreadsheets, i.e. the most recent at the top) 
    * Upload Delivery Ticket (link; with the following details / behaviors: 
      * located below the "Delivery Ticket" column of the "Attached Documents" memo; 
      * exits edit mode for the page after prompting to save any unsaved changes and opens the upload screen that allows a file to be dragged into the browser window to add it to the "Delivery Ticket Files" embedded spreadsheet; 
      * note that this upload screen includes a link back to the record screen for easy access)
    * Upload Buyer Grade Report (link; with the following details / behaviors: 
      * located below the "Buyer Grade Report" column of the "Attached Documents" memo; 
      * exits edit mode for the page after prompting to save any unsaved changes and opens the upload screen that allows a file to be dragged into the browser window to add it to the "Buyer Grade Report Files" embedded spreadsheet; 
      * note that this upload screen includes a link back to the record screen for easy access) 
    * View/Edit Documents (button; opens the "View/Edit Documents" child screen - see corresponding spec below) 



  


  * Buyer Grade $ (number; 2 decimals; used for documenting the Buyer's assessed post-discount value for lumber + Other Line Items from the Grade Report; with the following behaviors/notes: 
    * required if one or more attachments are included in the "Buyer Grade Report Files" embedded spreadsheet; 
    * defaults to blank; 
    * this is normally automatically set from the "Buyer Grade $" field on a linked Buyer Payment record; 
    * this value is used as the benchmark for knowing when the Buyer has paid in full, in situations where the "Total Buyer Payment $" ≠ "Buyer Invoice $") 



  


  * Ticket Value $ (read-only macro; displays the dollar value of the Delivery Ticket; with the following logic: 
    * if Status = "Closed": displays the value of "Total Buyer Payment $" (post-discount), in standard black text; 
    * otherwise, if "No Member Grade" checkbox is checked: displays the value of "Buyer Grade $", in gray text with "(Pending)" suffix; 
    * otherwise, if "Buyer Grade $" is blank: displays the value of "Buyer Invoice $", in gray text with "(Pending)" suffix; 
    * otherwise, if "Buyer Grade $" is not blank: displays the value of "Buyer Grade $", in gray text with "(Pending)" suffix) 



  


  * Ticket Value Source (read-only macro; displays the corresponding item from the "Ticket Value Sources" simple list as the source of the "Ticket Value $" number; with the following logic:  
    * if "Delivery Ticket Status" = "Closed": "Total Buyer Payment $"; 
    * otherwise, if "No Member Grade" checkbox is checked: "Buyer Grade $";
    * otherwise: "Buyer Invoice $") 



  


  * Buyer Grade Report Sent to Member (checkbox; with the following details / behaviors:
    * when checked or cleared, the "Grade Report Sent Date" is also set / cleared (see corresponding spec);
    * error on the field if checked when "Buyer Grade $" = blank: "Buyer Grade $ must be set before marking as Sent to Member.") 
  * Buyer Grade Report Sent Date (no label; date; with the following details: 
    * auto-set and read-only; 
    * sets when the "Grade Report Sent to Member" checkbox is checked; 
    * cleared when the corresponding checkbox is unchecked; 
    * displays the date on which the checkbox was checked, in the following format: mm/dd/yyyy) 



  


  * Buyer Payment Finalized + Delivery Ticket Closed (checkbox; stored field; with the following special behaviors:
    * read-only if the "Canceled" checkbox is checked; 
    * details about checking the checkbox: 
      * automatically checked, remaining editable, if "Condition 1" below is met (see corresponding spec): 
        * from the Delivery Ticket itself: on the first Save after the above conditions are met; 
        * from a linked Buyer Payment: via the "Close Delivery Ticket from Buyer Payment" automatic process (see corresponding spec); 
      * otherwise, must be manually checked to close the Delivery Ticket; 
      * on the first save after this is checked, the record enters limited editing mode; 



_EM: Tim Reitz 06/23/2025: Is this actually immediately, or on the first Save after it's checked? 

Ellis Miller 07/08/2025: _VA: First Save. 

_VA: Tim Reitz 06/23/2025: Double check the following Ticket (is it really in LEM after being reopened and reclosed?: [https://testloadhawk.silverloom.io/Detail/Edit/2?RecordType=Delivery+Ticket&NumberID=24&State=ctLVLwm53iQ&#](https://testloadhawk.silverloom.io/Detail/Edit/2?RecordType=Delivery+Ticket&NumberID=24&State=ctLVLwm53iQ&#)

_EM: Tim Reitz 07/19/2025: Upon further research, it seems like the page needs to be reloaded after the first save to enter Limited Edited Mode. Is this correct? 

_VA: Tim Reitz 07/21/2025: Per Ellis, this is a platform issue. See [[[IN11822](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11824&)]] - ZGW - Issue with entering Limited Editing Mode, and the PC linked in the incident body. 

Tim Reitz 10/16/2025: Platform probably won't be fixed for real for a while. 

TODO_: Tim Reitz 07/19/2025: Consider adding a warning on change when the checkbox is checked, to tell the user to save the record to fully close it (like the one we have for unchecking it). 

Tim Reitz 10/16/2025: This is written up in [[[IN12255](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12257&)]] - ZGW - Delivery Ticket - Add Warning When Entering Limited Editing Mode. 

  * details about unchecking the checkbox: 
    * if the checkbox is manually unchecked, it does not automatically re-check on the subsequent Save, to allow the Delivery Ticket to be fully re-opened and exit limited editing mode); however, it does automatically check on the next following Save where the conditions are met; 
    * warning message on the field when manually unchecked: "Save this Delivery Ticket before making any changes, to complete the reopening process." (this is because the record must be saved after unchecking the checkbox, to fully exit limited editing mode); 
  * one of the following conditions must be met to close the Delivery Ticket: 
    * Condition 1 (same condition as auto-closing): "Total Buyer Pmt. (Pre-Discount) $" is not zero and is equal to "Buyer Invoice $";
    * Condition 2 (for manual closing): "Total Buyer Payment $" (post-discount) is not zero and and is equal to "Buyer Grade $" and there is at least one attachment in the Buyer Grade Reports embedded spreadsheet;
  * if the checkbox is checked and neither above condition is true, a validation error message is displayed on the field: 
    * if Condition 1 above is not met and "Buyer Grade $" is blank: "To close this delivery ticket: The Total Buyer Pmt $ (Pre-Discount) must match the Buyer Invoice $"; 
    * if Condition 2 above is not met, and there are no rows in the "Buyer Grade Report" embedded spreadsheet: "To close this delivery ticket: The Total Buyer Payment $ must match The Buyer Grade $, and a Buyer Grade Report must be attached"; 
  * when checked, sets the "Closed by User & Date" field)


  * Closed by User & Date (no label; auto-set and read-only field; set when the "Closed" checkbox is checked; cleared when the corresponding checkbox is unchecked; displays details about the user who checked the checkbox, as well as the date and time when the checkbox was checked, in the following format: "<User ID> <mm/dd/yyyy h:mm:ss> <AM/PM>"; note that when checked automatically, the User ID displays something like "AutomationUser") 



  


  


  * "View/Edit Documents" child screen: 
    * Delivery Ticket Files (embedded spreadsheet with the following: 
      * Columns: 
        * File Name (read-only macro; displays the uploaded file name)
        * Upload Date (auto-set and read-only; date field; sets to the upload date)
        * Upload Time (read-only macro; displays the upload time)
        * Download (link to download file; displays as "Link"; opens the file in a new tab) 
        * Delete (link; displays as "Link"; opens a screen to confirm deletion of the file)  
      * Automatically sorted by: N/A (retains the upload sequence) 
      * Show 2 rows without scrolling
      * Validations: 
        * Warning on Save if there are any rows in the Load Itemization table and there are no files are uploaded here: "No Delivery Ticket from Member specified.") 
    * Upload Delivery Ticket (link; located below the "Delivery Ticket" column of the "Attached Documents" memo; exits edit mode for the page and opens a new tab that allows a file to be dragged into the browser window to add it to the "Delivery Ticket Files" embedded spreadsheet)
    * Buyer Grade Report Files (embedded spreadsheet with the following:  
      * Columns: 
        * File Name (read-only macro; displays the uploaded file name)
        * Upload Date (auto-set and read-only; date field; sets to the upload date)
        * Upload Time (read-only macro; displays the upload time)
        * Download (link to download file; displays as "Link"; opens the file in a new tab) 
        * Delete (link; displays as "Link"; opens a screen to confirm deletion of the file)  
      * Automatically sorted by: N/A (retains the upload sequence) 
      * Show 2 rows without scrolling
      * Validations: 
        * At least one attachment is required to close the Delivery Ticket unless "Total Buyer Payment $" = "Buyer Invoice $" (see the corresponding spec & validation on the "Closed" checkbox)
    * Upload Buyer Grade Report (link; located below the "Buyer Grade Report" column of the "Attached Documents" memo; exits edit mode for the page and opens a new tab that allows a file to be dragged into the browser window to add it to the "Buyer Grade Report Files" embedded spreadsheet)



  


Development Specification

Change Requests: 

  * Tim Reitz 02/28/2025: [[[IN11186](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11188&)]] - ZGW - Delivery Ticket - Clarifications for Auto-Closing Delivery Tickets.
  * Tim Reitz 05/12/2025: [[[IN11460](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11462&)]] - ZGW - Delivery Ticket - Various Improvements / Bug Fixes
  * Tim Reitz 05/19/2025: [[[IN11469](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11471&)]] - ZGW - Delivery Ticket - More Improvements / Bug Fixes 
  * Tim Reitz 10/04/2025: [[[IN11929](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11931&)]] - ZGW - Delivery Ticket Record - Changes to "Ticket Value $" Calculations
  * 


  


  


Ellis Miller 12/16/2024:

  


[ ] USA: code the DeliveryTktDocMemo. This concats the RG rows with nice labels using [[<URL> Label]] syntax formatted as cells. BID: 4 HOURS

  


[ ] BD: Upload links and child screen with 2 RG's. 4 HOURS

  


[ ] BD: Ticket Value:

[ ] Code a DeliveryTicketValueSource macro (displayed on detail screen) as outlined above. Use ValidatedListSTring.

[ ]  Code a DeliveryTicketValueDisplay string macro that calls the Source macro and returns the corresponding field, adding the " (Pending)" or " (Final)" as appropriate. with appropriate font formatting. 2 hours
