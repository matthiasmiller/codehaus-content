
# Matthias Miller - CodeHaus OBD - GA

## Lists

### GA Campaigns List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### GA Channel Types List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### GA Time Zones List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

## Records

### GA Account Record

Sections and Fields:

* GA Account section:
  * ID (string)
  * Name (text)
  * Time Zone (drop list of GA Time Zones)
  * Sync Cursor (text)

### GA Campaign Record

Sections and Fields:

* GA Campaign section:
  * Silverloom ID (autonumber; hidden & read-only)
  * ID (drop list of GA Campaigns; required)
  * Account ID (drop list of GA Accounts; required)
  * Name (text)
  * Ad Channel Type (drop list of GA Channel Types)

### GA Metric Record

Sections and Fields:

* GA Metric section:
  * Silverloom ID (autonumber; hidden & read-only)
  * Account ID (drop list of GA Accounts; required)
  * Campaign ID (drop list of GA Campaigns; required)
  * Date (date; required)
  * Impressions (number; 0 decimals)
  * Clicks (number; 0 decimals)
  * Conversions (number; 0 decimals)
  * Cost (Micros) (number; 0 decimals)