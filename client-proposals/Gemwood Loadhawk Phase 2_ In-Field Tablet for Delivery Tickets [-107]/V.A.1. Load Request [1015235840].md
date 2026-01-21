5.1.1. Load Request

Overview: This is a custom record type, used to track a load request for a member.

  


Accessed via: Main Menu | Mobile App | Load Requests

  


Sections and Fields: 

  * Load Request Overview section: 
    * <Status> Load Request: <Desc> (header label; status is open or closed, based on Close Date)
    * Desc (plain tex; requiredt)
    * Date (created date; uneditable)
    * Member (drop-list of active member contacts; required)
    * Create PO (visible if the load request is open; creates a Buyer PO for the member, filling in description and itemization and linking the PO to the load request via a hidden ID field)
    * Close Date (date; set by trigger)
    * Itemization (unlabeled; embedded spreadsheet with the following: 
      * Columns:  
        * Thickness (drop-list of Lumber Thicknesses; required)
        * Species (drop-list of Species; required)
        * Grade (drop-list of Lumber Grades; required)
        * BF Qty (number; no decimals; required)
        * Internal Notes (plain text)
        * Item ID (number; no decimals; hidden; auto-sets to a random integer between 0 and 2 * 1000^3)
      * Buttons to add/remove rows: "✚" / "🞭"
      * Shows 4 rows without scrolling 
    * Notes (memo)



  


  * Bottom report: displays all packs linked to the load request.
    * Columns:
      * Date (link to the record)
      * Pack ID
      * BF Qty
    * Grouped by: Thickness + Species + Grade
    * Sorted by: Pack ID



  


  * Record History section (unlabeled): 
    * Modification History (link to open the report for the record)


