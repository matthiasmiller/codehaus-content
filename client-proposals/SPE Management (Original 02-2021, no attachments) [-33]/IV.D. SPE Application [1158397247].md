4.4. SPE Application

  


Requirements

The SPE Application will track:

  * Name - This would be an auto-generated and read-only name, such as "SPE II - 2020, Year 2 of 2 - $150,000". This name will automatically be assigned/updated when saving the application. It will be used when selecting  the application for the SPE.
  * SPE (required; list of SPEs; links back to SPE)
  * Year # (required)
    * Year 1 of 2 (Initial)
    * Year 1 of 2 (Renewal)
    * Year 2 of 2
  * Application Date (required); choice of:
    * May 15 (normally the default)
    * July 1 (default if the Year # is "Year 1 of 2 (Initial)")
  * Application Year (required; calendar year)
  * Application Amount (required)
  * Application Number (warn on save if missing after application date is entered)
  * Application Status (automatic and read-only; Approved if an approval date is specified; Pending until June 30 of the year following the application year; otherwise, Denied):
    * Pending
    * Approved
    * Denied
  * Approval Date (entered from the state approval letter)
  * Approved Amount (required if approval date is specified; may be less than the application amount)5
  * Tax Year (editable; default to the calendar year of the approval date)
  * Receipt Submitted Due Date (defaults to using the approval date and the setting # of Days Until SPE Receipt Due; can be overridden)
  * Receipt Submitted Actual Date (warn on save if missing after the due date)



  


It will include an embedded spreadsheet to track disbursements. These will be entered manually. They will include the following columns:

  * Payee (list of Scholarship Organizations; required)
  * Check Number (required)
  * Date (required)
  * Amount (required)



  


Show a read-only Total Disbursements underneath the embedded spreadsheet's Amount column.

  


Show a read-only Funded checkbox. The application would be considered to be funded when the total disbursements equal the totals for all admitted member applications (being sure to appropriately handle SPE applications when both numbers are still zero).

  


It will include the following report links:

  * View Other SPE Applications
  * Admitted Members



  


Warn if the total disbursement amounts do not match the total contributions for that tax year and application (including held funds) for any entered Scholarship Organizations.

  


Warn if the year of the disbursement check date does not match the tax year.

  


Note that the approval amount may be less than the application amount.

  


Development Specification

Ellis Miller 02/08/2021: 

[ ] Lookup record

  


  


Target: 5 Days
