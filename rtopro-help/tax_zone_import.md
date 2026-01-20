# http://www.rtopro.com/help/tax_zone_import.htm

# Tax Zone Import

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** »No topics above this level« 

# Tax Zone Import

# 

|  [](welcome_welcome_1.md "Parent Chapter")  
---|---  
  
To import Tax Zones go to Setup Menu > Store Information Setup, click on the Sales Tax tab, click the Edit Tax Zones button, then click "Function Key" menu > Import Tax Zone info from CSV file.

The tax zone import can import CSV files only. A CSV file is a plain text file with values separated by commas. You can export Excel files to CSV files in Microsoft Excel and other spreadsheet software. With this feature and the Tax Zone export feature you can now export to XLS, open the file in Excel, made edits, save to CSV, then import with the changes.

Below are the fields that can be imported. Note the fields can be in any order.

Field name | Alternate field names that can be used | Description | Required  
---|---|---|---  
zone | tax zone | This is the Tax Zone identifier, 15 alpha numeric characters max | Yes  
taxrate | total rate | Total tax rate, including state and all local taxes.  | Yes  
staterate | state rate | Tax rate for state | Yes  
countyrate | county rate | Tax rate for county | No, but all rates together must = taxrate  
cityrate | city rate | Tax rate for city | No, but all rates together must = taxrate  
state |   
| State abbreviation, 2 characters max | NO, but should be included  
county |   
| County name 25 characters max | NO  
city |   
| City name 25 characters max | NO  
othertaxable | other taxable | Other charges are taxable "True" or "1" for taxable (defaults to not taxable) | NO  
deliverytaxable | delivery taxable | Delivery charges are taxable "True" or "1" for taxable (defaults to not taxable) |   
  
processtaxable | process taxable | Processing charges are taxable "True" or "1" for taxable (defaults to not taxable) |   
  
store |   
| Store number this zone is for (defaults to 0, all stores) | NO  
td1 | tax distr 1 | Tax District 1 description, max 25 characters | NO  
td1rate | td1 rate | Tax District 1 tax rate | NO  
td2 | tax distr 2 | Tax District 2 description, max 25 characters | NO  
td2rate | td2 rate | Tax District 2 tax rate | NO  
td3 | tax distr 3 | Tax District 3 description, max 25 characters | NO  
td3rate | td3 rate | Tax District 3 tax rate | NO  
epozone |   
| Zone to use for early payoff in this zone | NO  
isactive |   
| 1 for active, 0 inactive (defaults to active) | NO  
  
All rates can have values ".06" or "6%" for 6% for example.

The CSV file must have headers in the first line of the file, the fields can be in any order.

Any tax rate changes on contracts that are made as a result of an import file will be recorded in security, the same as when individual changes are made to a contract.

Below is an example of a CSV file with tax zone data

Tax Zone,Description,Total Rate,State Rate,County Rate,City Rate,State,County,City,Other Taxable,Delivery Taxable,Process Taxable,Tax Distr 1,TD1 Rate,Tax Distr 2,TD2 Rate,Tax Distr 3,TD3 Rate,EPOZONE,ISACTIVE

0001,"""test a long description of the tax zone here xxx""",0.06,0.06,0,0,GA,ORANGE,,True,True,False,TEST45,0,0,0,me,0,,1

0001EPO,test long zone,0.07,0.07,0,0,FL,,,True,True,True,,0,,0,,0,,1

0002,test,0.08058,0.04225,0,0.03833,GA,LAKE,,True,True,True,TEST D1,0,0,0,True,0,,1
