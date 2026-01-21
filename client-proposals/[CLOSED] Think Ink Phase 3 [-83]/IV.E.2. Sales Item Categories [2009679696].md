4.5.2. Sales Item Categories

This is a non-editable simple list used to track Sales Item Categories. It includes the following items: 

  * Device Model 
  * Warranty 
  * 


_EM: Tim Reitz 09/12/2023: Are you good with shipping the whole list and making it all non-editable, or just the basic items?

TODO_JM: Tim Reitz 09/12/2023: Do you want to be able to add your own specialized categories (with just the basic standard fields)?

  


TODO_IDD

  


This list is universal for all users.

  


Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

  


This list will be set up by CCI as part of the main development. If changes need to be made to this list, it will require some coding work.

  


\------------

Categories: 

  * Device Model
  * Warranty
  * Supply (used for both inventory and non-inventory items, with a field to track that)
  * Other Charge



  


  


DONE_JM: Tim Reitz 07/11/2023: Are these still the Sales Items that you / CA uses? 

Tim Reitz 09/19/2023: 

They have the following "Item Types" in CA: 

  * Asset Item: they haven't really been tracking these
  * Discount: they current use this, but maybe not needed in AHZ? 
  * Inventory Item: they want to have this option; they have some, but haven't really been tracking these
  * Non-Inventory Item: they want this one
  * Other Charge: they want this one
  * Sales Tax Item: they current use this, but maybe not needed in AHZ? 
  * Service: 



They also have a lot of "Inventory Groups": 

DONE_IDD: Tim Reitz 09/19/2023: Add a field to the Sales Item record: 

  * Inventory Group (



They also have a Supply Item "Type"

TODO_IDD: Tim Reitz 09/19/2023: This might be a "Subtype" for "Supply" items

  


Tim Reitz 09/12/2023: Should we have one for "Supplies" instead of inventory / non-inventory? (to use for supply sets)? 

TODO_EM: Tim Reitz 09/19/2023: We should probably get you on a call with us and the client sometime soon to discuss the accounting system (specifically here how it handles inventory vs. non-inventory items). 

  


DONE_JM: Do we need Discount, Other Charge, or Sales Tax for the Agreements? 

TODO_IDD4: Tim Reitz 09/19/2023: Everything gets taxed, including Monthly Base Prices and Page Count Overage (**though a school / non-profit can be tax-exempt of course). 

TODO_IDD4: Tim Reitz 09/19/2023: They need to start tracking sales tax for other states / localities. 

TODO_IDD4: Tim Reitz 09/19/2023: On a per-contact basis: should have a field to track whether they are taxable or tax exempt. 

  


TODO_IDD4: Tim Reitz 09/19/2023: No Discount needed on the Agreement level. But yes for the Invoice level (be able to apply a promo to an invoice). 

  


TODO_IDD4: Tim Reitz 09/19/2023: Other Charge: Yes for Invoices.
