11\. Data Migration

  


Requirements

The process of importing data and cleaning up migrated data during deployment will be determined after further design.

  


The following data will likely be migrated into the Solution:

  * Dispatch Track export
    * NOTE: This needs to include rows for the builders for informational purposes.
    * Prompt for
      * Status (default to Ordered)
      * Customer Region
    * Columns (see Excel file)
      * Order Number
      * Ship Name
      * Ship Address
      * Ship City
      * Ship State
      * Ship Zip
      * Delivery Date
      * Delivery Type - always DELIVERY
      * Description - always FURNITURE
      * Quantity - always 1
      * Location
      * Cube
      * Email
      * Phone1



  


Development Specification

  * TODO_HLD:
    * Process for determining which orders for pickups
    * Do we need a "Scheduled for PIckup"?


