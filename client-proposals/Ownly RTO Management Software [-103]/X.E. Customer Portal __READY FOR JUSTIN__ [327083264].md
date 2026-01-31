10.5. Customer Portal **READY FOR JUSTIN**

Justin - Wed/Thu

  


  * Customer Portal



  


  * We need some way to display help documentation or something similar, with an info page that pulls from wiki documents (?) and can explain RTO, how to use the portal, anything else that's needed
    * Delivered in the same interface behind a login
    * Top-level documents (no nesting) but with linking
    * Backend options:
      * Markdown (ideally) OR
      * Forcing fonts
    * Markdown needs formatting for:
      * Headings
      * Tables
      * Blockquotes
      * Code
      * Paragraphs
      * Separators (thematic breaks)
      * Unordered lists
      * Ordered lists
      * Need image support
    * Linking between documents



  


  


  * Customer Portal - context of the user
    * Adjustments to Payment Portal
      * Add pencil icon to edit address. Add pencil icon edit phone. Show text boxes for each with a Save button.
      * Use a "checkout style" process



  


  * Payment Methods



  


  * Customer Portal - context of a contract
    * NOTE - We have product descriptions such as DMS041213JS - 24 x 12 COTTAGE - 00222



  


  * Payment History
    * Payment Date
    * Payment Time
    * Payment Amount
    * Receipt (may including details for multiple contracts if multiple contracts were paid)



  


  * Payments
    * Allow paying a 1-time payment amount for any amount.



  


  * Autopay
    * The customer may have multiple autopay plans. Allow them to cancel it.
      * Design for modifying simple payment plans.
    * Note that we can suggest (but not require) late fees for certain states.
    * Allow customer's to set up autopay, and when creating it, prompt that they also need to make a 1-time payment to catch up their account, and that their autopay will continue after that
    * The customer must call in to autopay less than their minimum amount
    * Frequency
      * Weekly
      * Biweekly
      * Monthly
      * Semimonthly
    * Amount defaults to minimum amount to make monthly payments; can be increased above but not below
      * If the payment is > the monthly rent, it's a 'pay ahead'. Tell the customer.



  


  * Ability to download contract files (must have a 'allow customer download' checkbox checked)
    * File Description + Download Link (i..e Contract, Sales Order) - arbitrary # of items (0...n)



  


  * Ability to contact customer support (proposal: online form that submits and tags a note on their contact and/or contract)
    * Contract (optional list of contracts)
    * Request Type
      * Warranty Claim
      * Billing
      * Other
      * etc
    * Attach Files
    * Contents/Body
  * For design, it MIGHT make sense to give a way to show read-only view of past requests (date + time)



  


  * We need an ability for users to IMPERSONATE the customer, and it needs to be abundantly clear. This will be a read-only view.



  


  * RTO-Company Specific Theming
    * Logo (defined in Silverloom)
      * Aspect ratio
      * Minimum dimensions
    * List of specific theme colors (please can we make them simple and specific and say which ones need to contrast for readability?!)
      * Fields on RTO 
      * Preview Link that shows pending colors prior to save // colors cached on login
    * Additional Contact Info
      * Salesperson Name + Phone (tel link) + Email (link)
      * Dealer Name + Phone (tel link) + Email (link) + Website (link)



  


  * Privacy Policy & Terms
    * Presumably also defined as markdown
    * 


  


TODO_IDD:

  * Add a contact flag to require secured fund (i.e. no ACH, etc)
  * Fire a note anytime a customer cancels an autopay.
  * Let's talk about how to give visibility to notes without creating visibility into things that they shouldn't see
  * Let's log activity & interaction time
  * Markdown



  


Dev Spec:

  * WSGI Configuration
    * Map from CNAME -> database instance + RTO Company


