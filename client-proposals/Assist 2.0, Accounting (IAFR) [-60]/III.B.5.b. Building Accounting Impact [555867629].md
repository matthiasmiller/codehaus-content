3.2.5.2. Building Accounting Impact

  


Requirements

The Building Accounting Impact report will show the impact of one or more STINs to accounting.

  


Prompt For:

  * District (required)
  * STINs



  


Sort By:

  * Building Number ID



  


Repeating List:

  * Transaction Line Items (see table below)



  


Columns:

  * Accounting Company ID
  * Event Type
  * Event Record ID (building number ID)
  * Event RG ID (blank)
  * Date
  * Account Name (indented)
  * Debit (see table below)
  * Credit (see table below)



  


Subset:

  * Filter buildings based on the main Financial Allocations subset



  


  
| Event Type| Expected Debit| Expected Credit  
---|---|---|---  
Assets|   
|   
|   
  
FGI Source("____ to Inventory")| Building Built|   
| Building - Standard/Actual Cost (for each FGI Category)  
FGI Destination("Finished Goods -- ____")| Building Built| Building - Standard/Actual Cost (for each FGI Category)|   
  
FGI Destination("Finished Goods -- ____")| Building Delivered|   
| Building - Standard/Actual Cost (for each FGI Category)  
  
|   
|   
|   
  
Expense|   
|   
|   
  
COGS Expense| Building Delivered| Building - Accounting Cost (for each FGI Category)|   
  
COGS Variance| Building Delivered| Building - Accounting Variance (for each FGI Category)|   
  
  
  


  


Development Specification

Niccolas Miller 04/25/2023: [[PC0153552]] - ZFP - FGI: Building Accounting Impact (T&M)
