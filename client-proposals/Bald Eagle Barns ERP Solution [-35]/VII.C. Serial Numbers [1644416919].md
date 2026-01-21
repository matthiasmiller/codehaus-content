7.3. Serial Numbers

  


Requirements

Serial Numbers will be generated automatically when a Work Order is created for a Draft building The Serial Number is the primary reference/identifier for the users (this is what should show up for the links to the building record, etc.). The database will use the internal Building ID as the primary identifier. 

  


Serial Number Format: The Serial Number consists of the following pieces (sample Serial Number: “P1420W042118024R”): 

  * Building Type Code: ("P" = Painted; pulled from the base building SKU) 
  * Building Product ID ("1420W" = 14x20 Workshop; pulled from the base building SKU)
  * Date ("0421" = MMYY; based on the month and year of the date the the Work Order is generated)
  * Building Sequential Number ("18024" = number in all-time building count; pulled from the Building)
  * Option Code ("R" = radiant barrier; derived from the selected Options with Option Codes)
    * The current database only has one option code, but this solution will have capability for more
    * If there are multiple Option Codes for a building, they should be displayed in alphabetical order at the end of the Serial Number
    * If a building has multiple iterations of a given Option for a building, remove duplicate Option Codes so that only one displays per option



  


Starting Point for Sequential Number: The S/N's Building Sequential Number starts/started at 1 and continues from there. After the data migration, this will continue from the place where the prior system left off.

  


Changes to the Serial Number: 

If changes are made to a building that would impact the Serial Number but would not constitute changing the building itself (e.g. changing the Type or adding an Option with an Option Code), the following should apply: 

  * If the changes are made before the building is built (status = Built), the Serial Number should update. 
  * If the changes are made after the building is built, the Serial Number should not update. 



This means the Serial Number should be frozen when the Building status reaches Built. 

  


Admins will be able to edit the serial number after its been built.

  


Note that the Building Sequential Number will NEVER be editable. This will remain constant for the duration of the building. This is because the system will use it as the internal identification number for the building. 

  


Searching by Partial S/N: Currently, BEB's most common method for searching for a building is to use the last 4 characters of the Serial #. But in the new system, when searching by a partial S/N, should search for the entered characters anywhere in the number.

  


*Done.

  


Development Specification

For the starting point of the sequential number in the new system, use a system switch, or continue from existing records. The latter is simple and foolproof for migration, unless we need to run in parallel. Matthias thinks we can add the system switch later if we absolutely have to.
