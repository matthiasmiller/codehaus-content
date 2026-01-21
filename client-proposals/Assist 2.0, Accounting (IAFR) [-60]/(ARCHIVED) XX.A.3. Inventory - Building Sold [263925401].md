20.0.3. Inventory - Building Sold

When a building is sold, Assist freeze the following values on the building:

  


  * Production Labor Expense = Building's Sales Order Price * FGI Labor Expense %
  * Production Overhead Expense = Building's Sales Order Price * FGI Overhead Expense %
  * Production Materials Expense = remaining balance



  


Assist will then create a transaction:

  * BALANCE SHEET
    * Credit “Finished Goods Inventory - Production Labor" asset account by the building's Production Labor Expense
    * Credit “Finished Goods Inventory - Production Overhead" asset account by the building's Production Overhead Expense
    * Credit “Finished Goods Inventory - Materials” asset account by the building's Production Materials Expense
    * Debit “Accounts Receivable" by the Sales Order Balance
  * PROFIT & LOSS
    * Credit “Income" income account by the Sales Order Balance
    * Debit “Production Labor" by the building's Production Labor Expense
    * Debit "Production Overhead” by the building's Production Overhead Expense
    * Debit “Raw Materials Purchases” by the building's Production Materials Expense



  


TODO_IN - To clarify, is the Materials cost also calculated as a ratio, just like the others?
