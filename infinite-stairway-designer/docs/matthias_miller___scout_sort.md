
# Matthias Miller - Scout Sort

## Lists

### Scout Data Types List

This is a non-editable simple list.

It includes the following items:

* Boolean
* Date
* List
* Number
* String

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

### Scout Rule Booleans List

This is a non-editable simple list.

It includes the following items:

* is / does
* isn't / doesn't

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

### Scout Rule Conditions List

This is a non-editable simple list.

It includes the following items:

* equal*
* contain*
* start with*
* end with*
* greater than
* greater than or equal to
* less than
* less than or equal to
* empty

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

### Scout Rule Priorities List

This is a non-editable simple list.

It includes the following items:

* 1. Check First (Before Anything Else)
* 2. Check Early (Before Most Rules)
* 3. Normal Rule
* 4. Check Late (After Most Rules)
* 5. Check Last (After Anything Else)

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

## Records

### Scout Record Type Record

Sections and Fields:

* Scout Record Type section:
  * Name (string)

### Scout Rule Record

Sections and Fields:

* Scout Rule section:
  * ID (autonumber; hidden & read-only)
  * Record Type (drop list of Scout Record Types; required)
  * Specificity (number; 2 decimals; read-only)
* Rules section:
  * When to Check (drop list of Scout Rule Priorities; required)
  * Rules; embedded spreadsheet of:
    * Field Name (drop list of Scout Fields; required)
    * Boolean (drop list of Scout Rule Booleans; required)
    * Condition (drop list of Scout Rule Conditions; required)
    * Stored Value (text)
    * Display Value (text; auto-calculated)
    * Specificity (number; 2 decimals; hidden & read-only)
  * Note (text; auto-calculated; read-only)
  * Matching Records (report link)
* Actions section:
  * Actions; embedded spreadsheet of:
    * Field Name (drop list of Scout Fields; required)
    * Stored Value (text)
    * Display Value (text; auto-calculated)

### Scout Record Record

Sections and Fields:

* Scout Record section:
  * Record Type (drop list of Scout Record Types; required)
  * ID (autonumber; hidden & read-only)
* Fields section:
  * Fields; embedded spreadsheet of:
    * Name (drop list of Scout Fields; required)
    * Current Stored Value (text; auto-calculated; read-only)
    * Original Stored Value (text; read-only)
    * Original Disp. Value (text; auto-calculated; read-only)
    * Modify Value (checkbox)
    * Modified Stored Value (text)
    * Modified Disp. Value (text; auto-calculated)
    * Current Disp. Value (text; auto-calculated; read-only)
* Rules section:
  * Apply Rule (checkbox; auto-calculated)
  * Save Record Label (text; auto-calculated; read-only)
  * Applied Rule ID (number; 0 decimals)
  * Pending Rule String Table (text; hidden & read-only)
  * Pending Rule Field Names (text; auto-calculated; hidden & read-only)
  * View Rules (report link)

### Scout Field Record

Sections and Fields:

* Scout Field section:
  * Desc (string; read-only)
  * Calc Desc (text; auto-calculated; hidden & read-only)
  * Record Type (drop list of Scout Record Types; required)
  * Name (text; required)
  * Required (checkbox)
* Data Type section:
  * Data Type (drop list of Scout Data Types; required)
  * Advanced List Options (checkbox)
  * Keys & Values String Table (Expression) (user-entered expression; required)
  * List Items (Multi-Line) (text; auto-calculated)
  * Has Helper List (checkbox; auto-calculated; hidden & read-only)
  * Helper List (String Table) (text; auto-calculated; hidden & read-only)
  * Helper List (Keys) (text; auto-calculated; hidden & read-only)
  * Helper List (Values) (text; auto-calculated; hidden & read-only)
* Usage section:
  * Allow Matching This Field (checkbox)
  * Allow Setting This Field (checkbox)