6.4. Species List Record

  


Requirements

This is a custom, user-editable list, based on a very simple record, used to track various wood species that are used in the Solution. 

  


The record on which this list is based is extremely simple, and can be accessed via the Solution's Lists interface (no configuration report).

  


Sections and Fields: 

  * Short Code (required; plain text field)



  


Data Access: Visible to and editable for all users

  


Special Considerations: 

  * Copy Record: N/A (disallowed)
  * Delete Record: N/A (disallowed)
  * Merge Record: N/A (disallowed)



  


Other Notes:

  * The following initial Species items are hard-coded and included in the system automatically ("shipped"). These are read-only and cannot be deleted manually in the Solution:  
    * "BE" (for "Beech")
    * "HK" (for "Hickory")
    * "HM" (for "Hard Maple")
    * "POP" (for "Poplar")
    * "RO" (for "Red Oak")
    * "SM" (for "Soft Maple")
    * "WA" (for "Walnut")
    * "WO" (for "White Oak") 
  * Additional items can be added and edited by GemWood via the Solution's Lists interface. 
  * If at some point a more complete Species feature is desired, the optional add-on for the Species configuration record & report can be considered - see corresponding spec.



  


Development Specification

Tim Reitz 01/04/2025: This is a super simple lookup record with no configuration report (users can add items via the Lists UI). We're shipping the initial items, which cannot be edited or deleted.
