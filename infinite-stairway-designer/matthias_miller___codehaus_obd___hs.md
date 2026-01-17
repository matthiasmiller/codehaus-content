
# Matthias Miller - CodeHaus OBD - HS

## Lists

### HS Dispositions List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### HS Hubs List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### HS Time Zones List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

## Records

### HS Call Record

Sections and Fields:

* HS Call section:
  * Silverloom ID (autonumber; hidden & read-only)
  * Hub ID (drop list of HS Hubs; required)
  * Object ID (number; 0 decimals; required)
  * Disposition (drop list of HS Dispositions)
  * Timestamp (text)
  * Duration (number; 0 decimals)
  * Owner ID (number; 0 decimals)
  * Contact ID (number; 0 decimals)
  * Deals; embedded spreadsheet of:
    * Deal ID (number; 0 decimals)

### HS Contact Record

Sections and Fields:

* HS Contact section:
  * Silverloom ID (autonumber; hidden & read-only)
  * Hub ID (drop list of HS Hubs)
  * Create Date/Time (GMT) (text)
  * Owner ID (number; 0 decimals)
  * Object ID (number; 0 decimals)

### HS Deal Record

Sections and Fields:

* HS Deal section:
  * Silverloom ID (autonumber; hidden & read-only)
  * Hub ID (drop list of HS Hubs)
  * Object ID (number; 0 decimals)
  * Contact ID (number; 0 decimals)
  * Closed Won Date/Time GMT (text)

### HS Disposition Record

Sections and Fields:

* HS Disposition section:
  * Silverloom ID (autonumber)
  * ID (drop list of HS Dispositions)
  * Hub ID (drop list of HS Hubs)
  * Label (text)
  * Deleted (checkbox)

### HS Hub Record

Sections and Fields:

* HS Hub section:
  * Silverloom ID (autonumber; hidden & read-only)
  * Hub ID (drop list of HS Hubs)
  * Time Zone (drop list of HS Time Zones)
  * Sync Cursor (text)

### HS Owner Record

Sections and Fields:

* HS Owner section:
  * Silverloom ID (autonumber; hidden & read-only)
  * Hub (drop list of HS Hubs; required)
  * Object ID (number; 0 decimals; required)
  * First Name (text)
  * Last Name (text)
  * Email (text)