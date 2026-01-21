9.2. Buyer Invoice Printout

  


Requirements

Purpose/Overview: The Buyer Invoice Printout is sent to the Buyer after a Delivery Ticket has been set up and after the invoice has been approved by the Salesperson. 

  


This is a fully customized printout, with GemWood letterhead. 

  


Printed From: 

  * Delivery Ticket record
  * Buyer Invoices report
  * Buyer A/R Aging report



  


File Format/Name: "Invoice <Invoice #> (generated on <current date in yyyy-mm-dd format>.pdf"

  


Fields to be Filled: 

  * Letterhead section (no label):
    * GemWood Logo (hard-coded)
    * GemWood Address, Phone Number, and Email Address (hard-coded)



  


  * Details section (no label):
    * To: <Buyer Name and Address, in the standard multi-line format with the addressee name>
    * PO#: <Buyer's PO #> 
    * Invoice #: <Buyer Invoice #> 
    * Invoice Date: <Ticket Date in mm/dd/yyyy format> 
    * Terms: <Buyer Payment Terms> 
    * Due Date: <Buyer Due Date in mm/dd/yyyy format>



  


  * "Load Itemization (Member Grade)" section:
    * Table includes all rows from the "Load Itemization" table on the Delivery Ticket record, in the same sequence: 
      * Columns: 
        * Thickness
        * Species
        * Grade
        * Comments
        * BF Qty.
        * $/BF (shows 3 decimal places to match corresponding field on the Delivery Ticket record)
        * Amount (displays the contents of the "Member Grade $" column) 
      * Totals: 
        * BF Qty.: <sum of "BF Qty." column> (no label)
        * Amount: <sum of "Amount" column> (no label)



  


  * "Other Line Items" section:
    * Table includes all rows from the "Other Line Items" table on the Delivery Ticket record, in the same sequence:
      * Columns:
        * Date
        * Item
        * Description
        * Amount
      * Totals:
        * Amount: <sum of Amount column> (no label)
  * Total Due: <sum of Load Itemization "Amount" total and Other Line Items "Amount" total>



  


Template: N/A

  


Handling Page Breaks: N/A (everything should always fit on a single page)

  


Other Notes:

  * Includes the default "Powered by Silverloom -- Printed on <mm-dd-yyyy> at <HH:MM AM/PM>" footnote at the bottom of the page.



  


Development Specification

Change Requests: 

  * Tim Reitz 10/04/2025: [[[IN11689](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11691&)]] - ZGW - Buyer Invoice Printout - Rearrange and Fix "Load Itemization" columns
  * Ben Reitz 10/08/2025: [[[IN12207](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12209&)]] - ZGW - Buyer Invoice printout - Add Missing Date Column to "Other Line Items" Table
  * Ben Reitz 10/08/2025: [[[IN12096](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12098&)]] - ZGW - Buyer Invoice printout - Change $/BF column to show 3 decimals
  * 


  


  


Mockup: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1777266968#gid=1777266968](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1777266968#gid=1777266968)

  


  


Ellis Miller 12/18/2024: BID: 3 DAYS
