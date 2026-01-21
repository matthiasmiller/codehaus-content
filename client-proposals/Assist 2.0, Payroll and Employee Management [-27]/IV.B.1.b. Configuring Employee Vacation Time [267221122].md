4.2.1.2. Configuring Employee Vacation Time

  


Requirements

Vacation tracking can be enabled on a per employee basis. To enable it, check the "Receives Paid Vacation" checkbox and specify the Accrual Start Date. The Accrual Start Date will be the employees "hire date", except it can be adjusted as necessary for the correct number of vacations.

  


The employee screen will show the calculated number of vacation hours available as of today, based on the Accrual Start Date.

  


Burkholder Management will need to enter the exact date for any employees who've been there fewer than three years. For any employee who's been there longer than three years, they can simply enter any arbitrary date more than three years ago (for example, January 1, 2000).

  


Development Specification

ContactVacationEnabled

ContactVacationAccrualStartDate -- visible and required if ContactVacationEnabled

  


We will provide a ContactVacationAccrualYears macro that will accept an AsOf date and return a fractional number of years from ContactVacationAccrualStartDate. (One example vacation days calculation is 0 hours in the first year, 40 hours in years 2-3, and 80 hours in year 4+.)

  


Bid: 2 hour
