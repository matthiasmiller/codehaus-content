7\. Reports

  


Requirements

On all reports, filtering by name should match on beginning of name.

  


Any reports that prompt for screening type should include a “Vision” option that includes either ECHO or LIONS Vision.

  


We do NOT need that option for hearing since Pure Tone is not a type that's used anymore. (We are keeing Pure Tone Hearing for migration.)

  


Child Intake

  * Prompts:
    * Last name
    * First name
    * Middle name
    * Birth date
    * Status (Active / Inactive)
    * Hispanic or Latino checkbox
    * Race (drop down allowing for multiple selections)
  * Columns:
    * Last name
    * First name
    * Middle name
    * Birth date
    * Status
    * Hispanic/Latino
    * Race
  * Include a “New Child” button



  


Screening Count by Child

  * Prompts
    * Start Date
    * End Date



  


  * Grouped by child



  


  * Columns
    * Child Name
    * Date of Birth
      * Total row shows date of birth
    * Number of Screening Types
      * Total row shows the sum of the different types of screenings with any result excluding blank
    * # of Development Screenings
      * Total row
    * # of ECHO Vision Screenings
      * Total row
    * # of LIONS Vision Screenings
      * Total row
    * # of OAE Hearing Screenings
      * Total row
    * # of Tympanometry Screenings
      * Total row
    * # of Pure Tone Hearing Screenings
      * Total row
    * # of Social Emotional Screenings
      * Total row
    * # of Articulation Screenings
      * Total row
    * Number of Screenings
      * Total row



  


  * Rows
    * After the grouping for each child there will be a row for each screening result present



  


At the bottom of the report show

  * Number of Children : <number of children in the report>
  * ** Number of Screening Types : <number of screening types in the report>



  


Referrals

  * For each of the list options, match on ANY matches. 
  * The resulting rows must match ALL the criteria specified in the prompts.
  * Show referrals and outcomes in the report as mutli-line rows.



  


See [https://docs.google.com/spreadsheets/d/18L73Zq9LGsLgZK16d0GYhuKTx8ZMKSxqG4ooGiVYUxg/edit#gid=1320085304](https://docs.google.com/spreadsheets/d/18L73Zq9LGsLgZK16d0GYhuKTx8ZMKSxqG4ooGiVYUxg/edit#gid=1320085304)

  


Advanced Child Search

NOTE: The Screening types filter should look at all types of screenings during that time frame, not requiring all types on a single screening record. (For example, it should match even if the screening types were on different records.)

  


  * Prompts:
    * School district (matching any of multiple)
    * Screening (optional)
      * Start Date (optional)
      * End Date (optional)
      * Any of these types
      * All of these types
      * None of these types
    * State Risk Factors (multiple selection)
      * Any of these
      * All of these
      * None of these
    * Local Risk Factors (multiple selection)
      * Any of these
      * All of these
      * None of these
    * Age range (optional)
      * Minimum Age
      * Maximum Age
    * Income levels (matching any of multiple)
    * Program Filter:
      * Start of date range
      * End of date range
      * Criteria

  
| Criteria 1| Criteria 2| Criteria 3  
---|---|---|---  
Event| [Enrolled / Terminated / Active]| [Enrolled / Terminated / Active]| [Enrolled / Terminated / Active]  
Filter| [Any / All / None]| [Any / All / None]| [Any / All / None]  
Programs| [Multiple Choice of Programs]| [Multiple Choice of Programs]| [Multiple Choice of Programs]  
  
  


The Filter and Programs should only be visible when you have selected an Event for that criteria. They should both be required anytime they're visible.

  


  * Output:
    * Last Name
    * First Name
    * Middle Name
    * Primary Caregiver Name
    * Primary Caregiver Phone (Mother if both parents)
    * Birth Date
    * Age (if filtering by age)
    * Income Level
    * Screenings (only show screening types based on filter)
    * Criteria 1-3 Detail (three separate columns)
      * Column heading reflects the criteria event (Enrolled / Terminated / Active)
      * Column is hidden when selecting None
      * Column shows applicable programs (limited to the programs selected in the criteria)



  


Buttons:

  * We’d like to have a “Terminate Program” button that terminates a program for the selected children. These buttons will prompt for a program type and a termination date. For any children who were enrolled before the termination date and do not have a termination date, it will set the termination date to the specified date and update the Status to Terminated. We will not need to terminate multiple programs, since that will be handled by the Inactive Children tool.



  


Client Notes:

  * This report can be used to retrieve an Unduplicated Child Count by entering a date range for the screenings and selecting ANY of these types:
    * Development
    * ECHO Vision
    * LIONS Vision
    * Social Emotional
    * Hearing
  * This report can be used to retrieve an Unduplicated Child Count (Full Screening) by entering a date range for the screenings and selecting ALL of these types:
    * Development
    * Vision (either ECHO Vision or LIONS Vision)
    * Social Emotional
    * Hearing 



  


Inactivate Children

  * Prompts:
    * Birthdate (start and end date range)
  * Columns
    * Last name
    * First name
    * Middle name
    * Birthdate



This should only include active children. Add a button called “Inactivate Children” that inactivates the selected children. It prompts for an effective date, then updates the Terminate Date for all of them. This should also terminate all active programs as of the Terminate Date.

  


Risk Factors Summary

This report would filter by all active children who are actively enrolled in CPP as of a specific date

  


  * Prompts
    * Program (defaults to CPP)
    * Effective date (default to October 1 of current year)
  * Columns
    * Last name
    * First name
    * Middle name
    * Birthdate
    * State Risk Factors
    * Local Risk Factors



  


Pieces Referrals

This should include all children with Pieces referral dates within the specified date range and matching the selected Pieces categories. Optionally include completed and no contact referrals.

  


  * Prompts:
    * Start date (blank = all)
    * End date (blank = all)
    * Pieces category (multi-select choice)
    * Include completed and no contact (checkbox; default to unchecked)
  * Columns
    * Last name
    * First name
    * Middle name
    * Pieces category
    * Referral date
    * Status
    * Enrolled Programs (all programs enrolled in during the prompted date range)
    * Screening Referrals*
    * Program Referrals*



  


It's possible for the report to have multiple rows per child, if they had multiple Pieces referrals during the time period. In this case, the Enrolled Programs, Screening Referrals, and Program Referrals would be identical for each of the child's rows.

  


* These would be multi-line columns for all of the referrals/outcomes that were made during that time period. They should show "Referral: Outcome".

  


Development Specification

Matthias Miller 07/16/2020: 

  


  * To deactivate the program, I think we'll want detail variables and a button on the detail screen, so the logic is shared? We need to make sure this stays in sync...



  


Change Requests:

  * Ben Reitz 07/09/2025: [[[IN10900](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10902&)]] - ZEC - Advanced Child Search report - Add Insurance drop list filter


