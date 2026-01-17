
# Strasburg Pallet - Time Sheets

## Records

### Time Sheet Record

Sections and Fields:

* Time Sheet section:
  * Silverloom ID (autonumber; hidden & read-only)
  * Employee (drop list of Contacts; required)
  * View All Employees (checkbox)
  * Date (date; required)
  * Total Sawing Time (Seconds) (number; 0 decimals; auto-calculated; hidden & read-only)
  * Total Sawing Time (Hrs) (number; 2 decimals; auto-calculated; read-only)
* Entries section:
  * Start of Day (Internal) (number; 0 decimals; auto-calculated; hidden & read-only)
  * Start of Day (text; auto-calculated; read-only)
  * Entries; embedded spreadsheet of:
    * Cut List Subtype (drop list of Cut List Subtypes; hidden & read-only)
    * Category (drop list of Time Sheet Categories; hidden & read-only)
    * Start Time (Internal) (number; 0 decimals; hidden & read-only; required)
    * End Time (Internal) (number; 0 decimals; auto-calculated; hidden & read-only)
    * Type (text; auto-calculated; required)
    * Start Time (text; auto-calculated; required)
    * End Time (text; auto-calculated; read-only)
    * Break Time (Seconds) (number; 0 decimals; auto-calculated; hidden & read-only)
    * Break Time (Mins) (number; 0 decimals; auto-calculated; read-only)
    * Sawing Time (Seconds) (number; 0 decimals; auto-calculated; hidden & read-only)
    * Sawing Time (Hrs) (number; 2 decimals; auto-calculated; read-only)
  * End of Day (Internal) (number; 0 decimals; hidden & read-only)
  * End of Day (text; auto-calculated; required)
* Breaks section:
  * Breaks; embedded spreadsheet of:
    * Start Time (Internal) (number; 0 decimals; hidden & read-only)
    * End Time (Internal) (number; 0 decimals; hidden & read-only)
    * Start Time (text; auto-calculated)
    * End Time (text; auto-calculated; required)

### Time Sheet Category Record

Sections and Fields:

* Time Sheet Category section:
  * Name (string)
  * Active (checkbox)