# http://www.rtopro.com/help/rto_pro_manual_inventory_labels.htm

# Inventory Labels

<< [Click to Display Table of Contents](index.md) >> **Navigation:** RTO Pro Manual >

# Inventory Labels

|  [](rto_pro_manual_transfer_report.md "Previous Topic") [](welcome_welcome_1.md "Parent Chapter") [](rto_pro_manual_inventory_control_module.md "Next Topic")  
---|---  
  
Inventory Menu Option "C"

The Inventory Label function allows you to print inventory labels either as inventory is received, from the inventory report or from the inventory inquiry screen. To print labels for inventory as it is received, check the "Print Labels" check box at the bottom of the serial number entry window. You can create and save different label formats and select which to use before they are printed.

Field names can be inserted on the label by pushing F4 from the label screen and pushing ENTER on the field you wish to insert. These fields will be filled in with information from the inventory records when printed. You can also type the fields you wish to enter. Below is a list of available fields that can be used.

Model = {model}

Serial = {serial}

Stock# = {stock}

Description = {description}

Retail Price = {retail}

RTO Price = {rto} (This would print whatever is saved in the RTO$ field when you receive inventory. See below for pricing by category markup)

Cost code(r=random#) = {rr{cost}rr}

For the cost code you can arrange the random numbers to be anywhere before or after the cost that you want. For example you could enter it like this {rrr{cost}}, and the cost would be the value after the first 3 numbers are removed. A cost of $200.00, with the above code would print as follows "59220000".

The random numbers allows you to print the cost hidden on the label.

* * *

RTO Price based on line in individual price table or line from markup table = {RTOSF1WP}

The fields below can be used when you need to separate price, # of payments or total RTO price.

{RTOSF1W#} would print the number of weekly payments from line 1 (top line) of the markup table or individual price table.

{RTOSF1WP} would print the weekly payment from line 1 (top line) of the markup table or individual price table.

{RTOSF1WT} would print the total RTO price for weekly payments from line 1 (top line) of the markup table or individual price table.

This field can be edited manually in the following ways:

You can change the "1" in any of the fields above to any number between 1-6 for the line in the price table to use

You can change the "W" in any of the fields above to "M" for monthly, "B" for bi-weekly, "S" for semi-monthly

You can add a "+" if you want the price or total to include tax for instance {RTOSF1WP+} would print the weekly payment amount including tax from line 1 of the pricing table.

So for instance a label with the following line:

Rent to own for {RTOSF1M#} monthly payments of {RTOSF1MP} for a total of {RTOSF1WT}

Could print (if the 1st line in individual pricing is 12 months at 50.99):

Rent to own for 12 monthly payments of $50.99 for a total of $612.56

* * *

RTO Price based on individual price table = {RTOPT1MT}

This field can be edited manually in the following ways:

It must always start with "{RTOPT" and end with the "}" symbol, between the "{RTOPT" and the trailing "}" you can use the following: A number from 1 to 6 representing the line from the price table. The next character represents the term you want to print in that space. M=Monthly, W=Weekly, B=Bi-Weekly, S=Semi-Monthly, D=Daily. When a "T" follows the term the total RTO price would be printed. Note: Add a "+" at the end of the field if you want the price to be printed to include the default sales tax rate for the store.

Below are some examples or possible fields and a sample of what it would print:

{RTOPT1MT} would print the monthly rate and # of payments with total from the 1st line of the price table in a format like this (for the price table shown below): $50.00 X 18 Months = $900.00

{RTOPT1W} would print the weekly rate and # of payments from the 1st line of the price table in a format like this (for the price table shown below): $12.50 X 78 Weeks

{RTOPT2MT} would print the monthly rate and # of payments with total from the 2nd line of the price table in a format like this (for the price table shown below): $65.00 X 12 Months = $780.00

{RTOPT2MT+} would print the same as above but the amounts would include tax.

![image33](image33.gif)

* * *

RTO Price based on Category markup = {RTO$18MT}

This field can be edited manually in the following ways:

It must always start with "{RTO$" and end with the "}" symbol, between the "$" and the trailing "}" you can use the following: The number 18 can be replaced with any number of MONTHS you want the contract to be for. The "M" can be replaced with any term you want to print the price for. M=Monthly, W=Weekly, B=Bi-Weekly, S=Semi-Monthly, D=Daily. When a "T" follows the term the total RTO price would be printed. Note: Add a "+" at the end of the field if you want the price to be printed to include the default sales tax rate for the store.

Below are some examples or possible fields and a sample of what it would print:

{RTO$18M} would print: $31.78 X 18 Months

{RTO$18W} would print: $15.89 X 78 Weeks

{RTO$18W+} would print: $17.00 X 78 Weeks < This would include tax in the amounts E.G. $15.89 + 7% tax = $17.00

{RTO$18MT} would print: $31.78 X 18 Months = $572.04

{RTO$18MT+} would print: $34.00 X 18 Months = $612.00 < This would include tax in the amounts E.G. $31.78 + 7% tax = $34.00 X 18 = $612.00

If you want the payment printed without the dollar sign add "no$" in the code such as: {RTO$18MT+no$} 

To split the payment amount, number of payments and total into separate fields add -p for payment amt, -# for # of pmts or -t for the total contract field. Example 

{RTO$18MT+-p} would print "34.00"

{RTO$18MT+-#} would print "18"

{RTO$18MT+-t} would print "612.00"

* * *

RTO Price based on RTO$ field as total contract amount = {RTOF$18MT}

This field can be edited manually in the following ways:

It must always start with "{RTOF$" and end with the "}" symbol, between the "$" and the trailing "}" you can use the following: The number 18 can be replaced with any number of PAYMENTS you want to print the price for. The "M" can be replaced with any term you want to print the price for. M=Monthly, W=Weekly, B=Bi-Weekly, S=Semi-Monthly, D=Daily. When a "T" follows the term the total RTO price would be printed.

Below are some examples or possible fields and a sample of what it would print (if the RTO$ field is "1556.10" for the item):

{RTOF$18M} would print: $86.45 X 18 Months

{RTOF$78W} would print: $19.95 X 78 Weeks

{RTOF$78WT} would print: $19.95 X 78 Weeks = $1556.10

Note: To print labels using this function you must use a label printer that prints labels one at a time. Examples of these printers are Seiko Smart Label Printers or Dymo Labelwriter Printers. These printers are widely available at office supply stores and online computer stores such as [www.globalcomputer.com](http://www.globalcomputer.com) and [www.pcmall.com](http://www.pcmall.com).

Note: This feature was developed and tested with a Seiko SLP200 and a Dymo LabelWriter Turbo 330, though it should work the same with any brand of label printer.
