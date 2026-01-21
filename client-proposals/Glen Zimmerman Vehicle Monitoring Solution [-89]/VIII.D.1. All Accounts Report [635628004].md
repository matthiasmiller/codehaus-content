8.4.1. All Accounts Report

  


Requirements

Overview: This is a custom report of all Account records, with various filters. Pre-filtered versions of this report can be opened from different locations (see corresponding specs).

  


Accessed from: 

  * Providers | Accounts | All Accounts (opens the report directly, bypassing the filter screen)
  * Providers | Accounts | Account Search (opens the filter screen) 
  * Filtered versions of the report open from various menu options & links (see corresponding specs) 



  


Title: "Accounts", with the following prefixes and/or suffixes: 

  * if "Account Group" is not blank: includes "for <Group Name> Group" suffix
  * if "Account Reseller" is not blank: includes "(Reseller: <Reseller Name>)" suffix



  


Examples: 

  * All Accounts 
  * Accounts for Weaverland Conference Group 
  * Accounts (Reseller: <John Doe>)"



  


Preface: N/A

  


Columns: 

  * Account Status
  * Account # (link to open the record)
  * Account Name
  * Account Type
  * Business
  * Account Reseller
  * Account Group
  * Primary Account Manager
  * Additional Account Managers (comma-separated list of non-Primary "Account Managers" for the Account)
  * # Devices (displays the number of linked Devices)



  


Row-Specific Buttons:

  * N/A



  


Grouped by: The selection in the "Group By" filter:

  * if "Account Status": in the standard list sequence;
  * if "Account Type": in the standard list sequence;
  * if "Account Reseller": alphabetically;
  * if "Account Group": "Group Name" (alphabetically);
  * if blank: no grouping



  


Sorted by: Account # (lowest number at the top)

  


Filters: 

  * Add Recipients to Announcement (hidden; checkbox; defaults to checked when the report is opened from the "Select Recipients" link on the Announcement record) 
  * Account # (



TODO_VA: plain text or drop list?

  * Account Group (optional; drop list of all Account Group "Names"; defaults to blank = all; when one is selected, the report displays all Accounts with "Account Group" set to that Group; note that this does not look at Upline Groups)
  * Account Reseller (optional; drop list of all Account Resellers; defaults to blank = all; when one is selected, the report displays all Accounts with "Account Reseller" set to that Contact) 
  * Account Manager (optional; drop list of all Account Managers; defaults to blank = all; when one is selected, the report displays all Accounts for which that Contact is included on the "Account Managers" embedded spreadsheet)
  * Account Status (multi-select drop list of "Account Statuses" list items; defaults to all except "Closed" selected)
  * Group By (optional; drop list of "Account Status" / "Account Type" / Account Reseller" / "Account Group" / blank; defaults to "Account Status")



  


TODO_VA: Tim Reitz 10/23/2025: Per client today, there could be use cases for having these be multi-select: 

[ ] Account Group 

[ ] Account Reseller 

[ ] Account Manager

  


Buttons: 

  * New Account (opens a new Account record with the following fields defaulted:
    * "Account Group": defaulted if the "Account Group" filter is set on the report;
    * __;
    * other fields defaulted as noted in the Account record design)



TODO_VA: any other defaults?

  * Add Recipients (visible if the "Add Recipients to Announcement" filter checkbox is checked; runs the "Add Announcement Recipients from Accounts Report" automatic process to add all Account Managers on the report to the Announcement - see corresponding specs) 



  


Menu Visibility: 

  * 


  


  


Other Notes:

  * This is an "auto-push" report, meaning that if there is only 1 row, it opens that record directly.



  


_GZ (mockup): Tim Reitz 10/06/2025: Would you like a second pane to show the Devices for the Account selected in the left pane? Or just open the Account from this report, then view/open its Devices from there?

TODO_VA: Tim Reitz 10/23/2025: Per Glen today, this second pane would be really nice.

  


Development Specification

Mockups: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=2061457481#gid=2061457481](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=2061457481#gid=2061457481)

  


  


Tim Reitz 08/26/2025: Let's make sure that numbers sort correctly (i.e. that "100" comes after 99, not after 10).
