7.8. System Switches

  


Requirements

The Solution would include the following settings on the System Switches page: 

  * Allow manual editing of Contact records by Administrator users (less common, only available for Admin users; if this switch is set, all fields on the Contact records are editable by Admins with a warning banner and a warning on save - see details in the contact record, but nothing changes for non-Admin users; note that this would probably become irrelevant after the Accounting module is added to replace CA)



  


Data Access for System Switches:

  * All users can view, but only admins can edit (this is the standard setting)



  


Other Notes for System Switches:

  * N/A



  


Development Specification

Mockup: N/A

  


  


For more context on the "Allow manual editing..." switch, see [[[IN7565](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-7567&)]] - ZTK - Add System Switch to Allow Admins to Edit Contact Records:

[ ] Add switch Con fig_ContactsAllowAdminManualEditing

[ ] Add a macro ContactAllFieldsEditableByUser defined as:

Config_ContactsAllowAdminManualEditing AND UserIsAdmin

[ ] Change all of the CustomContact_CanEdit macros for standard fields that currently return vInImport to use:

vInImport OR ContactAllFieldsEditableByUser

[ ] Change all custom fields on detail screen that currently Editable: vInImport to also use OR ContactAllFieldsEditableByUser

[ ] The banner and warning on save can reference ContactAllFieldsEditableByUser AND NOT InImport

  


Priced with Contacts changes.
