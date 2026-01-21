25.1.3.2. Schools

  


Requirements

Schools are a Contact Type. They can be deactivated by deactivating the contact. They will show two custom sections.

  


Imported School section:

This section will be visible if the school is imported from a scholarship organization. It will show the following read-only fields:

  * Imported Scholarship Organization
  * Imported School Name
  * Imported County
  * Imported Contact First Name
  * Imported Contact Last Name
  * Imported Contact Address
  * Imported Contact City
  * Imported Contact State (unlabeled, to the right of city)
  * Imported Contact Zip (unlabeled, to the right of state)
  * Imported Contact Phone
  * Imported Contact Email



  


It will also include a "Keep Contact Up-to-Date With Scholarship Organization" checkbox.

  


If the checkbox is checked, a warning will be displayed at the top of the screen indicating that any changes to the contact information will be overridden on save. Whenever the contact record is saved, it will be updated to the latest imported information.

  


If the checkbox is unchecked, any of the fields can be changed (including the school name) without being overridden by the imported information.

  


The "Imported School ID" is an identifier that comes from the FBSS database. It is used to ensure that we continue updating the same school in SPE when we rerun the import. When importing schools from FBSS, the import will update the imported fields (see the Imported School section on the Contact) and update the other contact fields if the checkbox is checked to keep it up-to-date. If no matching school is found in the SPE database, it will create a new contact and set the Imported School ID to match.

  


School Details section:

These fields should include:

  * Default Scholarship Organization (list of scholarship organizations; read-only if Keep Contact Up-to-Date is checked; links back to scholarship organization)
  * Contact First Name (read-only if Keep Contact Up-to-Date is checked)
  * Contact Last Name (read-only if Keep Contact Up-to-Date is checked)
  * Financial Need (Warn but allow you to save if they're unset; list; choice of:
    * High
    * Medium
    * Low  list; choice of:
  * Targeting Level (Warns but permits saving if it is not set; list; choice of:
    * High
    * Medium
    * Low
  * [ ] Interested in Membership Communications
  * Hold Contribution Notification Until Date (editable date field)



  


The Hold Contribution setting is used in situations where Vivian is communicating with the school about prior contributions. This helps to eliminate confusion by waiting to communicate about new contributions until they've processed their prior contributions. This is detailed in the email communications section.

  


The school's county is in the normal contact Address section. It is still editable if Keep Contact Up-to-Date is checked, but it will be changed back to the original value on save.

  


Development Specification

Ellis Miller 02/08/2021: 

  


[ ] Imported School Section

[ ] 12 fields, all text or numeric

[ ] Editable on import

[ ] Add 12 Contact OnModify, Condition: ContactRespectSchoolImportFields (or something) statements

Target: 8 hours

  


[ ] School Detail Section: 

Target: 6 hours
