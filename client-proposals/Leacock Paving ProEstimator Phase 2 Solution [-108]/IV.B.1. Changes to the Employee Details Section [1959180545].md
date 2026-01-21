4.2.1. Changes to the Employee Details Section

  


Requirements

The following new items are being added to the Employee Details Section: 

  


  * Regular Rate (number; 2 decimals; visible to and editable for users with the "View and Edit Hourly Rates" Permission)
    * This captures the employee's standard hourly rate, which feeds into job costing calculations.
  * Primary Crew (drop list of active Crews; editable for users with the "Edit User Groups and Profiles" Permission)
    * This sets the crew an employee normally works with, so they default onto that crew's schedule without needing to be manually added each time.
  * Crew Foreman (checkbox; editable for users with the "Edit User Groups and Profiles" Permission; this designates this employee as the "Crew Foreman" for the selected "Crew"; warn if there are multiple foreman for the Crew)
    * This designates who has authority to approve time cards for each crew, so there's a clear chain of accountability before entries go to payroll and invoicing.
  * Enable Time Card PIN (checkbox; editable for users with the "Edit User Groups and Profiles" Permission; this make the fields related to the Time Card PIN visible) 
  * Enter Time Card PIN (4-digit numeric PIN; editable for users with the "Edit User Groups and Profiles" Permission; this sets the Time Card PIN for the employee, for logging into the Time Clock app)
  * Confirm Time Card PIN (4-digit numeric PIN; editable for users with the "Edit User Groups and Profiles" Permission)
    * This gives each employee a simple 4-digit code to clock in on shared tablets--especially useful for team members who don't have smartphones.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1529895558#gid=1529895558](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1529895558#gid=1529895558)

  


  


TODO_IDD: Matthias: Do we need to track equipment more specifically?

TODO_IDD: Matthias: I would use a Salt + Hash for the PIN. The editable expression should be "****" to show the password dots when it's set. We should validate that the PIN is either that, blank, or all-numeric. If it's blank, we should clear out the Salt + Hash and disallow login.

  


TODO_IDD: Tim Reitz 12/05/2025: For fields that are hidden from certain users, will those details also be hidden for the same users in Modification History?
