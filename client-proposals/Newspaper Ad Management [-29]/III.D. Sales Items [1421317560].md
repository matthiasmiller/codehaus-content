3.4. Sales Items

  


Requirements

The AppHosting Sales Items feature will be included, with significant customization, to handle configuration of Ad Sizes (and possibly Column Inch ads in the future), Customer Discounts, Prepay Discounts, and Special Placement Charges.

  


Sales Items will be linked to individual publications and the Sales Items codes will include the Publication Code as a suffix.

  


Development Specification

Sales Items Categories: The SalesItemCategoryList should include the following Investortools-owned items: 

  * Ad Sizes
  * Customer Discounts
  * Prepay Discounts
  * Other



  


Data Restrictions for all Sales Items:

  * Full Admins: Full access
  * Publication Admins: Full access for assigned publication
  * Standard Users: View only 



  


Note on some standard Sales Items fields: Ads are not taxable, so we do not need the Taxable checkbox from the standard Sales Item record. We also do not need the Income Account.

  


Ellis Miller 04/20/2021: 

  


Add restriction.

Prepopulate category list.

Add publication field.

Maybe auto-append suffix?

Maybe add a Config_ setting to always hide "Taxable?"

  


TODO_CH: Presumably we need a SalesItemPublication field that is set by OnInit and editable only when allowed (similar to UserPublication).

  


TODO_CH: Do we need to auto-add the suffix to the sales code if it isn't there?

  


1.5 days.
