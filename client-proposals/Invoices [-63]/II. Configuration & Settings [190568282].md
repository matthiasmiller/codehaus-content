2\. Configuration & Settings

  


Requirements

Sagar Sagar 12/17/2022: The system switches are

[ ] System Switches

[ ] Config switches

[ ] ConfigInvoice_IncludeSalesTax

[ ] If this is true we will be able to see Tax field in sales form detail screen, it accesses the InvoiceSalesTaxIncludeOptions list which has options Yes, Conditional, No

[ ] Label: Include Invoice Sales Tax

[ ] Coded in [[PC0072187]]

[ ] Used in following systems

[ ] External\Log City Meats [ZLC]

[ ] External\Weaverland Auto Insurance [ZWA]

[ ] ConfigInvoice_IncludeLineItemDate

[ ] If this is true we will be able to see Date field in sales form Itemization row in detail screen and in exports

[ ] Label: Invoice Includes Line Item Date

[ ] Coded in [[PC0073493]]

[ ] Used in following systems

[ ] External\Weaverland Auto Insurance [ZWA]

[ ] ConfigInvoice_InclLineItemQuantity

[ ] If this is true we will be able to see Quantity field in sales form Itemization row in detail screen and in exports

[ ] Label: Invoice Includes Line Item Quantity

[ ] Coded in [[PC0073493]]

[ ] Used in following systems

[ ] External\Log City Meats [ZLC]

[ ] External\Matthias Miller - Sheds Demo Premium [ZSP]

[ ] External\Quail Manufacturing [ZQM]

[ ] ConfigInvoice_IncludeLineItemCode

[ ] If this is true we will be able to see Code field in sales form Itemization row in detail screen and in exports

[ ] Label: Invoice Includes Line Item Code

[ ] Coded in [[PC0073493]]

[ ] Used in following systems

[ ] External\Log City Meats [ZLC]

[ ] External\Matthias Miller - Sheds Demo Premium [ZSP]

[ ] External\Quail Manufacturing [ZQM]

[ ] ConfigInvoice_UseCodeLookups

[ ] If this is true we will be able to populate items by Code lookup field in sales form Itemization row in detail screen

[ ] Label: Invoice use code lookups

[ ] Coded in [[PC0076133]]

[ ] Used in following systems

[ ] External\Log City Meats [ZLC]

[ ] External\Matthias Miller - Sheds Demo Premium [ZSP]

[ ] External\Quail Manufacturing [ZQM]

[ ] ConfigInvoice_UseMemos

[ ] If this is true we will be able to use and see Notes for Customer and Internal Notes memo fields in sales form in detail screen

[ ] Label: Invoice use customer & internal notes

[ ] Coded in [[PC0077436]]

[ ] Used in following systems

[ ] External\Matthias Miller - Sheds Demo Premium [ZSP]

[ ] ConfigInvoice_MaxDecimals

[ ] This switch specifies the maximum decimal places for the sales form amounts

[ ] Label: Invoice max decimals

[ ] Coded in [[PC0076972]]

[ ] ConfigInvoice_ItemAdditionalColumns

[ ] This switch specifies the additional columns in sales form Itemization table in detail screen

[ ] Label: Invoice Additional Number Columns

[ ] Coded in [[PC0065825]]

[ ] Used in following systems

[ ] External\AppHosting - Management [AHZ]

[ ] External\Log City Meats [ZLC]

[ ] External\Weaverland Auto Insurance [ZWA]

[ ] ConfigInvoice_IncludeTerms

[ ] If this is true we will see the Default Invoice Terms field from AppHosting Settings in sales form detail screen

[ ] Label: Invoice includes terms

[ ] Coded in [[PC0108989]]

[ ] Used in following catalog

[ ] External\AppHosting Invoicing Accounting Link

[ ] ConfigInvoice_IncludePaymentInfo

[ ] This switch specifies if the payment information should be added in invoices

[ ] Label: Invoice includes payment info

[ ] Coded in [[PC0111578]]

[ ] Used in following systems

[ ] External\Log City Meats [ZLC]

[ ] External\Weaverland Auto Insurance [ZWA]

[ ] ConfigSalesForm_SupportEstimates

[ ] This switch specifies if the estimates are supported in sales form

[ ] Label: Sales form supports estimates

[ ] Coded in [[PC0111842]]

[ ] Used in following systems

[ ] External\CodeCrafters - Sample System [E00]

[ ] ConfigInvoice_QuantityHasDP

[ ] If this is true we will see the decimal point in Quantity field in sales form Itemization table

[ ] Label: Invoice item quantity can be fractional

[ ] Coded in [[PC0113998]]

[ ] Used in following systems

[ ] External\CodeCrafters - CodeCrafters Admin [XCC]

[ ] External\Joel Iwashige [XJI]

[ ] External\Log City Meats [ZLC]

[ ] Config_InvoiceShowPONum

[ ] If this is true we will see the purchase order number in invoices

[ ] Label: Show PO number

[ ] Coded in [[PC0114317]]

[ ] Custom switches

[ ] CustomInvoice_ItemLookupDesc

[ ] This switch returns the item description from Code in Itemization table

[ ] Label: Invoice sales item description

[ ] Coded in [[PC0076133]]

[ ] CustomInvoice_ItemLookupDefaultUnits

[ ] This switch returns the item default unit from Code in Itemization table

[ ] Label: Invoice sales item default unit

[ ] Coded in [[PC0076133]]

[ ] CustomInvoice_ItemLookupUnitPrice

[ ] This switch returns the item unit price from Code in Itemization table

[ ] Label: Invoice sales item unit price

[ ] Coded in [[PC0076133]]

[ ] CustomInvoice_ItemShouldPrint

[ ] If this switch is true the invoice line items should be printed in invoice exports

[ ] Label: Invoice Should Print Line

[ ] Coded in [[PC0065825]]

[ ] CustomInvoice_LinePriceLabel

[ ] This switch returns the label of line item price in Itemization table

[ ] Label: Invoice line item price label

[ ] Coded in [[PC0124964]]

[ ] Used in following systems

[ ] External\Weaverland Auto Insurance [ZWA]

[ ] Max switches

[ ] MaxInvoiceNumber

[ ] This switch returns the maximum invoice number

[ ] Label: Maximum invoice number

[ ] Coded in [[PC0100575]]

[ ] MaxEstimateNumber

[ ] This switch returns the maximum estimate number

[ ] Label: Maximum estimate number

[ ] Coded in [[PC0111842]]

  


Sagar Sagar 01/02/2023: If Date, Quantity and Code columns are shown, Description column gets reduced by 10 in widths for each conditional columns. This is happening because we are controlling the dynamic width of Description column with some macros. They are

[ ] LineItemOptionalColumns - determines how many conditional columns should be shown

[ ] LineItemDescWidth1 - Description column but its width is 60, visible when LineItemOptionalColumns is 1

[ ] LineItemDescWidth2 - Description column but its width is 50, visible when LineItemOptionalColumns is 2

[ ] LineItemDescWidth3 - Description column but its width is 40, visible when LineItemOptionalColumns is 3

[ ] LineItemDescWidth4 - Description column but its width is 30, visible when LineItemOptionalColumns is 4

[ ] LineItemDescWidth5 - Description column but its width is 20, visible when LineItemOptionalColumns is 5

Sagar Sagar 01/02/2023: This has been coded in [[PC0073493]] - E00 - Enhancement of Generic Invoicing Module for dynamic columns

  


Development Specification

TODO: Document all config_ and Custom_ options. 

  


Note anything else that stands out that may not be obvious to a user looking at the detail screen (conditionally visible settings, configuration of Type fields, etc).
