6.4. Item Records

Overview: This is to track items.

  


Accessed via: Home | Items | Items

  


Sections and Fields: 

  


  * General section:
    * Code (string)
    * Customer (drop list of Contacts; required)
    * Desc (text)
    * Notes (text)
    * Board Feet (number; 7 decimals; read-only)
    * Hand Fasteners (number; 0 decimals; read-only)
    * Machine Fasteners (number; 0 decimals; read-only)
    * Parts (number; 0 decimals; read-only)
    * Assembly Method (drop list of AssemblyMethods)
    * Price (number; 2 decimals; read-only)
  * Lumber section:
    * Lumber; embedded spreadsheet of:
      * Quantity (number; 0 decimals; required)
      * Dimensions (text; read-only)
      * Thickness (In) (number; 4 decimals; required)
      * Width (In) (number; 4 decimals; required)
      * Length (In) (number; 4 decimals; required)
      * Raw Material INFO (Gangsaw & Scrag) (text)
      * Raw Material INFO (Sawing) (text)
      * Misc Prep (text)
      * Brewer (checkbox)
      * Keystone (checkbox)
      * Scalpy Hollow (checkbox)
      * Saw 1 (drop list of SawingEquipment)
      * Saw 2 (drop list of SawingEquipment)
      * Saw 3 (drop list of SawingEquipment)
      * Saw 4 (drop list of SawingEquipment)
      * Saw 5 (drop list of SawingEquipment)
      * Total BD FT (number; 7 decimals; read-only)
      * Import ID (number; 0 decimals; hidden & read-only)
  * Fasteners section:
    * Fasteners; embedded spreadsheet of:
      * Stored Fastener (drop list of Fasteners; hidden & read-only)
      * Fastener (text; required)
      * Amount (number; 0 decimals; required)
      * Type (text; read-only)



  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Other Notes: 

  * NA


