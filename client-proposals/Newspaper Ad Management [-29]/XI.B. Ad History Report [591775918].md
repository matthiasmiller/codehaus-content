11.2. Ad History Report

  


Requirements

The Ad History report shows all past run ads for all Customers. This can be opened from the Menu or from the Customer/Ads Page.

  


When opening from the Menu, show all ads for all customers.

  


When opening from Customer/Ads Page, show ads for only that customer.

  


If an ad was run multiple times, there should be a separate line for each time it was run. 

  


Columns:

  * Publication Date
  * Customer (link to Customer/Ads Page; will not have that ad selected)
  * Ad Title
  * Ad Size
  * Ad Color 
  * Special Placement ("location, page number" format)
  * Total Price (total amount paid - including the Ad Price, Multi-Run/Special Discount, Prepay Discount/2% prompt pay discount, and Special Placement Charge as applicable, as well as Late Fees as applicable)
  * Invoice Number
  * Invoice Status
  * Publication (Full Admin only)



  


Filters:

  * Customer (blank = all)
  * Publication Date (default to current; blank = all)
  * Publication (only for Full Admins; list of publications; default to blank = all)



  


Grouping/Sorting: 

  * Group by Publication Date if all; no grouping if only one Publication Date is selected
  * Sort by Customer Name, then Ad Title



  


Development Specification

To calculate the Total Price

  * AD BASE = Calculate a base price for each ad based on the information that's on that invoice (ad price, multi-run/special discount, prepay discount, and special placement charge)
  * For a given ad:
    * INVOICE BASE = Add up the base price for all ads on this invoice
    * AD % = This ad's base / invoice base
    * INVOICE NON-BASE = Sub-total (ignoring credit) - INVOICE BASE
    * AD NON-BASE = INVOICE NON-BASE * AD %
    * Total Price = AD BASE + AD NON-BASE


