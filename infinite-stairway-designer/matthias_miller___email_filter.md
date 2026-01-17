
# Matthias Miller - Email Filter

## Lists

### Email Filter Body Phrases List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### Email Filter Msg Types List

This is a non-editable simple list.

It includes the following items:

* Message
* Subscription
* List
* Calendar

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

## Records

### Email Filter Record

Sections and Fields:

* Email Filter section:
  * ID (autonumber; read-only)
  * Notes (text)
* Match section:
  * Priority (drop list of High Med Low; required)
  * Type (drop list of Email Filter Msg Types; required)
  * From (text)
  * List ID (text; sometimes required)
  * Include To (text)
  * Exclude To (text)
  * Subject (text)
  * Body (drop list of Email Filter Body Phrases)
* Action section:
  * Skip Inbox (checkbox)
  * Label (drop list of Email Filter Msg Labels; sometimes required)
  * Mark Read (checkbox; auto-calculated)
  * Mark Read (checkbox; hidden & read-only)

### Email Filter Msg Label Record

Sections and Fields:

* Email Filter Msg Label section:
  * Name (string)
  * Mark Read (checkbox)