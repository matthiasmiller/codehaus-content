19\. Initial Notes for HLD

Tim Reitz 12/08/2025: HLD calls with the clients: 

Call 1 (12/02/2025): 

[https://invtools.zoom.us/rec/share/sEZ_xNG3vy3J3PkNXtBnctoMBKuNmS3sXtxQdkjQt5RU4zbeJzF8fsBPkimWShIV.4hPYt0nZHj6EnoTF](https://invtools.zoom.us/rec/share/sEZ_xNG3vy3J3PkNXtBnctoMBKuNmS3sXtxQdkjQt5RU4zbeJzF8fsBPkimWShIV.4hPYt0nZHj6EnoTF) 

Passcode: !HXdu3@w 

  


Call 2 (12/02/2025): 

[https://invtools.zoom.us/rec/share/AyR73Wcfp5vjwxSvJ9uWa8K9x3JDHsdYa-CbFhyctah6O7126HZdsqpzUBR_sevJ.oyf1qHL2Il_gBYV-](https://invtools.zoom.us/rec/share/AyR73Wcfp5vjwxSvJ9uWa8K9x3JDHsdYa-CbFhyctah6O7126HZdsqpzUBR_sevJ.oyf1qHL2Il_gBYV-) 

Passcode: exw2XX@&

  


Matthias Miller 12/03/2025: _TR: We need the following records

  


  * QuickBooks Customer
    * Silverloom ID (autonumber)
    * Customer Name (string)
    * Phone (string)
    * QuickBooks Account Number (string)
    * Silverloom Account Number (automatic; formatted as SILVERLOOM_0001 or something similar)



  


  * Proposed Account Number (Next available account number through an autonumber)



  


  * Sync Process
    * Export Customers from QuickBooks
    * Import Customers into QuickBooks matching on:
      * Quickbooks Account Number (if possible)
      * Silverloom Account Number (if possible)
      * Customer Name (if possible)
      * (otherwise, new record)
      * NOTE: Delete unmatched records.
    * Export all QuickBooks customers from Silverloom that a blank account number
    * Import those customers into QuickBooks, matching on name, thus setting the accoount number in QuickBooks
    * Rerun the Export Customers from QuickBooks / Import Customers into Quickbooks process
    * Export the time data



  


  


NOTE: We need to pick apart the reports needed above

  


  


\----------------

  


  


  * Report - all QuickBook customers without an account number
    * Customer Name
    * Account Number (auto-numbered starting with the latest account number; use models or something similar)
  * Export & Import into Q



  


  


  * Proposal:
    * 


  


  * Proposal:
    * Require setting the customer account number in Quickbooks



DONE_HLD: Tim Reitz 12/04/2025: What does this entail (for purposes of the HLD)?

Matthias Miller 12/08/2025: Not relevant since we're not doing QB integration

  


  * Import
    * Matching on Account Number 
  * Contact record
    * QuickBooks Account Number
      * List of Quickbooks customers - 



DONE_HLD: Tim Reitz 12/04/2025: Are you thinking that this would link the Contact record and the QuickBooks Customer record together?

Matthias Miller 12/08/2025: That was the idea but we're not doing QB integration

  


Matthias Miller 12/02/2025: 

  


  


Settings

  * The 1 Call turnaround (back in 3 days) should be a configurable setting.
  * The 1 Call expiration (valid for 10 days) should be a configurable setting.



  


Lists

  * Crew Types; only two options:
    * Prep
    * Paving
  * Downtime Reasons (list of approximately 5-10 common reasons; TBD)
  * Event Types; following options:
    * Job
    * Time Off
    * Other
  * Prevailing Wage Types (example options include Equipment Operator, Laborer, Truck Driver, etc)
  * Shop Time Categories
  * QuickBooks Payroll Items (customizable list)



  


Event Types

  * Name (read-only)
  * Color (list of colors; hidden for Jobs)



  


Trucks

  * Name (automatic & read-only; Tk#116 Optional Desc)
  * Active (checkbox)
  * Truck # (number; 0 decimals; required; must be unique)
  * Description (string)



  


Trailers

  * Name (automatic & read-only; Tr#116 Belmont Crew #3)
  * Active (checkbox)
  * Trailer # (number; 0 decimals; required; must be unique)
  * Description (string)



  


Crews

  * Name (automatic & read-only; i.e. Paving Crew #1)
  * Crew Type (list of crew types; required)
  * Active (checkbox)
  * Crew # (number; 0 decimals; must be unique by type)
  * Calendar Color (list of colors)



  


  * Example Crews:
    * Prep Crew 1
      * Dave S
      * Clint
    * Prep Crew 2
    * Paving Crew 1
    * Paving Crew 2
    * Paving Crew 3



  


Contact Types

  * Asphalt Plant
  * Employee



  


Contacts

  * For Employee:
    * Regular Rate (number; 2 decimals)
    * Primary Crew (list of crews)
    * Crew Foreman (checkbox; warn if there are multiple foreman per crew)
    * [ ] Enable Time Card PIN
    * Enter Time Card PIN (4-digit numeric PIN; editable by Admin Only)
    * Confirm Time Card PIN
    * Quickbooks Payroll Item (editable by admin only; list of Quickbooks Payroll Items)



  


  


Calendar Event

  * Validation:
    * Warn when scheduling a prevailing wage job on a Friday.
    * Disallow having the same Job ID + Crew for the same day



  


  * Event Type
    * Job
    * Time Off
    * Other
  * Start Date (date; required)
  * Multiday (checkbox)
  * End Date (editable & required if checked & start date is specified; otherwise, read-only and equal to the start date)



  


  * For Time Off
    * Employee (list of active employees)



  


  * For Job type:
    * Job ID (link to view)
    * Groups (multi-select list of Groups; defaults to all groups for the linked job)
      * Hidden RG of Groups for the job
    * Crew Type (Crew Type; Prep or Paving; required)
    * Crew (list of active crews by type; required)
    * Embedded RG (NOTE: Checking the Foreman checkbox sorts the employee to the top of the list. This is defaulted based on the Employee's setting. Require exactly 1 foreman/day.)
      * Employee (required)
      * Foreman (checkbox; only allow 1 / day; require 1/day)
      * Truck (list of active trucks)
      * Trailer (list of active trailers)
    * # of Hired Haulers (number; 0 decimals)



  


  * For Other type
    * Title



  


  


Downtime Reporting

  


  * Prompt for
    * Date Range
    * Reason
    * Group by
      * Customer
      * Crew
      * Reason
  * Columns
    * Date
    * Crew
    * Reason
    * Customer Name
    * Job Name
    * Start Time
    * End Time
    * Duration (Totaled)



  


  


  


Reports

  * Jobs Waiting to be Scheduled
  * Jobs Reading for Final Invoicing report



  


Proposal PDF / Work Order PDF

  * Add an indication for prevailing wage jobs.



  


  


  


Phase 3

Job Costing

  * Sales Item
    * Primary Vendor
    * Additional Vendor



  


  * For the foreman...
    * Have them apply job costs...
    * Change Orders are word for word...



  


  


Calendar

  * Three Views
    * Daily (i.e. Dispatch Sheet)
    * Weekly
    * Monthly
  * Three Columns
    * Paving Crew 1
    * Paving Crew 2
    * Paving Crew 3
  * **Prep Crew shows up on the calendar for the Job's Paving Crew, but in green



  


  * The calendar event Title could be as simple as Customer Name #JobID Customer Phone
    * NOTE: We could give an easy way to show the materials on the job. It would be a comma-delimited list with the primary Qty+UOM and description, i.e. "32 tons of 19mm").
    * If the job is missing a deposit, show a "DEPOSIT REQUIRED" in the title.
  * Clicking into the Event would show:
    * Title
    * Dates
    * Location (Job Address)
    * Link to Google Maps
    * Attachments
    * View/Edit Job in ProEstimator



  


  


1 Call Report

  * Provide a report of open jobs needing 1 Call. This qualifies as any scheduled work days (any day from start to end of job) in the next 10 days where there's no certificate requested OR the certificate will have expired.



  


  


Time Cards (Silverloom - Customized)

  * Entries
    * NOTE: Shop Time and Job ID are mutually exclusive.
    * Shop Time Category (list of Shop Time Categories)
    * Job ID
    * Crew (editable if Job ID is set)
    * Prevailing Wage List (editable of Job ID is prevailing wage)
    * Approved by Foreman (checkbox)
    * Latitude (number; 6 decimals)
    * Longitude (number; 6 decimals)



  


Time Card Tablet/Mobile

  * Clock In/Out
    * On a shared device, have then log into Silverloom and give them a link for "Multi-User Time Clock". On a dedicated device require them to enter their email, get a 6-digit OTP with an option to remember their device.
    * Home Screen:
      * If not clocked in, show "Clock In". If clocked in, show "Clock Out" or "Switch Time"
      * On the bottom of the screen, show a list of timeslots with:
        * Start Time
        * End Time
        * Duration
        * Job or Shop Time Category
        * Prevailing Wage Type
        * Edit button with options to split time slots, adjust times, or edit details. Employees can't edit it after it's been approved.
        *     * When Cocking In or Switching Time:
      * Select Job (Customer Name / Job Name / Job Number; default to prior job when switching; include options for Shop Time)
        * NOTE: If someone gets moved in the middle of the day, you need to either have someone in the office add them to the schedule, have the foreman log into the scheduler, or you need to fix it up at the end of the day.
      * Select Prevailing Wage Type (if required; allow adding to the list)
    * NOTE: If it's not too much complexity, let's track latitude & longitude of the device when making entries.



  


  * Approvals:
    * Similar to the above. Show the foreman all the time cards for all their crews with an option to approve when they're happy with it.
    * NOTE: Foremen will have access to tablets, but likely not laptops.
    * NOTE: If the entire crew is wrong, the foremen will need to individually correct specific items.



  


  * Downtime
    * Provide a way for foremen to record specific downtime



  


  


QuickBooks to Silverloom

  * Most likely, we'll want to import Quickbooks Jobs into Silverloom.



  


Time Cards to QuickBooks

  


DONE_ HLD - What service item does office staff use?

DONE_ HLD - how do we push rate into QB?

  


  


Time cards will need to map to QuickBooks:

  * Customer/Job
  * Service Item
  * Payroll Item



  


  * Pushing time to QuickBooks
    * Through QB - so everything will stay there, so QB will be the tracking device
    * Report with a breakdown by Rate + Hours
      * Payroll by the day + week
        * Regular Rate + ____ + Hours
        * Category + Rate + Regular Hours + Overtime Hours
    * Overtime Calculations by Time of Week
      * i.e. prevailing wage by Friday Afternoon
    * Every 2 weeks (full calendar weeks)
    * NOTE: Presumably we will want to sync hours daily  so that hours can be tied out to a Job in QuickBooks.



  


DONE_ HLD/DONE_ IDD: FIgure out exactly how mapping translates to Service Item / Payroll Item

Recommending TransactionPro

Time Tracking| Name *| Time/Enter Single Activity - Name|   
| X| Char 209  
---|---|---|---|---|---  
Time Tracking| Transaction Date| Time/Enter Single Activity - Date|   
|   
| Date  
Time Tracking| Customer *| Time/Enter Single Activity - Customer: Job| '(16)| X| Char 41  
Time Tracking| Service Item *| Time/Enter Single Activity - Service Item|   
| X| Char 31  
Time Tracking| Payroll Item| Time/Enter Single Activity - Payroll Item|   
|   
| Char 31  
Time Tracking| Duration| Time/Enter Single Activity - Duration|   
|   
| Char 10  
Time Tracking| Class|   
| (4)|   
|   
  
Time Tracking| Billable|   
| (2),(6)|   
| Char 1  
Time Tracking| Notes| Time/Enter Single Activity - Notes|   
|   
| Char 4095  
  
  


  * Every Hour would go towards that Job in QuickBooks



  


  


  * Service Item = Job Labor



_TR: Tim Reitz 12/03/2025: Is this a new "Service Item" list?Matthias Miller 12/03/2025: addressed

  


_TR: Tim Reitz 12/03/2025: Is this a new "Payroll Item" list? Matthias Miller 12/03/2025: Addressed

  * Payroll Item
    *     * Office Staff is Indirect Labor
    * Anything outside the office is Direct Labor



DONE_HLD - support office guys tracking time

Tim Reitz 12/04/2025: I doubt there's anything special needed here (would just set the "Is Time Card User" checkbox on the contact record) -- does that sound right?

Matthias Miller 12/08/2025: EVen less w/o QB integration

  


  * NOTE: Overtime rate calculates based on actual entries passing 40hr



  


  


TODO - Probably need some kind of time report by job...

DONE_TR: Tim Reitz 12/03/2025: Is this part of the QB sync? Or a separate report in Silverloom? Matthias Miller 12/03/2025: report in silverloom

  


[ ] • Follow up system to remind customers

  * For residential customers, remind them every 3 weeks with an update on their schedule (?). They are mostly 1-time customers
  * For commercials customers do a dozen jobs a year, they are constantly talking to them anyway
    * Want to reach out to them about 10 days before the start date



  


  


TOD O_DEFER

  * Proposal
    * Have a way to lock in a specific price with a specific vendor...


