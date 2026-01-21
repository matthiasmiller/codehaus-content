9.3.1. Member Payment Printout Page

  


Requirements

Overview: This is the "Member Payment" portion of this printout. This is always printed with the "Delivery Ticket" portion.

  


This is a fully customized printout, with GemWood letterhead. 

  


Printed From: See main spec for the shared printout.

  


File Format/Name: See main spec for the shared printout.

  


Fields to be Filled: 

  * Letterhead section (no label; included only on the first page if there are multiple pages): 
    * "Member Payment" (heading; hard-coded) 
    * GemWood Logo (hard-coded) 
    * GemWood Address, Phone Number, and Email Address (hard-coded) 



  


  * Details section (no label):
    * Member: (displays "Member Name") 
    * Address: <Member Address, in the standard multi-line format without the addressee name)
    * Payment ID: <Member Payment ID>
    * Payment Type: <Member Payment Type>
    * Payment Date: <Ticket Date in mm/dd/yyyy format> 
    * Payment Terms: (displays "Payment Terms"; allows for text wrapping)  



  


  * "Ticket Details" section:
    * Load Type: <Load Type from the Payment> 
    * Buyer: <Buyer from the Payment> 
    * Buyer's PO #: <Buyer's PO # from the Payment> 
    * Ticket Value $: <Ticket Value $ from the Payment> (displays in gray font if "Delivery Ticket Status" ≠ "Closed") 
    * GemWood Fee $: <GemWood Lumber Brokerage Fee $ from the Payment> (displays in gray font if "Delivery Ticket Status" ≠ "Closed") 
    * GW Discount $ ((visible if "GW Discount $" ≠ 0.00 on the Payment): <GemWood Discount $ from the Payment> 
    * Member $: <Total Member $ from the Payment> (displays in gray font if "Delivery Ticket Status" ≠ "Closed") 
    * "Note: Values in gray font are current estimates, pending Buyer settlement." (visible if "Delivery Ticket Status" ≠ "Closed") 



  


  * "Payment on Ticket" section:
    * Table includes all rows from the "Payment on Ticket" table on the Member Payment record, in the same sequence, with the same data: 
      * Columns: 
        * Type 
        * Ticket # 
        * Ticket Date
        * Total Member $
        * Member Balance
        * Applied $
      * Totals: 
        * N/A (none)



  


  * "Applied Overpayments" section (visible if the Payment includes one or more rows on the "Applied Overpayments" table):
    * Table includes all rows from the "Applied Overpayments" table on the Member Payment record, in the same sequence, with the same data: 
      * Columns: 
        * Type 
        * Ticket #
        * Ticket Date
        * Orig. Total $
        * Balance $
        * Applied $
      * Totals: 
        * N/A (none)



  


  * Totals: 
    * Ticket Subtotal $: (visible if the Payment includes one or more rows on the "Applied Overpayments" table): <Ticket Subtotal $ from the Member Payment>
    * Applied Overpayment $: (visible if the Payment includes one or more rows on the "Applied Overpayments" table): <"Applied Overpayment $" from the Member Payment>
    * Payment Total $: <Payment Total $ from the Member Payment>



  


  


Handling Page Breaks: Normally this should all fit on one page, but if enough "Applied Overpayment" rows are included to require an additional page, the page should break between rows in the "Applied Overpayments" table. 

  


Other Notes:

  * Includes the default "Powered by Silverloom -- Printed on <mm-dd-yyyy> at <HH:MM AM/PM>" footnote at the bottom of each page. 
  * Includes page numbers at the bottom of the page, in the following format: "Page <X> of <Y>". 



  


Sample(s): (if needed, move to Dev Specs)

  


Development Specification

Change Requests: 

  * Tim Reitz 10/04/2025: [[[IN11653](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11655&)]] - ZGW - Clean up Various Labels
  * 


  


  


Mockup: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1880441998#gid=1880441998](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1880441998#gid=1880441998)

  


BID: 3 Days

  


Rahmot E Elahi 07/20/2025: [[PC0181220]] - ZGW - Member Payment/Delivery Ticket Printout - Replace Member info with Buyer info
