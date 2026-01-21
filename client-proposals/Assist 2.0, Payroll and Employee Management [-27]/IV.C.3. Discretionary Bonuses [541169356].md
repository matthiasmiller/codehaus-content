4.3.3. Discretionary Bonuses

  


Requirements

In addition to the production bonuses, Assist will support different types of discretionary bonuses to be given to individual employees. These include the following bonus types:

  * Extra Bonus (enabled for all employees)
  * Transport Bonus (enabled on a per-employee basis)



  


It will also allow adding specific user-configurable additional bonuses, such as the "Christmas Bonus"

  


The time card record will include a new spreadsheet at the bottom for discretionary bonuses:

Type| Amount| Comment  
---|---|---  
  
|   
|   
  
  
|   
|   
  
  
  


The Type  would be a choice of bonus types:

  * Extra
  * Transport



  


Burkholder Management could add additional bonus types.

  


The Amount would be a numeric field allowing two decimals.

  


Every time card would automatically populate to include a row for Extra Bonus. A row for the Transport Bonus would also be added if the setting is enabled for the employee.

  


Rows can be added, deleted, or adjusted as necessary.

  


Development Specification

The reason for choosing Monday as the default bonus date is to avoid potential issues/confusion if they ever choose to switch to a bimonthly pay period.

  


Add the RG:

  * TimeCardBonusType-- required (unchangeable TimeCardBonusTypes list)
  * TimeCardBonusAmount



  


Nate Kilcrease 12/31/2020: Dev Specs include a Weekday and Comment column, so this embedded spreadsheet should be updated.

Matthias Miller 01/15/2021: The client didn't want the weekday.

  


Enhance the x30

Update the x30 from prior step:

  * Add an "Extra Bonus" row with a blank amount.
  * Add "Transport Bonus" if setting is enabled on contact record.



  


Bid: 4 hours
