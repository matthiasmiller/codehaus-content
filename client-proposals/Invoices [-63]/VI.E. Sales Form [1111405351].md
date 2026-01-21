6.5. Sales Form

Sagar Sagar 12/18/2022: Previously we had invoicing module coded in [[PC0072187]] - E00 - Generic Invoicing Module. When time came we realized that we need to step one back and modify the module so that it become general sales form. So we converted invoicing module into sales module. Now our sales form can be divided into two categories. One is Estimate and another one is Invoice.

  


Sagar Sagar 12/18/2022: The fields of Invoice are given below

[ ] Fields

[ ] Label - "This invoice was copied from invoice number <Invoice Number>.", if the invoice is copied from another invoice.

[ ] Convert to Estimate - on change button to convert the invoice into an estimate

[ ] Invoice # <Invoice Number> \- section

[ ] Organization - list of legacy organizations, visible if Config_UseLegacyOrganizations is True

[ ] Contact - list of contacts

[ ] Choice report button for Addresses

Sagar Sagar 01/05/2023: Multiple address feature and the choice report button has been added in [[PC0076638]] - E00 - Allow Choosing from Contact's Multiple Addresses in Invoice

[ ] Address - line 1

[ ] Address - line 2

[ ] City

[ ] State - list of states

[ ] Zip

[ ] Country - list of countries

[ ] Invoice Date

[ ] Status - list of InvoiceStatusList, items are

[ ] Canceled

[ ] Draft

[ ] Invoiced

[ ] Paid

[ ] Payment Date

[ ] Ship to Separate Address

[ ] Choice report button for Addresses - for separate address

[ ] Address - line 1

[ ] Address - line 2

[ ] City

[ ] State - list of states

[ ] Zip

[ ] Country - list of countries

Sagar Sagar 01/05/2023: Canadian addresses were made supported sales form addresses in [[PC0077498]] - Addresses: Better support Canadian provinces

[ ] PO Number - visible if Config_InvoiceShowPONum is True and sales form is Invoice

Sagar Sagar 01/10/2023: The field was added in [[PC0114317]] - Accounting: Adding PO Num to Invoices

[ ] Itemization - section

[ ] Itemization table

[ ] Date

[ ] Quantity

[ ] Code

[ ] Product / Sales Items choice report button

Sagar Sagar 01/05/2023: This button has been added in [[PC0077257]] - E00 - Add Choice Report for Sales Items

[ ] Description

[ ] Taxable - checkbox

Sagar Sagar 01/08/2023: The field was coded in [[PC0078443]] - E00 - Invoices: Add "Taxable?" to Sales Items and Invoices

[ ] Unit Price

[ ] Price

[ ] Label - "To edit line items, the status must be changed back to 'Draft'. visible if status is not Draft

[ ] Late Fee - child detail button for late fee

[ ] Sub Total

[ ] Tax

[ ] Sub Total (After Tax)

[ ] Late Fee %

[ ] Late Fee Amount * - *Sales tax is not charged on late fees.

[ ] Total Invoiced

[ ] Sub Total

[ ] Tax - percentage field

Sagar Sagar 01/05/2023: The tax percentage was added in [[PC0077028]] - E00 - Invoices: Support Tax Percentages

[ ] Late Fee

[ ] Total Amount

[ ] Terms - expression field from AppHosting Settings

[ ] Override Terms - checkbox

[ ] View Invoice

[ ] Template - list of invoice templates, visible if the list has more than one items of templates

Sagar Sagar 01/02/2023: This has been coded in [[PC0074177]] - AHZ - Multiple invoice templates to choose from for export

[ ] View as PDF - button to export the invoice as pdf

Sagar Sagar 12/21/2022: Added in [[PC0072187]] - E00 - Generic Invoicing Module

[ ] View in Word - button to export the invoice as rich text format

Sagar Sagar 12/21/2022: Added in [[PC0072187]] - E00 - Generic Invoicing Module

[ ] Notes for Customer - section

[ ] Note - memo

[ ] Internal Notes - section

[ ] Note - memo

[ ] Modification History - link to track activity

  


Sagar Sagar 12/20/2022: The invoices detail screen was added in [[PC0072187]] - E00 - Generic Invoicing Module.

  


Sagar Sagar 12/18/2022: The Estimate have been coded from invoicing in [[PC0111842]] - Support Estimates in our Invoicing module. The fields of Estimate are given below

[ ] Fields

[ ] Label - "This estimate was copied from estimate number <Estimate Number>.", if the estimate is copied from another estimate.

[ ] Convert to Invoice - on change button to convert the estimate into an invoice

[ ] Estimate # <Estimate Number> \- section

[ ] Organization - list of legacy organizations, visible if Config_UseLegacyOrganizations is True

[ ] Contact - list of contacts

[ ] Choice report button for Addresses

[ ] Address - line 1

[ ] Address - line 2

[ ] City

[ ] State - list of states

[ ] Zip

[ ] Country - list of countries

[ ] Estimate Date

[ ] Itemization - section

[ ] Itemization table

[ ] Date

[ ] Quantity

[ ] Code

[ ] Product / Sales Items choice report button

[ ] Description

[ ] Taxable - checkbox

[ ] Unit Price

[ ] Price

[ ] Late Fee - child detail button for late fee

[ ] Sub Total

[ ] Tax

[ ] Sub Total (After Tax)

[ ] Late Fee %

[ ] Late Fee Amount * - *Sales tax is not charged on late fees.

[ ] Total Invoiced

[ ] Sub Total

[ ] Tax - percentage field

[ ] Late Fee

[ ] Total Amount

[ ] Terms - expression field from AppHosting Settings

[ ] Override Terms - checkbox

[ ] View Estimate

[ ] Template - list of estimate templates, visible if the list has more than one items of templates

[ ] View as PDF - button to export the estimate as pdf

[ ] View in Word - button to export the estimate as rich text format

[ ] Notes for Customer - section

[ ] Note - memo

[ ] Internal Notes - section

[ ] Note - memo

[ ] Modification History - link to track activity

  


Sagar Sagar 01/22/2023: The validations added in the sales form modules are

[ ] Validation

[ ] You do not have permission to edit this record.

[ ] Invoices can only be deleted if Status is Draft or Canceled.

[ ] Invalid sales form ID format. - if the sales ID format is not formatted properly

[ ] A contact or an organization should be specified. - if a contact or an organization is not specified

[ ] Country cannot be empty. - if a country is not specified

[ ] Status cannot be empty.

[ ] Itemization table cannot be empty. - if status is Invoiced or Paid and there is no row in Itemization table

[ ] If Status is Paid, a Payment Date must be specified.

[ ] If Status is Canceled, a Closed Date must be specified.

[ ] If the Status is "<InvoiceStatus>", the Payment Date must be cleared. - if its an invoice, status is not Paid but Payment Date is filled

[ ] Country cannot be empty. - if ship to different country is visible but not specified

[ ] Quantity cannot be blank. - if Quantity in Itemization table is blank

[ ] Tax rate is required for an invoice with taxable items. - if there are taxable sales items in Itemization table and Status is Draft or Canceled

[ ] Tax % cannot be negative.

[ ] Tax cannot be negative.

  


Sagar Sagar 01/05/2023: We show an invoice table in both contacts and organizations detail screen. We have that documented in the living spec of contacts([https://zch.apphosting.zone/Detail/Edit/2?RecordType=ClientProposals&NumberID=-61&State=ISwSvCyE0ts&](https://zch.apphosting.zone/Detail/Edit/2?RecordType=ClientProposals&NumberID=-61&State=ISwSvCyE0ts&)) and it was added in [[PC0076187]] - E00 - Add Invoice tables to Contacts and Organization
