8.6. Clipboard Sheet Printout

  


Requirements

Purpose/Overview: This printout is used by the truck driver for reference as he's making a delivery. 

  


Printed From: 

  * "Print Clipboard Sheet" button on the Delivery record



  


File Format/Name: PDF: "Clipboard Sheet for Delivery #<Delivery #> (exported on <current date>)"

  


Fields to be Filled: 

  * Delivery Details section (unlabeled table of the following:
    * Customer (displays the Customer from the Delivery record)
    * Job Name (displays the Job Name from the Delivery record)
    * Delivery Address (displays the Delivery Address, City, State, and Zip from the Order record in 2- or 3-line format, from the corresponding Order record)
    * Phone (with the following behaviors:
      * if "Job Phone" on Order record is set, displays that number;
      * if "Job Phone" on the Order record is not set, displays the "Customer Phone" number)
    * Sales Name (displays the "Salesperson" from the corresponding Order record)
    * Sales Phone (displays the "Sales Phone" from the corresponding Order record))



  


  * Trucker Details section (unlabeled table with the following:
    * Trucker (unlabeled; displays the selected "Trucker" from the selected Delivery record)
    * Trailer (unlabeled; displays the selected "Trailer" from the selected Delivery record)
    * Set/Drop (unlabeled; displays "Set" if the corresponding checkbox on the selected Delivery record is checked; displays "Drop" if the corresponding checkbox on the selected Delivery record is checked)
    * Item (unlabeled; displays the "Item" field from the selected Delivery record)
    * Time (unlabeled; displays the "Time" field from the selected Delivery record)
    * Info (unlabeled; displays the "Info" field from the selected Delivery record)
    * Drive Time (unlabeled blank row)



  


  * Pick Up Check section:
    * Truss Spacers (displays "          x $<value of "Truss Spacers $/pc" from Silverloom Settings> =          ", with space on each side of the filled portion for numbers to be written by hand)
    * Setting Fee (displays "          hrs x $<value of "Setting Fee" from Silverloom Settings> =          ", with space on each side of the filled portion for numbers to be written by hand)
    * All other rows in this table remain labeled and blank



  


Handling Page Breaks: N/A (everything should fit on one page)

  


Other Notes:

  * Includes the default "Powered by Silverloom" footnote at the bottom of the page. 
  * Note that printout templates may be subject to limitations of the PDF templating library. CCI will communicate with the client in places where the template library requires significant changes from the original design.



  


Development Specification

Change Requests:

  * Ben Reitz 11/26/2025: [[[IN11979](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11981&)]] - ZTD - Add new "Clipboard Sheet" printout


