# http://www.rtopro.com/help/taxjar_refresh_contracts.htm

# TaxJar Refresh Contracts

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# TaxJar Refresh Contracts

# 

|  [](taxjar_integration.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](on_screen_account_manager_report_options.md "Next Topic")  
---|---  
  
This function will update tax zones from current info from TaxJar.

When tax rates are updated for a state, it looks up the state, county, and city rates for the contract and determines if a new tax zone should be created. So if the rate changes for a STATE, COUNTY, CITY then a new taxzone is created for that contract and it is placed in it. So if you previously had:

TJ0001 for TX, JIM WELLS, ALICE at a rate of 0.065, 0.05, 0 and then you ran update and the county rate increased, it would make a new zone:

TJ0002 for TX, JIM WELLS, ALICE, 0.065, 0.055, 0, for example

Technically only the open contracts that are part of the 0.055 county rate would be placed in there. Old contracts would retain their previous tax zone. In other words, we aren't updating tax zones, we're creating new ones when they are required.
