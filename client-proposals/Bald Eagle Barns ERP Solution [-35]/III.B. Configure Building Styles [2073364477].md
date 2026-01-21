3.2. Configure Building Styles

  


Requirements

Overview: BEB has various styles of buildings, each with its corresponding abbreviation, called the "Style Code". The same style can be used for buildings of various sizes. These styles will be configured and stored on separate records, called "Building Styles". 

  


Accessed via: Building Styles Report

  


Sections and Fields: 

Building Type section:

  * Active (checkbox; default to filled)
  * Style Name (required; text field; validate against duplicates, including inactive styles)
  * Style Code for Serial # (required; text field; validate against duplicates, including inactive styles; used for entering the letter at the end of the Product ID, e.g. "SLB" for "Side Lofted Barn")



  


Data Access: Visible to Everyone; Editable by Admins

  


Other Notes:

  * There should be validation against deactivating Building Styles that are used in buildings with active
  * When a Building Style is deactivated, the corresponding information should remain as-is throughout the system (building records, etc.).
  * CCI/CH would take care of importing/doing the initial setup for Building Styles, based on information provided by BEB.
  * The current list of building styles (and corresponding codes) are as follows:
    * Barn Cabin (BC)
    * Cabin (C)
    * Garage (G)
    * High Barn (HB)
    * Quaker (Q)
    * Regular Barn (RB)
    * Side Cabin (SC)
    * Side Lofted Barn (SLB) 
    * Side Lofted Barn Cabin (SLBC)
    * Value Shed (VS)
  * The database would include a platform-owned "Custom" Building Style (code: CUS, probably called "Fully Custom Building") used exclusively for fully custom buildings. This would allow Salespeople to create a new Base Building SKU with the Custom building style, then create the custom building using that SKU. 



  


*Done.

  


Development Specification

This is a lookup record. 

  


Note the Investortools-owned custom building style. 

  


Mockup: 

[https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=2058201491](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=2058201491)
