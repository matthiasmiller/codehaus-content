2\. TODO - Phase 1: Project Management

  


Requirements

Current Priorities:

  * Project Management
  * Quoting
  * CRM



  


TODO - Eventually want to drive customers from Leads.

  


\----

Niccolas Miller 12/17/2025: Mockups.

[https://docs.google.com/spreadsheets/d/1UWnOkEYlXAvGi2oFyyJSl6t9tFuGADRCMTJxQWcIwp4/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1UWnOkEYlXAvGi2oFyyJSl6t9tFuGADRCMTJxQWcIwp4/edit?usp=sharing)

PC: [[PC0188048]] - ZHS - Phase 1: Project Management

  


Scope 1 - Managing the tasks

  


NOTE: There is a single component within each order.

  


The Resource is the crew that's doing that phase.

  


Contact Type [[PC0188069]]

  * Customer
  * Integrator
  * Employee 



  


  * NOTE - Customers will be entered manually for the time being.



  


Silverloom Settings

  * JobPack Operations
    * Description (string)
    * Job Milestone (list of Job Milestones)



  


JobPack Workplace

  * Silverloom ID (autonumber; read-only)
  * JobPack ID (number; 0 decimals)
  * Name (string)
  * Active (checkbox; default to true)



  


JobPack Order

  * Silverloom ID (autonumber; read-only)
  * Order No (number)
  * Order Name (string)
  * Operations
    * No (number; required)
    * Seq Num (number)
    * Name (string)
    * Description (string)
    * Scheduled Start Date (date)
    * Scheduled End Date (date)
    * Actual Completed Date (date)
    * JobPack Workplace ID (number)



  


Job Milestones [[PC0188051]]

  * Name
  * Active (checkbox)
  * JobPack Milestone (checkbox)
  * JobPack Operation (list of JobPackOperations; visible & required if JobPack Milestone is checked; list should be user-editable [CanAddToList:InImport]) [[PC0188967]] TODO_MM: Is the spec for JobPack Operations in Silverloom Settings outdated? If so, do we match JobPack Operation here to the Name string in the Operations RG on the JobPack Order record? If not, shouldn't JobPack Operations here just be a macro that looks it up from Silverloom Settings?



  


  * NOTE: The software will ship with the following milestones:
    * Concrete Scheduled Start
    * Construction Scheduled Start
    * Equipment Scheduled Start
    * Electric Scheduled Start
    * Walkthrough Date
    * Bird Date
    * Committed Date
    * Farmer Training Date
    * Packer Install Date



  


Job Task Template

  * Update Existing Jobs button
    * NOTE:
      * Add this task to any open job where it's <= 14 days past due
      * Remove deleted tasks from any open jobs where it's not been completed
    * Prompt For:
      * Maximum Days Past Due (default to 14)
  * Tasks (embedded RG)
    * Task (string)
    * Department (list of active Departments)
    * Milestone (required; list of Job Milestones)
    * Number of Days +/- (number; 0 decimals)
    * Flag When Overdue from Schedule Changes (checkbox)



  


Department [[PC0188985]]

  * Name
  * Active (Checkbox; default to checked)



  


NOTE: Ship with a "Project Management" department.

  


Contact

  * Visible if Contact Type = Employee:
    * Department (list of active departments)



  


Crew

  * Silverloom ID (autonumber; read-only)
  * Name (read-only; pulls from JobPack)
  * Willing to Travel (checkbox)
  * JobPack Workplace No (number; not editable interactively; error on change if there is another crew with the same workplace number) [[PC0188968]]



  


Job

Job

  * Silverloom ID
  * JobPack Order No (number; not editable interactively; 0 decimals)



  


JobPack Details

  * Job Name (expression; lookup from JobPack Order based on JobPack Order No.)
  * Job Description (plain text field)
  * Estimated Finish Date (read-only; greatest date for JobPack milestones in the Milestones RG)
  * Days Ahead of Committed (read-only macro; Scheduled For date for Committed Date milestone - the maximum of Estimated Finish Date and the greatest Completed On date in the job milestones RG)



  


Job Details

  * Customer (list of Customers)
  * Phone (read-only; from Customer)
  * Email (read-only; from Customer)
  * Project Manager (list of active employees in Project Management department)
  * Crew (read-only macro; list of Crews; finds the crew record that matches the JobPack Workplace for the linked JockPack Order No)
  * Location (string)
  * Integrator (list of Integrators)
  * Notes (memo button) [[PC0189007]]



  


Milestones

  * Milestones (embedded RG)
    * Type (list of active Job Milestone record names; error if there are duplicate types)
      * Concrete Scheduled Start
      * Construction Scheduled Start
      * Equipment Scheduled Start
      * Electric Scheduled Start
      * Walkthrough Date
      * Bird Date
      * Committed Date
      * Farmer Training Date
      * Packer Install Date
    * Needs Approval (checkbox; read-only & automatic; is checked when any linked task are marked as Needs Approval) [[PC0188969]]
    * Scheduled For (date; editable in import for JobPack milestones, always editable for non-JobPack Milestones)
      * When modified via import, checks Needs Approval on any linked tasks that have "Flag When Overdue from Schedule Changes" checked are newly (not previously) overdue. 
    * Scheduled End Date (read-only date; only visible for JobPack milestones) [[PC0188969]]
    * Completed On (date; editable in import for JobPack milestones, always editable for non-JobPack Milestones)
    * TODO_NM: For linking, I expect we just want to go from Milestone -> JobPack Operation -> Looking it up on the JobPack Order



  


Documents

  * Documents (embedded RG)
    * Name (plain text; read-only)
    * Upload Time
    * Upload Date
    * Download (link)
    * Delete (link)
  * Upload Attachment (link)
    * Mirror what we do in ZRT/ZFP.
      * For each DB level, set the up the fields/detail screen RG. See ZFP for inspiration.
      * Create a Std Service Attachments Info.r20 (i.e. copy it from ZFP) and create the AttachmentInfo macro.



  


Tasks

  * TODO_NM: How do we add tasks from template? OnInit?



Niccolas Miller 01/20/2026: Perhaps the same x30 as we use for updating tasks from template? Triggered upon record creation?

  


  * Matthias Miller 01/19/2026: System Switch for the minimum JobPack Order No to import (?)


  * Tasks (embedded RG; rows cannot be edited if they are complete)
    * Columns:
      * Task (string)
      * Assignee (blank; list of Project Managers) 
      * Department (list of active departments; non-editable interactively for template rows) [[PC0188969]]
      * Milestone (list of active job milestone records; non-editable interactively for template rows)
      * Days +/- (number; non-editable interactively for template rows; when modified, sets Needs Approval for the related milestone according to the Set Milestone Needs Approval shared OnChange; this is needed when updating the task template)
      * Due Date (date; auto-calculated from Milestone date +/- days)
      * Flag When Overdue from Schedule Changes (checkbox; non-editable interactively for template rows)
      * Needs Schedule Change Approval (checkbox; automatically set when updating from JobPack; editable non-interactively; editable interactively by admin or by Department member) [[PC0188969]] 
      * Template Task ID (number; hidden; non-editable interactively)
      * Completed (editable boolean macro; unchecked if Completed Date is blank; checked if it is not blank; sets Completed Date to the current date when checked)
      * Completed Date (date)
    * Append/Delete buttons (rows cannot be deleted if Template Task ID is not blank)



  


  


  * NOTE:
  * Payments (downpayment, progress payment, and final payment) can all be driven off Committed Date and other Milestones.



  


  


Imports

TODO_NM: Review these specs & sign off on them please

  


Niccolas Miller 01/20/2026: Approved. [[PC0188974]]

  * Std Service JobPack Resources.x30list (An x30list is a bit redundant, except it makes it easier to update in the future if we need additional things to happen with this.
    * Std Service JobPack Resources.x30 - Match on column names:
      * jobpack_resource_no - JobPackWorkplace - JobPack ID (match records on this ID)
      * jobpack_resource_name
      * jobpack_resource_status (0 means it's active; 100 means archive)
      * Deactivate unmatched records.



  


  


Niccolas Miller 01/20/2026: Written up, TODO_NM in design [[PC0188977]]

  * Std Service JobPack.x30list
    * Std Service JobPack - Import JobPack Orders (with both non-RG and RG changes). Match on column names". Match RG rows on op_no. Match on the first one, and delete unmatched rows.



  


Input Column| JobPack Order Field  
---|---  
order_no| Order No  
order_name| Order Name  
op_no| Operations → No  
op_seqnum| Operations → Seq Num  
op_name| Operations → Name  
op_descr| Operations → Description  
op_scheduled_start_date| Operations → Scheduled Start Date  
op_scheduled_end_date| Operations → Scheduled End Date  
op_actual_end_date| Operations → Actual Completed Date  
op_pwplace_no| Operations → JobPack Workplace ID  
  
  


  * Std Service JobPack - Sync Job Milestones
    * r20/x30 pair
      * Run on JobPack Orders with a Repeat for List of active milestones that link to JobPack
      * Columns
        * JobPack Order No
        * Milestone Name
        * Scheduled Start Date
        * Scheduled End Date
        * Actual Completed Date
    * x30:
      * Match on JobPack Order No
      * RG - match on JobPack Op No; create if missing
        * Milestone
        * Scheduled For <\- Scheduled Start Date
        * Scheduled End Date <\- Scheduled End Date
        * Completed On <\- Actual Completion Date



  


  


  * Std Task Template - Update Existing Jobs.x30 [[PC0188848]]
    * Ask Prompts:
      * Task Template ID (hidden)
      * Maximum Days Past Due (default to 14)
    * The import updates all open jobs that are <= Maximum Days Past Due prompt past due.
      * Remove tasks that were deleted on the task template if the task has not been completed on the job. 
      * Set the following fields for new/existing tasks:
        * Task
        * Milestone
        * Number of Days +/-



  


  * S3 Support [PC0189008]]
    * Add a UserProfileAltWSGIHost field a la ZFP
    * Add a macro called S3WSGIUrl that evaluates to blank in the S3 base catalog.
    * Change ZFP to evalute it to WSGIUrl( '')
    * Move ZFP's overrides of WSGI_AttachmentUrl, WSGI_DeleteAttachmentUrl, and WSGI_AddAttachmentUrl to the base folder. Keep the new Assign vURL format.
    * Change the last line to check if the S3AltWSGIUrl is blank, and return the URL as-is. Otherwise, do the replace that had been in ZFP
    * Please have Seth very carefully review this change and maybe even figure out how to test it to make sure that URL generation does not change. You might note in these macros that is' VERY important to generate the original URL first so that the HMAC calculates correctly.



  


Reports

  * Jobs Dashboard (report of Jobs) [[PC0188068]]
    * Columns
      * Integrator
      * Job Name
      * Bird Date
      * Committed Date
      * Estimated Finish Date
      * Days Ahead of Committed (progress bar 0-14; green if > 0; red if <= 0; use absolute value for number [-5 displays same length as 5])
      * PM (Project Manager)
      * Location
      * # Tasks Completed
      * # of Overdue Tasks (uncompleted tasks with due date in the past)
      * Walkthrough Date
      * Farmer Training Date
      * Packer Install Date



  


  * Tasks [[PC0188070]]
    * Menu:
      * My Open Tasks (defaults Assignee to the current user's linked contact record)
      * All Open Tasks (defaults Status to "Past Due" and "Upcoming")
      * Search Tasks
    * Prompts
      * Assignee (list of project managers; blank = all)
      * Customer (list of customers; blank = all)
      * Departments (multi-select list of departments; blank = all) [[PC0188973]]r
      * Milestone (list of milestones)
      * Status (multi-select; use list)
        * Past Due
        * Upcoming
        * Complete
      * Date (list)
        * Today
        * This Week - based on Saturday
        * Now Thru Next Week - based on next Saturday
        * Current Month
        * 30 Days
        * 90 Days
        * Anytime
        * Other (specific date)
      * Date (if Other)
      * TODO: Consider: Text search - TODO_NM: Yes, both Notes and the tasks
    * Columns
      * Assignee
      * Customer
      * Department
      * Milestone
      * Task
      * Due Date (red text if past due)
        * NOTE: The due date should be red if it's < the completion date (if completed) or < today if it's not completed
      * Completed
      * Completion Date
    * Sort by:
      * Due Date
    * Group by:
      * Schedule Changes Needing Approval (group at top if linked milestone is marked Needs Approval; all others are grouped below)



  


  * Notifications [[PC0189010]]
    * Report Alert
      * All tasks needing schedule approval linked to the current user as a project manager, or linked to the current user's department. Does NOT disappear until everything is resolved, either via JobPack or via approval.
      * Columns
        * Job ID
        * Assignee
        * Customer
        * Department
        * Milestone
        * Task



  


Development Specification

TODO_DEVSPEC:

  * x30s
    * JobPack Order + Operations
    * JobPack Resources
    * Sync JobPack Milestones to jobs
    * Update Tasks When Template Changes
  * Add macros to pull a specific milestone dates



  


SQL

  


SELECT

    or_order.no AS order_no,

    or_order.name AS order_name,

    or_op.no AS op_no,

    or_op.seqnum AS op_seqnum,

    or_op.name AS op_name,

    or_op.descr AS op_descr,

    CAST(DATEADD(s, or_op.startsec, or_op.STIME) AS DATE) AS op_scheduled_start_date,

    CAST(DATEADD(s, or_op.endesec, or_op.etime) AS DATE) AS op_scheduled_end_date,

    PETIMEMIN AS op_actual_end_date,

    or_op.pwplace AS op_pwplace_no

FROM

    or_op

INNER JOIN

    or_order ON or_op.orno = or_order.no

INNER JOIN

    wp_mai1 ON or_op.pwplace = wp_mai1.no

WHERE

    or_order.einlast = 1

    AND or_order.status <> 2

    AND or_op.stime IS NOT NULL

ORDER BY

    or_order.no ASC,

    or_op.seqnum ASC;

  


  


SELECT

wp_ma1.no AS jobpack_resource_no

wp_ma1.name AS jobpack_resource_name

wp_ma1.status AS  AS jobpack_resource_status

FROM

wp_mai1

  


  


Field| Technical Meaning (Suffix)| Actual Usage in Model  
---|---|---  
PSTIMEMIN| Min Start| Plan: Earliest allowable start  
PSTIMEMAX| Max Start| Actual: Real Start (SFDC)  
PETIMEMIN| Min End| Actual: Real End (SFDC)  
PETIMEMAX| Max End| Plan: Latest allowable end  
  
  

