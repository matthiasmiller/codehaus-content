6.3. Organizations (Legacy)

Sagar Sagar 11/10/2022: We added Organization in [[PC0065327]] - E00 - Add standard "Organization" and then improved it. Now we call it legacy organization as we merged the concept of organization configuring contact type.

  


So the legacy organization has below fields

[ ] Fields

[ ] Organization - section

[ ] Name

[ ] Summary

Sagar Sagar 11/16/2022: The field was added in [[PC0086059]] - Contacts: Make contact report more useful

[ ] Type - list field

  


[ ] Address - section

[ ] Type - list of address types, visible if there are multiple addresses

Sagar Sagar 11/13/2022: The list was added in [[PC0076374]] - E00 - AppHosting Contacts: Support multiple addresses

[ ] Address - line 1

[ ] Address - line 2

[ ] City - shows a warning if City is blank and ConfigContacts_CityRequired is True

[ ] Sate - list of states in short form, visible if selected county is a country with states, shows a warning if States is blank and ConfigContacts_StateRequired is True

Sagar Sagar 11/17/2022: For country USA we show USA's states. For Canada we treat provinces as states and show a list of short form of provinces. This has been done in [[PC0077498]] - Addresses: Better support Canadian provinces.

[ ] Zip - shows a warning if Zip is blank and ConfigContacts_ZipRequired is True, if selected country is not a country with states, then Postcode label will be visible

[ ] Country - list of all countries, visible if ConfigContacts_ShowCountry is True

Sagar Sagar 11/13/2022: Country was added in [[PC0066449]] - E00 - AppHosting Contacts: Add Country to contact and organizations

[ ] Export Address - link to export the address in Commercial 10 envelop

Sagar Sagar 11/13/2022: The link and exporting address was added in [[PC0076678]] - E00 - Module for Printing Addresses. The template for commercial 10 was added in [[PC0077465]] - E00 - Add Default Template for Exporting Address

  


Sagar Sagar 11/13/2022: Address fields were transformed as repeating fields in [[PC0076374]] - E00 - AppHosting Contacts: Support multiple addresses. Previously an organization would have only one address.

  


[ ] Phone & Website - section

[ ] Phone table (RG)

[ ] Phone - phone number

[ ] Type - list of phone types, Fax, Home, Mobile, Work

[ ] Notes

[ ] Website - in edit mode you can enter website, in non-edit mode the website will be a link

[ ] View / Create Contacts - link to the contact report that are linked with the organization

[ ] O linked Contacts - label to indicate how many contacts are linked with the organization, the number changes when there are linked contacts

  


[ ] Executive Notes - section, visible if user has Custom_Executive permission

[ ] Executive Notes - memo

Sagar Sagar 11/13/2022: Executive notes was added in [[PC0069845]] - E00 - Add Executive Notes fields to Contact and Organization detail screens

  


[ ] Notes - section, visible if ConfigContacts_CanViewNotes is true

[ ] Notes - memo

  


[ ] Incidents - section, visible when the system includes incidents module

[ ] Incidents table (RG) - non-editable, visible if the organization has incidents

[ ] Origination Date

[ ] Type

[ ] Title

[ ] Status

[ ] View Incidents - link to the report of incidents of the organization, visible if the organization has incidents

[ ] Create Incident - link to create a new incident for the organization

Sagar Sagar 11/13/2022: The section was added in [[PC0073821]] - E00 - Show table of incidents on contacts and organizations

  


[ ] Invoices - section, visible when the system includes sales forms module

[ ] Invoices table (RG) - non-editable, visible if the organization has invoices

[ ] Invoice #

[ ] Date

[ ] Contact

[ ] Status

[ ] Amount

[ ] View - link to the invoice

[ ] View Invoices - link to the report of invoices of the organization, visible if the organization has invoices

Sagar Sagar 11/17/2022: The link has been added in [[PC0085796]] - E00 - Contacts Should Link to Invoice Detail Screen

[ ] Create Invoice - link to create a blank invoice for the organization

Sagar Sagar 11/13/2022: The section was added in [[PC0076187]] - E00 - Add Invoice tables to Contacts and Organization

[ ] Modification History - link to the activity report, not visible for new record

  


Sagar Sagar 11/28/2022: The organization detail has many validations.

[ ] Validations

[ ] Errors

[ ] Organization records are not supported in this system.

[ ] You cannot save a blank address.

[ ] An organization cannot have duplicate addresses.

[ ] Country cannot be empty.
