
# Matthias Miller - CodeHaus OBD - FB

## Lists

### FB Ad Action Types List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### FB Ad I Ds List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### FB Ad Sets List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### FB Campaign I Ds List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### FB Custom Event Types List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### FB Optimization Goals List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### FB Pixel I Ds List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### FB Time Zones List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

## Records

### FB Account Record

Sections and Fields:

* FB Account section:
  * ID (string; required)
  * Name (text)
  * Time Zone (drop list of FB Time Zones)
  * Sync Cursor (text)

### FB Ad Set Record

Sections and Fields:

* FB Ad Set section:
  * Silverloom ID (autonumber; hidden & read-only)
  * ID (drop list of FB Ad Sets; required)
  * Account ID (drop list of FB Accounts; required)
  * Name (text)
  * Optimization Goal (drop list of FB Optimization Goals)
  * Promoted Pixel ID (drop list of FB Pixel I Ds)
  * Prom. Custom Event Type (drop list of FB Custom Event Types)

### FB Insight Record

Sections and Fields:

* FB Insight section:
  * Silverloom ID (autonumber)
  * Account ID (drop list of FB Accounts; required)
  * Campaign ID (drop list of FB Campaign I Ds; required)
  * Ad Set ID (drop list of FB Ad Sets; required)
  * Ad ID (drop list of FB Ad I Ds; required)
  * Impressions (number; 0 decimals)
  * Clicks (number; 0 decimals)
  * Action; embedded spreadsheet of:
    * Type (drop list of FB Ad Action Types)
    * Value (text)
  * Date (date; required)
  * Conversions (number; 0 decimals)
  * Spend (number; 2 decimals)