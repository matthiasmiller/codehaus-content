16.6. Paperwork Packet/Disposition

  


Requirements

Overview: This is used to collect and prepare all the forms that need to be sent along with the order. This has been called the "Disposition" in the existing software, but probably will be renamed to "Paperwork Packet" or something similar. 

  


Note that this might be a feature on the Order Record, or it might be its own separate record type (to be determined in in-depth design). 

  


Accessed via: Details to be specced out in in-depth design.

  


Sections and Fields: 

  * Date (editable)
  * Reason for Release (droplist list of Sale, Exchange or Transfer, Donation)
  * Serial (editable report of the serial numbers of all animals that are part of the release)
  * Seller (droplist of sellers)
  * Seller Address (auto-fills according to seller)
  * License Number (license number of seller; auto-filled according to seller)
  * USDA Number (auto-fills according to ?)
  * Buyer (droplist of all customers)
  * Buyer Address (auto-fills according to buyer)
  * Delivery By (droplist of Commercial Shipper, Buyer's Vehicle, Seller's Vehicle)
  * Information of Company (name and address; auto-fills according to Delivery By selection)
  * Driver (droplist of all drivers)
  * Business Address of Driver (auto-fills based on driver)
  * Ship To (droplist of customers)
  * Received By (single line plain text field)
  * Title (title of receiver)
  * Date (editable)
  * Paperwork Type (droplist of Original - Seller's Record, USDA Copy - To be retained by seller, Buyer's Copy - To accompany shipment and be retained by owner)



  


Data Access: Details to be specced out in in-depth design. 

  


Special Considerations: 

  * Copy Record: Details to be specced out in in-depth design. 
  * Delete Record: Details to be specced out in in-depth design. 
  * Merge Record: Details to be specced out in in-depth design. 



  


Other Notes:

  


Development Specification

TODO_IDD: Currently, when the user clicks Save on the Disposition, it marks all included dogs as Sold (marks the dog as Inactive and sets the Reason to Sold).
