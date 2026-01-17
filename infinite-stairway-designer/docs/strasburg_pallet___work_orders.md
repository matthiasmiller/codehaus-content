
# Strasburg Pallet - Work Orders

## Lists

### Work Order Statuses List

This is a non-editable simple list.

It includes the following items:

* Unscheduled
* Scheduled
* Complete

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

### Work Order Types List

This is a non-editable simple list.

It includes the following items:

* Assembly
* Sawing
* Sizers

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

## Records

### Work Order Record

The work order is used to track cut list and assembly tasks.

Cut lists are automatically grouped to mirror the printed cut list:

General Work Order Fields
[ ] Completion Date
[ ] Scheduled
[ ] Sort Order

Cut List Fields
[ ] Cut List Subtype
[ ] Customer
[ ] Due Date
[ ] Lumber
*     Thickness
*     RW
*     Width (NA if RW, since RW gets translated to Qty as layers)
*     Length
[ ] Misc Prep

Sawing
[ ] Raw Material
Sizer
[ ] Overage Waste %
Sizer w/ Cants
[ ] Cant Size
[ ] Cant Length
[ ] Cant Notes
Sizer w/o Cants
[ ] Species (Non-Cant)

When it comes to sending orders to the cut list, we use this logic:

*     We want to ignore added/deleted lumber. If the sage order row's work orders are all completed, and all of the lumber items add up to the order quantity, consider it done.

*     When generating the cut list, calculate the order quantity based on the total order quantity, minus the completed order quantity for that lumber item.

*     If this lumber item is already on the schedule, update it with the total quantity. Use the smallest (earliest) sort number of any scheduled items.

*     If not, add this to the unscheduled list.

*     Delete incomplete lumber that is not currently on the cut list.

NOTE: Waste only applies to sizers. However, either waste/nowaste macros can be used for both sawing and sizers.

Sections and Fields:

* Work Order section:
  * New Assembly Work Order (report link)
  * Silverloom ID (autonumber; hidden & read-only)
  * Scheduled (checkbox)
  * Completed On (date)
  * Status (drop list of Work Order Statuses; auto-calculated; read-only)
  * Sort Order (number; 0 decimals)
  * Type (drop list of Work Order Types; required)
* Assembly Item & Time section:
  * Workers; embedded spreadsheet of:
    * Start Time 1 (Stored) (number; 0 decimals; hidden & read-only)
    * End Time 1 (Stored) (number; 0 decimals; hidden & read-only)
    * Employee (drop list of Contacts; required)
    * Start Time 1 (text; auto-calculated; sometimes required)
    * End Time 1 (text; auto-calculated; sometimes required)
    * Break Time (Mins) (number; 0 decimals; auto-calculated; read-only)
    * Total Time (Hrs) (number; 2 decimals; auto-calculated; read-only)
    * Time String Table (text; auto-calculated; hidden & read-only)
    * Setup Time (Mins) (number; 0 decimals; auto-calculated; read-only)
    * Down Time (Mins) (number; 0 decimals; auto-calculated; read-only)
    * Assembly Time (Hrs) (number; 2 decimals; auto-calculated; read-only)
    * Contribution % (number; 2 decimals; auto-calculated; read-only)
  * Assembly Item (drop list of Items; sometimes required)
  * Assembly Item Description (text; auto-calculated; read-only)
  * Assembly Customer (drop list of Contacts; auto-calculated; read-only)
  * Assembly Method (drop list of Assembly Methods)
  * Includes Setup (checkbox; auto-calculated)
  * No Setup (checkbox; auto-calculated)
  * Setup (Yes/No) (drop list of Yes No; hidden & read-only)
  * Setup Time (Mins) (number; 0 decimals; required)
  * Down Time (Mins) (number; 0 decimals)
  * Notes (text)
  * Assembly Historical Import ID (number; 0 decimals; hidden & read-only)
  * Assembly Historical Quantity (text; hidden & read-only)
* Assembly Completed section:
  * Quantity Completed (number; 0 decimals; auto-calculated)
  * Sage Orders; embedded spreadsheet of:
    * Sage Row ID (Num) (number; 0 decimals; hidden & read-only)
    * Sage Order Row ID (text; auto-calculated)
    * Total Needed (number; 0 decimals; auto-calculated; read-only)
    * Remaining Needed (number; 0 decimals; auto-calculated; read-only)
    * Quantity Assembled (number; 0 decimals; required)
  * Partial Work Orders; embedded spreadsheet of:
    * Silverloom ID (number; 0 decimals; hidden & read-only; required)
    * Partial Work Order (text; auto-calculated; required)
    * Total Assembly Time (Hrs) (number; 2 decimals; auto-calculated; read-only)
    * View (report link)
  * Completed WO Silverloom ID (number; 0 decimals; auto-calculated; hidden & read-only)
  * Completed Work Order (report link)
  * Total Assembly Time (Hrs) (number; 2 decimals; auto-calculated; read-only)
* Assembly Break Times section:
  * Breaks; embedded spreadsheet of:
    * Start Time (Stored) (number; 0 decimals; hidden & read-only)
    * End Time (Stored) (number; 0 decimals; hidden & read-only)
    * Start Time (text; auto-calculated; required)
    * End Time (text; auto-calculated; required)
* Cut List section:
  * Manual Sawing Entry (checkbox)
  * Work Order Is Cut List (checkbox; auto-calculated; hidden & read-only)
  * Cut List Subtype (drop list of Cut List Subtypes; required)
  * Customer (drop list of Contacts; read-only)
  * Cut List Item (drop list of Items; read-only)
  * Due Date (date)
  * Lumber Thickness (In) (number; 4 decimals; sometimes required)
  * Lumber Random Width (checkbox)
  * Lumber Width (In) (number; 4 decimals; sometimes required)
  * Lumber Length (In) (number; 4 decimals; sometimes required)
  * Lumber Dimensions (text; auto-calculated; read-only)
  * Misc. Prep (text)
  * Sizer Uses Cants (checkbox; auto-calculated; hidden & read-only)
  * Sizer Cant Qty Override (number; 0 decimals)
  * Sizer Cant Size (drop list of Cant Sizes)
  * Sizer Cant Description (text; auto-calculated; read-only)
  * Sizer Cant Length (In) (number; 0 decimals)
  * Sizer Cant Notes (text)
  * Sizer Species (Non-Cant) (text)
  * Sizer Overage Method (drop list of Sizer Overage Methods; auto-calculated; hidden & read-only)
  * Sizer Overage Waste % (number; 2 decimals)
  * Raw Material Info (Sawing) (text)
  * Sizer (drop list of Cut List Subtypes; auto-calculated; hidden & read-only)
  * Saw (drop list of Cut List Subtypes; auto-calculated; hidden & read-only)
  * Daily Sawing; embedded spreadsheet of:
    * Date (date; required)
    * Actual Cant Qty (number; 0 decimals; sometimes required)
    * Actual Cant LF (number; 2 decimals; auto-calculated; read-only)
    * Actual Yield Qty (number; 0 decimals; sometimes required)
    * Actual Yield BF (number; 7 decimals; auto-calculated; read-only)
  * Mark Completed for Cut List (checkbox; auto-calculated; hidden & read-only)
  * Total Actual Yield (Qty) (number; 7 decimals; auto-calculated; read-only)
  * Total Actual Yield (BF) (number; 7 decimals; auto-calculated; read-only)
  * Total Target Yld (Qty) No Waste (number; 0 decimals; auto-calculated; hidden & read-only)
  * Total Target Yld (Qty) With Waste (number; 0 decimals; auto-calculated; hidden & read-only)
  * Total Estimated Cant Qty (number; 0 decimals; auto-calculated; hidden & read-only)
  * Total Actual Cant Qty (number; 7 decimals; auto-calculated; read-only)
  * Total Remaining Cut List Qty (number; 0 decimals; auto-calculated; read-only)
* Cut List Items section:
  * Items; embedded spreadsheet of:
    * Sage Row ID (number; 0 decimals; hidden & read-only)
    * Sales Order Number (number; 0 decimals; auto-calculated; read-only)
    * Order Date (date; auto-calculated; read-only)
    * Order Item Lumber RG ID (number; 0 decimals; hidden & read-only)
    * Times Sold Last 12 Mo (number; 0 decimals; auto-calculated; read-only)
    * Qty Sold Last 12 Mo (number; 0 decimals; auto-calculated; read-only)
    * Unit Price (number; 2 decimals; auto-calculated; read-only)
    * Order Qty (number; 0 decimals)
    * Order Item / Depr (drop list of Items; hidden & read-only)
    * Single Item Qty (number; 2 decimals)
    * Total Order Qty (number; 0 decimals; auto-calculated; read-only)
    * Inventory Qty (number; 0 decimals)
    * Target Yld Qty (No Waste) (number; 0 decimals; auto-calculated; read-only)
    * Sizer Additional Count (number; 0 decimals)
    * Target Yld Qty (With Waste) (number; 0 decimals; auto-calculated; read-only)
    * Sawing # (number; 0 decimals; auto-calculated; read-only)
    * Delete From Cut List Import (checkbox; hidden & read-only)
    * Actual Yield (Qty) (number; 0 decimals; auto-calculated; read-only)
    * Remaining Cut List Qty (number; 0 decimals; auto-calculated; read-only)