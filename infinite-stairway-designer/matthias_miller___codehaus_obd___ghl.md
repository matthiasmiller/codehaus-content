
# Matthias Miller - CodeHaus OBD - GHL

## Lists

### GHL Call Statuses List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### GHL Custom Field I Ds No Case List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### GHL Lost Reason I Ds No Case List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### GHL Message Directions List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### GHL Message Statuses List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### GHL Message Types List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### GHL Opportunity Statuses List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### GHL Tags List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

## Records

### GHL Location Record

Sections and Fields:

* GHL Location section:
  * Silverloom ID (string; read-only)
  * GHL ID (text)

### GHL Contact Record

Sections and Fields:

* GHL Contact section:
  * Silverloom ID (autonumber; hidden & read-only)
  * Location Silverloom ID (drop list of GHL Locations; required)
  * Date Added (text; required)
  * Assigned To (text)
  * GHL ID (text)
  * Tags; embedded spreadsheet of:
    * Tag (drop list of GHL Tags; required)
  * First Name (text)
  * Last Name (text)
  * Business Name (text)
  * Source (text)

### GHL Message Record

Sections and Fields:

* GHL Message section:
  * Silverloom ID (autonumber; hidden & read-only)
  * GHL ID (text)
  * Message Type (drop list of GHL Message Types)
  * Location Silverloom ID (drop list of GHL Locations)
  * Conversation GHL ID (text)
  * Date Added (text)
  * Direction (drop list of GHL Message Directions)
  * Status (drop list of GHL Message Statuses)
  * Call Duration (Seconds) (number; 0 decimals)
  * Call Status (drop list of GHL Call Statuses)
  * User GHL ID (text)
  * Contact GHL ID (text)

### GHL Opportunity Record

Sections and Fields:

* GHL Opportunity section:
  * Silverloom ID (autonumber; hidden & read-only)
  * GHL ID (text)
  * Contact GHL ID (text)
  * Status (drop list of GHL Opportunity Statuses)
  * Last Status Change At (text)
  * Pipeline GHL ID (text)
  * Pipeline Stage GHL ID (text)
  * Assigned To (text)
  * Created At (text)
  * Location Silverloom ID (drop list of GHL Locations)
  * Monetary Value (number; 2 decimals)
  * Lost Reason ID (No Case) (drop list of GHL Lost Reason I Ds No Case)
  * Custom Fields; embedded spreadsheet of:
    * ID (No Case) (drop list of GHL Custom Field I Ds No Case)
    * Value (text)
  * Name (text)

### GHL Pipeline Record

Sections and Fields:

* GHL Pipeline section:
  * Silverloom ID (autonumber; hidden & read-only)
  * GHL ID (text)
  * Location Silverloom ID (drop list of GHL Locations)
  * Name (text)
  * Stages; embedded spreadsheet of:
    * GHL ID (text)
    * Name (text)

### GHL User Record

Sections and Fields:

* GHL User section:
  * Silverloom ID (autonumber; hidden & read-only)
  * GHL ID (text)
  * First Name (text)
  * Last Name (text)
  * Email (text)
  * Location Silverloom ID (drop list of GHL Locations)

### GHL Conversation Record

Sections and Fields:

* GHL Conversation section:
  * Silverloom ID (autonumber; hidden & read-only)
  * GHL ID (text)
  * Contact GHL ID (text)
  * Location Silverloom ID (drop list of GHL Locations)

### GHL Custom Field Record

Sections and Fields:

* GHL Custom Field section:
  * Silverloom ID (autonumber; read-only)
  * Location Silverloom ID (drop list of GHL Locations; required)
  * GHL ID (No Case) (drop list of GHL Custom Field I Ds No Case; required)
  * Name (text)
  * Key (text)