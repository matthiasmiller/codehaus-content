6.1. Contacts

Tim Reitz 10/04/2025: Note that I am currently building out / maintaining the living spec for the standard Contact record spec in the following Snippet, since that is most useful for designs: [https://zch.apphosting.zone/Detail/Edit/2?RecordType=Snippets&NumberID=-53&State=ctLVLwm53iQ&](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Snippets&NumberID=-53&State=ctLVLwm53iQ&). 

  


  


Sagar Sagar 11/22/2022: After implementing the columns in detail screen, we adopted the setting to some of our detail screens. Among them, contacts screen is one of the earliest that we changed. This was done in [[PC0126257]] - ZWA - 2-Column Contact Layout

  


Sagar Sagar 11/17/2022: The contact detail screen has below fields

[ ] Fields

[ ] Contact - section including Contact ID

[ ] Active Contact - checkbox for active/inactive status

Sagar Sagar 11/13/2022: The checkbox was added in [[PC0068877]] - E00 - AppHosting: Add Active checkbox and show Override checkbox in EditMode in contact module. It was placed up of section header in [[PC0077284]] - E00 - Tweaks to Active Contacts.

[ ] This contact is inactive as of <Date> \- date field, visible if Active Contact checkbox is unchecked

Sagar Sagar 11/21/2022: The inactive date was added in [[PC0123161]] - ZWA - Contact Inactive Date

[ ] Contact ID - hidden field, shows only in the section header, increments automatically as we add new contacts

Sagar Sagar 11/21/2022: This field was coded in [[PC0123301]] - ZWA - Contacts: Numeric ID. Later it was added to the contacts in [[PC0129539]] - Contacts: Make ContactID a standard feature

[ ] Contact Type - list of contact types

[ ] Tags - button to open tag RG

[ ] Tags - multi-selection list so that multiple tags can be selected

Sagar Sagar 11/24/2022: Tag feature was added in [[PC0144063]] - Make Contact Tag Generic Feature 

[ ] Organization - checkbox, visible if Config_UseLegacyOrganizations is false

Sagar Sagar 11/20/2022: This field was coded in [[PC0127723]] - Contacts: Organizations are contacts

[ ] First Name

[ ] Middle Name

Sagar Sagar 11/21/2022: Middle Name field was added in [[PC0124831]] - Contacts: Make Middle Name Generic

[ ] Last Name

[ ] Display Name - read-only field consists of names

[ ] Override Name - checkbox to override name

[ ] Summary

Sagar Sagar 11/16/2022: The field was added in [[PC0086059]] - Contacts: Make contact report more useful

[ ] Organization - list of organizations

[ ] Organization - RG of organization, visible if Config_AllowMultipleOrganizations is True

Sagar Sagar 11/19/2022: This was added in [[PC0087514]] - Allow Multiple Organizations per Contact

[ ] Date of Birth, visible if ConfigContacts_ContactShowBirthDate is True and a contact is not organization

[ ] Gender - list of genders, Female and Male, visible if ConfigContacts_ShowGender is True and a contact is not organization

  


[ ] Address - section

[ ] Type - list of address types, visible if there are multiple addresses

Sagar Sagar 11/13/2022: The list was added in [[PC0076374]] - E00 - AppHosting Contacts: Support multiple addresses

[ ] Primary Address - checkbox to determine if the address is primary, visible if ConfigContacts_EnablePrimaryAddress macro is overridden as True in outer catalog

Sagar Sagar 12/06/2022: The checkbox was added in [[PC0127492]] - XFB - Records: Contacts (Members/Businesses/Schools/Other)

[ ] Address - line 1

[ ] Address - line 2

[ ] City - shows a warning if City is blank and ConfigContacts_CityRequired is True

[ ] Sate - list of states in short form, visible if selected county is a country with states, shows a warning if States is blank and ConfigContacts_StateRequired is True

Sagar Sagar 11/17/2022: For country USA we show USA's states. For Canada we treat provinces as states and show a list of short form of provinces. This has been done in [[PC0077498]] - Addresses: Better support Canadian provinces.

[ ] Zip - shows a warning if Zip is blank and ConfigContacts_ZipRequired is True, if selected country is not a country with states, then Postcode label will be visible

[ ] Country - list of all countries, visible if ConfigContacts_ShowCountry is True

Sagar Sagar 11/13/2022: Country was added in [[PC0066449]] - E00 - AppHosting Contacts: Add Country to contact and organizations.

[ ] County - list of all counties when a state will be mentioned in Config_LimitCountiesToState system swtich, visible when ConfigContacts_ShowCounty is True

Sagar Sagar 11/22/2022: The field was added in [[PC0127429]] - XFB - Records: Contacts - add general information fields

[ ] Google Maps - link to the google maps to search the address

Sagar Sagar 11/24/2022: This link was added in [[PC0143967]] - Geocoding Config

[ ] Apple Maps - link to the apple maps to search the address, visible if Config_ContactShowAppleMapUrl is True

Sagar Sagar 11/24/2022: This link was added in [[PC0143967]] - Geocoding Config

[ ] Export Address - link to export the address in Commercial 10 envelop

Sagar Sagar 11/13/2022: The link and exporting address was added in [[PC0076678]] - E00 - Module for Printing Addresses. The template for commercial 10 was added in [[PC0077465]] - E00 - Add Default Template for Exporting Address

[ ] GPS Coords - GPS coordinates of the address, comma separated latitude and longitude

Sagar Sagar 11/24/2022: This was added in [[PC0143968]] - Contacts: Support specifying GPS coordinates

[ ] View All - button to show all of the addresses in RG in the child detail

[ ] Address RG

[ ] Move Up - RG button to move an address one row up of its original position

[ ] Move Down - RG button to move an address one row down of its original position

Sagar Sagar 11/23/2022: The buttons have been added in [[PC0129793]] - Contacts Address RG: Add view all button

[ ] New - button to add a new address

[ ] Delete - button to delete an address

  


Sagar Sagar 11/13/2022: Address fields were transformed as repeating fields in [[PC0076374]] - E00 - AppHosting Contacts: Support multiple addresses. Previously a contact would have only one address.

  


[ ] Phone - section

[ ] Phone table (RG)

[ ] Phone - phone number

[ ] Type - list of phone types, Fax, Home, Mobile, Work

[ ] Notes

  


[ ] Email - section

[ ] Login Email - default login email address, visible if system user, filled with log in email that has been specified in user profile.

Sagar Sagar 11/19/2022: This has been coded in [[PC0086288]] - E00 - Duplicate Email Addresses are Confusing

[ ] Email table (RG)

[ ] Email

[ ] Primary - checkbox

[ ] Notes

[ ] Send Email - link to send email specified in the selected row

Sagar Sagar 11/24/2022: The RG has been coded in [[PC0142478]] - Consider changing contact email to an RG

[ ] Override Email - checkbox, shows Email table if checked, visible if contact is a system user

Sagar Sagar 11/19/2022: This has been coded in [[PC0086288]] - E00 - Duplicate Email Addresses are Confusing

[ ] Send Email - link to send email address specified on the first row of Email table

[ ] Send Email to Primary Addresses - link to email to the contact's primary email address. If a contact has multiple primary addresses, this link will send email to all of them.

Sagar Sagar 11/23/2022: Both of the link have been added in [[PC0133276]] - Contacts: Add Email link in edit mode

  


[ ] Executive Notes - section, visible if user has Custom_Executive permission

[ ] Executive Notes - memo

Sagar Sagar 11/13/2022: Executive notes was added in [[PC0069845]] - E00 - Add Executive Notes fields to Contact and Organization detail screens

  


[ ] Notes - section, visible if ConfigContacts_CanViewNotes is True

[ ] Notes - memo

  


[ ] Incidents - section, visible when the system includes incidents module

[ ] Incidents table (RG) - non-editable, visible if the contact has incidents

[ ] Origination Date

[ ] Type

[ ] Title

[ ] Status

[ ] View Incidents - link to the report of incidents of the contact, visible if the contact has incidents

[ ] Create Incident - link to create a new incident for the contact

Sagar Sagar 11/13/2022: The section was added in [[PC0073821]] - E00 - Show table of incidents on contacts and organizations

  


[ ] Invoices - section, visible when the system includes sales forms module

[ ] Invoices table (RG) - non-editable, visible if the contact has invoices

[ ] Invoice #

[ ] Date

[ ] Status

[ ] Amount

[ ] View - link to the invoice

[ ] View All Invoices - link to the report of invoices of the contact, visible if the contact has invoices

Sagar Sagar 11/17/2022: The link has been added in [[PC0085796]] - E00 - Contacts Should Link to Invoice Detail Screen

[ ] Create Blank Invoice - link to create a blank invoice for the contact

[ ] Statement - link to the statement of the contact, visible if the contact has invoice of status "Invoiced"

Sagar Sagar 11/20/2022: The link has been added in [[PC0113277]] - Invoicing: Create generic statements export

  


Sagar Sagar 11/13/2022: The section was added in [[PC0076187]] - E00 - Add Invoice tables to Contacts and Organization

  


[ ] AppHosting Settings - section, this section is not visible if the contact is organization

[ ] User ID - list of user profiles

Sagar Sagar 11/13/2022: The list was added in [[PC0072095]] - E00 - Tie the user profile to a specific contact

[ ] Is Incident Assignee - checkbox

Sagar Sagar 11/13/2022: The checkbox was added in [[PC0066454]] - E00 - AppHosting: Standard Incidents module

[ ] Is Time Card User - checkbox

Sagar Sagar 11/13/2022: The checkbox was added in [[PC0070570]] - AHZ - AppHosting: Add a checkbox for time card user in contact module

[ ] Billable Rate - numeric field to determine the rate of billable incident for the contact

[ ] Subscribe to All Sales Opportunity Updates - checkbox

  


[ ] Created label - label with "Created: <MM/DD/YYYY> <HH:MM:SS> <AM/PM> by <UserName>" format

[ ] Last Modified label - label with "Last Modified: <MM/DD/YYYY> <HH:MM:SS> <AM/PM> by <UserName>" format

Sagar Sagar 11/21/2022: Both of the labels were added in [[PC0123140]] - ZWA - Contact Record Behaviors

[ ] Modification History - link to the activity report, not visible for new record

  


Sagar Sagar 11/28/2022: The contact detail has many validations.

[ ] Validations

[ ] Errors

[ ] Contact types are not configured correctly in this system: contact type is required but not visible. -

[ ] Organization type contacts should not be linked to an AppHosting User.

[ ] Only one phone number can be marked as primary.

[ ] A primary phone number is required for this contact.

[ ] Only one address can be marked as primary.

[ ] A primary address is required for this contact.

[ ] This contact has duplicate tags.

[ ] Organization should not be checked if the contact type does not support organizations.

[ ] Organization must be checked if the contact type only supports organizations.

[ ] First Name cannot be empty.

[ ] Last Name cannot be empty.

[ ] A contact named <ContactName> already exists. If this is a different person, check “Override Name” and enter a unique name.

[ ] A contact named <ContactName> already exists. Please enter a unique name.

[ ] Name cannot be empty. (Organization)

[ ] <Organization> is included multiple times in the linked organizations.

[ ] You cannot save a blank address.

[ ] A contact cannot have duplicate addresses.

[ ] Country cannot be empty.

[ ] Please enter valid GPS coordinates.

[ ] Primary phone number is missing.

[ ] Please enter a valid email address.

[ ] This user ID is already used by another contact.

[ ] Warnings

[ ] The contact address type is marked as <ContactAddressType>. Consider using the 'Primary Address' checkbox instead.

[ ] GPS coordinates may need to be updated.

[ ] City is missing.

[ ] State is missing.

[ ] Zip code is missing.

[ ] This is not a valid county.

[ ] A 'Fax' type number may not be set as primary phone.

[ ] The contact email will be erased as it was linked with the user.
