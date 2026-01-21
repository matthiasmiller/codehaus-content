6.5. Lumber Grades List Record

  


Requirements

This is a custom, user-editable list, based on a very simple record, used to track various lumber grades that are used in the Solution. 

  


The record on which this list is based is extremely simple, and can be accessed via the Solution's Lists interface (no configuration report).

  


Sections and Fields: 

  * Grade Name/Code (required; plain text field)



  


Data Access: Visible to and editable for all users

  


Special Considerations: 

  * Copy Record: N/A (disallowed)
  * Delete Record: N/A (disallowed)
  * Merge Record: N/A (disallowed)



  


Other Notes:

  * The following initial Lumber Grades items are hard-coded and included in the system automatically ("shipped"). These are read-only and cannot be deleted manually in the Solution:  
    * "FAS" (stands for "First and Second"; a plain sawn grade)
    * "F1F" (stands for "One Face"; FAS on one side of the board, with the other side of the board being lower quality; usually priced like FAS but some buyers pay less; a plain sawn grade)
    * "1C" (stands for "1 Common"; highest grade of "common" lumber; a plain sawn grade) 
    * "2C" (stands for "2 Common"; middle grade of "common" lumber; a plain sawn grade) 
    * "3C" (stands for "3 Common"; lowest grade of "common" lumber; a plain sawn grade) 
    * "Rift" (highest-value product on the market)
    * "Quartered" (priced like FAS most of the time)
    * "Rustic" (essentially ungraded lumber with knotty character; pays more than what it would grade as) 
    * "Veneer" (separate grade all by itself) 
  * Additional items can be added and edited by GemWood via the Solution's Lists interface.
  * If at some point a more complete Lumber Grades feature is desired (i.e. with active checkbox, ability to limit certain Grades to certain Buyers, etc.), the optional add-on for the Lumber Grades configuration record & report can be considered - see corresponding spec.



  


Development Specification

Tim Reitz 01/04/2025: This is a super simple lookup record with no configuration report (users can add items via the Lists UI). We're shipping the initial items, which cannot be edited or deleted.
