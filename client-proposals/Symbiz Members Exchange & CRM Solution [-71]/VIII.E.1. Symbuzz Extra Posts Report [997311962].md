8.5.1. Symbuzz Extra Posts Report

  


Requirements

This is an editable report of Symbuzz Extra Posts from Growth Ring Meetings with Status = Complete, with various filtering options. 

  


This is accessed from: 

  * Admin | Symbuzz Extra | Symbuzz Extra Posts (bypasses the filter screen to open the report directly) 
  * Links in user notifications (with various filters set) 



  


Title: Symbuzz Extra Posts (<Weekly / Monthly>) (<Post Entry Date Start - <Post Entry Date End>)

  


Columns: 

  * Reviewed (editable checkbox that displays as Yes/No; defaults to No; "Yes" displays in green text and "No" in red) 
  * Growth Ring Group 
  * Meeting Date (link to record)
  * Development Resource 
  * Secretary
  * Growth Ring News (wrapped text; editable; pulls from corresponding field on the record)
  * Prayer Requests (wrapped text; editable; pulls from corresponding field on the record)
  * Networking Requests (wrapped text; editable; pulls from corresponding field on the record)



  


Grouped by: Week (Sunday-Saturday, i.e. 12/31/2023 - 01/06/2024)

  


Sorted by: Meeting Date (most recent date at the top)

  


Filters: 

  * Growth Ring Group (drop list of all Groups; defaults to blank = all)
  * Format (drop list of Monthly / Weekly / Custom; defaults to Weekly) 
  * Month (visible if Format = Monthly; required; drop list of months in the "MMMM YYYY" format, with the current month at the top; starts with the month of the first Symbuzz Extra Post entry, through the current month; defaults to the current month) 
  * Week Of (visible if Format = Weekly; required; drop list of dates in the mm/dd/yyyy format, with most recent date at the top; starts with the week of the first Symbuzz Post entry, through the most recent Sunday; defaults to the second-most recent Sunday)
  * Post Entry Date Start (visible if Format = Custom; optional; date; looks at the date that the first entry was made on a Post field for a Meeting record; defaults to 1 month before the current date) 
  * End (visible if Format = Custom; optional; date; looks at the date that the first entry was made on a Post field for a Meeting record; defaults to blank = all) 
  * Meeting Date Start (date; looks at the Meeting Date; defaults to blank = all)
  * Meeting Date End (date; looks at the Meeting Date; defaults to blank = all)
  * Search for Text (plain text; defaults to blank; results in the report are filtered to Meetings that include the exact text in one or more of their Posts, and the matches are highlighted on the report) 
    * Extra label text to the right of the "Search for Text" label: "(entering search text will make the Post fields read-only)"
  * Hide Review Column (checkbox; only visible for Super Admins; defaults to unchecked) 



  


Buttons: 

  * Print PDF (prints the printout for the selected filters)



  


Menu Visibility: Regional Reps and Super Admins (by virtue of the Admin Menu being restricted)

  


Save Type: Instant Save

  


Other Notes:

  * Note at the top of the report (visible only for Super Admins; only visible if the Hide Review Column checkbox is unchecked): "To prevent a post from being included in the Symbuzz Extra, either delete it or cut & paste it into the Internal Meeting Notes."
  * Date range for Monthly: 
    * Post Entry Start Date: The third Thursday of the previous month
      * Example: On Thursday, 1/18/24, this would default to Thursday, 12/21/23.
    * End: Wednesday before the third Thursday of the current month; 
      * Example: On Thursday, 1/18/24, this would default to Wednesday, 1/17/24.
  * Date range for Weekly: 
    * Post Entry Start Date: 2 Sundays prior to the current date 
      * Example: On Monday, 1/15/24, this would default to Sunday, 1/7/24. 
    * End: 7 days after the Start date;  
      * Example: If the Start date is Sunday, 1/7/24, this would default to Saturday, 1/13/24.



  


Development Specification

Tim Reitz 04/11/2024: Added with [[[IN8960](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8962&)]] - ZSB - Add Features for Symbuzz Extra (prev. called Cross Network Forum).

  


Change Requests: 

  * Tim Reitz 04/11/2024: [[[IN9417](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9419&)]] - ZSB - Symbuzz Extra - Revisions (#1)


