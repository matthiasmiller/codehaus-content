10.2.2. Automatic Payments

  


Requirements

The payment module will allow for automatic/repeating payments on a per-customer basis, for customers who have at least one stored card.

  


If a customer has at least one stored card, a "Auto-pay Invoices with Selected Card" checkbox will appear on the Manage Payments console. Checking this box will cause the selected card to be used to automatically charge any Invoiced invoices for the customer until this setting is changed.

  


Development Specification

When creating invoices for a customer that has auto-pay, create the corresponding Stripe charge
