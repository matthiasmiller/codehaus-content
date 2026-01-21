3.2.5.3. Sales Order Accounting Impact

  


Requirements

The Sales Order's "Sale Date" will become "Order Date"

  


The Sales Order will now have an SO Invoice Date. This will be populated historically based on this logic:

  


  * Sales Order With Retail Building - Building Delivery Date
  * Sales Order With Wholesale SDI Building - Mark - is this the same as below?
  * Sales Order With Wholesale Non-SDI Building - Day After Building Build Date
  * Sales Order Without Building - Sales Order Creation Date



  


"Invoicing" is not an action for sales orders.

  * The Q prefix is used for Quote
  * The R prefix is used for Sales Orders (prior to invoicing)
  * The N prefix is used for Invoices (upon invoicing)



  


The Sales Order template will show "Est. Tax" on the sales order before it's invoiced. After it's invoiced, it will show "Tax."

  


Create a "Sales Orders Needing Invoicing" report. Columns:

  * Sales Order ID
  * Building Built Date
  * Building Size and Description
  * Shipping Name
  * Building Delivery Date
  * Sales Order Total
  * Checkbox - i.e. [    ]



Prompt:

  * District



Buttons

  * Invoice Selected SOs
  * Flyout option on a per-row basis to "Override Invoice Date"



  


Sales Order Impact

This report is the same as the "Building Accounting Impact", except that it works from a sales order. The mapping will be based on the building's district.

  


NOTE:

  * For cancelations, anything PRIOR to cancelation gets pushed into accounting. Anything after does NOT.



  


TIMELINE| InternalEvent Name| Expected Debit| Expected Credit  
---|---|---|---  
Payments Before Invoice|   
|   
|   
  
Undeposited Funds| Sales Order Paid| Sales Order: Payment Totals (Account Based on Payment Type)|   
  
Customer Deposits| Sales Order Paid|   
| Sales Order: Payment Totals (Account Based on Payment Type) - if paid prior to sale  
  
|   
|   
|   
  
Sales Order "Invoiced"|   
|   
|   
  
Assets|   
|   
|   
  
Accounts Receivable| Sales Order Invoiced| Sales Order: Total minus Payments Made Prior to Sale|   
  
FGI Raw Materials| Sales Order Invoiced|   
| Additional Raw Materials Cost  
  
|   
|   
|   
  
Liabilities|   
|   
|   
  
Customer Deposits| Sales Order Invoiced| Sales Order: Payment Totals (Account Based on Payment Type) - if paid prior to sale|   
  
Sales Tax Liability| Sales Order Invoiced|   
| Sales Tax Amount  
  
|   
|   
|   
  
Income|   
|   
|   
  
Accessory Income Account| Sales Order Invoiced|   
| Total of Accessories, based on assigned account. If an accessory doesn't have an account, it gets assigned to Building Income  
Building Income Account| Sales Order Invoiced|   
| Sales Order: Subtotal + Discounts  
Shipping Income Account| Sales Order Invoiced|   
| Shipping  
Discounts| Sales Order Invoiced| Sales Order: Discounts|   
  
  
|   
|   
|   
  
Expenses|   
|   
|   
  
Raw Materials COGs| Sales Order Invoiced|   
| Additional Raw Materials Cost  
  
|   
|   
|   
  
Payment After Invoice|   
|   
|   
  
Undeposited Funds| Sales Order Paid| Sales Order: Payment Totals - Fees (Account Based on Payment Type)|   
  
Accounts Receivable| Sales Order Paid|   
| Sales Order: Payment Total  
Payment Fee| Sales Order Paid| Sales Order: Payment Fee (Account Based on Payment Type)|   
  
  
  


  


Development Specification

TODO_CCI: Confirm that we can use a Bill Pay linking to pay for sales tax liabilities.

  


Niccolas Miller 04/25/2023: [[PC0153598]] - ZFP - FGI: Sales Order Accounting Impact (T&M)
