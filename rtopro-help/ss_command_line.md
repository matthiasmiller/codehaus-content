# http://www.rtopro.com/help/ss_command_line.htm

# Checking if Social Security exists by Command Line

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Checking if Social Security exists by Command Line

# 

|  [](importing_customer_info.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](importing_payment_transactions.md "Next Topic")  
---|---  
  
It is possible to have RTO Pro check if a customer with a passed social security number already exists in the database. Below are the command line options and returned file with results.

Command line to use: 

c:\rtowin\rto-win.exe %ssnum 111-22-3333 

(The ssnum can be formatted with or without the "-" 's)

RTO Pro would then create a file in the local folder "ssnum.txt" with the following content possibilities.

***-**-3333 Match Account # 100

Or

***-**-3333 Match Alt-Name Account # 100 (When the SS# matches the alternate name SS#, the spouse etc)

Or

***-**-3333 NO Match

Please note, if there are multiple matches in your database only the first match will be returned.
