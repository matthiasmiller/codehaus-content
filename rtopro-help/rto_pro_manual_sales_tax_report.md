# http://www.rtopro.com/help/rto_pro_manual_sales_tax_report.htm

# Sales Tax Report

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** RTO Pro Manual >

# Sales Tax Report

# 

|  [](rto_pro_manual_retail_sales_report.md "Previous Topic") [](welcome_welcome_1.md "Parent Chapter") [](rto_pro_manual_apu_bor_income_graph.md "Next Topic")  
---|---  
  
Revenue Reports Option "4"

This report will show income and tax collected for each tax percentage used in your store. This is useful for filling out sales tax returns. Report options are described below.

Transaction Date: Enter the transaction date range. The default date range is the first to the last of last month.

Print or Display: Choosing display will cause the report to be displayed before printing, you can click the "Print" button from the report viewer if you want to print it after reviewing it.

Zones are used in RTO Pro to split customer into different areas or routes. This is usually used to seperate customers for mulitple account managers. This is not the same as "Tax Zones".[Zone:](javascript:void\(0\);) If you want the report to be only for customers in a certain zone, enter the zone here.

Push F5 to begin the report.

Below the tax income information is the information to fill out the Florida Department of Revenue Tax Return DR15. Remember to always double check these figures before sending in your tax return.

If this form is different in your state contact RTO Pro Software about getting one customized for you.

* * *

Notes about fractions of cents and how they can make totals figures look off on sales tax report.

A question we often get when people look at the totals page of their sales tax report is for example "My tax rate is 4%, my revenue was 1990.00, why does the total tax collected = $80.00 instead of $79.60?"

This is because tax is calculated on each transaction, not at the end of the month based on your total revenue, so rounding can make the number look total figures for the month wrong when they are correct.

For instance with the example above if the 1990.00 in revenue was from 100 payments of $19.90, 19.90 x .04 = 0.796, which is rounded to $0.80, so you collected 100 x .80 = $80.00, not $79.60.

* * *

Notes about fractions of cents and how they affect your exempt amounts on sales tax reports.

Below are a couple of examples of instances where the sales tax report can show more or less as tax exempt than the actual exempt items total.

Payment | Tax on 1 pmt (.069 tax rate) | DWF (tax exempt in this example) | Total payment  
---|---|---|---  
9.62 | .66 | 2.00 | 12.28  
x3 | x3 | x3 | x3  
28.86 | 1.98 | 6.00 | 36.84  
  
In this example 3 payments are paid on the contract above. Multiple payments are treated like individual transactions for calculating tax etc. The amounts above are correct and what should be collected.

The sales tax report has to make all the numbers match, and because of fractions of cents and or multiple payments in one transaction, sometimes it looks like you did not collect enough sales tax. In the example above 28.86 x .069 = 1.99, so it looks like you did not collect enough sales tax, when really you did. So to make the numbers all match it must account for the penny it looks like you did not collect in sales tax, and flag that penny worth of revenue as tax exempt, so the sales tax report would show 6.16 as tax exempt, instead of the $6.00 you were expecting.

There will be other instances where it does the opposite, shows less tax exempt than there really is because of the same reason, fractions of cents.

Payment | Tax on 1 pmt (.069 tax rate) | DWF (tax exempt in this example) | Total payment  
---|---|---|---  
13.00 | .90 | 2.00 | 15.90  
x3 | x3 | x3 | x3  
39.00 | 2.70 | 6.00 | 47.70  
  
39.00 x .069 = 2.69, so when you look at it as 1 transaction it looks like you charged too much tax, so the sales tax report reduces the tax exempt amount for this transaction, so instead of showing $6.00 exempt, it shows $5.87 exempt.
