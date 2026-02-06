10.2.4. Receive Payments

  


Requirements

This is the full payments option, with the ability to receive card payments and use stored card numbers through the AppHosting database, using a "payments dashboard" for card, check, and cash payments. 

  


Clicking on "Receive Payment" or "Manage Payments" from the Main Menu, the Customer/Ads Page, the Payments Due Report, or the Invoice Detail would open the Manage Payments page. This would be the central location or "payments dashboard" for collecting payments and managing saved card information.

  


Note that the finished product of this page may look different from the page that was mocked up. 

  


The Manage Payments page would have the following sections and fields:

  * Customer Section:
    * Customer (required; list of all Customers, filters down as you type; if opened from the Menu default to blank, read-only after an invoice has been selected; auto-filled and read-only if opened from the Customer/Ads Page or from a specific Customer on the Payments Due Report or from an Invoice)



  


  * Payment Methods Section:
    * Payment Method (required; drop list of "Check", "Cash", "(New Card)", and stored cards in a format such as "####, exp. mm/yy"; default to the Auto-pay Card if one is specified, otherwise default to blank)
      * if Check is selected, show:
        * Check # (number field; allow 10 digits)
      * if Cash is selected, no conditional prompt
      * if (New Card) is selected, show:
        * New Card (probably a pop-up window):
          * prompt for (maybe in line)
            * Card #
            * Expiration
            * Security Code
          * Save button
      * If a stored card is selected, show:  
        * Auto-pay Invoices with Selected Card (checkbox; only allow one Auto-pay Card at a time; selecting a new card would clear the old one)
        * Remove Card (button to remove selected card, with prompt to confirm)



  


  * Payment Details Section:
    * Payment Amount (default to total outstanding balance of all unpaid invoices for the selected customer; modifying this will adjust the payment amount on each invoice)
    * Payment Date (today for card payments; default to today but allow editing to a past date for check/cash payments)



  


  * Invoices Section:
    * Invoices (table of all unpaid invoices for the selected customer - all with "Invoiced" status)
      * Invoice # (link to the invoice detail)
      * Invoice Date
      * Invoiced Amount
      * Invoice  Balance
      * Include in Payment (checkbox; default to cleared; if filled the selected invoice is included in the payment; if cleared the invoice does not receive any payment; require at least one to be filled)
      * Invoice Payment Amount (editable; if there is only one invoice in the table, this field defaults to the full Payment Amount; if there are multiple invoices in the table, this field defaults to an equal portion of Payment Amount for all invoices, with any remaining portion applied to the oldest invoice; if the "Include" checkbox is cleared, this field should be blank and non-editable)
    * Payment Total (read-only; sum of all Invoice Payment Amount fields; must equal the Payment Amount before the payment can be processed)



  


  * Process Payment (button) 



  


Clicking the Process Payment button would do the following:

  * Create and apply the payment to the selected invoice(s), setting the Payment Date 
  * Enter summary notes into the Notes section of the invoice(s): "Paid with card ending in xxxx - $xxxx.xx" or "Paid with card ending in xxxx - in full" (as applicable)
  * Update the invoice status to Paid (if payment is complete)



  


Development Specification

This page is an integration, not a detail screen. We don't need to try too hard to keep the visual layout of the mockups. (use WSGI integration for card, check, and cash payments)

  


  


  


  


  


Tim Reitz 03/23/2021: The following is being saved here in case John wants to cut cost by removing the card processing: 

OPTION 2 - Can be used to reduce scope and cost - removes card processing: 

This option is more basic and less expensive that the full payments option. This option does not include the ability to process card payments or access stored card numbers with the AppHosting database. Rather, card payments would be run manually through Stripe and all payments are recorded in a common way in AHZ. 

Note that if this option is used, some changes will be needed to update links, etc. For example, the Customer/Ads Page will need to have the "Manage Payments" link removed and replaced with "Receive Payment" link. 

  


To receive/record a check, cash, or card payment:

  * Selecting the "Receive Payment" option on the Main Menu, the Customer/Ads Page, or from the Payments Due report with no line selected, it will open the "Receive Payment Intro" prompt page.
  * Selecting the "Receive Payment" option from an Invoice Detail or the Payments Due Report with a line selected will auto-fill and skip over the "Receive Payment Intro" prompt page and go directly to the "Receive Payment Details" prompt page.



  


  


The Receive Payment Intro prompt page would have prompts for the following:

  * Customer (required; list of all Customers, filters down as you type; auto-filled if opened from the Customer/Ads Page)
  * Invoice # (required; list of all Invoiced invoices for the selected customer; default to blank)



  


Clicking Continue would open the Receive Payment Details prompt page.

  


The Receive Payment Details prompt page would have prompts for the following:

  * Payment Amount (required; number field, to 2 decimal places; auto-filled from the selected invoice; editable)
  * Payment Type (required; choice of Check and Cash; default to Check)
    * If Check: Check # (visible and required if Payment Type = Check; number field)
    * If Card: Last 4 of Card # (visible and required if Payment Type = Check; number field; validate for 4 digits)
  * Payment Date (required; default to today; editable)



  


Clicking Continue would do the following:

  * Create and apply the payment to the selected invoice, setting the Payment Date as selected in the prompt
  * Enter the summary notes into the Notes section of the invoice:
    * For check payments: "Paid with check #xxxx -- $xxxx.xx" or "Paid with check #xxxx -- in full"
    * For cash payments: "Paid with cash -- $xxxx.xx" or "Paid with cash -- in full"
    * For card payments "Paid with card ending in xxxx - $xxxx.xx" or "Paid with card ending in xxxx - in full" (as applicable)
  * update the invoice status to Paid (if payment is complete)



  


Tim Reitz 02/25/2021: See this from the Graber project: [https://mys.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-2835&State=zGbMKtxvWAo](https://mys.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-2835&State=zGbMKtxvWAo)
