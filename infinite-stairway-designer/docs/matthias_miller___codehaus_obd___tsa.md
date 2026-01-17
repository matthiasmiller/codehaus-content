
# Matthias Miller - CodeHaus OBD - TSA

## Lists

### TSA Product Build I Ds List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### TSA Order Statuses List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### TSA Order Types List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### TSA Purchase Methods List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

## Records

### TSA Domain Record

Sections and Fields:

* TSA Domain section:
  * Domain (string)
  * Email (text)
  * Sync Cursor (text)

### TSA Order Record

Sections and Fields:

* TSA Order section:
  * Silverloom ID (autonumber)
  * TSA Domain (drop list of TSA Domains)
  * TSA ID (number; 0 decimals)
  * Promised By Date (text)
  * Submitted At (text)
  * Processed At (text)
  * Salesperson TSA ID (number; 0 decimals)
  * Total Order Amount (number; 2 decimals)
  * Product Build ID (drop list of TSA Product Build I Ds)
  * Product TSA ID (number; 0 decimals)
  * Fulfilled At (text)
  * Store TSA ID (number; 0 decimals)
  * Bill To Phone (phone)
  * Bill To Email (email)
  * Ship To Phone (phone)
  * Ship To Email (email)
  * Updated At (text)
  * Order Status ID (drop list of TSA Order Statuses)
  * Delivery Scheduled Date (text)
  * Delivery Completed Date (text)
  * Type (drop list of TSA Order Types)
  * Purchase Method (drop list of TSA Purchase Methods)

### TSA Product Record

Sections and Fields:

* TSA Product section:
  * Silverloom ID (autonumber; hidden & read-only)
  * TSA Domain (drop list of TSA Domains)
  * TSA ID (number; 0 decimals)
  * Serial Number (text)

### TSA User Record

Sections and Fields:

* TSA User section:
  * Silverloom ID (autonumber; hidden & read-only)
  * TSA Domain (drop list of TSA Domains)
  * TSA ID (number; 0 decimals)
  * First Name (text)
  * Last Name (text)
  * Email (text)
  * Archived (checkbox)
* Stores section:
  * Stores; embedded spreadsheet of:
    * Store TSA ID (number; 0 decimals; required)

### TSA Store Record

Sections and Fields:

* TSA Store section:
  * Silverloom ID (autonumber; hidden & read-only)
  * TSA Domain (drop list of TSA Domains)
  * TSA ID (number; 0 decimals)
  * Business Name (text)