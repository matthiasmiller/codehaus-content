# http://www.rtopro.com/help/excluding_customers_from_webpay.htm

# Excluding Customers From Webpay

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Excluding Customers From Webpay

# 

|  [](processing_web_payments.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](webpay_master_login_and_report.md "Next Topic")  
---|---  
  
You can exclude customers from the Webpay service by customer zone, customer rating/status, and you can also exclude NSF checks from showing up on the Webpay system. 

Create a text file on your server computer named "webpayexclude.txt". This file should have a list of customer zones and / or ratings/statuses you want to exclude from the Webpay process. This file would need to be saved in your RTO Pro folder on the server, the default folder is "C:\RTOwin", however it could be installed anywhere.

Each zone within the file should be on a separate line. To exclude ratings add a "<ratings>" line with the ratings to exclude listed below it. To exclude NSF add "<nonsf>". 

See the example file below, which would exclude the customer zone "ZONE1", exclude ratings 1 and 2 and would exclude NSF checks.

ZONE1

<ratings>

1

2

<nonsf>

The example file contents below would exclude Zone1 and Zone2 only.

ZONE1

ZONE2

The example file contents below would exclude ratings 1 and 2 only.

<ratings>

1

2

Note: Zones are used in RTO Pro to split customers into different areas or routes. This is usually used to separate customers for multiple account managers. Various reports can be ran to only include customers in a specific zone so this can be used for any reason you want to split customers into groups. This is not the same as "Tax Zones".

Prevent a customer from paying online by ACH

When you flag a customer to not accept checks / ACH payments this setting does apply to webpay also. Remember any settings you apply will not take affect on webpay until the next time you sync data to the webpay server.
