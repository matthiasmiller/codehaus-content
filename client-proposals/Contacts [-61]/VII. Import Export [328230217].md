7\. Import Export

Sagar Sagar 11/17/2022: The import export files have been added in [[PC0086160]] - E00 - Export/import: contacts and organizations data. They were added for contacts and organizations in case we need data from other systems or we need further operation with records with excel files. We set the export files such a way that it can be used as an input file for importing data again in our system.

  


Contact importing fields are

[ ] Active

[ ] Type

[ ] Name

[ ] First Name

[ ] Middle Name

[ ] Last Name

[ ] Gender

[ ] Organization

[ ] Legacy Organization - if Config_UseLegacyOrganizations is True, we support importing two organizations

[ ] Organization - if Config_UseLegacyOrganizations is False, we support importing two organizations defined with contact type

[ ] Address RG - 2 addresses including

[ ] Address Type

[ ] Address

[ ] Address 2

[ ] City

[ ] State

[ ] Zip

[ ] Country

[ ] Phone RG - 3 phone numbers including

[ ] Phone

[ ] Phone Type

[ ] Email

[ ] Notes

  


Organization importing fields are

[ ] Name

[ ] Address RG - 2 addresses including

[ ] Address

[ ] City

[ ] State

[ ] Zip

[ ] Phone

[ ] Website

  


Contact exporting columns are

[ ] Contact Name

[ ] Contact First Name

[ ] Middle

[ ] Contact Last Name

[ ] Contact Address Type 1

[ ] Contact Address Type 1 Address 1

[ ] Contact Address Type 1 Address 2

[ ] Contact Address Type 1 City

[ ] Contact Address Type 1 State

[ ] Contact Address Type 1 Zip

[ ] Contact Address Type 1 Country

[ ] Contact Address Type 2

[ ] Contact Address Type 2 Address 1

[ ] Contact Address Type 2 Address 2

[ ] Contact Address Type 2 City

[ ] Contact Address Type 2 State

[ ] Contact Address Type 2 Zip

[ ] Contact Address Type 2 Country

[ ] Contact Phone Type 1

[ ] Contact Phone 1

[ ] Contact Phone Type 2

[ ] Contact Phone 2

[ ] Contact Phone Type 3

[ ] Contact Phone 3

[ ] Contact Active

[ ] Contact Gender

[ ] Contact Type

[ ] Contact Legacy Organization 1

[ ] Contact Legacy Organization 2

[ ] Contact Email

[ ] Contact Notes

[ ] Is Organization

[ ] Contact Linked Organization 1

[ ] Contact Linked Organization 2

  


Organization exporting columns are

[ ] OrganizationName

[ ] OrganizationAddress1

[ ] OrganizationCity1

[ ] OrganizationState1

[ ] OrganizationZip1

[ ] OrganizationAddress2

[ ] OrganizationCity2

[ ] OrganizationState2

[ ] OrganizationZip2

[ ] OrganizationPhone

[ ] OrganizationWebsite
