5.2. Hourly Rate Calculations

  


Requirements

The production bonus is calculated as follows.

  


Calculate the total bonus amount for the week.

  * This is 7.5% of production (or as configured on the company) for the total production pool size.
  * Add any labor-intensive production bonuses. 
  * Subtract all production base wages (production hours * daily pool bonus % * pool pay, adjusted for overtime)
  * This is the total bonus that will get paid to employees.



  


Calculate each employee's production bonus equivalent hours.

  * For each day, calculate the number of bonus hours. This is their production hours for the day, multiplied by their production bonus % for the week on the time card.
  * Find the overtime adjustment ratio, which is "Max(1, 1.5 - 20 / Total Hrs)".
  * Calculate the total bonus hours for the week by adding the above.
  * Multiply it by the overtime adjustment ratio to get the Production Bonus Equivalent Hours.



  


Calculate the Production Bonus Equivalent Hours for all employees.

  * Add all the individual equivalent hours for all employees.



  


Calculate each employee's total bonus amount.

  * Find what percentage of the total bonus this employee receives. This is the employee's Production Bonus Equivalent Hours, divided by the Production Bonus Equivalent Hours for all employees.
  * Find the employee's bonus amount by multiplying that percentage by the total bonus amount for all employees for the week (see above).



  


Calculate each employee's hourly bonus.

  * Divide the employee's total bonus by the employee's TOTAL equivalent hours (all working hours, not just production wages).



  


NOTE: The reason for using Equivalent Hours is that it allows an hourly base rate in compliance with IRS overtime requirements, while restricting bonus compensation to the designated pool amount.

  


Development Specification

The formula for the overtime adjustment ratio is:

  * (((Hrs - 40) * 1.5) + 40) / Hrs
  * (1.5H - 20) / H


