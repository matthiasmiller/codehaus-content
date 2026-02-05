9.2.2. Standard All Contacts Report

  


Requirements

*Done.

  


Overview: This is the standard Silverloom Contacts report, which may include customizations. Note that any customizations are noted as such in the spec.

  


Note that this report is only accessible to users with the "Full Access" Permission (to help protect the integrity of client data usage). 

  


Accessed from: 

  * Administrators | Contact Management | All Contacts (opens the report directly, bypassing the filter screen)



  


Title: Contacts

  


Columns: 

  * Name (displays the "Display Name"; link to Contact record)
  * Type
  * Phone
  * Phone Type
  * Email (link to directly email the Contact)
  * City (displays the City and State)
  * Organization
  * Contact Role(s) (custom; displays all Contact Roles that apply to the Contact, in a comma-separated list; text wraps if needed)
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
  * Contact Role (custom; multi-select drop list of "Contact Roles" list items; defaults to none selected = all)
  * Account Group (custom; drop list of "Group Name" values for active Account Groups; defaults to blank = all; if a selection is made here, the report shows Contacts that are included as "Account Members" on Accounts under that Group) 
  * Account Reseller (custom; drop list of "Display Name" values for active Contacts with the "Is Account Reseller" checkbox checked; defaults to blank = all; if a selection is made here, the report shows Contacts that are included as "Account Members" of Accounts under that Reseller) 
  * Account (custom; drop list of "Account #" values for active Accounts; defaults to blank = all; if a selection is made here, the report shows Contacts that are included as "Account Members" on that Account)
  * Match All of These Conditions (checkbox; defaults to checked)



  


Buttons: 

  * New Contact (opens blank new Contact record)



  


Menu Visibility: Visible to all users who can view the "Administrators" menu 

  


Other Notes:

  * N/A



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=1825291167#gid=1825291167](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=1825291167#gid=1825291167)
