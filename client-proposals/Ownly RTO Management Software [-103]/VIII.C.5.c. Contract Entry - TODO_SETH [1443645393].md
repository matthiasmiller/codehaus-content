8.3.4.3. Contract Entry - TODO_SETH

TODO_HLD - Review

  


  


NOTE: It is VERY VERY important to prompt & require manufacturer early in the process because this is the #1 leading cause of indigestion by entry of contract into the wrong RTO company.

  


  


Seth Miller 01/22/2026: TODO_Jasper: [[PC0189139]]

Contract Entry lookup type (investortools-owned list with 1 record)

  * Rental Company (detail variable with list of active rental companies; changing blanks out other fields)
  * Manufacturer (detail variable; only visible if rental company is selected; list of active manufacturers for that RTO company; changing it blanks out/product)
  * Contact (detail variable; only visible if rental company is selected; list of customers for the selected RTO company)
  * Product (detail variable; list of owned products not assigned to active contracts for the selected RTO company + manufacturer)
  * Enter Contract link (goes to a dashboard; only visible if RTO Company & Manufacturer are entered)



  


Seth Miller 01/22/2026: TODO_NM: [[PC0189145]]

Contract Entry Dashboard:

  * Prompt for same fields on detail screen
  * Left Pane - Contact
    * Create/Open Contact - for new, set RTO Company
  * Middle Pane 3 - Product
    * Create/Open Product - for new, set RTO Company, Manufacturer
  * Right Pane 4 - Contract (always a new one)
    * Create - set RTO Company, Asset ID, and Primary Customer



  


Permissions

  * View Full Contract Details (enable by default) Seth Miller 01/22/2026: TODO_KS: [[PC0189146]]
  * View Full Asset Details (enable by default) Seth Miller 01/22/2026: TODO_KS: [[PC0189141]]
  * These are needed for external contract entry.



  


Seth Miller 01/22/2026: TODO_Jasper: [[PC0189148]]

ContractPDFTypes (list; Investortools-owned):

  * Printable
  * E-Sign



  


Contract

Seth Miller 01/22/2026: TODO_KS: [[PC0189146]]

  * Hide Transfer Contact on New Record
  * Primary Customer OnChange
    * Set Contract ID to primary customer account number on a New Record
    * Set State when you set the primary customer on a New Record
  * Hide Resolution until Contract Start Date (or if the date is blank)
  * Hide Fees & Payments for New Records and also hide if not "View Full Contract Details"
  * Move Payment Terms above Term Length
  * Move -Contract Resolution & Fees & Payments sections. They  should go down below Notes
  * Contract Start Date should stay blank



  


  * TODO_SETH - Can we use Shared OnChanges for updating contract calculations so you see numbers as you enter? Seth Miller 01/22/2026: TODO_KS [[PC0189147]]. 



  


  * Contract Generation Seth Miller 01/22/2026: TODO_Jasper for RG: [[PC0189148]]
    * Add a read-only RG (only visible for admin/testing mode) with the following columns:
      * PDF Type with options for Printable and E-Sign
      * Stored Contents (memo)
      * Stored Middle Footer (memo)
      * Stored Right Footer (memo)
    * Add a macro intended for the RG row context called #ContractPrintable( "", "{{etc}}") that returns the first value if it's printable, else the 2nd parameter
    * Add code to the Shared OnChange that makes sure the RG has these two rows and does a RepeatRG and does an Eval for each of these templates.
    * On the main screen, add a PDF download for both Printable and E-Sign. Create a Contract Definition Template that takes an ask prompt with the PDF type and just grabs the right PDF row (mirror ZFP - 0.5" margin; middle & right footer)



  


Seth Miller 01/22/2026: TODO_KS: [[PC0189142]]

  * Contract Definition
    * Move Max Price & Max Width to beginning of RG (for minimum payments)
    * Add read-only expressions under the RG
      * Max. Rentable Price (max from the RG)
      * Max. Rentable Width (max from RG)
    * Unrentable Building Message (multiline plain text)
      * Pick one of the fields to rename and delete the other one.
      * Confirm that we enforce it.
    * Add a Middle Footer and Right Footer template memo expressions



  


Seth Miller 01/22/2026: TODO_KS: [[PC0189141]]

Asset:

  * Add a permission to View Full Asset Details. If you don't have this permission, hide everything EXCEPT
    * Asset section
    * Structure section
    * Purchase Amount
  * Yes, even hide NOTES


