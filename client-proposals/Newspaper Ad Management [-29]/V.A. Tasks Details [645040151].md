5.1. Tasks Details

  


Requirements

Each Customer/Ads Page should have a Tasks section with tasks and reminders related to that customer. Most Tasks are connected with a certain publication date and ad, but all are at least associated with a customer. In some cases the task process would be started before the ad is started; in these situations the user should be able to enter the ad once it has been created.

  


Tasks can be edited after they have been marked complete.

  


Incomplete Tasks from on Publication Date should automatically carry over to the next Publication Date, and should continue to do so until they have been marked complete. There will be an automatic process to do this.

  


The Tasks section would have the following:

  


Embedded spreadsheet:

  * List of Tasks:
    * Incomplete at the top, Complete at the bottom
    * Sorted by date within the groupings (newest at the top)
    * Completed Tasks should be in gray
  * Each row shows a summary:
    * Task Name
    * Assignee
    * Publication Date
    * Ad Title
    * Complete (checkbox) 
    * Reminder (link)
    * Prior Comments (ellipsis button)
    * Allow Editing (checkbox)
    * New Comment (ellipsis button)
    * Note that not all columns will show; some will be hidden to the right side, but can be viewed by scrolling at the bottom of the embedded spreadsheet.



  


New Task Button: See details in the "Creating New Tasks" section of this proposal. 

  


Tasks Details: Each Task should track the following things:

  


  * Task Name (required; text field)
  * Customer (required if created from the report; auto-filled if created from the Customer/Ads Page; read-only after save, but still updates automatically if the Customer name is edited)
  * Publication Date (required; defaults to current; editable; warn if they set the date to a past pub date)
  * Ad Title (optional; drop list of all Ad Titles for the selected Customer for the selected Publication Date; auto-filled if created from an Ad Detail; read-only after save, but still updates automatically if the Ad Name is edited)
  * Assignee (required; defaults to Unassigned; editable; list of "Unassigned", all Full Admin Users, and all Users assigned to the current publication)
  * Repeating Task (checkbox; defaults to unchecked)
  * Number of Times (visible and required if Repeating Task is checked; see details in Repeating Tasks section of this proposal)
  * Create Reminder (link; see the Reminders section of this proposal for more information) 
  * View Reminders (link; see the Reminders section of this proposal for more information) 
  * Prior Comments (memo; normally read-only, but editable if the "Allow Editing" checkbox if filled)
  * New Comment (memo; upon saving the Customer/Ads Page, anything entered in this memo will be automatically moved to the Comments memo.
    * Each comment will be separated from the one above it with a line that is automatically added.
    * Each comment would automatically show the author, date, and time in a format such as "John Doe 01/26/2021 8:33 AM: " 
    * Note that edits in the main memo would not automatically show the separator line or the name/date/time stamp, but they can be added.
  * Allow Editing (checkbox; defaults to unchecked; if checked, the Prior Comments memo becomes editable; automatically unchecks on Save)
  * Complete (checkbox; defaults to unchecked; when checked, the Task is considered complete and its line in the embedded spreadsheet turns gray and is moved to the bottom part of the list).



  


Note that the memos used for New Comment and Prior Comments do not scroll due to platform limitations. If the entered text is longer than the initial size of the memo, the memo will expand down the screen, pushing other sections below it further down. 

  


General Notes: 

  * Memos can display the following file types: GIF, PNG, JPG, BMP. Other file types can be saved in the memos, but the actual image will not be displayed.



  


Development Specification

Matthias: Technically, we can give him a Virtual RG (but no MRG) to view/edit tasks just for the current ad, but I'm hesitant to offer that unless it's needed.

  


  


Tim Reitz 02/02/2021: For name, time, and date stamp: Use the FormattedText function.
