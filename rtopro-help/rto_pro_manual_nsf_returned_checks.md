# http://www.rtopro.com/help/rto_pro_manual_nsf_returned_checks.htm

# NSF / Returned Checks

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** RTO Pro Manual >

# NSF / Returned Checks

# 

|  [](rto_pro_manual_contract_printing.md "Previous Topic") [](welcome_welcome_1.md "Parent Chapter") [](rto_pro_manual_loaners.md "Next Topic")  
---|---  
  
Point of Sale Menu option "6"

This features allows you to enter NSF or returned checks/ ACH transactions that you receive. After loading them you can take payments on them the same as a regular contract. The income reports will show NSF checks received and paid. 

This function can also print an NSF check letter to be sent to the customer if you wish. The NSF letter can be customized in [Printer Setup](rto_pro_manual_printer_form_setup.md) You can select how many copies of the letter to print and also the tax rate for NSF check charges. The default tax rate for NSF charges can be setup in [Store Setup](rto_pro_manual_store_setup_information.md) .

Below are the definitions of the fields you enter when loading an NSF:

Check#: This is the check number of the NSF you are loading, you should just enter ACH here if it is a returned ACH transaction instead of an actual check.

Check Amount: The actual amount of the check or ACH Transaction.

Check Date: The date you originally processed the original check or ACH payment, in the case of checks this is not always the date on the check itself, it should be the date you accepted the check.

NSF Fee: This is the fee you are charging the customer for the returned Check / ACH, this is typically $20 or more, you should check your state regulations to see what you are legally able to charge for returned checks / ACH transaction.

Bank Name: This is the name of the bank the check or ACH is drawn from, the customers bank.

Signer (if different from primary name): This is for when someone signed the check other than the primary name on the account. The NSF letter will be addressed to this person if this field is filled in, otherwise, the letter will be addressed to the primary account name.

Reason Returned: This is a drop down list where you can choose the reason the item was returned, NSF, Stop Payment, Account closed or ACH error (wrong account number or routing number).

Print Letter: This can be set to either Yes or No, set to yes if you want to print an NSF letter when this item is loaded. NSF letters can be reprinted anytime from the contract info/detail screen (from customer inquiry or F8 from the payment screen, then clicking on the NSF line).

Letter Count: If you want to print an NSF letter enter the number of copies to print here.

Sales Tax Rate for NSF Fees: If NSF fees are taxable in your state enter the tax rate here. If you set the tax rate at .06 and NSF charges to 10.00, when the customer comes in it will show $10.60 due in other charges. The tax is added to the NSF charge amount.

Do Not Accept any more checks or ACH Payments: Check this box if you want to prevent this customer from paying by check or ACH again. If a customer is flagged to not accept checks you cannot use check or ACH as a payment form for transactions. Also if you use the RTOWebpay.com service they would not be able to pay by ACH when paying payments online. This flag can be set / unset from customer maintenance (Payment or inquiry screen, then push F11).

Receipt Number: This is an option where you can enter the original receipt number the returned item paid for.

"Do not collect on this..." check box: Check this box if the item has been sent to an outside collection agent and should not be collected by store personnel, this can be set / unset from contract maintenance. When an item is flagged to not collect you cannot take a payment on the item from the payment screen but instead will be notified the customer has NSF(s) in outside collections.

To load the NSF transaction fill in the necessary fields and push F6 to save. 

When you receive an NSF check, the normal way of handling it is to load an NSF through this function and NOT to back out the payment. If you back out the payment and load an NSF the customer would be double paying. The reason for loading an NSF is because when you receive an NSF check it is treated as a separate collection item, it is now something the customer owes besides their normal payments, this way you can collect an NSF fee and also if not paid you generally have more legal recourse for an NSF check than you do for a normal rental agreement payment. After some time goes by and you do not believe you will be able to collect for the NSF you should charge off the NSF and reverse the payment so you get a credit for any tax in the original transaction.

Another option for handling NSF checks is to just reverse the transaction as soon as you get the returned item and add any NSF to other charges due and NOT use this feature to load the returned item.

NSF and Accounting

Note if you load an NSF transaction instead of reversing the transaction a payment transaction for that amount should generally be added to your checking account register, these is an option to create that transaction in your IIF/QIF file exports in the End of Day Setup, if you use the option to create IIF/QIF files to import into accounting software. [Click here for more info on handling NSF in accounting](nsf-and-accounting.md)
