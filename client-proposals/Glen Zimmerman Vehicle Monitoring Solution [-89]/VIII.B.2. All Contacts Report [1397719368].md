8.2.2. All Contacts Report

  


Requirements

Overview: This is the standard Silverloom Contacts report, which may include customizations. Note that any customizations are noted as such in the spec.

  


Note that this report is only accessible to users with the "Full Access" Permission (to help protect the integrity of client data usage). 

TODO_NM: Tim Reitz 01/17/2026: How do we restrict this? Just based on the "Administrators" menu being hidden for others? Or something stronger? 

  


Accessed from: 

  * Administrators | Manage Contacts | All Contacts (



  


Title: Contacts

  


Columns: 

  * Name (displays the "Display Name"; link to Contact record)
  * Type
  * Phone
  * Phone Type
  * Email (link to directly email the Contact)
  * City (displays the City and State)
  * Organization
  * Summary



  


Grouped by: Active / Inactive

  


Sorted by: Name (alphabetically)

  


Filters: 

  * Contact Type (multi-select drop list of all Contact Types; defaults to blank = all)
  * Name (plain text field; searches the "Display Name")
  * City (plain text field)
  * State (drop list of State abbreviations; defaults to blank = all)
  * Zip (plain text field)
  * Email (plain text field)
  * Phone # (plain text field) 
  * Active Contacts Only (checkbox; defaults to checked) 
  * Account Reseller (custom; drop list of "Display Names" for Account Resellers; defaults to blank = all) 
  * Account (custom; drop list of __



TODO_VA:

  * Match All of These Conditions (checkbox; defaults to checked)



  


Buttons: 

  * New Contact (opens blank new Contact record)



  


Menu Visibility: Visible to all users who can view the "Providers" menu 

  


Other Notes:

  * N/A



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=1825291167#gid=1825291167](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=1825291167#gid=1825291167)
