# http://www.rtopro.com/help/rto_pro_manual_depreciation_report.htm

# Depreciation Report 

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** RTO Pro Manual >

# Depreciation Report 

# 

|  [](rto_pro_manual_flips.md "Previous Topic") [](welcome_welcome_1.md "Parent Chapter") [](rto_pro_manual_non_serialized_cost_of_sale.md "Next Topic")  
---|---  
  
Inventory Menu Option "7"

This report will calculate your depreciation expense monthly and decrease the inventory items RBV / balance by the amount of depreciation deducted. The FLIPS should be run before the depreciation (if you have rental and retail agents, most stores do not need to run flips). The depreciation can only be run once a month after the first of the month. The only agents that will come up are the ones that are setup for depreciation. See [Depreciation / Agent Setup](rto_pro_manual_depreciation_agent_setup.md).

Depreciation can be setup for Tax and Book accounting purposes if needed. Some stores will set Tax depreciation to 3 year MACRS since that is required by the IRS and set Book depreciation to straight line to give them a more realistic figure for internal P&L purposes.

When you open the Depreciation screen the following information is displayed:

Agent list table has the following fields:

Agent: This is the agent name, the only agents that will display are the ones that have been setup to depreciate (set this up in Agent Maintenance).

Last Run: This is the last date depreciation was ran for this agent, for instance if the last month depreciation was ran for was July 2009 the date displayed here would be 8/1/2009.

Tax Dep. Type: This is the type of depreciation this agent is setup for TAX depreciation.

# of Months for Type 5 Depr.: If you set your depreciation type to 5 (Straight line with # of months changeable) this is the number of months you have it set to depreciate for.

Bonus Depr. Ran Through: If you use the bonus 9-11 depreciation this is the date it has been ran through. Note: The bonus depreciation was only good through 2004.

Book Dep. Type: This is the type of depreciation this agent is setup for BOOK depreciation.

# of Months for Type 5 Depr.: If you set your depreciation type to 5 (Straight line with # of months changeable) this is the number of months you have it set to depreciate for for BOOK type.

Book Last Run: This is the last date depreciation was ran for this agent for BOOK depreciation, for instance if the last month depreciation was ran for was July 2009 the date displayed here would be 8/1/2009.

Other options:

Print Report: Select this if you want to print the report.

Display Report: Select this if you want to display the report (it can be printed after it is displayed).

Print Last Page Only: Select this box if you want to print the last page (summary page ) only.

Sort by Stock Number: Check this box if you want the inventory on the report sorted by stock number instead of model/serial.

Run Book Depreciation instead of Tax: Check this box if you want to run the Book depreciation instead of Tax depreciation.

To the right of the Begin Report button there are two settings that are displayed, the last month of your fiscal year and whether depreciation starts after it is received or after it is rented. Verify these settings are correct for you before running depreciation. These options are set in Store Setup under the Other tab.

When you go into this the agents that can be depreciated will be listed in the grid. Select which agent to run then push F5. You will be prompted are you sure you want to continue. The report will list all inventory under the selected agent, the old RBV/balance, amount of depreciation and the new RBV/balance.

A backup of the depreciation report will be saved in the "\flips" subdirectory of the data directory. The backup file will be named as follows:

Agent name : Month and year depreciation report is for : 001.txt

Example: "ITT Retail Mar-2000 001.txt"

The backup file is a precaution in case the original report is lost there is no other way of recreating the report other than the backup file.

See [Instructions for setting up depreciation.](rto_pro_manual_instructions_for_setting_up_depreciation.md)
