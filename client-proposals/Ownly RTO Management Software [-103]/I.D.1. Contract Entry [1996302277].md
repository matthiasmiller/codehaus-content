1.4.1. Contract Entry

  


Requirements

Seth Miller 12/08/2025: TODO_IDD:

we have a macro ContractCRAAmountWithoutTax that is calculating how much we think the CRA amount should be not how much was paid. Should all our calculations be using that value or the amount that was paid to CRA?

  


  


Contact record:

[ ] add a Enter Contract link

  * Ask prompts
    * Hidden field for customer contact
    * Primary ID
  * Detail Screen
    * Sets a detail variable for New Contract Customer



  


Product Record

  * New Contract link (passes through the New Contract Customer if it's set, also passes through the Product itself)
    * Saw "Enter Contract for CUSTOMER NAME" if we have a New Contract Customer.
    * Hide the link if there are any contracts with a resolution of either Early Payoff or Payout.
  * Amount Collected By Manufacturer (number; 2 decimals)
    * Under Purchase Amount. No I don't know how to fit it in. We need to take it into account when calculating the amount owed to the manufacturer.



  


Contract Record:

  * 


  


  


  


NOTE: Contract Start Date is effectively the starting period. The is the due date of the first month of rent and is the basis for all future due dates

TODO_SETH - We need to document this.

  


TODO_JB: When entering non-CC/non-ACH payments, we need to prompt for date and default to today. Do not allow backdating prior to the latest payment date.

  


  


  


Feb/Spring

TODO_IDD - Figure out handle payments received outside of the system.

  


  


  


  


  


[X] how do we handle entering the initial payment?

[X]  CRA amounts?

  


[ ]  mismatched values, etc

  


[ ] Allow overriding the building value by checking a box, then require a value and a justification notes

  


  


  


  


  * TODO_IDD - This will be populated as part of the contract entry to simplify entry


  * TODO_IDD - Contract Entry Process - during contract entry, ask whether they opted into  SMS



  


  


Niccolas Miller 07/23/2025: TODO_IDD/DB: Will we be sending out contracts to be signed? Is this an integration?

  * TODO_IDD: Spec out how this works in the contract entry process



  


  


  * 


  


DONE_IDD - Do we need a way to assign contacts / contracts / etc to a different rental company if someone messes up? Probably not a standard use case

Matthias Miller 08/06/2025: There is no way to do this. You need to close out the contact, close out the contract, and re-enter it. THis is because we have different RTO contract definitions per company.Matthias Miller 08/06/2025: We could handle this in contract entry, potentialy with a TODO_PERMISSIONS that only allows super admins to copy (and/or save the copy)

  


  


  


TODO_IDD - Add a way to be able to enter additional fees

  


  


  


  


  


  * TODO_IDD: How do we handle the custom contract value for bad contracts? Scenarios:
    * Monthly payment too "high" in written/signed/legal contract
      * TODO_DB: presumably use lower payment OR higher payment and pay off early ??
    * Monthly payment too "low" in written/signed/legal contract
      * TODO_DB: presumably lower contract value to result in this monthly payment??
    * Contract value too "high" in written/signed/legal contract
      * TODO_DB: presumably use standard payment and intended contract value ??
    * Contract value too "low" in written/signed/legal contract
      * TODO_DB: presumably use same payment amount, but fewer payments, resulting in lower contract value being paid??



Matthias Miller 08/07/2025: Move to contract entry. Usually we use the lower of the amounts and in extreme cases will require a contract rewrite.

  


  


TODO_IDD - handle depr start date in contract entry

  


  


  


* etc

  


  


From a business case, this is important for demos and marketing.

  * Option 1 - WSGI. The menu would have a portal for entering contracts. It would allow uploading the contract first, then perhaps show it side-by-side with entry fields, running an import at the end to push it into the database.



  


  * Option 2 - Contract Entry Record. Silverloom would have a special Contract Entry record that would collect all the information in an intuitive way, then kick off imports on the backend.



  


  * Option 3 - Use Existing Silverloom Records.
    * Create new contract
    * Search & select customer. If it doesn’t exist, click the ellipsis to open a new contact in a new tab, save it, and return to select the newly created customer. (We could make this easier by tracking the time the detail screen was opened, and showing the first contact that was created by this user after the screen was opened, with a button to use that contact.)
    * Select the building if it’s in inventory. If it doesn’t exist, follow a similar process as the customer to set it up. Then, return and select it.



  


Matthias Miller 07/17/2025:

  


Development Specification

TODO_IDD - Needs design, preferably Silverloom.
