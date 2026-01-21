3.4. Configure Manufacturing Task Types

  


Requirements

Overview: Manufacturing Tasks are used for the various activities that must be completed in the construction of a building. There will be various types of tasks, with different settings connected to them. These types will be defined on separate records, called "Manufacturing Task Types". 

  


Accessed via: Manufacturing Task Types Report

  


Sections and Fields: 

Task Type section:

  * Active (checkbox; default to filled) 
  * Task Name (required; text field; disallow duplicates)
  * Manufacturing Department (required; drop list of active departments)
  * Sequence (required; whole number; disallow duplicates)
  * Payment Type (required; drop list of the following:) 
    * Piece Work
    * Fixed
    * Hourly
  * Payment % (visible and required if Payment Type = Piece Work; number with up to 2 decimal places; this is a percentage of the PWBP of the associated SKU/item)
  * Payment $ (visible and required if Payment Type = Fixed; number with up to 2 decimal places)



  


Data Access: Admin Only

  


Other Notes:

  * There should be validation against deactivating Manufacturing Task Types that are being used by active tasks on Work Orders.
  * CCI/CH would take care of importing these/doing the initial setup, based on information provided by BEB.



  


*Done.

  


Development Specification

This is a lookup record. 

  


[ ] When migrating, we need to map blank departments to a "General" department.

  


There are 70+ task types currently. We'll need to pull these out of the existing system.

  


  


Mockup: [https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1312292163](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1312292163)
