7.7. Historical Buildings by Customer Report

  


Requirements

This is a report of all Buildings that are drafts, ordered, owned, or have been owned by a selected customer. 

  


This would be accessed:

  * from the "Customer's Buildings" link on the Customer's contact record 
  * as part of the main Contacts report, the Contact Search, or the Building Search.



  


Title: Historical Buildings by Customer Report

  


Columns: 

  * Building (serial #; link to building record)
  * Item Code 
  * Last Salesperson (salesperson initials)
  * Last Sale Date (mm/dd/yyyy) 
  * Last Sale Price 
  * Last Sale Type (Cash, RTO)
  * Last Delivery Date (mm/dd/yyyy) 



TODO_TR: is this really "Last"? or is if for this customer? 

TODO_TR: Can we just put the building history in the subpane?

  


Grouped by: N/A 

  


Sorted by: Sale Date (sales order for searched customer... 

  


Filters:  

  * Building (serial #; search by partial) 
  * Customer (required; drop list of all Contacts; filter down as you type) 



  


Buttons: 

  * New Building (opens a new Building record defaulted to the selected Contact) 



  


Color Coding: 

  * Current draft, currently ordered and currently owned buildings: Black text, white background
  * Previously owned (repo, trade-in) buildings: Black text, yellow background 
  * Canceled buildings: White text, red background



  


Other Notes:

  


Development Specification

Mockup:[https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1619383528](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1619383528)

Austin Priest 10/22/2021: I'm not sure how to do the filters? Does this need to be it's own tab as well as be in the the contacts report? TODO_TR answer questions

Tim Reitz 04/07/2022: Let's table this for now and plan to pick it up if/when the design picks up again. 

  


Tim Reitz 04/07/2022: Per Matthias, this probably should report on Buildings rather than Sales Orders, in case a customer didn't get a quote, etc.

  


Tim Reitz 04/07/2022: Not sure if the following is relevant any more (if we report on Buildings):

  * Create an index of WOs and SOs by customer. Do something like an NdxConcat on them to get a list of buildings to show. Include draft buildings for the customer.


