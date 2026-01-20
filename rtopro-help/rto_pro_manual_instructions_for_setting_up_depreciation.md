# http://www.rtopro.com/help/rto_pro_manual_instructions_for_setting_up_depreciation.htm

# Instructions for Setting up Depreciation

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** RTO Pro Manual >

# Instructions for Setting up Depreciation

# 

|  [](rto_pro_manual_special_considerations_for_multiple_stores.md "Previous Topic") [](welcome_welcome_1.md "Parent Chapter") [](depreciation-start-here.md "Next Topic")  
---|---  
  
Before using depreciation in RTO Pro you should consult with an accountant to determine what type of depreciation your business should be using and if you have been depreciating the inventory you will be receiving into RTO Pro before you started using RTO Pro. Before you actually set up and run depreciation in RTO Pro you need to know the answer to these questions.

Depreciation is the method to amortize the cost of assets over their useful life. In a rent to own store you use Depreciation to calculate your cost of inventory. If you purchase a $400 TV to place on rent to own, the IRS does not want you to count the $400 as your cost the month you buy the TV or the month you rent it out, instead you depreciate it over what the IRS considers its useful life (We have been told by accountants in the business that 3 Year MACRS is the depreciation type and length RTO stores are supposed to use according to the IRS... consult legal council or an accounting professional, we do not provide legal or accounting advice). So for the $400 TV your inventory cost for the first year the item was placed in service would be $133.32 (400 x 0.3333, the percentage used for the first year with 3 YR MACRS). This amount would be divided into the monthly depreciation reports you run to get the monthly cost, starting with the month the item is received or rented, depending on your setting to start depreciation as soon as received or to start after an item is rented (this option is set in Store Setup under the "Other tab" in the Depreciation settings section). See the help topic in the help file [Installment vs Rent to Own Accounting](installment_vs_rent_to_own_acc.md) for an example of how a rent to own transaction flows to your accounting records.

The type of depreciation used in RTO Pro is determined by the Inventory's F/P Agent. You can group your inventory by the F/P Agent if you need different types of depreciation for different groups of inventory. Most stores only need to have 1 agent; however there are instances where multiple agents may be useful, for instance if you want to depreciate different groups of inventory with different depreciation methods multiple agents can be used. There is also a special agent you can setup "ALL AGENTS". The ALL AGENTS agent can be used when you want to run just 1 depreciation report for all inventory. If you use the "ALL AGENTS" agent you can use the agent field in inventory to hold vendor, supplier, etc information.

In RTO Pro Depreciation can be setup for Tax and Book accounting purposes using a different depreciation type for each. Most stores only need to run TAX depreciation, the only reason you would need to run tax and book is if you want to use one type of depreciation to calculate for the IRS and a different type for you own internal purposes.

Setting up depreciation can be hard to understand, we recommend you call tech support to help you set it up when you start using RTO Pro. Once it is setup all you have to do is run depreciation reports monthly, you would never have to change the settings for depreciation.

Some examples of how to use agents and how to setup depreciation are below.

Example 1: ABC Rental purchases RTO Pro 11-1-98 and opens their store the same day. They purchase all of their own inventory and do not have anybody floor plan any inventory for them so they do not need a retail inventory agent to track inventory that is floor planned and they do not need to perform flips. They decide they want to use the inventory Agent field to store some other info about the inventory (what lot its on for a portable building business for instance). So therefore they have multiple agents. They want to use the special agent "ALL AGENTS" so they only have to run 1 depreciation report per month. In Agent Maintenance they add the agent "ALL AGENTS" and set it up for the depreciation type they wish to use and set depreciation last run date to 11-1-1998. The other agents they do not setup for depreciation. When they run depreciation the report will depreciate all inventory on 1 report.

Example 2: ABC Rental purchases RTO Pro 11-1-98. They receive all old inventory that they were using a manual system to depreciate with an agent name of "ABC OLD". They do not setup "ABC OLD" for depreciation instead they plan to continue with the manual system to depreciate these items.

All items that have not began depreciating yet and all merchandise received after 11-1-98 they receive with "ABC NEW" as the agent. They set up "ABC NEW" for 3 year MACRS depreciation. They also set up 11-1-98 as the Last Depreciation Ran date. (See Agent Maintenance). Then Monthly after the first of each month they would run a depreciation report for "ABC NEW". (Depreciation reports do not have to be run monthly, you could wait until the end of the year and run all months at one time.)

Example 3: ABC Rental does a lot of retail sales and they want to be able to get retail cost of sale figures weekly. In this case they would want to have at least 2 agents, a retail agent and a rental agent. The rental agent would be setup for the type of depreciation you wish to use. The retail agent would not be setup for depreciation.

ABC Rental purchases RTO Pro 11-1-98. They receive all old inventory that they were using a manual system to depreciate with an agent name of "ABC OLD". They do not setup "ABC OLD" for depreciation instead they plan to continue with the manual system to depreciate these items.

All items that have not began depreciating yet and all merchandise received after 11-1-98 they receive with "ABC RETAIL" as the agent. They also create an agent named "ABC RENTAL" and set it up for 3 year macrs depreciation. They also set up 11-1-98 as the Last Depreciation Ran date.

Once a week, or whenever they wanted they would run a flip report. They select agent to flip from as "ABC RETAIL" and flip to "ABC RENTAL". When they run this report it shows them the inventory that was sold and gives the total cost of sale for these items. It also shows items that are flipped to "ABC RENTAL" (The items flipped to "ABC RENTAL" would be the items that were rented out so that they may begin depreciating.). Monthly they would run the depreciation report for the agent "ABC RENTAL". This report gives them the depreciation or rental cost for the month.

Agents can also be used to handle inventory that is financed or floor planned by banks, etc.

Above are only examples of how depreciation works it is generally different from store to store depending on how you wish to handle it. RTO Pro can also depreciate merchandise that you were doing manually before, however to set it up for that the merchandise must be loaded and then edited for the correct remaining book value (cost â depreciation claimed) and depreciation began date (See Inventory Maintenance). To setup old merchandise for depreciation in the above examples you would load all old inventory that has begun depreciation as "ABC NEW" then edit the RBV Tax (Remaining book value for tax purposes) and optionally RBV Book (Remaining book value for book purposes) values and begin depreciation date, then RTO Pro would depreciate all of the old inventory for you also. Note you would get the RBV tax and RBV book from your old accounting/ depreciation system. For example if you opened your business on 1/1/2010 and start using RTO Pro on 7/1/2011, you should correct the RBV values in RTO Pro to match the RBV values as of 7/1/2011 from your old system you were running depreciation from.

Note to companies who used other software or some manual system to run their store before they started using RTO Pro:  It is recommended you keep pre-RTO Pro and post RTO Pro inventory separate and only have RTO Pro depreciate your new inventory or items you have not previously depreciated and continue to use your previous depreciation system to depreciate your old items(like in example 2 above), unless you have never calculated depreciation and have been in business less than a year and have never reported any depreciation on your inventory to the IRS. The only way RTO Pro can take over depreciation from another system is if the RBV values on old items are correctly entered in RTO Pro manually from the RBV values in your old system or a data conversion is done that brings over the correct RBV's from your old system. You should consult your accountant before making any decisions about depreciation.

An example of how depreciation works in RTO Pro

If you have an item that costs you $1000.00, you receive it in January 2015 and rent it out February 2015 and you elect to start depreciation after an item is rented and use [3 year MACRS GDS 200 DB HY Convention as your depreciation method](depreciation-types-in-rto-pro.md).

January 2015: No depreciation claimed, it was not rented until February. Note in store setup you can elect to start depreciation the month an item is received instead of when it is first rented out.

February 2015: $30.30 depreciation claimed, Remaining Book Value = $969.70

March 2015: $30.30 depreciation claimed, Remaining Book Value = $939.40

...

How this is calculated:

According to IRS Publication 946 (2013), page 73, the 1st year depreciation for 3 YR MACRS GDS 200 DB HY Convention is 33.33% of your cost basis. 

Cost of $1000.00 x .3333 = $333.30 (Depreciation for the entire first year 2015)

$333.30 divided by 11 (since we started depreciating in February we only have 11 months to depreciate the entire years depreciation of $333.30) = $30.30

The item would continue depreciating following this method and the prescribed yearly percentages according to IRS publications until the item depreciates fully through normal depreciation (Remaining book value =0) or if the item is sold or paid out before it fully depreciates the item would fully depreciate the month it is sold or paid out.

Please note using MACRS depreciation methods your depreciation figure can have a considerable jump the last few months of the year if you rent a lot of new items the last few months, since they only have a few months to split the full year depreciation in, or for example if you rent a new item in December only 1 month to take the whole years depreciation in.

See [Depreciation Types in RTO Pro](depreciation-types-in-rto-pro.md)

See [Income Forecasting Depreciation Type](help_desk_income_forecasting_depreciation_type.md)

See [Depreciation / Agent Setup](rto_pro_manual_depreciation_agent_setup.md)

See [Flip Report](rto_pro_manual_flips.md)

See [Depreciation Reports](rto_pro_manual_depreciation_report.md)
