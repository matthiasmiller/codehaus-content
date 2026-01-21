13.2.6. Invoices

  


Requirements

Overview: The Solution will use the standard AppHosting Invoices module with some customizations. These invoices will be used for invoices generated within the Solution (page counts, base charges, and occasional sales through the Solution), and Classic Accounting would still be used to invoice sales made through there (which would be most or all of the sales of supplies, printers, etc.).

TODO_CH: We need to work through how to keep things separate/combine things with invoicing in CA and AHZ. What if a client gets 2 invoices - one from each, and wants to pay them with one check? The vast majority of the invoices in AHZ would be to managed/recurring customers; the invoices from CA would mainly go to non-managed customers (for included supplies to managed customers, CA generates an invoice, but the customer never sees it - it's only for record keeping) .

Matthias Miller 05/19/2022: Should we be looking to push these to CA?

TODO_CH -- Seems like an invitation for disaster to allow selling random things from AHZ, vs. forcing all non-subscription purchases to be from CA.

  


Accessed via: 

  * New Invoice option in the Invoices section on the Home Menu and on the Invoices report
  * All Invoices report
  * Invoices by Customer report



  


Sections and Fields: 

  * All standard invoice fields, for example:
    * Organization
    * Contact
    * Address
    * Invoice Date
    * Invoice Status
    * Payment Date
    * Due Date
    * PO Number
    * Itemization
    * Discounts & Fees
    * Sub Total
    * Tax
    * Total Amount
    * Invoice Terms (required; drop list; default to what is set for the customer; editable) 



TODO_CH: Is this standard or ZTK-specific? 

Matthias Miller 05/19/2022: We have standard terms. I don't know if it's everything they need.

  * Notes


  * Sales Rep (custom field; required; drop list of Employee OR Sales Rep-type contacts; default to ___ ; editable by admins; __



TODO_JM: default?

TODO_JM: editability?

  


Data Access: All users can view, create, and edit invoices

  


Other Notes:

  * Since this Solution will not use the Accounting module, it will not use the Accounting Transactions section on the Invoice detail screen.



  


  


TODO_IDD: Tim Reitz 04/20/2023: For some customers there are both manual and automatic reporting printers. They'd probably want to wait to bill a client like this until they have all counts. 

  


TODO_TR: (if not done already) Add the following to the User Groups (and update permissions accordingly): 

  * Accounting: Has limited access, mainly only the financial reports



  


  


TODO_IDD: Any Add-On items included with the Device at setup should be included on the initial invoice as separate line items & $0.00 charges

  


TODO_IDD: For the monthly invoice, the total for any Add-On items could just be lumped together (would not need to include line items for the add-ons).

  


TODO_EM: Tim Reitz 07/20/2023: we should make sure that we can link Devices to invoice line items.

Tim Reitz 08/10/2023: This would be for devices that are sold by TI, and also for the initial invoice when setting up a TI-owned managed device

  


TODO_JM: Tim Reitz 09/14/2023: Do you want the invoice to include an extra note for Prepay printers, or just the reduce price?

  


TODO_IDD (Phase 4): Tim Reitz 09/21/2023: Make sure we think through how billing for Agreements will work, how invoices are created, etc.

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=2070326121](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=2070326121)

  


HL Est: 18 Hours 

  * Field - 2 hours
  * Template: 16 hours


