2.1.1. Shop Supplies Record

Austin Priest 01/20/2023: [[[IN5224](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-5226&)]] - ZGA - Incidents - Add Tracking for Shop Supplies (T&M)

  


[[PC0147956]] - ZGA - Shop Supplies (T&M)

Shop Supplies Record (new): 

  * Add a new Shop Supply record with the following: 
    * Fields: 
      * Active (checkbox; defaults to filled) 
      * Description (required; plain text; validate against duplicate names for records, active or inactive) 
        * Validation message for duplicates: "This Description already has been used for another Shop Supply record. Change the description on one of the records to save this record." 
    * Data Access: View and edit for all users 
    * Other Notes: 
      * Shop Supply records cannot be deleted. 
        * Validation message for attempted deletion: "This Shop Supply item is used in the system. It cannot be deleted, but it can be marked inactive." 



  


[[PC0147957]] - ZGA - Shop Supply Import (T&M)

Initial Setup: 

  * The initial list of Shop Supplies items will be created by importing an Excel file (Column D - "Item" is the column to use for the import) 
  * There will be an "Import Shop Supplies" menu option on the "Imports and Exports" section of the Advanced menu that can be used to run the import to set up the shop supplies records. 
  * Good's Ag Repair will take care of preparing an export file of the descriptions of the applicable sales items from QuickBooks. 
  * Good's Ag Repair will take care of cleaning up the item names in QB to avoid duplicate names, etc. 
  * CCI/CH will provide assistance for the initial setup as needed. 



  


Ongoing Imports: 

  * Additional imports can be run (annually, etc.) via the "Import Shop Supplies" menu option. 
  * New items on the import file will automatically be added as records in AppHosting when an import is run. 
  * Missing items on the import file will automatically be marked Inactive in AppHosting when an import is run. 
  * If an item marked Inactive in AppHosting matches an item included in the import, it will be marked Active when the import is run. 
  * If items are renamed in QB, they will be added as new items in AppHosting and the old name will be marked Inactive when an import is run. This can be resolved by manually merging the old and new records (CCI/CH can provide guidance and assistance with this). 
    * If an item description is edited or merged with another in AppHosting, the description would be updated accordingly everywhere it has been used in the database. 



  


Other Notes: 

  * Inventory tracking is done in QB, so it would not be done in the AppHosting Solution. 
  * Price tracking and invoicing is done in QB, so it would not be done in the AppHosting Solution. 
  * Unit of Measure is not fielded in QB, so it would not be used in the AppHosting Solution (the UOM is included in the description of some of the items). 
  * No reporting is needed for used Shop Supplies - Good's Ag will open the incidents to get the information they need.



Here is a sample of the Good's Ag Repair supplies list (the import probably would be only the "Non-inventory Part" items): [https://docs.google.com/spreadsheets/d/12olKDUC8e6AkeGGBN_27R5p3X0z6DvKX/](https://docs.google.com/spreadsheets/d/12olKDUC8e6AkeGGBN_27R5p3X0z6DvKX/).
