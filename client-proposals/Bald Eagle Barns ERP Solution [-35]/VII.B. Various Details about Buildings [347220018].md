7.2. Various Details about Buildings

  


Requirements

Creating New Lot Buildings (Copying from Existing Buildings): 

  * To create 1 new lot building that is a duplicate of an existing or previously built building, open the record of an existing building like the one you want to create, make a copy of it, and adjust any details as needed, then save the new record. 
  * To create multiple new lot buildings: See the "Create Multiple New Lot Building Records" section in this proposal ("Optional/Future Features").



  


Copying Building Records: Whenever a Building record is copied, the data from the following fields should not be copied into the new record:

  * Building Contact
  * Inactive status, if applicable (copied buildings should always be active)
  * Deactivation Reason
  * Building ID
  * Serial Number Counter
  * Serial Number
  * SRB Date
  * Status (copied building should always start with Draft status)
  * Status Date
  * SRB stamp 
  * Build Date
  * Current Location
  * Days in Current Location
  * Notes
  * Building History
  * Salesperson
  * Dealer
  * Building MSRP (should be recalculated for the new building) 
  * Associated Sales Orders, Work Orders, etc.



  


Essentially, the details that should be copied over are the ones needed to build a replica of the original building (including the layout diagram).

  


Making Changes to Sold Buildings: After a building has been been assigned its Serial Number, any changes to the building that would affect the price and/or the Serial Number must be made via a Change Order (see corresponding section of this proposal). 

  


  


Fully Custom Buildings: In the uncommon event that a customer wishes to design and purchase a building that is fully custom (not corresponding to any existing Base Buildings), the Salesperson should create a new Base Building SKU (using the "Custom" Building Style) and use that SKU for the custom building. After the building has been sold, an admin can deactivate that new SKU to take it off the lists of Base Building items. This is similar to BEB's current process for fully custom buildings.

  


The SKUs will:

  * Only allow editing by an admin, unless it is a Custom building style
  * Validate that the building style is Custom for any edits made by a non-admin



  


*Done.

  


Development Specification

The copy for the layout diagram is documented in the layout diagram section.
