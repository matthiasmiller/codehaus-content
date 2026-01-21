3.3. Configure Manufacturing Departments

  


Requirements

Overview: Manufacturing Departments are used to sequence the manufacturing process. These will be stored on separate records, called "Manufacturing Departments". 

  


Accessed via: Manufacturing Departments Report

  


Sections and Fields: 

Manufacturing Department section: 

  * Active (checkbox; default to filled) 
  * Department Name (required; text field; disallow duplicates)
  * Sequence (required; whole number; disallow duplicates)



  


Data Access: Admin Only

  


Other Notes: 

  * There should be validation against deactivating Manufacturing Department records that have active tasks associated with them on Work Orders. 
  * CCI/CH would take care of importing these/doing the initial setup, based on information provided by BEB.
  * The current active Departments are as follows:
    * Cutout
    * Framing
    * Painting
    * Roofing
    * Yard Man



  


*Done.

  


Development Specification

This is a lookup record. 

  


  


Mockup: [https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1424174634](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1424174634)
