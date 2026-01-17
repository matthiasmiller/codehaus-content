
# Strasburg Pallet - Sage 100

## Lists

### Sage Order Statuses List

This is a user-editable simple list.

It includes the following items:

* A
* C
* X

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### Sage Invoice Types List

This is a user-editable simple list.

It includes the following items:

* CM
* IN
* XD

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### Sage Product Types List

This is a non-editable simple list.

It includes the following items:

* Finished Good
* Raw Materials
* Discontinued
* Kit

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

### Sage Item Types List

This is a non-editable simple list.

It includes the following items:

* Regular Item
* Charge Item
* Comment Item
* Miscellaneous Item

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

## Records

### Sage Order Row Record

The Sage Order Row is a direct import of data from Sage.

Sections and Fields:

* Sage Order Row section:
  * Silverloom ID (autonumber; hidden & read-only)
  * Row ID (number; 0 decimals; read-only)
  * SO Number (number; 0 decimals; read-only)
  * Order Date (date; read-only)
  * Due Date (date; read-only)
  * Order Status (drop list of Sage Order Statuses; read-only)
  * Item Code (text; read-only)
  * Item Code Desc (text; read-only)
  * Customer Name (text; read-only)
  * Quantity Ordered Original (number; 6 decimals; read-only)
  * Quantity Ordered Revised (number; 6 decimals; read-only)
  * Original Unit Price (number; 6 decimals; read-only)
  * Last Unit Price (number; 6 decimals; read-only)
  * Quantity Sold (12 Mo) (number; 6 decimals; read-only)
  * Times Sold (12 Mo) (number; 6 decimals; read-only)
  * SO Header Upd. Date (date; read-only)
  * SO Header Upd. Time (Hrs) (number; 6 decimals; read-only)
  * Inv. Item Upd. Date (date; read-only)
  * Inv. Item Upd. Time (Hrs) (number; 6 decimals; read-only)
  * Deleted (checkbox; read-only)
* Invoicing section:
  * Invoice Date (date; read-only)
  * Invoices; embedded spreadsheet of:
    * Invoice Number (number; 0 decimals; read-only)
    * Invoice Row ID (number; 0 decimals; read-only)
    * Invoice Quantity (number; 5 decimals; read-only)
  * Quantity Invoiced (Per Sage) (number; 6 decimals; hidden & read-only)
  * Quantity Invoiced (number; 5 decimals; auto-calculated; read-only)
  * View Invoices (report link)
* Customized for Strasburg Pallet Company section:
  * Processed Non-Cut List Item (checkbox)
  * Override Total (number; 0 decimals)
  * Total Needed (number; 5 decimals; auto-calculated; read-only)

### Sage Invoice Row Record

Sections and Fields:

* Sage Invoice Row section:
  * Silverloom ID (autonumber; hidden & read-only)
  * Invoice Number (number; 0 decimals; read-only; required)
  * Row ID (number; 0 decimals; read-only)
  * Type (drop list of Sage Invoice Types; read-only)
  * Date (date; read-only)
  * Item Code (text; read-only)
  * Qty Ordered (number; 6 decimals; read-only)
  * Qty Shipped (number; 6 decimals; read-only)
  * Qty Backordered (number; 6 decimals; read-only)
  * Ship Date (date; read-only)
  * Unit Price (number; 6 decimals; read-only)
  * SO Number (number; 0 decimals; read-only)
  * View Sales Order (report link)
  * Deleted (checkbox; read-only)

### Sage Product Line Record

Sections and Fields:

* Sage Product Line section:
  * Desc (text; required)
  * Code (string)
  * Product Type (drop list of Sage Product Types)

### Sage Item Record

Sections and Fields:

* Sage Item section:
  * Code (string)
  * Type (drop list of Sage Item Types)
  * Desc (text)
  * Use In AR (checkbox)
  * Use In SO (checkbox)
  * Use in PO (checkbox)
  * Use in BM (checkbox)
  * Product Type (drop list of Sage Product Types)
  * Product Line (drop list of Sage Product Line Codes)