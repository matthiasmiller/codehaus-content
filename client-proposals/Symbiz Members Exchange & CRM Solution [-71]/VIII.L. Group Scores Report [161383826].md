8.12. Group Scores Report

  


Requirements

The client would like to be able to track Group scoring within the software. We are creating this User Report to allow them to do this. In the future, this report will likely be standardized and integrated into the rest of the system.

  


Overview: This is a report of all Scoring metrics used by Symbiz. By default, this report shows one row per Completed Growth Ring Meeting but can be filtered to only show point totals per Group.

  


Accessed from: Shared Folder

  


Title: Group Scores

  


Columns: 

  * Meeting Date (link to record)
  * Members Attended (displays the number of points allotted for the number of Members that attended the Meeting, based on the Attendance table on the Meeting record) 
  * Book Impact Completed / Application Made (displays the number of points allotted for the number entered in the corresponding field on the Meeting record) 
  * Goals Set (displays the number of points allotted for the number of Goals set by Members, based on the corresponding field on the Meeting record)
  * Goals Achieved (displays the number of points allotted for the number of Goals achieved by Members, based on the corresponding field on the Meeting record)
  * Symbiz Core Value Stories (displays the number of points allotted for the number entered in the corresponding field on the Meeting record)
  * New Members Added (displays the number of points allotted for the number of Members who were not in the Attendance table in the last Completed Meeting)
  * Vision Statements Memorized (displays the number of points allotted for the number entered in the corresponding field on the Meeting record)
  * Symbuzz Extra Posts Entered (displays the number of points allotted for the number of Symbuzz Extra Posts entered, based on one or more of the Symbuzz fields being non-blank on the Meeting record) 
  * Credit for New Group(s) (displays the number of points allotted for the total number of new Groups + Members that have been credited to this Group in the past 3 month if this Meeting is the first Meeting since the "Credit as of" field on the new Group record) 
  * Members Not Attended (displays the points deducted for the total number of Members that did not attend the Meeting, based on the Attendance table on the Meeting record; number is displayed as negative) 
  * Goals Not Achieved (displays the number of points deducted for Members that did not achieve Goals, based on the Attendance table on the Meeting record and "Total Goals Achieved" field on the Meeting record; number is displayed as negative)
  * Members w/o Vision Memorized (displays the number of points deducted for Members without the Vision memorized, based on the "Total Group Members" and the "Members with Symbiz Vision Memorized" fields on the Meeting record; number is displayed as negative) 
  * Total Points (displays the total points allotted for each Group, using the Symbiz scoring formula; total row shows average per meeting) 
  * Member Average (displays the average of points per Member for the row; like the following: 100 Total Points for the Group for a Meeting, 5 members in the Group, so 20 Points/Member; total row shows Member average per meeting) 



  


Grouped by: Growth Ring Group

  


Sorted by: Growth Ring Meeting (most recent date at the top)

  


Filters: 

  * Growth Ring Group (optional; drop list of all Growth Ring Groups; defaults to blank = all)
  * Time Period (optional; drop list of the following:
    * Date Range 
    * Year To Date 
    * All Time
    * Last Fiscal Year (runs the report for the last Fiscal Year)
    * Current Fiscal Year (runs the report for the current Fiscal Year)
    * Previous Two Months (runs the report to show data for the previous two full calendar months;
    * defaults to "Previous Two Months") 
  * From (date field; optional; visible if "Time Period" = "Date Range"; defaults to blank = all)
  * Through (date field; optional; visible if "Time Period" = "Date Range"; defaults to blank = all)
  * Totals Only (checkbox; defaults to unchecked; when checked, displays the report with only the totals per Group)



  


Buttons: 

  * N/A



  


Menu Visibility: 

  * N/A (User Report)



  


Other Notes: 

  * This report uses alternate gray/white backgrounds for the rows. 
  * Scoring system:
    * Member Attended: 10
    * Dev. Resource / Assignment Completed: 10
    * Goal Set: 10
    * Goal Achieved: 10
    * Core Value Story shared: 20
    * New Member Added: 200
    * Group Credited: 500 + 200 per member
    * Vision Statement Memorized: 10
    * Resource Impact Submitted: 20
    * Symbuzz Extra Post: 50
    * Member Not Attended: -20
    * Goal Not Achieved: -10
    * Vision Statement Not Memorized: -50
  * The grouping totals will be at the top of the group and the grand total will be at the top of the report
  * Fiscal Year is May 1st - April 30th
  * Columns for the actual metric numbers could be added as an additional enhancement



  


Development Specification

Change Requests:

  * Ben Reitz 06/09/2025: [[[IN10519](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10521&)]] - ZSB - Add Group Scoring features and report
  * Ben Reitz 09/17/2025: [[[IN11622](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11624&)]] - ZSB - Growth Ring Meeting record - Change "Dev. Resource / Impact Submitted" field


