4.1.1.2. Configure Company Types and Pools

  


Requirements

On the Configure Payroll child screen there is a section for Configure Company Types and Pools. This section contains the following: 

  * Embedded spreadsheet with the following: 
    * Columns: 
      * Effective Date (single-line plain text field)
      * Company Type (droplist of Independent Child Company, Parent Company, Payroll Child Company)
      * Owner Pool % (single-line plain text field)
      * Prod Pool % (single-line plain text field)
    * Automatically sorted by: Effective Date
    * Buttons to add and remove rows ("+"/"-" OR "Add"/"Remove") 
    * Show 4 rows without scrolling



  


  


  


Production employees are paid out of a shared production pool, based on a percentage of the weekly production. All companies use this compensation model, regardless of type. Owners and non-production employees are paid from a non-pool payroll.

  


Each company can be one of three types:

  


  * Parent Company (Payroll Shop) - Parent Company pays owners and staff as non-pool payroll.



  


  * Independent Child Company (Independent Subshop) - Parent Company pays Owner Pool (15%) to the independent child company with recommended (but not enforced) production, non-production, and owner compensation.



  


  * Payroll Child Company (Payroll Subshop) - Parent Company uses production employees directly from the Production Pool. If the payroll child company has an owner, it pays child company expenses and owner compensation from an Owner Pool



  


For the purposes of reporting in Assist, all shops can be treated identically. Burkholder Management will configure which shops to receive Owner Payroll Verification Reports. All other differences between shops are handled by the accountant.

  


NOTE: Work orders are paid by the parent company and the cost is passed on to the child company as a deduction from their owner, and the child company passes it on to the employees as a deduction from their paychecks.

  


These percentages will be configured in an embedded spreadsheet, allowing Assist to generate historical time cards. Most companies would have only one row. However, they will have multiple rows if they change compensation methods. For example:

Effective Date| Company Type| Owner Pool %| Production Pool %  
---|---|---|---  
11/29/2020| Parent Company| 15| 7.5  
08/04/2019| Independent Child Company| 15| 7.5  
04/26/2017| Payroll Child Company| 15| 7.5  
  
  


The Owner Pool % will be blank if the company does not use an owner pool for non-production payroll.

  


NOTE: The 7.5% production pool is subtracted from the 15% owner pool.

  


Development Specification

Design Notes:

  * [[File:Transcribed notes from 11-27&28 pict.pdf]]
  * [[File:Emloyee pool info.pdf]]



  


  * Company: Add Dated RG with fields:
    * CompanyProdBonusMethodDate -- date, required.
    * TODO



  


Bid: 2 hours
