# http://www.rtopro.com/help/depreciation-types-in-rto-pro.htm

# Depreciation Types in RTO Pro

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** »No topics above this level« 

# Depreciation Types in RTO Pro

# 

|  [](welcome_welcome_1.md "Parent Chapter")  
---|---  
  
Types of depreciation that can be used with RTO Pro:

"1 = 'Term of Lease' Straight Line over lease term." : This is straight line depreciation over the term of the lease. The term of the lease is set at the time the first depreciation is ran, so if you rent an item out on 7/1 for 18 month contract and run depreciation on 8/1 the item would depreciate over 18 months, even if it was returned in September and re-rented at 12 months it would continue to depreciate at 18 months straight line until fully depreciated. You can edit the depreciation term manually under inventory maintenance. Straight line is just the cost divided by the depreciation term, for instance an item that costs $180. depreciated straight line for 18 months would depreciate $10 per month.

"2 = 'Modified Term of Lease' No Depr. while In Stock." : Same as above except when an item is returned to stock it does not depreciate.

"3 = 'MACRS GDS 200DB HY Convention 5 Year Recovery Period'" : Modified Accelerated Cost Recovery System, General Depreciation System with 200% declining balance method (200% DB) over a 5-year recovery period. 

"4 = 'MACRS GDS 200DB HY Convention 3 Year Recovery Period'" : Modified Accelerated Cost Recovery System, General Depreciation System with 200% declining balance method (200% DB) over a 3-year recovery period.

"5 = 'Straight Line from date received' # of months is changeable" : This is straight line depreciation from the date received, you select the number of months for recovery period.

"6 = 'MACRS GDS 200DB HY Convention 2 Year Recovery Period" : Modified Accelerated Cost Recovery System, General Depreciation System with 200% declining balance method (200% DB) over a 2-year recovery period.

"7 = 'MACRS GDS 150DB HY Convention 3 Year Recovery Period'" : Modified Accelerated Cost Recovery System, General Depreciation System with 150% declining balance method (150% DB) over a 3-year recovery period.

"8 = 'MACRS GDS 200DB HY Convention 3 Year Recovery Period with 50% bonus for Economic Stimulus Act of 2008" : Modified Accelerated Cost Recovery System, General Depreciation System with 200% declining balance method (200% DB) over a 3-year recovery period, with a 50% "Bonus" depreciation taken in the 1st year. The Bonus part just means that you will be taking more depreciation in the first year than normal but less depreciation in the following years (if an item costs you $100 you will still only get to charge off $100 as cost).

For this depreciation type 1st year is 0.6667 x cost, 2nd year 0.2223, 3rd year 0.0741, 4th year 0.0371

The 2008 act was for 50% 1st year bonus + .5 of normal depreciation %.

Normal 3 yr macrs 1st year = .3333 so with bonus .50 + (.3333 * .5) = .66665 (rounded to .6667)

"9 = 'Income Forecasting Depreciation" : See the help topic [Income Forecasting Depreciation Type](help_desk_income_forecasting_depreciation_type.md) for more info about this depreciation type (this should generally only be used for Book depreciation).

See IRS Publication 946 to see the percentages used to calculate depreciation based on the type of depreciation. 

Here is a link to the PDF Publication 946, this link was good as of 12/2022 <http://www.irs.gov/pub/irs-pdf/p946.pdf> The details for most of the depreciation types can be found on page 69 and 70. If the link does not work for you go to [www.irs.gov](http://www.irs.gov) and search for Publication 946.

Below are some screen shots from page 69 and 70 of Publication 946 (2021) with MACRS depreciation percentages for different recovery periods.

![depreciationclip1](depreciationclip1.png)

![depreciationtable](depreciationtable.png)
