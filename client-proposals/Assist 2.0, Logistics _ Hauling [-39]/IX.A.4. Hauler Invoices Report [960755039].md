9.1.4. Hauler Invoices Report

  


Requirements

This is an editable report that repeats on the Building Locations. It should group by:

  * Invoice Date (Uninvoiced at the top) + Hauler + Builder



  


The line items would have information about each of the specific hauls.

  


Columns:

  * Invoice # (hauler invoice prefix + numeric representation of date; i.e. HH-0414; left-padded DateToNum)
  * Invoice Date
  * Hauler
  * Builder
  * STIN
  * Desc (BuildingCalcedDescription)
  * Delivery Type (Customer vs Lot)
  * Miles
  * Mileage $
  * Other $
  * Total (i.e. Mileage + Other)



  


Sort By:

  * Delivered Date + Load Number



  


Prompt for

  * Hauler (blank = all)
  * Builder (blank = all)
  * Invoice Date (blank = all)



  


The STIN would link to the building.

  


Development Specification

Use DateToNum for generating the InvoiceNumber
