
# Strasburg Pallet - Cut List Generator

## Lists

### Raw Material Types List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### Sizer Overage Methods List

This is a non-editable simple list.

It includes the following items:

* Waste %
* Additional Count

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

### Item Types List

This is a non-editable simple list.

It includes the following items:

* Non-Material Item
* Material - Lumber
* Material - Mulch
* Cut List Only
* Assembly Only
* Cut List & Assembly

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

### Item Wings List

This is a non-editable simple list.

It includes the following items:

* Flush
* End Wing
* Side Wing
* Full-Wing

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

### Coefficient Methods List

This is a non-editable simple list.

It includes the following items:

* Linear
* Inverse
* Log

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

### Coefficient Features List

This is a non-editable simple list.

It includes the following items:

* Assembly Quantity
* Board Feet Per Item
* # Parts Per Item
* Max Lumber Length (In)
* Cubes (Per Item)
* Max Lumber Thickness (In)
* Max Outside Dim. (In)

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

### Coefficient Types List

This is a non-editable simple list.

It includes the following items:

* Intercept
* Item Feature
* Assembly Method
* Fastener Present
* Fastener Count
* Item Category

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

### Units Of Measure List

This is a non-editable simple list.

It includes the following items:

* Board Feet With Kerf
* Board Feet Without Kerf
* Each
* Outside Dimensions (SF)
* Linear Feet

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

### Item Dimensions List

This is a non-editable simple list.

It includes the following items:

* Thickness/Height
* Width
* Length

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

### Raw Material Keywords List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

## Records

### Item Record

The Item is used to represent Sage items in the cut list generator and the assembly tracker.

Sections and Fields:

* Item section:
  * Code (string)
  * Category (drop list of Item Categories)
  * Type (drop list of Item Types)
  * Customer (drop list of Contacts; sometimes required)
  * Description (text)
  * Notes (text)
  * Heat Treat (checkbox; auto-calculated; read-only)
  * Has Finished Dimensions (checkbox; auto-calculated; hidden & read-only)
  * Wing (drop list of Item Wings; required)
  * Outside Length (In) (number; 4 decimals)
  * Base Length (In) (number; 4 decimals; sometimes required)
  * Outside Width (In) (number; 4 decimals)
  * Base Width (In) (number; 4 decimals; sometimes required)
  * Outside Height (In) (number; 4 decimals)
  * Outside/Base Dimensions (text; auto-calculated; read-only)
* Value section:
  * Parts (number; 0 decimals; auto-calculated; read-only)
  * Price (number; 2 decimals; auto-calculated; read-only)
  * Qty for Pricing (number; 0 decimals)
  * Override Assembly Value (checkbox; auto-calculated)
  * Assembly Value (number; 2 decimals; auto-calculated)
  * Assembly Value (Stored) (number; 2 decimals; hidden & read-only)
  * Total BF Without Kerf (number; 7 decimals; auto-calculated; read-only)
  * Total BF With Actual Kerf (number; 7 decimals; auto-calculated; read-only)
  * Outside Dimensions (SF) (number; 4 decimals; auto-calculated; read-only)
* Assembly section:
  * Stock Item (checkbox)
  * Sample Pallet (checkbox)
  * Assembled As (drop list of Items)
  * View Assembled As Item (report link)
  * Sold As (View Items) (report link)
  * Assembly Method (drop list of Assembly Methods)
  * Number of Fastener Types (number; 0 decimals; auto-calculated; read-only)
  * Hand Fasteners (number; 0 decimals; auto-calculated; read-only)
  * Machine Fasteners (number; 0 decimals; auto-calculated; read-only)
  * Cost of All Fasteners (number; 2 decimals; auto-calculated; read-only)
  * Setup Time (Mins) (number; 0 decimals; auto-calculated; read-only)
  * Score (number; 2 decimals; auto-calculated; read-only)
  * Needs Assembly (checkbox; auto-calculated; hidden & read-only)
* Lumber section:
  * Needs Cut List (checkbox; auto-calculated; hidden & read-only)
  * Lumber; embedded spreadsheet of:
    * Quantity (number; 1 decimals; required)
    * Quantity (Lyr) (number; 2 decimals; auto-calculated; read-only)
    * Dimensions (text; auto-calculated; read-only)
    * Thickness (In) (number; 4 decimals; required)
    * Width (In) (number; 4 decimals; required)
    * Random Width (checkbox)
    * Length (In) (number; 4 decimals; required)
    * Raw Material (drop list of Raw Materials)
    * Sizer (drop list of Cut List Subtypes)
    * Cant Description (text; auto-calculated; read-only)
    * Cant Size (drop list of Cant Sizes)
    * Cant Dimensions (text; auto-calculated; hidden & read-only)
    * Cant Thickness (In) (number; 4 decimals; auto-calculated; hidden & read-only)
    * Cant Width (In) (number; 4 decimals; auto-calculated; hidden & read-only)
    * Cant Length (In) (number; 0 decimals)
    * Cant Lumber Qty / Cant (number; 4 decimals; auto-calculated; read-only)
    * Cant Species (text)
    * Cant Qty (number; 0 decimals; auto-calculated; read-only)
    * Cant Override Waste % (number; 0 decimals)
    * Cant Additional Count (number; 0 decimals)
    * Sizer Misc Prep (text)
    * Raw Material Info (Sawing) (text)
    * Enable Sawing Multiplier (checkbox)
    * Saw 1 (drop list of Cut List Subtypes)
    * Saw 1 Misc Prep (text)
    * Saw 1 Yield Qty (number; 2 decimals; auto-calculated; read-only)
    * Saw 1 Yield Dimensions (text; auto-calculated; read-only)
    * Saw 1 Yield Thickness (In) (number; 4 decimals; required)
    * Saw 1 Yield Width (In) (number; 4 decimals; required)
    * Saw 1 Yield Random Width (checkbox)
    * Saw 1 Yield Length (In) (number; 4 decimals; required)
    * Saw 1 Unit Qty (number; 0 decimals)
    * Saw 2 (drop list of Cut List Subtypes)
    * Saw 2 Misc Prep (text)
    * Saw 2 Multiplier (number; 1 decimals; required)
    * Saw 2 Unit Qty (number; 0 decimals)
    * Saw 3 (drop list of Cut List Subtypes)
    * Saw 3 Misc Prep (text)
    * Saw 3 Unit Qty (number; 0 decimals)
    * Saw 4 (drop list of Cut List Subtypes)
    * Saw 4 Misc Prep (text)
    * Saw 4 Unit Qty (number; 0 decimals)
    * Saw 5 (drop list of Cut List Subtypes)
    * Saw 5 Misc Prep (text)
    * Saw 5 Unit Qty (number; 0 decimals)
    * BF Without Kerf (number; 7 decimals; auto-calculated; read-only)
    * Import ID (number; 0 decimals; hidden & read-only)
    * Sizer Species (Non-Cant) (Depr) (text; hidden & read-only)
    * Actual Kerf % (percentage; 0 decimals; auto-calculated; hidden & read-only)
    * BF With Actual Kerf (number; 7 decimals; auto-calculated; hidden & read-only)
  * Flag in Cut List Generator (checkbox)
* Raw Materials section:
  * Raw Materials; embedded spreadsheet of:
    * Raw Material (drop list of Raw Materials; required)
    * Unit of Measure (drop list of Units Of Measure; auto-calculated; read-only)
    * Entered Amount (number; 2 decimals)
    * Amount (number; 2 decimals; auto-calculated; read-only)
    * Type (drop list of Raw Material Types; auto-calculated; read-only)
    * Setup Cost (number; 2 decimals; auto-calculated; read-only)
    * Cost (Each) (number; 4 decimals; auto-calculated; read-only)
    * Cost (Total) (number; 4 decimals; auto-calculated; read-only)
* Attachments section:
  * Attachments; embedded spreadsheet of:
    * Key (text; hidden & read-only)
    * Name (text; auto-calculated; read-only)
    * Item (drop list of Items)
    * Notes (text)
    * Date (date; auto-calculated; read-only)
    * DateInternalGMT (date; hidden & read-only)
    * Time (text; auto-calculated; read-only)
    * TimeInternalGMT (number; 0 decimals; hidden & read-only)
    * Download URL (text; auto-calculated; hidden & read-only)
    * Download (report link)
    * Delete URL (text; auto-calculated; hidden & read-only)
    * Delete (report link)
  * Attachment Upload URL (text; auto-calculated; hidden & read-only)
  * Upload Attachment (report link)

### Raw Material Record

The Raw Material defines the raw materials (lumber, fasteners, etc) and is used to score assembly of items, calculate the cost, as well as specify the cut list.

Lumber uses board feet and linear feet for pricing. All others use per-item pricing.

Standard Dimensions are used to round up.

Sections and Fields:

* Raw Material section:
  * Name (string)
  * Type (drop list of Raw Material Types; required)
  * Active (checkbox)
  * Sort Order (number; 0 decimals)
  * Nominal Thickness (In) (number; 4 decimals; required)
  * Nominal Width (In) (number; 4 decimals; required)
* Expected Keywords section:
  * Keywords; embedded spreadsheet of:
    * Keyword (drop list of Raw Material Keywords)
* Dimensions section:
  * Lumber Thickness (In) (number; 4 decimals; required)
  * Lumber Width (In) (number; 4 decimals; required)
  * Lumber Length (In) (number; 4 decimals; required)
* Cost section:
  * Cost Unit of Measure (drop list of Units Of Measure)
  * Setup Cost (number; 2 decimals)
  * Unit Cost (number; 4 decimals)
  * Standard Dimensions; embedded spreadsheet of:
    * Dimension (drop list of Item Dimensions; required)
    * Amount (rounds up for pricing) (number; 2 decimals; required)
* Fasteners section:
  * Fastener Category (drop list of Fastener Category Names)
  * Fastener Score (number; 0 decimals; sometimes required)

### Cant Sizes Record

Sections and Fields:

* Cants section:
  * Cant Dimensions (string; read-only)
  * Cant Thickness (In) (number; 4 decimals; required)
  * Cant Width (In) (number; 4 decimals; required)

### Cut List Subtype Record

Sections and Fields:

* Cut List Subtype section:
  * Work Order Type (drop list of Work Order Types; required)
  * Name (string)
  * Active (checkbox)
  * Sort Order (number; 0 decimals)
  * Sizer Uses Cants (checkbox; auto-calculated; read-only)
  * Allow Write-In Quantities (checkbox)
* Pricing section:
  * Use Unit Pricing (checkbox)
  * Raw Material for Pricing (drop list of Raw Materials; required)

### Assembly Method Record

Sections and Fields:

* Assembly Method section:
  * Name (string)

### Item Category Record

Sections and Fields:

* Item Category section:
  * Name (string)

### Fastener Category Name Record

Sections and Fields:

* Fastener Category Name section:
  * Name (string)

### Lumber Size Record

Sections and Fields:

* Lumber Size section:
  * Yield Dimensions (string; read-only)
  * Yield Thickness (In) (number; 4 decimals; required)
  * Yield Width (In) (number; 4 decimals; required)
* Rough-Cut Lumber section:
  * Cant Kerf % for Pricing (percentage; 2 decimals)
  * Cants; embedded spreadsheet of:
    * Cant Size (drop list of Cant Sizes; required)
    * Yield Qty (number; 0 decimals; required)
    * Actual Kerf % (number; 0 decimals; auto-calculated; read-only)
* Dimensional Lumber section:
  * Dim. Lbr. Kerf % for Pricing (percentage; 2 decimals)
  * Dimensional Lumber; embedded spreadsheet of:
    * Thickness (In) (number; 4 decimals; required)
    * Width (In) (number; 4 decimals; required)
    * Dimensions (text; auto-calculated; read-only)
    * Yield Qty (number; 0 decimals; required)
    * Actual Kerf % (number; 0 decimals; auto-calculated; read-only)