9.1. GemWood Purchase Order Printout

  


Requirements

Purpose/Overview: This is a printout of GemWood Purchase Orders, based on details from the Buyer Purchase Order record and the GemWood Purchase Order details, to be sent to Members as a request for lumber.

  


This is a fully customized printout, with GemWood letterhead. 

  


Printed From:

  * On the Purchase Order record: The "View PDF" link on the "GemWood Purchase Orders" embedded spreadsheet
  * Included as an attachment on the "GemWood Purchase Order Email" 
  * On the GemWood Purchase Orders report: The "View PDF" link



  


File Format/Name: "GemWood Purchase Order #<GemWood PO #> (generated on <current date in yyyy-mm-dd format>.pdf"

  


Fields to be Filled: 

  * Letterhead section (no label):
    * "GemWood Purchase Order" (heading; hard-coded) 
    * GemWood Logo (hard-coded)
    * GemWood Address, Phone Number, and Email Address (hard-coded) 



  


  * Details section (no label):
    * Deliver To: <Delivery Location, in the standard multi-line format without the addressee name>
    * "This purchase order has been canceled." (message in red text; visible if the GemWood Purchase Order "Status" = "Canceled") 
    * GemWood ID #: <GW PO #> 
    * Purchase Order Date: <PO Date> 
    * Member: <Member Name>
    * PO # / Buyer Reference: <Buyer's PO #>



  


  * "Itemization" section:
    * Table includes a row for each row in the "Itemization" table on the Buyer Purchase Order record, in the same sequence: 
      * Columns: 
        * Thickness (displays the "Thickness" for the corresponding row from the Buyer Purchase Order)
        * Species (displays the "Species" for the corresponding row from the Buyer Purchase Order)
        * Grade (displays the "Grade" for the corresponding row from the Buyer Purchase Order)
        * Notes (shared column heading for the following 2 columns, which don't have a border line separating them): 
          * Short Notes (no separate label; displays the "Short Notes" from the corresponding row from the Buyer Purchase Order) 
          * Buyer Notes (no separate label; displays the "Buyer Notes" for the corresponding row from the Buyer Purchase Order)
        * BF Qty. (displays the following calculation for the corresponding row from the Buyer Purchase Order: <"BF Qty." / "Target # Loads", rounded to the nearest whole number>; total row displays the sum) 
        * $/BF (displays the "$/BF" for the corresponding row from the Buyer Purchase Order)



  


  * "Special Instructions" section:
    * Text box, displaying the contents of the "Special Instructions" memo on the Buyer Purchase Order record.



  


Template: N/A

  


Handling Page Breaks: N/A (everything should always fit on a single page)

  


Other Notes:

  * Includes the default "Powered by Silverloom -- Printed on <mm-dd-yyyy> at <HH:MM AM/PM>" footnote at the bottom of the page.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1695545268#gid=1695545268](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1695545268#gid=1695545268)

  


Change Requests:

  * Ben Reitz 10/09/2025: [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature
  * Ben Reitz 01/06/2026: [[[IN12259](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12261&)]] - ZGW - GemWood PO Printout - Terminology changes


