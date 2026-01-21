4.2.1.1. Configuring Employee Compensation

  


Requirements

Assist is already tracking the hourly rate and the tier bonus, but not with history. It will no longer track tier rates, and it will start tracking full compensation history, including both owners and employees.

  


Employees may be partially or fully paid from the owner pool. However, owners can never be paid from the employee pool. This means that if an owner works in production, their hourly equivalent is removed from the pool, creating a pool surplus. However, they are still paid from non-pool payroll/owner payroll. This allows the owner to fully replace himself with another employee without a significant impact on the production bonuses of the other employees.

  


The following information will be tracked:

  * Effective Date (required; must be the start of a week)
  * Company (required)
  * Employee Type (required); choice of:
    * Employee
    * Owner
  * Compensation Type (required); choice of:
    * Hourly
    * Salary
  * Salary (visible if Salary; must specify at least ONE salary)
    * Weekly Salary
    * [ ] Enable Time Tracking
  * Hourly (visible if hourly; must specify at least ONE wage)
    * Total Paid Hourly Wage
    * Pool Hourly Wage (defaults to Total Hourly Wage)
    * Guaranteed Hourly Wage
    * Paid Holidays (checkbox)
  * Time Tracking (if hourly or salary using time tracking)
    * Hourly Wage Toward Labor Cost (required and editable if salary using time tracking)
    * Total Paid Production Bonus %
    * Pool Production Bonus %
  * Owner (if owner)
    * Owner % (required)
  * Bonuses
    * Include Transport Bonus



  


This information will be accessible through a button the employee record. It will pop up an embedded spreadsheet with one row per setting, and one column per date. (For developers, this will be a VRG.)

  


You will add a new entry whenever we change ANY of these settings for the employee. Adding a new entry will automatically deactivate the previous settings. (The effective end date is implied.)

  


Salaried employees using time tracking will reduce the production pool based on their calculated hourly compensation. However, they will only be paid a salary (coming from the owner pool/nonpool payroll).

  


The guaranteed wage is calculated BEFORE any discretionary bonuses are paid. This is reflected in the order of the bonuses in the payroll reports. The guaranteed wage does NOT reflect any overtime rate.

  


The Total Paid Production Bonus % determines the bonus the employee is PAID (based on their production hours). For example, an employee receiving 50% bonus will receive half as much as another employee receiving 100% bonus (assuming the same wage and number of hours).

  


The Pool Production Bonus % determines the bonus that is WITHHELD from the pool for the employee. If this percentage is less than the total paid production bonus, part of the employee's bonus will be paid from overhead (non-pool payroll/owner payroll). If this percentage is more than the total, the calculations will withhold more from the pool than is actually paid, resulting in "unspent" money in the production pool.

  


The employee record will include a setting called "Include Transport Bonus". This will automatically include the Transport Bonus on the time cards and on the Production & Payroll Verification Report.

  


NOTE: Editing historical compensation will have unexpected implications. Editing historical entry will require clicking an "Edit Historical Compensation" checkbox for that date. All entries with a current or future effective date will always be editable.

  


Important: The employee compensation settings may significantly change compensation for other employees. It's important to think through ALL implications before adding new employees or changing compensation for existing employees. (This warning will be included in the software.)

  


This covers a number of scenarios:

  * Employees who work part-time in production
  * Summer help
  * New employees (without immediate bonus)
  * Salaried employees in production
  * And more



  


NOTE: Using weekly salaries simplifies rounding issues when trying to match QuickBooks (for accounting purposes), and it simplifies the weekly owner compensation.

  


Development Specification

To reverse-engineer the bonus calculations, see [https://docs.google.com/spreadsheets/d/1YaGy1FMpIYpBkSXxGq87o02H4Rrfg34Xo1E7aStANQ4/edit#gid=0](https://docs.google.com/spreadsheets/d/1YaGy1FMpIYpBkSXxGq87o02H4Rrfg34Xo1E7aStANQ4/edit#gid=0)

  


We don't need to transfer the Comp data when we switch to RGs.

  


  * ContactEmpEffectiveDate -- required, see validation above.
  * ContactEmpCompany -- required
  * ContactEmpCompType -- from unchangeable CompensationTypes list -- required
  * ContactEmpHourlyRate -- visible and required if hourly, 2 decimals
  * ContactEmp%HoursInProd -- defaults to 100, visible and required if hourly
  * ContactEmpIncludeInBonus -- defaults to true
  * ContactEmpHasPaidHolidays -- visible if hourly
  * ContactEmpAnnualSalary -- 0 decimals, commas, visible and required if Salary



  


If we want to explicitly show the end date, we can do so with a macro.

  


Seth Miller 09/22/2021: The fields given in the dev spec are out of date. Use the ones listed in the requirements.

  


Bid: 6 hours
