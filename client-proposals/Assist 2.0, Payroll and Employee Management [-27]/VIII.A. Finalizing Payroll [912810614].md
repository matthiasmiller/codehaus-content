8.1. Finalizing Payroll

  


Requirements

The Finalize Payroll process will:

  * Freeze the Production total in the Pool Production Override
  * Mark all 1099 payouts as non-pending
  * Mark the payroll as being verified



  


The Finalize Payroll will NOT freeze any wages, since wage changes should be entered on the employee with a new effective date.

  


After Assist has received verification for both the Owner (if used) and the Production & Payroll Verification reports, it would:

  * Use the time entries to calculate building labor costs. (Freeze the number.)
  * Send the profitability report to the Company. (This will be completed in a separate module.)
  * Send the payroll information to the accountant.



  


NOTE: If the Owner verification report goes out to multiple people, only one person needs to respond to mark it as verified. We do not need to have multiple people verify. The same is true for the Production & Payroll verification report.

  


Assist will include an option to force a recalculation of prior numbers, as needed. For example, if a building is missed by the verification report, adding it will update the production totals. However, it will not update building costs without a manual recalculation.

  


Development Specification

Nate Kilcrease 01/15/2021: Will this be a separate setting somewhere, or perhaps a popup/warning? What would this look like?

Matthias Miller 01/15/2021: No mockup needed.
