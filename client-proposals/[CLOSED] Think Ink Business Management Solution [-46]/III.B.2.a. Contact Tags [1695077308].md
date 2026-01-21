3.2.2.1. Contact Tags

  


Requirements

The Contact record will include an option for "Tags" underneath the "Type" drop list. This will be an editable multi-select drop list and will serve to track "subtypes" for Contacts. This will allow for multiple Tags to be set for a given Contact. If multiple Tags are selected, they will appear as a comma-separated list when the drop list is closed.

  


The Contact Tags will include the following:

  * School Customer
  * Large Business Customer
  * Medium Business Customer
  * Small Business Customer
  * Residential Customer
  * Cold Lead
  * Hot Lead



  


Users can create, edit, and delete Tags through the Lists menu option in the Advanced menu (there will not be a "\+ Add New Item" feature on the list on the detail screen).

  


The Contacts report will allow filtering by one or more Tags.

  


Note that Contact Tags are not included in the import from Classic Accounting.

  


Development Specification

Simple list.

  


Matthias: I think this should be a standard feature. I don't care whether it's enabled for everyone, or if it's just enabled via a config switch.

  


The CanAddToList can be a config macro, default to True but disable for ZTK

  


We will add a new Config_ContactsShowTags and a Config_ContactsCanAddToTags switches.

  


A multi-select droplist will show selected items. Checking and unchecking items will modify an underlying RG. We will also make the "Tags" label that lets you drill into the underlying RG (a simple RG with a ghost row and Add/Delete buttons -- can use a full-screen RG). Write up a child job to also do this for Incidents.

BID: 1 day
