
# Matthias Miller - Accounting Loan

## Records

### Loan Record

Sections and Fields:

* Loan section:
  * Name (string)
  * Contact (drop list of Contacts; required)
  * Interest Rate % (percentage; 4 decimals; required)
  * Maturity Date (date; required)
  * Help (formatted text; auto-calculated; read-only)
* Accounting section:
  * Accounting Company (drop list of Accounting Company I Ds; required)
  * Principal Account (drop list of Financial Accounts; required)
  * Interest Account (drop list of Financial Accounts; required)
  * Clearing Account (drop list of Financial Accounts; required)
* Events section:
  * Events; embedded spreadsheet of:
    * Date (date; required)
    * Amount (currency; 2 decimals; required)
    * Interest Adjustment (currency; 2 decimals; auto-calculated; read-only)
    * Principal Adjustment (currency; 2 decimals; auto-calculated; read-only)
    * Principal (currency; 2 decimals; auto-calculated; read-only)
    * Days Balance Held (number; 0 decimals; auto-calculated; read-only)
    * Is Cash Payment (checkbox; auto-calculated; hidden & read-only)
    * Is Disbursement (checkbox; auto-calculated; hidden & read-only)
    * Is Payment In Kind (checkbox; auto-calculated; hidden & read-only)
  * Cached Principal Adj String Table (text; hidden & read-only)