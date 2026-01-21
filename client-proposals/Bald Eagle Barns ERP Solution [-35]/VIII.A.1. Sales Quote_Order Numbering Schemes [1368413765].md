8.1.1. Sales Quote/Order Numbering Schemes

  


Requirements

Similar but separate schemes are used for Quotes and Orders:

  * The ID for Sales Quotes will be "SQ-YY-XXXXX" where "YY" is the current year in YY format and "XXXXX" is the autonumber of the quote, based on all quotes.
  * The ID for Sales Orders will be "SO-YY-XXXXX" where "YY" is the current year" and "XXXXX" is the autonumber of the order, based on all orders. 



  


If the autonumber rolls past 5 digits, the ID will automatically include additional digits.

  


The new database will pick up the numbering sequence where the old database leaves off (based on the last numbers on the imported quotes and orders.

DONE_CH: Correct? If yes, how will we do that? 

TODO_TR: See dev spec

DONE_JM: Do they care if we diverge from the above and make it so that the Sales Order uses the same autonumber scheme as the Sales Quote?

Tim Reitz 10/22/2021: Jason said this would be fine. 

DONE_CH: Does it make a difference for us? 

TODO_TR: It makes it simpler for us.

TODO_TR: update spec here accordingly 

  


DONE_CH: will the number advance indefinitely, or do we have to do something special to make it roll over to an additional digit?

TODO_TR: Noted above

  


Development Specification

  * We will need a way to import a SO/SQ autonumber from the old system, and it needs to allow duplicate autonumbers. For example, you might have a SQ with an autonumber of 1, as well as a SO with an autonumber of 1. The ID itself will not be duplicate.


