4.4. SKU Record

  


Requirements

TODO_AP: Ben Reitz 11/14/2025: Standardize this spec as needed.

  


Overview: The Solution uses the standard Silverloom SKUs module, utilizing the standard SKU record with its  sections and fields, which may have custom behaviors. Additional custom sections & fields may be added as well. Any customizations are noted as such in the spec. 

  


Accessed via: 

  * Manage SKUs report



  


Sections and Fields: 

  * SKU section:
    * SKU (optional; plain text field; validate against active duplicate SKUs)
    *  Is Active (optional; checkbox; defaults to checked)
    * Desc (optional; plain text field; validation against duplicate descriptions: "Another SKU has the same description. (Field: Desc)")
    * Category (optional; custom drop list of Lumber, Metal)
    * Next SKU for Lumber (optional; custom button; visible if no SKU is specified and Category is set to Lumber when clicked, sets the SKU to the next in the sequence for lumber)
    * Next SKU for Metal (optional; custom button; visible if no SKU is specified and Category is set to Metal; when clicked, sets the SKU to the next in the sequence for metal)
    * Yard Sort Order (optional; visible if Category = Lumber; custom number field with no decimals; maximum of 5 digits; used to set the sort order on the Order record)
    * Metal Type (optional; visible if Category is Metal; custom drop-list of Central States, Everlast)
    * UOM (optional; editable drop list)
    * Display UOM (optional; editable drop list)
    * Alternate UOMs (button; opens a child screen with the following:
      * embedded spreadsheet of:
        * UOM (editable drop list of UOMs)
        * UOM Multiplier (number field; 2 decimals)
      * Insert Row (button)
      * Append Row (button)
      * Delete Row (button)
    * Vendors (button; opens a child screen with the following:
      * embedded spreadsheet of:
        * Vendor (editable drop list)
        * Vendor Sku (plain text field)
        * Vendor UOM (editable drop list of UOMs)
      * Insert Row (button)
      * Append Row (button)
      * Delete Row (button)
    * Sales Price (optional; custom number field; two decimals; displays sum of Unit Cost from SKU Lot record and Profit Margin %)
    * Price per Inch (optional; custom read-only number field; five decimals; visible if UOM is set to Ft; displays difference of Sales Price and 12)
    * Profit Margin % (optional; custom number field; five decimals; dynamically updates if Sales Price or Unit Cost is changed)
    * Unit Weight (optional; custom number field; 2 decimals; visible if UOM is not set to Ft)
    * Weight per Ft (optional; custom number field; 2 decimals; visible if UOM is set to Ft)
    * Weight per Inch (optional; custom field; auto-set and read-only; visible if UOM is set to Ft; displays difference of Weight per Ft and 12)



  


  * Inventory section (displays to the right of the SKU section):
    * SKU Lots (link; opens SKU Lots report, filtered to the corresponding SKU)



  


  * Notes
    * Unlabeled optional memo



  


Data Access: 

  * Visible to all users



  


Special Considerations:

  * Copy Record: No fields are cleared
  * Delete Record: Deletion is allowed
  * Merge Record: N/A



  


Other Notes:

  * Negative or zero inventory is permitted in SKU Lots. There is a possibility that the client will have a single SKU lot's inventory become negative.
  * Note that this record includes a link to access Modification History.



  


Development Specification

Change Requests:

  * Ben Reitz 05/08/2025: [[[IN10787](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10789&)]] - ZTD - Add Yard Packing List Printout (prev. Changes to Lumber Order RG)


