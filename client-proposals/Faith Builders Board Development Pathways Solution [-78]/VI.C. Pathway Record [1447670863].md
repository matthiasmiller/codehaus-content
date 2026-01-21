6.3. Pathway Record

  


Requirements

Overview: Pathways will be configured on the Pathway records and viewed on a Pathways report.

  


Accessed via: (TBD in IDD)

  


Sections and Fields: 

  * Pathway Details section:
    * Active (checkbox; defaults to checked; if unchecked, the Pathway does not show up as an option for signing up; if unchecked while one or more Organizations are taking the Pathway, emails continue to go out but no one else can sign up for it)
      * This could also be a "Status" drop-list (i.e. "Draft", "Allow New Subscriptions", "Archive", etc. TBD in IDD)
    * Pathway Title (required; plain text)
    * Pathway Description (required; multi-line plain text)
    * Tags (multi-select drop list of Pathway tags; used to specify one or more themes in the Pathway)
    * Number of Lessons (required; number with no decimals)
    * Lessons (embedded spreadsheet of all Lessons in the Pathway):
      * Columns:
        * Lesson # (required; number field with no decimals; auto sets when a new row is added)
        * Lesson Title (required; wide enough to handle 60+ characters)
        * Lesson Type (required; drop list of "Book" / "Video"; used to ensure that the right content items are added)
        * PDF Attachments (required; details to be determined) 
        * Digital Resource Link (editable and required if Lesson Type = Video; used for pasting in a link to an external video)
        * Additional Notes (optional; multi-line plain text)
        * Additional Email Text (button; opens a child screen with a memo that supports expressions; contents of this memo are included in the corresponding Lesson email)
      * Automatically sorted by: Lesson #
      * Buttons to insert/append/remove rows: "Insert", "Append", "Delete"
      * Show 20 rows without scrolling



  


  * Pricing section:
    * Base Price/Seat $ (required; number field to 2 decimals; this is the price for Email [and Fax if not too much extra])
    * Additional fee per lesson for Fax (required; number field to 2 decimals) (possible field)
    * Additional $/lesson for Print Seat (required; number field to 2 decimals)
    * Additional $/lesson for Canada Print Seat (required; number field to 2 decimals)



  


  * Reporting section:
    * View Subscriptions (link; opens a report of Subscriptions filtered to the corresponding Pathway)
    * Times Purchased (auto-set and read-only; displays the number of times that this Pathway has been purchased)
    * Times Completed (auto-set and read-only; displays the number of times that this Pathway has been completed)
    * # of Participants (auto-set and read-only; displays the number of current and past Participants)



  


Data Access: (TBD in IDD)

  


Special Considerations: (TBD in IDD)

  * Copy Record: 
  * Delete Record: 
  * Merge Record: 



  


Other Notes:

  * If a Pathway needs to be edited significantly, the user should make a copy of the existing record and spec out the details on the new record, then deactivate the old so that it cannot have new subscriptions created for it. Details for this, including what would quantify "significantly", are to be determined in the IDD. 
  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

PDF Attachments: 

  


TODO_IDD: Tim Reitz 09/07/2023: Planning to add support for attachments from Document Archive (see [[PC0122636]] - Email Templates: Support attaching archived documents).
