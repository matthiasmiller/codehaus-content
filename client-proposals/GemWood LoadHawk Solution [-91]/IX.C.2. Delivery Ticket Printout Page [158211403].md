9.3.2. Delivery Ticket Printout Page

  


Requirements

Purpose/Overview: This is the "Delivery Ticket" portion of this printout. As mentioned elsewhere, this can be printed by itself, or with the "Member Payment" portion.

  


By itself, it can be referred to as the "Delivery Ticket printout", and is printed from the Delivery Ticket record and included in various outbound emails.

  


This is a fully customized printout, with GemWood letterhead. 

  


Printed From: See main spec for the shared printout.

  


File Format/Name: See main spec for the shared printout.

  


Fields to be Filled: 

  * Letterhead section (no label):
    * "Delivery Ticket" (heading; hard-coded) 
    * GemWood Logo (hard-coded)
    * GemWood Address, Phone Number, and Email Address (hard-coded)



  


  * Details section (no label):
    * Buyer: <Buyer Name>
    * To: <Buyer Address (in the standard multi-line format with / without the addressee name)
    * "Values are pending until the delivery ticket is closed." (message in red text; visible if "Delivery Ticket Status" ≠ "Closed" or "Canceled")
    * "This delivery ticket has been canceled." (message in red text; visible if "Delivery Ticket Status" = "Canceled")
    * PO#: <Buyer's PO #> 
    * Ticket #: <Delivery Ticket #> 
    * Ticket Date: <Ticket Date in mm/dd/yyyy format> 
    * Closed Date: <Closed Date in mm/dd/yyyy format, or blank if N/A>
    * Ticket Value (Buyer Grade): <Ticket Value $> 



  


  * "Load Itemization (Member Grade)" section:
    * Table includes all rows from the "Load Itemization" table on the Delivery Ticket record, in the same sequence: 
      * Columns: 
        * Thickness
        * Species
        * Grade
        * Notes 
        * BF Qty.
        * $/BF 
        * Member Grade $ 
      * Totals: 
        * BF Qty.: <sum of "BF Qty." column> (no label)
        * Member Grade $: <sum of "Member Grade $" column> (no label)



  


  * "Other Line Items" section:
    * Table includes all rows from the "Other Line Items" table on the Delivery Ticket record, in the same sequence:
      * Columns:
        * Date 
        * Type 
        * Description
        * Amount $
      * Total:
        * Amount: <sum of Amount column> (no label)



  


  * Itemization Total: <sum of Load Itemization "Amount" total and Other Line Items "Amount" total> 



  


Template: N/A

  


Handling Page Breaks: N/A (everything should always fit on a single page)

  


Other Notes:

  * Includes the default "Powered by Silverloom -- Printed on <mm-dd-yyyy> at <HH:MM AM/PM>" footnote at the bottom of the page.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=8223207#gid=8223207](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=8223207#gid=8223207)

  


Change Requests:

  * Ben Reitz 09/17/2025: [[[IN11740](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11742&)]] - ZGW - Member Payment/Delivery Ticket Printout - Replace Member info with Buyer info
  * 


  


Ellis Miller 12/18/2024: Can clone a lot of the Buyer Invoice (use the same shared reports where possible).

  


BID: 1.5 Days
