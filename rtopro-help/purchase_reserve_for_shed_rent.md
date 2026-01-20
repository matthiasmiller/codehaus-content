# http://www.rtopro.com/help/purchase_reserve_for_shed_rent.htm

# Purchase Reserve for Shed Rental

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Purchase Reserve for Shed Rental

|  [](help_desk_whatisafederallease.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](installment_vs_rent_to_own_acc.md "Next Topic")  
---|---  
  
Purchase Reserve is a method to "effectively apply" extra cash upfront to the cash price that was developed by the National Barn & Storage Rental Association ([www.nbsra.com)](http://www.nbsra.com\)), this feature has been implemented in RTO Pro according to the their specs.

If this feature is enabled extra money paid down can be applied to purchase reserve to reduce the rental payment amount. The purchase reserve is almost the same as a deposit, except it is used to reduce the payment on the agreement. Also the purchase reserve amount cannot be added to later, it has to be paid up front. It is not taxed until the agreement is paid out and it is refundable to the customer in the event of return of merchandise (minus any back rent and other charges due).

To have a separate agreement for agreements with Purchase Reserve you must save a file named "PR-Agreement.rtf" in your "RTOwin\Docs" folder (For central server companies it needs to be saved in each stores sub folder "RTOwin\Docs\001" for example) on your server computer for RTO Pro. If that file is present it will be the agreement printed when you load an agreement with Purchase Reserve. New contract fields are now available for the Purchase Reserve feature to print the reduced payment amount, regular payment amount, regular contract amount, the purchase reserve discounted contract and payment amounts.

To create or edit a purchase reserve agreement see the form below in Printer/Forms Setup (scroll to the bottom of the form list to see it). If you create the form through the feature below it will save the file with the correct name in the correct location in your "Docs" folder. There is a sample purchase reserve agreement included in the RTO Pro sample documents, double click on the line below in printer/forms setup when no file name is displayed and the sample will be displayed, you can edit it as needed. Be sure your agreement meets all the legal requirements in your state before using it,

![clip0091](clip0091.png)

When using this feature, the extra down payment (Purchase Reserve), is handled like a deposit. It is not revenue and not taxed until it is applied to the payoff of the contract. So at the time of payoff the purchase reserve will be taxed. If the customer decides to return the merchandise you would refund the purchase reserve amount minus any back rent or fees the customer has due, the same as you would a deposit.

When using this feature all agreements with purchase reserve should be paid out through early payoff, they can not be allowed to go to full term. The purchase reserve feature as designed in RTO Pro was to the provided specs that all contracts with Purchase Reserve would be closed as Early Payoff, there is no mechanism to close a purchase reserve contract as paid out from the payment screen, they have to be closed through Contract Close.

To see a sample agreement for purchase reserve see the files at the links below:

[PDF sample http://www.rtopro.com/SamplePR-Agreement.pdf](http://www.rtopro.com/SamplePR-Agreement.pdf)

[RTF sample http://www.rtopro.com/SamplePR-Agreement.rtf](http://www.rtopro.com/SamplePR-Agreement.rtf)

More information is not currently available about this feature, contact tech support or NBSRA @ [www.nbsra.com](http://www.nbsra.com) for more details.

Please note before enabling this feature: If you had the box checked to keep track of extra down payments and loaded agreements with extra down payments, then un-check that box and check the use purchase reserve box, those contracts loaded with extra down payment would be incorrectly handled as if it was purchase reserve paid down.

It's recommended that if you use Purchase Reserve and your early payoff methods could result in a customer having a negative EPO amount you should check the box highlighted below(#35 in Store Setup Main tab), and possibly #36 also. This will prevent taking payments that would result in a negative EPO amount, at that point you could close the contract as Early Payoff instead of taking a normal payment.

![clip0085](clip0085.png)

* * *

Below are notes and comparisons of using Purchase Reserve vs Extra Money Down.

Below is an agreement loaded with purchase reserve

![clip0052](clip0052.png)

![clip0053](clip0053.png)

Note the only amount taxed is the rent paid down, not the purchase reserve, it is treated similar to a deposit.

![clip0054](clip0054.png)

When the agreement is paid out the purchase reserve amount is taxed at that time, see the example above.

Below is an agreement loaded with extra money down feature (not purchase reserve)

![clip0047](clip0047.png)

![clip0048](clip0048.png)

Note the total down payment is taxed

![clip0050](clip0050.png)

Below is what the above agreement would look like if loaded as extra rent down, then you changed the system to use Purchase Reserve, note the customer would incorrectly be charged tax again on the extra rent paid down. This is why you cannot switch between Extra Down and Purchase Reserve without handling those agreements manually or reloading them as purchase reserve.

![clip0051](clip0051.png)

NOTICE:

RTO Pro Software does not provide legal advice and makes no representation nor assurance as to the legality or adequacy of any of the features in RTO Pro. RTO Pro Software urges you to obtain a legal opinion from your counsel as to specific regulations in the states and country in which you operate. This advice should be updated annually. 
