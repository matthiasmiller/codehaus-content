# http://www.rtopro.com/help/late_fees_by_state.htm

# Late Fees by State

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Late Fees by State

|  [](non_serialized_vs_serialized_i.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](online_signing_center.md "Next Topic")  
---|---  
  
Late fees can be setup differently for each state you do business in. This is setup in Store Setup under the Late Fee tab.

Bellow is an explanation of each field you can enter info for your states late fees.

State: Enter the initials of the state you wish to enter the late fees for, this must be 2 characters and must match the state in the customers address or optionally you can set the system to get the state from the contracts tax zone data.

Start Date: This is the starting contract date this late fee record is for. Each state can have multiple late fees based on contract date. So if you charge your Florida customers who's contract date is 5/1/2015 and after have a $10.00 late fee, but contract dates before 5/1/2015 have a $5.00 late fee, you would create 2 records. One records would have a start date of 5/1/2015 with $10 as the late fee and a 2nd record with a start date of 1/1/2000(if you started business after 1/1/2000) with a $5.00 late fee.

Monthly Late Fee: Enter the late fee for Monthly contracts, if you use a set late fee. If you use late fee by percentage of payment leave this field 0.

Weekly Late Fee: Enter the late fee for Weekly contracts, if you use a set late fee. If you use late fee by percentage of payment leave this field 0.

Monthly charge late fee on ? day overdue: If you charge a late fee on their 5th overdue day enter 5 here, so if they are due on the 1st a late fee would be due if they pay on the 6th or after.

Weekly charge late fee on ? day overdue: If you charge a late fee on their 5th overdue day enter 5 here, so if they are due on the 1st a late fee would be due if they pay on the 6th or after.

Percent for lates by % of pmt: If you charge late fee based on a percentage of their payment amount enter the percentage here. For 2% enter .02.

Min Late Fee for by%: If using late fees by percentage and there is a minimum late fee enter it here. For instance you may charge a 2% late fee with a $5.00 minimum, if so enter "5.00" here.

Max Late Fee for by%: If using late fees by percentage and there is a maximum late fee enter it here. For instance you may charge a 2% late fee with a $10.00 maximum, if so enter "10.00" here.

Store: This is only visible for Central Server companies. If this late fee record is for all companies enter -1 here, otherwise if it is just for one company enter the store number it is for here.

Central Server Notes:

Starting with version 5.9.25 preference is given to matching store over the all stores record. 

So for store 1, a contract in LA, as long as the contract date is 1/15/2020 or newer the top record would be used, no matter what startdate was in the 2nd record. Contracts with contract date before 1/15/2020 would use the 2nd record in the example below. 

![clip0035](clip0035.png)

Before version 5.9.25 below is how it was handled:

Before this update preference was given by newest "Startdate"(as long as the startdate is on or before contract date) for all records with the specific store or -1 as the store.

Below is the SQL string to retrieve the state late fee record for a given store/state for central server. The example below is for the state LA (Louisiana), contract date 3/31/2020, for store 1. It gives preference by the newest "startdate" for any record flagged -1 (all stores), or 1 (store 1 only). So if you have 5 stores for instance that all have the same late fees in LA, and 1 store that has different late fees for LA, be sure you set the start date for the record with store 1 to a newer date than the date with -1 as the store.

select FIRST 1 * from statelatestable where state ='LA' and startdate <= '3/31/2020' and (store = -1 or store=1) order by startdate desc

In the example records below for store 1 any contract in LA with contract date 1/15/2020 or after would use the top record for late fees.

For store 1 any contract in LA with contract date before 1/15/2020 would use the 2nd record for late fees.

For all other stores for contracts in LA the 2nd record would be used.

![clip0035](clip0035.png)
