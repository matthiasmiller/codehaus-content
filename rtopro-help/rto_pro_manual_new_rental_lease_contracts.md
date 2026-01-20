# http://www.rtopro.com/help/rto_pro_manual_new_rental_lease_contracts.htm

# New Rental / Lease Contracts

<< [Click to Display Table of Contents](index.md) >> **Navigation:** RTO Pro Manual >

# New Rental / Lease Contracts

|  [](rto_pro_manual_retail_sales.md "Previous Topic") [](welcome_welcome_1.md "Parent Chapter") [](rto_pro_manual_contract_maintenance_and_inventory_switchout.md "Next Topic")  
---|---  
  
Point of Sale Menu option "2"

[Watch a demo video on our website on loading a rent to own agreement.](http://www.rtopro.com/index_videolb/player.swf?url=video/loadrental.mp4&volume=100)

The first Rental/Lease Contract screen has boxes for customer name or account #. When entering customerâs name put last name first, It is not necessary to type in full name or even the full last name you can just type a few letters of their last name. After you have a name or account # typed in push ENTER and the customer list screen will come up. After selecting the customer from the list the Rental/Lease Screen will come up.

New Customers: If the customer does not show on the customer list screen, from the list screen push Esc to get back to the first screen for Rental/Leaseâs then push F5 to add a new customer record.

When the Rental/Lease Screen comes up you may edit the customer record by pushing F-11.

You continue by entering a model, serial or stock number to search for inventory that is being rented. The inventory list screen will come up select first item, then repeat this process for any additional items rented. After the last item on contract is selected leave the model and serial boxâs blank and push ENTER. The contract information screen will come up, fill in the contract # (This must be a unique number), contract type, payment terms, billed option, # of pmts or # of months, next due date, processing fee, if any (including tax). You can also optionally enter a salesman and if you want to setup the contract to be paid automatically by ACH or Credit Card you can enter the # of payments to auto pay each due date and the # of days before due to autocharge the payment.

Then push ENTER and the rental rate screen will come up. Enter the rental rate for each item, Insurance/damage waiver amount if any. You should then verify the contract amount and cash price displayed on this screen and correct it if needed then push F6 to complete. The tendered screen will come up where you enter the payment form and push Enter to load the contract and to print a receipt / contract.

From the rental rate screen you can also change the # of pmts paid today box if more than 1 payment is being paid or put 0 if nothing is being paid. You can also enter other charges due on next payment and you can change the tax rate for this contract if necessary. If you need to change the contract amount push F12 the number of payments will automatically be changed to match the contract amount entered.

Description of fields entered when loading rental agreements:

Contract #: This is a unique identifier for the contract. This can be set to auto-generate in Store Setup under the "Contracts" tab.

Type: This is the contract type. R = Rent to Own, T = Rent to Rent, L = Lease (no discount for early payoff), A = Airtime Account (similar to rent to rent, does not have a set # of payments), G = As Collection, O = Other. The G and O type can be used for any type of agreement that you need to have revenue separated from normal revenue. On revenue reports G and O type revenue is separate from other types.

Term: This is the term or payment frequency for the agreement. W = Weekly, M = Monthly, B = Bi-Weekly, S = Semi-Monthly, D = Daily.

Billed: This determines whether this agreement will be billed or invoiced automatically when billing is run. Set it to YES if you want to mail invoices to this customer.

# of Months: The number of months the agreement is for, note if this is not a monthly agreement the # of payments field will be converted to the weekly, bi-weekly count automatically. For instance if it is a weekly agreement and you enter 12 months, the # of payments will be set to 52. This field can be left blank and you can simply fill in the # of Payments (the next field).

# of Payments: This is the total # of payments this agreement is for.

Next Due Date: This is the date the customers next payment is due. This is filled in automatically according to the term entered. If you need to change this date you can type in a new date, use the + or - sign to change the date forward or backwards or you can click on a date on the calendar to the left to select the date.

End Rental Date: For Rent to Rent "T" type agreements you can optionally enter a contract end date. This is for rentals like home rentals or any other type of rental where it is rent to rent, but it is for a set term. When the agreement gets within 35 days of the end contract date the payment screen will show that contract line in red, the contract end date will be displayed in the popup display that comes up when you hover over the contract line. This will not prevent you from going beyond that date, it just alerts you so you know it is close to or past the end date. Typically at the contract end date either the contract is extended with possibly a higher rental fee or the contract is closed. 

Processing / Delivery Fee: This is where you put any processing, delivery or any other fee you charge with the new agreement. Note if other charges are taxable you put the total amount including tax here.

Discount % for early payoff for Rent to Own: This will only be displayed if you have Early Payoff Discounts to be set individually for each contract. Enter the discount you give for early payoff, for example for a 40% discount enter ".4".

Salesman: Enter the salesman for this agreement (optional).

PO / Ref#: If your customer needs to have a reference # on invoices enter that # here. This is mainly to print on invoices as a reference for the customer, if you want this field to print on invoices you would have to edit the default invoice and add this field. This is only available when you have 9 or less items on the agreement.

Autocharge this Agreement through Autopay: If the customer wants to pay this contract automatically by credit card or ACH check this box. Leave this unchecked if this agreement is not being paid by Autopay.

* * *

Rate Screen

Accept Y/N: This is set to YES by default which means to put that item on the agreement. If you selected an inventory item by mistake you can set that item to NO and it will be left off the agreement.

Rate: This is the rental rate for the inventory item, for multiple items you should enter a rate for each item. Note this is the rate without tax, tax is added automatically. In Store Setup under the contracts tab you can setup to have the rates entered automatically based on markups entered for categories.

DWF/GRP/LDW: This is for Damage Waiver if the customer is opting for Damage Waiver and you offer it. See the glossary for the definition of damage waiver. Please note the fee amounts saved in the system INCLUDES tax, so the fee you enter should include tax if it is taxable, so for a $5.00 DWF at 6% tax rate you should enter 5.30 as the DWF fee. This fee can be calculated automatically and added to agreements automatically during contract load by default, see Store Setup > DWF tab to set this up.

Club: If you offer Club Program and the customer wishes enter the Club fee here. See the glossary for definition of Club program.

Contract Amount: This is the total of all payments not including tax. This is automatically calculated as "# of payments x payment amount" if you need to change this amount push F12 to edit. Please note this amount is the TOTAL payments not including tax the customer is going to pay you throughout the entire agreement. Shed rental companies often get this amount wrong. If a customer is paying you $500 down + tax and then 36 payments of $100 +tax, the contract amount should be $4100.00 (36 x 100 + 500) NOT $3600.00.

Cash Price: This is the cash price if the customer were to buy it outright.

Same as Cash Exp.: If you offer a "Same as Cash" option enter the last date the Same as Cash offer is good til.

# of Pmts Paid Today: Enter the # of payments the customer is paying down.

Total Down Payment: This is the total amount the customer is paying as a down payment today. This amount includes rent, other charges and tax. Make sure this is correct before you push F6 to complete.

Other Charges Due Next Payment: If the customer has any other extra charges due on their next payment enter the amount here.

Sales Tax Rate: This is the sales tax rate for this agreement.

Deposit Paid: If the customer is paying any deposit along with the down payment enter the amount here. Deposit money is money you are holding for the customer, it is not taxed or applied to the agreement until it is "spent" toward a payment or payoff. Note you should check your state laws before accepting deposits. Among other regulations, some states require you to keep deposit money you are holding in separate bank accounts.

Deposit Spent: If the customer has a deposit balance and wishes to use any of it toward the down payment enter the amount here.

Total W/Deposit: This is the total amount the customer is paying today with any deposit paid added or deposit spent taken out of the total. Ensure this is the total you are actually collecting from the customer before pushing F6 to continue.

* * *

Tendered Screen

Total Due: This is the total down payment due, this amount is the total down payment taken from the previous screen. If this amount is not correct hit the "ESC" key and correct it on the previous screen.

AMT Tendered: This is the amount the customer is tendering or handing to you. This is so the change if any can be determined. For instance the total due could be $50.25 and the customer tenders or hands you a $100 bill, you enter 100 and push enter and the change due of $49.75 would be displayed.

PMT Form: Enter the payment form the customer is using, for instance cash, check etc. You can enter the corresponding letter for the payment form they are using "C", "K" etc. or you can click on the payment form in the list to the right to select.

Check NO: If the customer is paying by check enter the check # here.

Change Due: This is the change due, if any. For instance if the amount they are paying down is $55.00 and the customer tenders or hands you $60.00 you enter 60 in the tendered box and the change due would be $5.00.

"Use Credit Card on file" button: If you process credit cards through RTO Pro with X-charge you can store customers credit card information and click this button to charge this transaction to the credit card on file. If the customer is handing you a credit card as payment you should enter the correct payment form and if you use X-charge the credit card interface will display where you can swipe the card or enter the card #. For more information about processing credit cards through your computer using X-charge or for information about ACH payments call 352-383-9375.
