8.11. Packing Slip Record

  


Requirements

This would include:

  * Customer Name/Address/Phone
  * Shipping Name/Address/Phone
  * Customer PO (if generated from sales order)
  * Embedded spreadsheet of:
    * SKU (list of all customer SKUs in stock, as well as general SKUs)
    * Lot (list of all lots in stock for the selected SKU)
    * Description (automatic & read-only)
    * Qty
    * UOM



  


Development Specification

TODO_IDD: Handle the workflow for creating the packing slips from a sales order, etc. We will presumably want to automatically link between SO -> items created in WO -> items shipped via SO
