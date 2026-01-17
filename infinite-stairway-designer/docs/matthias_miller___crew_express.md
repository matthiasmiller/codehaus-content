
# Matthias Miller - Crew Express

## Lists

### Allergies To Ignore List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

### Child Genders List

This is a non-editable simple list.

It includes the following items:

* Boy
* Girl

This list is universal for all users.

Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

This list will be set up as part of the main development. If changes need to be made to this list, it will require some coding work.

### Station Times List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

## Records

### Child Record

Sections and Fields:

* Child section:
  * Desc (string; read-only)
  * Parent / Caregiver (drop list of Contacts; required)
  * First Name (text; required)
  * Last Name (text)
  * Age (number; 0 decimals; required)
  * Gender (drop list of Child Genders)
  * Allergies (formatted text)
  * Crew (drop list of Crews; hidden & read-only)
  * Crew (text; auto-calculated)
  * Checkins; embedded spreadsheet of:
    * Date (date; required)
    * User (drop list of User Profiles; read-only)
  * Check In Today (checkbox; auto-calculated)
  * Full Name (text; auto-calculated; hidden & read-only)
  * Parent Import ID (number; 0 decimals; hidden & read-only)

### Crew Record

Sections and Fields:

* Crew section:
  * Number (string)
  * Minimum Age (number; 0 decimals)
  * Maximum Age (number; 0 decimals)
  * Maximum Children (number; 0 decimals)
  * Dismissal Group (number; 0 decimals)
  * Required Gender (drop list of Child Genders)

### Station Record

Sections and Fields:

* Station section:
  * Name (string)
  * Schedule; embedded spreadsheet of:
    * Time (drop list of Station Times; required)
    * Starting Crew (drop list of Crews; required)
    * Ending Crew (drop list of Crews; required)
  * Show Allergies on Schedule (checkbox)