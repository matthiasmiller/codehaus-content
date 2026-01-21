6.1.5. Stored Calculations

  


Requirements

Rather than calculating labor costs on demand, Assist will store these calculations to allow faster reporting and to allow changing the pricing model without affecting prior history.

  


This will still allow full control to slice and dice our profitability numbers for comparisons and reporting.

  


These calculations will automatically be stored once the Production & Payroll Verification Report has been confirmed by the production manager.

  


Development Specification

Whenever we archive old entries, we need to be sure to add blank entries as needed.

Building RG:

  * Station (list)
  * Employee (list)
  * Date
  * Time
    * Start Time
    * End Time
    * Number of Builders
    * Stored Breaks (amount of time in the Start/End time that overlaps with breaks)
    * Total Hours (auto-calculated using start and end time, excluding breaks)
  * Rates:
    * Stored Hourly Base RateStation
    * Hourly Pool Bonus Rate (auto-calculated by taking the total pool multiplied by this time slot's % of total hours)
  * Base Labor Cost (auto-calculated)



  


On the main detail screen, show:

  * Base labor cost
  * Production bonus
  * Total production cost 



  


Nightly Process

We would have an automated process (nightly x30) that would move these into individual rows into an RG on the building.

  


It would also turn all historical owner expenses on the company record as not pending.

  


Weekly Process

My thought with this is that we have a "Calculate Labor Costs" that

  


Some notes:

  * For station and employee tracking, we will need to go back to the prior week and update numbers based on the overtime pay. Matthias Miller 11/08/2021: I think this is irrelevant because we enter this stuff on a weekly basis.
  * For ShedTime, calculate the adjusted hours when the production hours are within X% (10?) of the worked hours OR it's been longer than X days (both of these controlled via system switches) Matthias Miller 11/08/2021: Same as above. I think this is irrelevant.
  * Any time that you enter new production times for a given date, you need to recalculate the adjusted hours for that date. (This might happen if there was a little bit of work done framing a new building---any time when using station tracking, or if the prior buildings were within the acceptable threshhold for per-employee, ...) Matthias Miller 11/08/2021: Same as above.


