21.4. RTO Contract Template

  


Requirements

TODO_TR finish speccing out what is filled and from where

  


  


The main body of the contract should be filled from the "RTO Contract Template" memo on the RTO Company contact record. 

  


The following should be filled automatically on the template:

  * Date ("Today") 
  * Agreement # (auto-numbered; sequential) 
  * Lessee (customer name and address in the following format:) 



FirstName LastName

Street Address

City, ST Zip

  * Model # (the Building's style code) 
  * Description (the Building's base description) 
  * Serial # (the Building's serial number) 
  * Condition ("New" or "Pre-Leased"; based on the Building's status - __ = "New" and "SRB" = "Pre-Leased") 
  * Rent (
  * Sales Tax 
  * LDW Fee (fill with calculated amount if selected on the Sales Order; fill with "Declined" if not selected)
  * Total Payment 
  * Security Deposit 
  * Total Initial Payment 
  * Monthly Rental Payment (same as "Rent") 
  * Cash Price for property (
  * Renewal Dates/next due date (
  * __ payments of $___  (
  * EPO price (
  *  Accept LDW/Reject LDW checkboxes (fill according to selection on the Sales Order) 
    * TODO_TR: highlight on PDF
  * $__ per month (always be fill with the LDW amount, even if the customer rejected the LDW - it currently it only fills if they accept it)
    * TODO_TR: highlight on PDF



  


  


Changes to to template: 

  * The text in parentheses after "Monthly Rental Payment" should be changed from "(plus tax)" to "(plus tax and LDW)"
    * TODO_JM: could you send us an updated copy? 
  * 


  


TODO_TR

1\. Could you confirm that the items that I've highlighted with yellow are the things that are to be auto-filled from the building/order? Are there any other things that you see that should be included as well? 

\- All of these should be on the Sales Quote and Sales Order (except maybe the EPO ) 

TODO_JM: "maybe" ?? 

  


*Also next due date (manually set on the Sales Order by the salesperson based on the estimated delivery date; required date field for RTO sales only; reference only) 

*make sure we have a delivery date on the sales order 

*make sure we have a Accept/Reject LDW on the sales order for RTO sales only ("Accept LDW" checkbox; default to unchecked)

  


Development Specification

File: (to be replaced/updated) [[File:RTO Contract sample_Redacted.pdf]]

  


RTO Contract Agreement #:  Starts as an arbitrary number, then goes sequentially from there. When the contract goes to the RTO company, they manually set the number in their system to match.

TODO_JM: how should this be set? should this start with the last number in your current system when we deploy?

TODO_JM: what if an RTO contract with a # is generated, but the customer doesn't sign? do you want to re-use that number?
