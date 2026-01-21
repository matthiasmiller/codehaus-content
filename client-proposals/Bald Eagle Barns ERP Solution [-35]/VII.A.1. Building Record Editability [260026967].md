7.1.1. Building Record Editability

  


Requirements

Certain fields on the Building record must become read-only at some point to prevent undocumented changes from happening:

  * All fields on the Building record that affect the Serial # and/or building Price become read-only when when a Work Order is created. For a New Customer Building, this happens when the initial Sales Order is advanced to "Order" status. The fields to be locked are:
    * Building Item Code (Style and Size) 
    * Options 
    * Layout 
  * All other fields in the Building Details section of the Building record become read-only when the first Task on the building has been started. 



  


After fields have been locked, changes still may be done via a "Change Order" (a type of Work Order). This creates a new (supplementary) Sales Order for the changes (see the corresponding section of this proposal).

  


*Done.

  


Development Specification

Mockup: N/A

  


Add a macro for the Sketch Pad for editability that can be referenced in the detail screen as well as in the WSGI editing interface.
