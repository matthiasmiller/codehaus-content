10.2.1. Store & Manage Cards

  


Requirements

Credit/debit card processing is done through Stripe. John has an existing Stripe account that CCI/CH would link to the software. John would be responsible for ongoing maintenance of the Stripe account.

  


There would be the option to store card information for multiple cards per customer. This happens through an integration with Stripe; Stripe stores the actual card information and shares a token with the software. The software could display the type (VISA, MasterCard, etc), the last 4 digits of the card number, and the Expiration Date. 

  


Credit card payments would be taken over the phone or run automatically for stored cards, as applicable.

  


The Manage Payments page would be the central location for collecting payments and managing saved card information. See more details in the following sections of this proposal.

  


Development Specification

Card info would be stored on a hidden Stripe customer record.

  


Stripe charge record needs to be linked
