8\. Reports

Sagar Sagar 11/16/2022: The contacts report was added by Josh in [[PC0046380]] - NWR: Side projects. Then we improved it in [[PC0065112]] - E00 - Improve standard contact detail screen.

  


Sagar Sagar 11/16/2022:

[ ] Contacts

[ ] Columns are

[ ] Name

[ ] Type - visible if ConfigContacts_ShowType is true

[ ] Phone - show the primary phone, link to call the contact

[ ] Phone Type

[ ] Email - link of sending email to the contact

[ ] City - city and state in <City, State> format

Sagar Sagar 11/16/2022: Added in [[PC0065112]] - E00 - Improve standard contact detail screen.

[ ] Organization - one organization, visible if the contact is a contact of legacy organization and Config_AllowMultipleOrganizations is not true

[ ] Organization - multiple organizations, visible if the contact is a contact of legacy organization and Config_AllowMultipleOrganizations is true

[ ] Summary

[ ] the report is grouped by active status

[ ] the report is sorted by Contact Name

  


[ ] the prompts are

[ ] Contact Type - multi-selection list

[ ] Name

[ ] City

[ ] State - list of states in short form

[ ] Zip

[ ] Phone #

[ ] Active Contacts Only - checkbox, checked by default, by un-checking you can see the all (both active and inactive) contacts

[ ] Match All of These Conditions - checkbox, checked by default

[ ] the report will show filtered results if you search by these prompts

Sagar Sagar 11/19/2022: The prompts were added in [[PC0098417]] - E00 - Contact report should have option to view inactive contacts. We had another report for searching contacts. On that job we eliminated the report and incorporated the searching in contacts report.

  


[ ] New Contact - report button to create a new contact

[ ] if you run the report from View Contacts menu and press New Contact, an empty contact detail screen will open

[ ] if you search by the ask prompts and then press New Contact, the search terms will be defaulted to the respected fields 

Sagar Sagar 11/20/2022: This was coded in [[PC0108111]] - Lost: auto-population of contact fields from "Find or Create Contacts"

  


  


Sagar Sagar 11/16/2022: The organizations report was added [[PC0065112]] - E00 - Improve standard contact detail screen. But then it was improved by [[PC0065327]] - E00 - Add standard "Organization".

  


Sagar Sagar 11/16/2022: 

[ ] Organizations

[ ] Columns in the left pane are

[ ] Name

[ ] Type - visible if organization type list is non-empty

[ ] Phone - shows primary phone, link to call the organization

[ ] Phone Type

[ ] Location - city and state in <City, State> format

[ ] Website

[ ] Summary

[ ] the left pane is sorted by Organization Name

  


[ ] Columns in the right pane are

[ ] Contact Name - link to the contact detail screen

[ ] Phone - link to call the contact

Sagar Sagar 11/16/2022: The link was added in [[PC0066295]] - E00 - Standard Contacts Enhancements (Round 2)

[ ] Email - link of sending email to the contact

Sagar Sagar 11/16/2022: The link was added in [[PC0066295]] - E00 - Standard Contacts Enhancements (Round 2)

[ ] the right pane is grouped by active status

Sagar Sagar 11/17/2022: The grouping was added in [[PC0086057]] - Contacts: Organization report subpane should group by active status

[ ] the right pane is sorted by Contact Name

  


Sagar Sagar 11/16/2022: The right pane was added in [[PC0066295]] - E00 - Standard Contacts Enhancements (Round 2)

  


Sagar Sagar 11/16/2022: The Find Or Create Organizations report was added in [[PC0065112]] - E00 - Improve standard contact detail screen. 

[ ] Find Or Create Organizations

[ ] Columns in the left pare are

[ ] Name

[ ] Type - visible if organization type list is non-empty

[ ] Phone - shows primary phone, link to call the organization

[ ] Phone Type

[ ] Location - city and state in <City, State> format

[ ] Website

[ ] the left pane is sorted by Organization Name

  


[ ] Columns in the right pane are

[ ] Contact Name - link to the contact detail screen

[ ] Phone - link to call the contact

Sagar Sagar 11/16/2022: The link was added in [[PC0066295]] - E00 - Standard Contacts Enhancements (Round 2)

[ ] Email - link of sending email to the contact

Sagar Sagar 11/16/2022: The link was added in [[PC0066295]] - E00 - Standard Contacts Enhancements (Round 2)

[ ] the right pane is grouped by active status

Sagar Sagar 11/17/2022: The grouping was added in [[PC0086057]] - Contacts: Organization report subpane should group by active status

[ ] the right pane is sorted by Contact Name

  


Sagar Sagar 11/16/2022: The right pane was added in [[PC0066295]] - E00 - Standard Contacts Enhancements (Round 2)

  


Sagar Sagar 11/20/2022: Configure Contact Types report has been added in [[PC0127723]] - Contacts: Organizations are contacts. This was added to configure different types of contact types as well as to add new contact types.

[ ] Configure Contact Types

[ ] Columns

[ ] Type

[ ] Supports Individual - visible if Config_UseLegacyOrganizations is False

[ ] Supports Organization - visibe inf Config_UseLegacyOrganizations is False

[ ] Only ask prompt - Show inactive contact types, checkbox

[ ] If its checked, the report is grouped by Active Inactive status

[ ] Only report button New Contact Type to create new contact type
