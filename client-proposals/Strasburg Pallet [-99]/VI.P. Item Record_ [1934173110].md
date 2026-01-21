6.16. Item Record*

  


Requirements

The Item is used to represent Sage items in the cut list generator and the assembly tracker.

Sections and Fields:

•     Item section:

–     Code (string)

–     Category (drop list of Item Categories)

–     Type (drop list of Item Types)

–     Customer (drop list of Contacts; sometimes required)

–     Description (text)

–     Notes (text)

–     Heat Treat (checkbox; auto-calculated; read-only)

–     Has Finished Dimensions (checkbox; auto-calculated; hidden & read-only)

–     Wing (drop list of Item Wings; required)

–     Outside Length (In) (number; 4 decimals)

–     Base Length (In) (number; 4 decimals; sometimes required)

–     Outside Width (In) (number; 4 decimals)

–     Base Width (In) (number; 4 decimals; sometimes required)

–     Outside Height (In) (number; 4 decimals)

–     Outside/Base Dimensions (text; auto-calculated; read-only)

•     Value section:

–     Parts (number; 0 decimals; auto-calculated; read-only)

–     Price (number; 2 decimals; auto-calculated; read-only)

–     Qty for Pricing (number; 0 decimals)

–     Override Assembly Value (checkbox; auto-calculated)

–     Assembly Value (number; 2 decimals; auto-calculated)

–     Assembly Value (Stored) (number; 2 decimals; hidden & read-only)

–     Total BF Without Kerf (number; 7 decimals; auto-calculated; read-only)

–     Total BF With Actual Kerf (number; 7 decimals; auto-calculated; read-only)

–     Total BF With Optimal Kerf (number; 7 decimals; auto-calculated; read-only)

–     Outside Dimensions (SF) (number; 4 decimals; auto-calculated; read-only)

•     Assembly section:

–     Stock Item (checkbox)

–     Sample Pallet (checkbox)

–     Assembled As (drop list of Items)

–     Sold As (View Items) (report link)

–     Assembly Method (drop list of Assembly Methods)

–     Number of Fastener Types (number; 0 decimals; auto-calculated; read-only)

–     Hand Fasteners (number; 0 decimals; auto-calculated; read-only)

–     Machine Fasteners (number; 0 decimals; auto-calculated; read-only)

–     Cost of All Fasteners (number; 2 decimals; auto-calculated; read-only)

–     Setup Time (Mins) (number; 0 decimals; auto-calculated; read-only)

–     Score (number; 2 decimals; auto-calculated; read-only)

–     Needs Assembly (checkbox; auto-calculated; hidden & read-only)

•     Lumber section:

–     Needs Cut List (checkbox; auto-calculated; hidden & read-only)

–     Lumber; embedded spreadsheet of:

•     Quantity (number; 1 decimals; required)

•     Quantity (Lyr) (number; 2 decimals; auto-calculated; read-only)

•     Dimensions (text; auto-calculated; read-only)

•     Thickness (In) (number; 4 decimals; required)

•     Width (In) (number; 4 decimals; required)

•     Random Width (checkbox)

•     Length (In) (number; 4 decimals; required)

•     Raw Material (drop list of Raw Materials)

•     Sizer (drop list of Cut List Subtypes)

•     Optimal Cant Sizes (text; auto-calculated; read-only)

•     Cant Description (text; auto-calculated; read-only)

•     Cant Size (drop list of Cant Sizes)

•     Cant Dimensions (text; auto-calculated; hidden & read-only)

•     Cant Thickness (In) (number; 4 decimals; auto-calculated; hidden & read-only)

•     Cant Width (In) (number; 4 decimals; auto-calculated; hidden & read-only)

•     Cant Length (In) (number; 0 decimals)

•     Cant Lumber Qty / Cant (number; 4 decimals; auto-calculated; read-only)

•     Cant Species (text)

•     Cant Qty (number; 0 decimals; auto-calculated; read-only)

•     Cant Override Waste % (number; 0 decimals)

•     Cant Additional Count (number; 0 decimals)

•     Sizer Misc Prep (text)

•     Raw Material Info (Sawing) (text)

•     Enable Sawing Multiplier (checkbox)

•     Saw 1 (drop list of Cut List Subtypes)

•     Saw 1 Misc Prep (text)

•     Saw 1 Yield Qty (number; 2 decimals; auto-calculated; read-only)

•     Saw 1 Yield Dimensions (text; auto-calculated; read-only)

•     Saw 1 Yield Thickness (In) (number; 4 decimals; required)

•     Saw 1 Yield Width (In) (number; 4 decimals; required)

•     Saw 1 Yield Random Width (checkbox)

•     Saw 1 Yield Length (In) (number; 4 decimals; required)

•     Saw 1 Unit Qty (number; 0 decimals)

•     Saw 2 (drop list of Cut List Subtypes)

•     Saw 2 Misc Prep (text)

•     Saw 2 Multiplier (number; 1 decimals; required)

•     Saw 2 Unit Qty (number; 0 decimals)

•     Saw 3 (drop list of Cut List Subtypes)

•     Saw 3 Misc Prep (text)

•     Saw 3 Unit Qty (number; 0 decimals)

•     Saw 4 (drop list of Cut List Subtypes)

•     Saw 4 Misc Prep (text)

•     Saw 4 Unit Qty (number; 0 decimals)

•     Saw 5 (drop list of Cut List Subtypes)

•     Saw 5 Misc Prep (text)

•     Saw 5 Unit Qty (number; 0 decimals)

•     BF Without Kerf (number; 7 decimals; auto-calculated; read-only)

•     Import ID (number; 0 decimals; hidden & read-only)

•     Sizer Species (Non-Cant) (Depr) (text; hidden & read-only)

•     Optimal Cant Sizes Pipe List (text; auto-calculated; hidden & read-only)

•     Optimal Cant Size (drop list of Cant Sizes; auto-calculated; hidden & read-only)

•     Optimal Kerf % (percentage; 0 decimals; auto-calculated; hidden & read-only)

•     BF With Optimal Kerf (number; 7 decimals; auto-calculated; hidden & read-only)

•     Actual Kerf % (percentage; 0 decimals; auto-calculated; hidden & read-only)

•     BF With Actual Kerf (number; 7 decimals; auto-calculated; hidden & read-only)

–     Flag in Cut List Generator (checkbox)

•     Raw Materials section:

–     Raw Materials; embedded spreadsheet of:

•     Raw Material (drop list of Raw Materials; required)

•     Unit of Measure (drop list of Units Of Measure; auto-calculated; read-only)

•     Entered Amount (number; 2 decimals)

•     Amount (number; 2 decimals; auto-calculated; read-only)

•     Type (drop list of Raw Material Types; auto-calculated; read-only)

•     Setup Cost (number; 2 decimals; auto-calculated; read-only)

•     Cost (Each) (number; 4 decimals; auto-calculated; read-only)

•     Cost (Total) (number; 4 decimals; auto-calculated; read-only)

•     Attachments section:

–     Attachments; embedded spreadsheet of:

•     Key (text; hidden & read-only)

•     Name (text; auto-calculated; read-only)

•     Item (drop list of Items)

•     Notes (text)

•     Date (date; auto-calculated; read-only)

•     DateInternalGMT (date; hidden & read-only)

•     Time (text; auto-calculated; read-only)

•     TimeInternalGMT (number; 0 decimals; hidden & read-only)

•     Download URL (text; auto-calculated; hidden & read-only)

•     Download (report link)

•     Delete URL (text; auto-calculated; hidden & read-only)

•     Delete (report link)

–     Attachment Upload URL (text; auto-calculated; hidden & read-only)

–     Upload Attachment (report link)

  


Development Specification

DO_NOT_REMOVE_ZMM_ISD_ID=935

  


  

