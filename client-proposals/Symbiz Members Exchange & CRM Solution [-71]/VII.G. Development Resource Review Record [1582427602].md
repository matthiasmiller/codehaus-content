7.7. Development Resource Review Record

  


Requirements

Overview: Members review their Group's monthly Development Resource, and can review additional Development Resources as desired. This record stores a member's review of a selected Resource.

  


Accessed via: Various Development Resource Reviews links and reports

  


Sections and Fields: 

  * Development Resource Impact Worksheet section:
    * Review ID (hidden field; auto-set and read-only; unique identifier for the record)
    * Reviewer's Name (drop list of the current user and any/all downlines; with the following behaviors: 
      * for standard Members: editable and required for new (unsaved) records, defaulting to the current user since there are no downlines; becomes read-only after the initial save; 
      * for Facilitators and uplines, this is required, drop list of all downlines with active memberships, defaulting to blank, filters down as you type; 
      * becomes read-only after the initial Save)
    * Resource (required; list of Development Resource Descriptions; error on Save if blank: "Resource is required."; validate against the same Member reviewing the same Resource more than once - validation error message on the field: "The selected Reviewer already has a Review record for this Resource."; becomes read-only after the initial Save)
    * View Resource (link; visible if a Development Resource is selected; opens the corresponding record) 
    * Author / Creator (auto-set and read-only; based on selected Resource)
    * Category (required; drop list of Development Resource Categories; this selection counts toward the "vote" that determines the Resource's Primary Category - see details in the Development Resource record section of the proposal; error on Save if blank: "Category is required.")
    * Date of Review (required; date; default to the current date; error on Save if blank: "Date of Review is required.")
    * Personal Thoughts (required; memo; error on Save if blank: "Personal Thoughts is a required field.")
    * Negative Comment / Cautions (optional; memo)
    * Overall Rating (label in bold text; required; drop list of numbers 1-5; error on Save if blank: "Overall Rating is required.")



  


  * Personal Reference section (visible only for the reviewing Member and uplines):
    * Add Knowledge Tree Entries (link to open the editable Knowledge Tree Quick Entry Report in a new browser tab to enter the key points; requires the user to save the current Review before continuing; see the "Knowledge Tree Quick Entry Report" section of the proposal for more details)
    * Knowledge Tree Entries (read-only embedded spreadsheet of the following; displays Entries matching the Reviewer's Name and Resource):
      * Columns: 
        * Knowledge Tree Entry
        * Page Number
        * Knowledge Tree Branch
        * View (displays as "Link" for each row; link to open the corresponding Knowledge Tree Entry record) 
        * ID (displays the Knowledge Tree Entry ID)
      * Automatically sorted by: N/A
      * Show 10 rows without scrolling
    * Add Knowledge Tree Entries (link to open an editable report in a new browser tab to enter the key points; see the "Knowledge Tree Quick Entry Report" section of the proposal)
    * Related Meeting(s) (conditional visibility - see note below; automatic and read-only embedded spreadsheet with the following:) 
      * Columns: 
        * Meetings (one row for each Meeting; displays the Growth Ring Meeting(s) for which the Reviewer is on the Attendance list and for which the Resource was the selected Development Resource; uses the format of "<Growth Ring Group Description> \- <Meeting Date>")
        * View (displays a link with the text "Open Record"; opens the corresponding Meeting record) 
      * Automatically sorted by: Meetings (alphabetically)
      * Show 4 rows without scrolling
      * Other Notes: 
        * Conditional visibility: This table is hidden if there are no linked Meetings for the reviewer. In this case the table is replaced with the following message on the screen: "This resource has not been used in any of your Growth Ring Group Meetings.



  


Data Access: See the Data Access Controls section of the proposal for details.

  


Special Considerations: 

  * Copy Record: N/A
  * Delete Record: Prevent deletion if the record is referenced anywhere in the Solution: "This Review cannot be deleted because it is referenced by another record in the database."
  * Merge Record: Only can be merged by Super Admins. All other users would get a message to contact an Admin to resolve a duplicate. 



  


Other Notes:

  * As mentioned, the same Member cannot create multiple Review records for the same Resource. If a member wishes to review the same resource again, he must update his existing review. 
  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Change Requests:

  * Tim Reitz 02/26/2024: [[[IN9066](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9068&)]] - ZSB - Resource & Review Records - Improve Creation & Field Defaults
  * Tim Reitz 04/08/2024: [[[IN9637](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9639&)]] - ZSB - Improve User Workflow for Growth Ring Meetings (prev. Add links to Members Menu and...)
  * Tim Reitz 04/08/2024: [[[IN8933](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8935&)]] - ZSB - Dev. Resource Review Record - Misc. Changes
  * Tim Reitz 09/03/2024: [[[IN10488](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10490&)]] - ZSB - Review Record - Knowledge Tree Entries RG - Column Labels
  * 


  


  


  


Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=398976222](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=398976222)
