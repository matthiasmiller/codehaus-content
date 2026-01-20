# http://www.rtopro.com/help/nsf-and-accounting.htm

# NSF and Accounting

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# NSF and Accounting

# 

|  [](help_desk_quickbooks_or_other_accounting_software_integration.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](help_desk_sql_strings.md "Next Topic")  
---|---  
  
NSF Checks example accounting

Examples of how NSF should flow to your accounting.

In these examples we will have the following today

$500 in rental revenue

$35.00 tax collected

$100 NSF returned that was $94.00 rental revenue and $6.00 tax

If you reverse the $100 NSF transaction.

Description | Splits | Split Amt. | Deposit Amt |   
---|---|---|---|---  
Regular Deposit |  |  | 535.00 |   
| Rental Revenue | 406.00 |  | *The reduced revenue and sales tax is booked in this transaction  
| Tax Collected | 29.00 |  |   
| Temp Holding | 100.00 |  | *The temp holding is used to balance the transaction and to account for the negative NSF deposit.  
NSF Deposit |  |  | -100.00 |   
| Temp Holding | -100.00 |  | *When the negative NSF deposit is entered the temp holding acct = 0 again  
|  | Total | Total |   
|  | 435.00 | 435.00 | *Everything is in balance  
  
If you Load an NSF for the $100 NSF transaction.

Description | Splits | Split Amt. | Deposit Amt |   
---|---|---|---|---  
Regular Deposit |  |  | 535.00 |   
| Rental Revenue | 500.00 |  | *The reduced revenue and sales tax is booked in this transaction  
| Tax Collected | 35.00 |  |   
|  |  |  |   
*NSF Transaction |  |  | -100.00 |   
| NSF Account | -100.00 |  | *This creates an expense of $100.00, when the NSF is paid it would remove the $100 expense  
|  | Total | Total |   
|  | 435.00 | 435.00 | *Everything is in balance  
  
*These is an option to create this NSF transaction in your IIF/QIF file exports in the End of Day Setup, if you use the option to create IIF/QIF files to import into accounting software.
