# http://www.rtopro.com/help/help_desk_maine_letters_right_to_cure_and_5_day_demand.htm

# Maine Letters Right to Cure and 5 Day Demand

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Maine Letters Right to Cure and 5 Day Demand

|  [](extra_paiddown_feature.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](help_desk_server_not_found.md "Next Topic")  
---|---  
  
Beginning in Version 5.2.64 of RTO Pro you can print Maine required letters from the On Screen Account Manager. First you have to check the "This store is in Maine" checkbox in Store Information Setup under the Store Setup tab.

The letters have to be present on the server computer with the file names below:

"Datapath + \docs\mainefivedaydemand.rtf"

"Datapath + \docs\mainerighttocure.rtf"

The fields that can be used in the letter are below, note they have to have the {} around them:

{store} store name

{staddr1} store address line 1

{staddr2} store address line 2

{phone} Store phone#

{acct} Cust acct #

{date} todays date

{name} customer name

{altname} alternate cust name

{addrapt} customer address line

{citystzip} customer city st zip

{zipbarcode} zip barcode

{hmphone} customer home phone

{wkphone} customer wk phone

{messphone} message phone

{cellphone} cell phone#

{otherphone} other phone #

{totaldue} total line from OSAM for this contract

{duedate} contract due date

{nextdue} next due date from OSAM

{other} other amount from OSAM

{lastdatefp} today + 10 days

{contr} contract #

{de1} - {de10} Inventory description

The description line should be as shown below, comma's will be inserted in code if multiple inventory is present

{de1} {de2} {de3} {de4} {de5} {de6} {de7} {de8} {de9} {de10}
