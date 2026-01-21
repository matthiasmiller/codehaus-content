19.7. Building Profitability Report

This is a report of building profitability, specifically price per square foot for Delivered buildings. This will include new and Trade-In buildings (cash sales and RTO sales), but excluding SRB sales. 

TODO_TR / DONE_CH: run on Sales Orders, Work Orders, and Buildings?

TODO_TR: I think this runs on completed move requests, then we look up the related building information from that. We only include initial moves. Does this sound right? We can look up values by record linking.

  


This would be accessed from a "Building Profitability" link on the __ menu. 

  


Title: Building Profitability

  


Columns: 

  * Building (Serial #, link
  * Building Base $
  * Options $
  * Total Building $
  * Discount $ (if "Include Discounts" is filled)
  * Building Sale $ (if "Include Discounts" is filled)
  * Labor Cost per square foot on the Building Style (look at the piece work base pay) TODO_TR
  * Price Per Sq Ft (Total Building $ / Sq Ft if "Include Discounts" is not filled; Building Sale $ / Sq Ft if "Include Discounts" is filled)



DONE_CH: is this the right way to do it?

TODO_TR: Or, we could have two columns, each one conditionally visible. Then, we could clarify the heading. For example, is Total Building $ the MSRP? If so, can we do MSRP $ / Sq Ft and Sale $ / Sq Ft? It might be nice to differentiate if it's easy.

  * Profit Margin (profit portion of the whole / gross of the whole = profit margin of the whole; total only)



  


Grouped by:

  


Sorted by:

  


Filters:

  * Date (look at Delivery Date) 



TODO_TR: same

  * Building Style (multi-select of all Building Styles; blank = all)
  * Dealer (list of all Dealers; blank = all)
  * Salesperson (list of all Salespeople; if a Dealer is selected, filter to Salespeople under that Dealer; blank = all)
  * Include Discounts (checkbox)
  * 


  


Buttons: 

  


Data Access:
