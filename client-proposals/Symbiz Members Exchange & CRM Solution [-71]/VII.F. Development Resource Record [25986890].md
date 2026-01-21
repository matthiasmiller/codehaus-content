7.6. Development Resource Record

  


Requirements

Overview: Each month, each Growth Ring Group has a chosen resource to go through. This is usually a book that all members in the group read, but it could also be a coaching program that runs for a few months, a video or video series, etc. A member can also refer to / use a Development Resource for personal growth outside of the group. This record stores information for the Development Resources that are created and shared by members.

  


Accessed via:

  * The Development Resources reports
  * The Development Resource link on the Growth Ring Meeting record
  * Members Menu | Development Resources | New Resource (menu option for creating a new record)



  


Sections and Fields: 

  


  * Development Resource Overview section: 
    * Status (required; drop list of Development Resource Status items; editable for Regional Reps and Super Admins; defaults to "Submitted" when created)
    * Status Date (auto-set and read-only; defaults to the date of the most recent Status change) 
    * Status Time (hidden time field; auto-set and read-only; defaults to the time of the most recent Status change; uses US Eastern Time)
    * Description (auto-set and read-only; displays "<Title>, <Author / Creator>")
    * Title (required; plain text field; unique identifier for the record; validate against duplicates)
    * Author / Creator (required; drop list of Development Resource Creators; filters down as you type; with option to add new item; used to track the author/publisher/presenter)
    * Media Type (required; multi-select drop list of Media Types - see corresponding section of the proposal)
    * Cover Image (read-only memo that displays an uploaded photo) 
    * Upload Photo (button; visible and editable for the submitting Member and all uplines; hidden if the screen is not in edit mode; opens a child screen to upload a photo - see Child Screen details) 
    * Primary Category (automatic and read-only; when users fill out a Development Resource Review record, they must select a Development Resource Category, and the most frequently selected Category displays here; if there is a tie for the most frequent, the most recently selected option of the tied items is the tiebreaker)
    * View All Categories (button; clicking it opens the All Categories child screen - see details below)
    * Initial Category (required; drop list of Development Resource Categories; the selection here is added as the first row on the All Categories embedded spreadsheet)
    * Average Overall Rating (auto-calculated and read-only; average of all "Overall Rating" values from all Reviews for the Resource; number to 1 decimal place) 
    * Suggested By (for standard users, auto-set and read-only, defaulting to the Contact name of the current user; for Facilitators and all their uplines, required drop list of their own name and all downlines, defaulting to the Contact name of the current user; for users with the "Edit Super Admin fields" permission, this drop list contains all Member Individual-type Contacts)
    * Submitted Date (auto-set and read-only; defaults to the current date when the record is saved for the first time) 
    * View Reviews for This Resource (link; visible if there is one or more reviews; opens the Development Resource Reviews report, filtered to the current Development Resource Record) 
    * "There are no reviews yet for this Resource." (note in gray text; visible if there are no reviews; displays in the place of the "View Reviews..." link) 
    * Review This Resource Now (link; with the following behaviors:
      * for standard members: visible if the user has not written a Review for the Resource; opens a new blank Development Resource Review record, with Resource defaulted to the current Resource and Reviewer's Name defaulted according to the spec for that field - see the Review spec in the corresponding section of this proposal;
      * for Facilitators & all uplines: always visible; opens the New Review Prompt page - see details in the corresponding section of the proposal) 
    * View/Update My Review (visible if the current user is the Reviewer on an existing Development Resource Review for this Resource; link to open the corresponding Review)
    * Overview (required; multi-line plain text field, with enough space for 15 lines)



  


  * Attachments section
    * Attachments (allows users to insert attachments of worksheets, questionnaires, etc.; editable for all users; embedded spreadsheet with the following:) 
      * Columns:  
        * File Name (auto-set and read-only; original file name) 
        * Upload Date (auto-set and read-only; upload date)
        * Upload Time (auto-set and read-only; upload time)
        * View (link to open the document in a new tab) 
        * Download (link to download file) 
        * Delete (displays as "Delete"; only available for the submitting user and all Facilitators, Regional Reps, and Super Admin) 
      * Automatically sorted by: N/A (keep in the entry sequence) 
      * Show 4 rows without scrolling
      * Other notes:
        * N/A
    * Add Attachment (link; exits edit mode for the page after prompting to save any unsaved changes and opens the upload screen that allows a file to be dragged into the browser window to add it to the Attachments table; note that this upload screen includes a link back to the record screen for easy access)



  


  * Purchase Options section (visible if Media Type = one that has the corresponding checkbox filled on its configuration record): 
    * Purchase Options (memo; can be used to paste in links and/or type in notes about where to obtain the Resource)



  


  * Downloads section (visible if Media Type = one that has the corresponding checkbox filled on its configuration record): 
    * Downloads (used for uploading and then accessing Resources that are available for download; embedded spreadsheet with the following:) 
      * Columns:  
        * File Name (auto-set and read-only; original file name) 
        * Upload Date (auto-set and read-only; upload date)
        * Upload Time (auto-set and read-only; upload time)
        * View (link to open the document in a new tab) 
        * Download (link to download file) 
        * Delete (displays as "Delete"; only available for the submitting user and all Facilitators, Regional Reps, and Super Admin) 
      * Automatically sorted by: N/A (keep in the entry sequence) 
      * Show 4 rows without scrolling
      * Other notes:
        * N/A 
    * Add Download File (link; exits edit mode for the page after prompting to save any unsaved changes and opens the upload screen that allows a file to be dragged into the browser window to add it to the Downloads table; note that this upload screen includes a link back to the record screen for easy access)



  


Child Screens: 

  * Update Photo Child Screen: This child screen contains the following:
    * Photo (editable memo) 
    * Instructions text: "To upload a photo, copy and paste a .jpg or .png file into field below, or use the Insert Image button on the field's toolbar. If there are multiple photos in the field, the first one will be displayed as the cover image. To remove photos, click Delete Photo(s). " 
    * Delete Photo(s) (button; clicking this button will delete any photos in the Photo memo)
    * Other notes:
      * The user would need to click a "Close" button to exit the child screen.



  


  * View All Categories Child Screen
    * Embedded spreadsheet with the following:
      * Columns: 
        * Category (one row for each Category that has at least one selection in a Development Resource Review for this Resource or that was selected as the Initial Category here on the Resource record)
        * Number of Selections (the number of times the corresponding Category has been selected, on the Reviews and on the Initial Category)
      * Automatically sorted by: Number of Selections (highest number at the top) 
      * Show 15 rows without scrolling



  


Data Access: See the Data Access Controls section of the proposal for details.

  


Special Considerations: 

  * Copy Record: N/A
  * Delete Record: Prevent deletion if the record is referenced anywhere in the Solution: "This Development Resource cannot be deleted because it is referenced by another record in the database."
  * Merge Record: Only can be merged by Super Admins. All other users would get a message to contact an Admin to resolve a duplicate. 



  


Other Notes: 

  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Change Requests:

  * Tim Reitz 02/26/2024: [[[IN9066](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9068&)]] - ZSB - Resource & Review Records - Improve Creation & Field Defaults
  * Tim Reitz 03/06/2024: [[[IN8910](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8912&)]] - ZSB - Development Resource Record - Misc Changes
  * Tim Reitz 04/08/2024: [[[IN9638](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9640&)]] - ZSB - Various Changes March 2024 (batch 1)
  * Tim Reitz 07/20/2024: [[[IN9836](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9838&)]] - ZSB - Dashboard - Add Scrolling News Feed
  * Tim Reitz 07/20/2024: [[[IN9728](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9730&)]] - ZSB - Various Cleanup Changes #2 (prev. "April 2024 (batch 1)")
  * Ben Reitz 09/17/2025: [[[IN11161](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11163&)]] - ZSB - Development Resource record - "Suggested By" drop list showing all Contacts
  * 


  


  


  


Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1861499078](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1861499078)

  


For reference, view: [https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=0%3A1&node-id=324%3A2900&scaling=min-zoom&starting-point-node-id=9%3A3](https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=0%3A1&node-id=324%3A2900&scaling=min-zoom&starting-point-node-id=9%3A3)

  


DONE_CCI: Tim Reitz 06/01/2023: This record should be editable for all users via import, and we should always show the Add Attachment link. However, we should hide the Attachments Delete option if they do not have permission to edit the record interactively.

Jonathan Bergen 09/13/2023: This restriction is noted and has been bundled into the table of restrictions [[[https://clientscope.invtools.com/Detail/View/2?RecordType=Holding&StringID=PC0156265&NumberID=0&State=Nig9bGMYDug&](https://clientscope.invtools.com/Detail/View/2?RecordType=Holding&StringID=PC0156265&NumberID=0&State=Nig9bGMYDug&) here].

  


  


Tim Reitz 05/09/2023: From Matthias, about the Category: "it's just a matter of defining an expression for the Development Resource to calculate the category. (Dev Spec - Iterate over categories, and create a string such as [Left-Padded Number of Reviews][Tab][Max Review ID][Tab][Category]. Sort the list and return the last one. If we're using the Default Category field, use that value if the prior expression is blank.)"

Tim Reitz 05/30/2023: Updated dev spec from Matthias on 5/22: 

Assign vAllCategoriesForResource = ___NdxConcat(..., ListString(..., BinStringToNum(Mid(NdxKey)))

Assign vDefaultCategory = ...;

  


Assign vCategoriesWithSortKey = ListSubstitute(vAllCategoriesForResource,

  


Assign vCount = NdxSum(...) + If (CurrentItem = vDefaultCategory, 1, 0);

Assign vMaxReviewID = NdxMax(...);

  


Assign vMaxReviewIDLen = 10;

Assign vReverseSortID = 10^ vMaxReviewIDLen - 1 - vMaxReviewID;

  


PadL(String(vCount), '0', 4) +

PadL(String(vReverseSortID), '0', vMaxReviewIDLen) +

Tab +

CurrentItem);

  


Assign vSortedCategories = ListSubstitute(PipeListSort(vCategoriesWithSortKey), TabListItem(CurrentItem, 2));

  


vSortedCategories
