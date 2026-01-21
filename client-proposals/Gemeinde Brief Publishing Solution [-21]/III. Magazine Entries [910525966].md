3\. Magazine Entries

  


Requirements

We will have multiple magazine entry types associated with a publication date. Many (but not all) of them will be associated with a church.

  


All of these have:

  * Entry Type
  * Publication Date
  * Number of times run (default based on type).
  * End Date (based on Publication Date and number of times to run).
  * Needs Followup checkbox
  * Show a warning message if any fields are empty
  * Created By ______ on Date/Time
  * Modified By ______ on Date/Time
  * Export Section (Late Reports for late church reports; otherwise, entry type)
  * Export Preview (demonstrating how it will be published)



  


Here are the types and fields of magazine entries:

  * Church
    * Last Church (This should auto-fill from the Next Church for the same church from the prior publication date.)
    * Next Church
    * Visiting Minister
    * Visitors
    * Notes
    * Late (checkbox)
    * Church Date (visible if late)
  * Obituaries
    * Associated Church #
    * Name
    * Obituary
    * Preview
    * Template should include church number.
  * Births
    * Correction?
    * Last Name
    * Parent Names (and Previous Value text field if correction)
    * Birth Date (and Previous Value text field if correction)
    * Child Name (and Previous Value text field if correction)
    * Grandparents (and Previous Value text field if correction)
    * Preview
  * Birthdays
    * Text
  * Showers
    * Text
  * Accidents & Fire
    * Associated Church #
    * Text
    * NOTE: The template should have the church number
  * Marriages
    * Associated Church #
    * Last Names and Husband
    * Husband Parents
    * Wife First Name
    * Wife Parents
    * Date
    * Bishop
    * Notes
    * NOTE: The bold formatting to match the template..
  * Ordinations
    * Associated Church #
    * Name
    * Text
  * Notices
    * Type (free-form text) -- warning if it's not filled
    * Text
  * This & That
    * Associated Church #
    * Text
  * Lost & Found
    * Type (free-form text)
    * Text
  * Newlywed Addresses (renamed from New Addresses)
    * Associated Church #
    * Name
    * Address
    * Template -- make the names bold
  * Addresses
    * Associated Church #
    * Correction checkbox?
    * Name
    * Text
    * Template -- the name should be bold here as well.
  * Published
    * Associated Church #
    * Last Names and Man's First Name
    * Man's Parents
    * Woman's First Name
    * Woman's Parents
    * Date
    * Notes
    * NOTE: The bold formatting to match the template..
  * Funds
    * Fund Name
    * Fund Reason
    * Fund Payment
    * Run these 6 times by default.
  * Poems
    * Text
  * Late Reports
    * This section will be used for late Church reports
  * This & That
    * Associated Church #
    * Name
    * Text
    * Example: 14\. Henry Fisher, This and That Text.
  * Classified Ads
    * Start Date
    * Title
    * Text
    * Phone Number
    * Run these multiple times. Editable.
    * Payment Type; list of:
      * Cash
      * Check
      * Credit Card
    * Check Number



  


Development Specification

Ellis Miller 07/21/2020: 

  


PubEntryType record

  * ShowChurchNum
  * DefaultTimesRun - number
  * Template - expression field that uses #expr# at the Publication level



  


Publication Record

  * Common fields include PubAssocChurch
  * Layout of all fields from top to bottom
  * Template Output: uses Evaluate on the appropriate expression



  


Matthias Miller 07/21/2020: If it's easy to add a New Entry link to the top of the entry detail screen (perhaps with a SaveAndExitEditMode), they may be interested in it.
