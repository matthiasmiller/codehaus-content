6.1. Weekly Time Sheets Record

  


Requirements

Overview: The Weekly Time Sheet is used by members to track hours or days worked and PTO time used. The record itself contains the fields for tracking both hours and days, but only the appropriate fields would be visible (based on the corresponding member's Base Compensation type). 

  


Accessed via: 

  * My Time Sheet option on the Main Menu 
  * Time Sheets Report 



  


Sections and Fields: 

Summary section: 

  * Employee (auto-filled and read-only) 
  * Work Week (mm/dd/yyyy - mm/dd/yyyy; starting on Thursday and ending on the following Wednesday)
  * View All Weekly Time Sheets (link to the Time Sheets Report for the current member)
  * Left and right arrows beside the above link, to navigate directly to the previous or subsequent Time Sheets for the current member 
  * Total Hours (visible if Base Comp = Hourly; total for the work week; auto-filled and read-only)
  * Total Days (visible if Base Comp = Daily or Salary; total for the work week; auto-filled and read-only)
  * Tasks $ (total for the work week; auto-filled and read-only)



  


Hours / Days Worked section: (shows "Hours" if the member's Base Comp = Hourly; shows "Days" if Base Comp = Daily or Salary) 

  * Embedded spreadsheet with the following: 
    * Columns:
      * Weekday (required; choice of weekdays, Thursday-Wednesday) 
      * Date (auto-filled and read-only; corresponds to the selected Weekday for the row; always for the selected Work Week)
      * Worked Hours (visible and required if Base Comp = Hourly; number field to 1 decimal place; default to blank; accepts "0" as a value)
      * PTO Hours Used (visible if Base Comp = Hourly; editable only for admins; number field to 1 decimal place; default to 0)
      * Worked Days (visible and required if Base Comp = Daily or Salary; drop list of 0, .25, .5, .75, 1; default to blank) 
      * PTO Days Used (visible if Base Comp = Daily or Salary; editable only for admins; drop list of 0, .25, .5, .75, 1; default to 0) 
      * Notes (plain text field)
    * Sorted by: Weekday (Thursday-Wednesday)
    * Buttons to add and remove rows ("+" and "-")
    * Show at least 10 rows without scrolling
    * Each week should default to having one row for for each work day
  * Worked Hours (if Base Comp = Hourly; total for the work week; auto-filled and read-only)
  * Overtime Hours (if Base Comp = Hourly; total for the work week; auto-filled and read-only; sum of Worked Hours in excess of 45.0)
  * PTO Hours (if Base Comp = Hourly; total for the work week; auto-filled and read-only)
  * Total Hours (if Base Comp = Hourly; total for the work week; auto-filled and read-only)
  * Worked Days (if Base Comp = Daily or Salary; total for the work week; auto-filled and read-only)
  * PTO Days (if Base Comp = Daily or Salary; total for the work week; auto-filled and read-only)
  * Total Days (if Base Comp = Daily or Salary; total for the work week; auto-filled and read-only)



  


Tasks bottom report: See corresponding section of this proposal.

  


Data Access:

  * Admins have full access to all Time Sheets
  * Other Member-type users can view and edit only their own Time Sheets
  * Non-member Salespeople can not view or edit any Time Sheets 



  


Other Notes:

  * The Time Sheet should become read-only 18 days (2.5 weeks) after its Work Week Start Date. 
  * Note that there is no overtime tracked for Daily and Salary compensations.



  


  


*Done.

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1539016650](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1539016650)

  


Custom lookup record (NOT the standard AppHosting Time Cards).

  


Tim Reitz 10/21/2021: We're thinking that the Hours Worked and Days Worked would be one and the same RG, with conditionally visible columns. Have a hidden field on the time sheet that gets copied from the user, indicating that this is a Day vs Hour time sheet.
