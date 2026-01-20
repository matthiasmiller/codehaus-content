# http://www.rtopro.com/help/rto_pro_manual_store_setup_information.htm

# Store Setup Information

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** RTO Pro Manual >

# Store Setup Information

# 

|  [](rto_pro_manual_beginning_to_load_you_customer_and_inventory_data_.md "Previous Topic") [](welcome_welcome_1.md "Parent Chapter") [](rto_pro_manual_additional_information_for_network.md "Next Topic")  
---|---  
  
Main Menu Option "5" Setup Option "1"

Not all items in Store Setup have a description here, however all of the items in Store Setup have a detailed description for them that is displayed at the bottom of the screen when the item is selected. To display the description click on the line you wish to see the description for. [Click here to see a full listing of options in setup with descriptions](help_desk_setup_details.md) (look in help file if you are reading this in the manual... F1 from RTO Pro).

The image below shows how the description (circled in red at the bottom) is displayed when a setting is selected. 

![clip0006](clip0006.png)

When you first start using RTO Pro the first thing you should do is setup your store information. Fill in the blanks with your store information. The ADDRESS and PHONE #, will be printed on receipts the way it is entered here. The Store Name is automatically filled in from the registration info. Note: If you format the city state and zip line as shown (City, ST Zip), your state will show as default when loading new customers.

The DISCOUNT FOR EARLY PAYOFF ON RENT-TO-OWN is the discount rate that you give on Rental Contracts for early payoff if any this will only affect "R" or Rent-To-Own type contracts. Enter "0" if you do not offer an early payoff discount.

DO NOT ALLOW DISCOUNT WHEN IN THE FINAL ? MONTHS OF CONTRACT This is used when you do not allow an early discount when in the final # of months of the contract, enter the # of months here.

The STORE NUMBER is for multiple store operations and will activate the Transfer Inventory capabilities between stores. For single store operations enter "0", for multiple store operations enter a unique store number for each store between 1 and 99. See [Special Considerations for Multiple Stores.](rto_pro_manual_special_considerations_for_multiple_stores.md)

USE ZONES FOR OVERDUE CUSTOMERS Answer yes to this if you wish to separate your customers into zones for multiple account managers.

THIS STORE SENDS DATA TO A RTO PRO HOME OFFICE MODULE Check this box if you have purchased the RTO Pro Home office and you wish to have this store send data to the home office. The actual data sending is handled through the [Income and Deposit Report](help_desk_income_and_deposit_report.md) program.

DIRECTORY FOR DATA FILES is to select the directory on your computer or a computer on your network that is to be used for the master Database files. All computers on the network running RTO Pro must use the same Data files. You can either enter the path or click on Search and use the directory listing to find the Master Data Directory. If you are not using a network then the directory should be the directory that RTO Pro was installed in. Default = C:\RTOwin (Note: This is only in the Demo and Network Versions of RTO Pro).

SALES TAX TAB

The DEFAULT SALES TAX RATE is the rate that will be charged automatically for each sale or rental contract. You can manually change the rate from the default rate on each individual contract if necessary.

In this section you have the option to set rather other charges and GRP charges are taxable in your location.

You also can set the default handling of open sales, either as Accounts Receivable or like a rental. When an open sale is treated like AR the total sale amount is booked as revenue and the entire sales tax amount is treated as being paid the date sold. Payments are then booked as AR Paid without tax. When open sales are treated like a rental the revenue and tax are booked when actually paid. The option of how to treat open sales can be set at the time of loading a sale also, this is just for the default choice.

LATE FEE TAB

The AUTO LATE FEE can be setup to charge any amount per day late, per monthly late or per payment late. Also you can charge a late fee by % of payment with a min. and max. amount. You have the option to give a grace period before charging late fees, an option to charge every contract when customer has multiple late contracts, an option to charge late fees for everyday or just days you are open. You also can choose which contract types to charge late fees for.

DWF/LDW TAB

The DWF/LDW SECTION allows you to enter the initials for Insurance or the equivalent that you offer. GRP (guaranteed replacement policy), PPP (product protection plan), DWF (damage waiver fee), LDW (loss damage waiver), INS (Insurance) are different options that are commonly used. This section also allows you to have the option of automatic calculation and at the percentage you require. You may also enter a minimum insurance amount. The automatic calculation may be used on your choose of contracts types when loading the contracts. You may override the automatic calculation of the contract types.

OTHER TAB

The OTHER SECTION gives you the ability to enter the next customer account number to assign. You can also use the Auto Generate Serial number feature, which you can select how many digits to use. The Auto Generate Stock number feature allows you to choose the stock number you want to begin with and the amount of digits used. 

This is also where you configure FTP settings, company wide master inventory and remote payments, RTOWebPay settings, Depreciation settings, and customer ratings/statuses.

CONTRACTS TAB

Auto Generate Contract #âs: Set this to yes and enter any prefix and the next number you want to use and RTO Pro can generate contracts numbers automatically.

Do not allow billing or invoicing in this store.: Checking this box will make the billing prompt not display when loading contracts. Check this box if you do not do billing in your store.

By default set contract billed to YES.: This will set all contracts to be billed by default, can be changed to no manually when loading the contract.

Suggest an Inventory Pmt. Rate when loading / printing a contract.: This will cause RTO Pro to automatically fill in a payment rate based on the rate table for each inventory category. The rate tables are setup when a new category is entered and they can be edited from Master Model / Category Maintenance (Inventory Menu option 3). The default or minimum rate table can be setup in Security Features (Setup Menu option 5).

Prompt to print contract if not preprinted when loading.: When this is checked and a contract is loaded in New Rentals / Leases (Point of Sale menu option 2) that was not preprinted you will be prompted if you want to print the contract after loading.

CASH ADVANCE TAB

For Cash Advance use ? days for APR calculation: 365 or 360. Some states require you to use 360 days for a year to calculate the annual interest.

Allow Cash Advance Renewals Without New Contract: Checking this box will allow you to setup Cash Advances so that your customers can renew them by paying the loan fee only and then extending the due date according to the term you setup. Some states allow this. If this box is not checked a new contract must be created each time a cash advance transaction is paid. When this box is checked you can also enter a default number of renewals to allow before requiring the full loan amount to be paid and a new contract to be done to renew.

Do Not Reuse Contract Records For Cash Advance: When you allow renewals you can also check this box to force creation of new contract records for every Cash Advance contract. The advantage of this is you can then pull up individual Cash Advance contracts individually from customer inquiry no matter how many the cash advance agreements your customer has had with you. The disadvantage of this is it can create lots of contract records making it difficult to find a history for a particular closed contract for a customer with many agreements. This feature must be enabled if you require a unique contract number for each agreement even after it is paid out.

When renewing and overdue set next due from paid date. Some states require you to make the next due date calculation from date paid instead of last due date when overdue. Checking this box will enable this feature.

Do NOT print receipt on renewal or New C-A Contract. If you do not want a receipt printed when loading new cash advance contracts and when taking a renewal payment check this box.

BONUS BUCKS TAB

Bonus Bucks is a customer incentive program. Bonus Bucks are setup in the Bonus Bucks tab from Store Setup. Bonus Bucks accumulate when a customer pays payments on time or early. You can determine how much to credit in Bonus Bucks as either a percentage of the payment amount or as a set amount per payment. After Bonus Bucks are accumulated the customer can then use this credit to pay payments or toward down payments on new rentals. You can allow Bonus Bucks to be used toward payments only, new rentals only or both. Bonus Bucks are spent by checking the "Use Bonus Bucks" button which will be visible on the tendered screen from the payment function and/or the new rental function depending on the options you set.. When you check the "Use Bonus Bucks" button the balance of the payment due if any will display so it can be collected from the customer.

When Bonus Bucks are activated revenue reports will show the amount of Bonus Bucks earned and spent. Bonus Bucks spent are automatically taken out of cash revenue figures.

To activate Bonus Bucks check the "Use "Bonus Bucks" in this store." Checkbox and check either the "% of Payment" or the "Set amount" box according to which method you want to use. Enter the percentage of payment to use or the set weekly amount of Bonus Bucks to credit if using the "set amount" option.

When using the "set amount" method you can also enter a minimum payment to credit Bonus Bucks for. For example you may not want to give someone Bonus Bucks if his or her payment is only $2.00 a week. The weekly bonus figure and the minimum payment figure are multiplied by 4 for monthly contracts and by 2 for bi-weekly and semi-monthly contracts.

You determine which contract types to credit Bonus Bucks for by checking the check boxes by the types to include.

Tools Menu

The tools menu has 3 functions which can be accessed by clicking on tools then the desired function, or by pressing Alt-T then using the arrow key to select the function. The functions under the tools menu are described below.

Tax Rate Change

This function will change the tax rate on all open contracts from one rate to another. You will be prompted for the old rate and the new one. All open contracts that match the old rate will be changed to the new rate. This is useful when your tax rate is changed by your state etc. and you wish to change all open contracts to the new rate.

Check Same as Cash Months on Contracts

This function to verify same as cash months on all open contracts. This function will prompt you for the # of months same as cash should be set for then it will automatically check all open contracts to make sure they have that value. If you want to make sure there are no contracts with same as cash enabled set the number of months to 0.

Change All Customers to a Specified Zone.

This function will change all existing customers to a specified zone. If there are customers with zones assigned already you will be prompted how to handle them. You will have the option to leave the current zones that are already assigned or change all to the specified zone. This function is useful when first starting to use zones , you can set all customers to your biggest zone then you only have to change the customers that are in other zones instead of adding zones to all customers.

REGISTER: To register RTO Pro Call (352) 383-9375 to order and you will be given a registration # which will remove the demo restrictions. After registering you will be able to change the store information and also be able to load Rentals and Retail Sales.

To enter the registration # assigned click on the register button on the Store Setup Screen. Enter the store name exactly as registered and enter the registration #, then push Enter or click on the register button. If the databases contain sample data still it will be deleted and new empty databases will be created. After successful registration you will have to restart RTO Pro for the registration to take effect.

Note: When you have a RTO Pro subscription your company name is registered when you install RTO Pro.
