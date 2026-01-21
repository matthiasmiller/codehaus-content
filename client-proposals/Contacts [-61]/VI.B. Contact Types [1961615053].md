6.2. Contact Types

Sagar Sagar 11/10/2022: Previously contact type was a simple list. When we started to incorporate organizations with contacts, we moved the contact type to be different database level and added sufficient support. This was coded in [[PC0127723]] - Contacts: Organizations are contacts

  


The contact type has below fields

[ ] Fields

[ ] Type

[ ] Active - checkbox

[ ] Supported Entity Types - label

[ ] Individual - checkbox

[ ] Organization - checkbox

[ ] Default to organization - checkbox

[ ] Created label - label with "Created: <MM/DD/YYYY> <HH:MM:SS> <AM/PM> by <UserName>" format

[ ] Last Modified label - label with "Last Modified: <MM/DD/YYYY> <HH:MM:SS> <AM/PM> by <UserName>" format

[ ] Modification History - link to the activity report, not visible for new record

  


Sagar Sagar 11/28/2022: The contact types has some validations.

[ ] Validations

[ ] You do not have permission to edit this contact type

[ ] At least one supported entity type must be specified.

[ ] This contact type cannot be deactivated because active contacts reference it.

[ ] Contact type cannot default to organization if it does not support organizations.
