
# Matthias Miller - Reddit

## Lists

### Subreddits List

This is a user-editable simple list.

This list is universal for all users, and all users can add to it via the "Advanced | General | Lists" option.

The initial items for this list are to be set up during the initial migration.

## Records

### Reddit Post Record

Sections and Fields:

* Reddit Post section:
  * Silverloom ID (autonumber; hidden & read-only)
  * Reddit ID (text; read-only; required)
  * Title (text; read-only)
  * URL (text; read-only)
  * Subreddit (drop list of Subreddits; read-only)
  * Date (date; read-only)
  * Contents (formatted text; read-only)
* Comments section:
  * Comments; embedded spreadsheet of:
    * ID (text; required)
    * Created UTC (number; 0 decimals; hidden & read-only)
    * Created Date (date; auto-calculated; read-only)
    * Permalink (text)
    * Parent ID (text)
    * Score (number; 0 decimals)
    * Ups (number; 0 decimals)
    * Downs (number; 0 decimals)
    * Author (text)
    * Body (Text) (formatted text; read-only)
* Content Priority section:
  * Priority (number; 0 decimals; read-only)
  * Reason (text; read-only)
* Content Response section:
  * Response Date (date)