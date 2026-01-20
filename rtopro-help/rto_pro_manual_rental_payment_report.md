# http://www.rtopro.com/help/rto_pro_manual_rental_payment_report.htm

# Payment / Transaction Report

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** RTO Pro Manual >

# Payment / Transaction Report

# 

|  [](rto_pro_manual_revenue_summary.md "Previous Topic") [](welcome_welcome_1.md "Parent Chapter") [](rto_pro_manual_retail_sales_report.md "Next Topic")  
---|---  
  
Revenue Reports Option "2"

This report will show rental, cash advance and check cashing revenue income for any given date range. The report options are described below.

Transaction Date: Enter the transaction date range

Detail / Summary: Summary will give totals only and Detail will list each customer and amount paid.

Revenue type options: You have the option to include rental, check cashing and cash advance, rental only or cash advance and check cashing revenue only. You can also choose to show moved due date transactions only.

Print or Display: Choosing display will cause the report to be displayed before printing, you can click the "Print" button from the report viewer if you want to print it after reviewing it.

Zones are used in RTO Pro to split customer into different areas or routes. This is usually used to separate customers for multiple account managers. This is not the same as "Tax Zones". [Zone:](javascript:void\(0\);) If you want the report to be only for customers in a certain zone, enter the zone here.

Salesman: If you want to include only revenue for 1 salesman enter the salesman here.

Push F5 to begin the report.

Some of the values displayed on this report are described below:

PMT Form (Payment Form): C=Cash, V=Visa, M=MasterCard, A=American Express, D=Discover, H=ACH, K=Check (1, 2 and 3 are custom payment forms you can define in store setup).

PMT Type: R=New Rental Agreement Loaded, P=Payment, S=Retail Sale Transaction, C=Close transaction (A rental agreement was closed), D=Due Date Move

![rental payment report](hmfile_hash_aed0a9a7.jpg)

Each section of the report is explained in the detail below:

1\. This is the base rental fee, this does not include taxes or any other charges.

2\. This is the total retail revenue, without including taxes or any other charges.

3\. Total row shows the total of all labeled columns. Note this is total of all revenue, there may be other figures included in #10, "Total $ Received" that are not revenue, like deposit paid and purchase reserve paid etc.

4\. The damage waiver, could have different initials, can be changed to different default initials in store setup. this is the total for the damage waiver, not including taxes or other charges.

5\. The total for Club fees, not including taxes or other charges.

6\. Other charges not including tax, but including any type of fees, ex; late fees, NSF fees, delivery fees, processing fees, trip fees. Including anything added to other charges.

7\. This is the total of all taxes added together from rental and retail.

8\. This is the total of each line; rental, retail and total put into their own column.

9\. This section shows how the money has been collected by certain payment form, cash, check, etc.

10\. This is the total amount for all money taken in (not including petty cash payouts). Note this can be different than the #3 total line, this includes all money collected, #3 is revenue only. Deposit paid and purchase reserve paid as well as some other items such as accounts receivable paid are not revenue. Talk to your accountant if you have questions about why some items are revenue and others are not.

The formula for "Total $ Received" is Total $ Received = Total(#3 above) + ARPaid(accounts receivable paid) + NSF Paid + Deposit Paid - (ARBooked(accounts receivable booked) + Deposit Spent)

Convenience Fees Collected(not on above screen shot): If the report shows convenience fees collected (it would be directly below "Custo3" in this screen shot if there were any) it is just broken out for your convenience, it would be included in either other charges or the club column, depending on your store settings at the time the payment was taken.
