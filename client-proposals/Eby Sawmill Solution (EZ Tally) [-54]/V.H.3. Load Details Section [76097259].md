5.8.3. Load Details Section

  


Requirements

  * Load Details section: Note that this entire section is read-only if the Confirmed checkbox is not checked, so that an unconfirmed Tally cannot be loaded. Also note that the whole section can still be edited via imports, including any fields that have separate validations. 
    * Removed Logs? (required if "Loaded" checkbox is filled - error message on Save if empty: ""Removed Logs?" is blank."; drop list of Yes, No; defaults to blank)
    * Container # (plain text field; wide enough for 13 characters; validate that the entry is 11 characters long; error on Save if the entry does not match the specified format -- validation message: "Container # should be 11 characters long and in the format of "ABCD1234567"")
    * Heavy Weight (pounds; number; 0 decimals)
    * Light Weight (pounds; number; 0 decimals)
    * Net Weight (auto-calculated and read-only; difference of Heavy Weight and Light Weight)
    * Photos (embedded spreadsheet with the following:) 
      * Columns: 
        * File Name (auto-set and read-only; original file name) 
        * View / Download (link to open the photo in a new tab; the user can right-click on the link and select "Save link as" if they want to download it directly; note that this link is open to anyone who has it, even if they are not logged into the Solution, but the link does expire automatically after 15 minutes) 
        * Date (auto-set and read-only; upload date)
        * Time (auto-set and read-only; upload time) 
      * Automatically sorted by: N/A (keep in the entry sequence) 
      * Button to remove rows ("-")
        * Note that the files remain stored on S3 even though the row is deleted. 
      * Show 4 rows without scrolling
      * Other notes: 
        * At least one photo is required to mark the Tally as Loaded (see validation message for Loaded checkbox)
        * Note that photos for deleted rows are retained in the online storage for archival purposes 
    * Add Photo (link; clicking this links opens a child screen that prompts the user to exit edit mode for the page; after the user clicks "Yes", the Solution exits edit mode and opens a screen that allows a file to be dragged into add it to the Photos table) box on the browser window; when the photo is dropped into the box, it automatically uploads to S3 and is added to the Photos embedded spreadsheet; the user can upload as many photos as are needed for the load, then click a link back to the Export Tally record; note that the process is different for the Yard App - see the corresponding section of the proposal) 
    * Seal # (number; wide enough for 10 digits)
    * Loaded (checkbox + date and time + user name; cannot be checked if the Confirmed checkbox is not checked - error message on Save: "This Export Tally cannot be marked as Loaded because it has not been Confirmed."; filling the checkbox auto-fills the date/time and user name, which all are read-only; all other editable fields in the Load Details section must be filled in before it can be marked as Loaded - validation message on the checkbox: "All other fields in the Load Details section must be filled in before the Tally can be marked as loaded.")
    * Export Bill of Lading (link; visible if Loaded checkbox is filled; opens the PDF printout in a new tab)



  


Development Specification

Change Requests: 

  * Austin Priest 10/04/2023: [[[IN8561](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8563&)]] - ZET - Export Tally - View/Download on Photos RG
  * Tim Reitz 06/10/2024: [[[IN9371](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9373&)]] - [[PC0163079]] - ZET - Change Container number format and validation
  * 


  


  


TODO_EM: When speccing this with Josh, figure out details from him regarding:

  * Cost to set up S3 w/ the client
  * What validation (if any) to do on the S3 (Only allow pictures to be dropped in?)
  * What format to do the upload links (Presumably we want to run a specified x30 on upload)
  * What format for delete links (presumably we want to run a specified x30 on delete and not actually delete the file if the x30 fails to modify the record).
  * What format to do the view links 



  


TODO_EM: Note that client will own S3 account and we will help configure.

TODO_EM: Ask Matthias if CH can bid setting up the S3 accounts? Two-factor, don't worry about hackers, don't actually delete file ever from S3.

$500 base + $100 for each level ($600 for 1 level, $700 for 2 levels).

  


  


Ellis Miller 12/20/2022:

[ ] Simple screen

[ ] Use a ContainerIDs list under the hood (The ExportTallyContainerIDEntry string macro will set the list field via an OnChange). This will give a list field for reporting, but keep a simple text string for entry.

[ ] Use Seal# as a list under the hood in the same way.

[ ] Josh provides macros for the Download / Delete / View / Add buttons.

[ ] We may provide simple x30's to modify these records to add an RG row / Delete an RG row.

[ ] "Print Export" link should use SaveDetail.

BID: 8 HOURS because of uncertainty of integrations

  


  


Photos RG: 

  * Delete (link that exits edit mode for the page and opens a confirmation prompt; deletes the photo from the online storage and removes the row from the table; link is hidden if there is only one row on the table and the Loaded checkbox is filled) 



DONE_AP: Tim Reitz 01/26/2023: remove this column from the RG on the mockup

 Ellis Miller 12/20/2022: _CH: I think rows should automatically be removed when we delete. I think the Delete link should ExitEditMode and then the Delete action will delete the row. We should hide the Delete link if we have only one row and the Tally is marked as loaded? Or we can give an error when they try to delete. Ellis Miller 01/03/2023: Or maybe just don't use a Delete link and have the "-" button delete.

DONE_MM: Tim Reitz 01/19/2023: Thoughts on Ellis's suggestions?

DONE_CCI: Tim Reitz 01/24/2023: Per Matthias, the plan was that if we keep/use the "-" button, it will keep the photo in S3 and delete the row. If at some point they are concerned about how much data they have in S3, we can give them a cleanup report - what's linked to records in the AppHosting database vs. what's not. It's barely worth it to go to the work of deleting the file from S3 every time.

Matthias is thinking it's cleanest to keep the Delete link and remove the "-" button. This will delete the file from S3 and will remove the row from the RG. We've updated the spec here. 

Tim Reitz 01/26/2023: Per Ellis, let's stick to the original plan of using the delete button and keeping the files on S3. Can be discussed further if needed.
