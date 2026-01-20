# http://www.rtopro.com/help/help_desk_tax_zones.htm

# Tax Zones

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Tax Zones

# 

|  [](rto_pro_information_backing_up_data.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](taxjar_integration.md "Next Topic")  
---|---  
  
Tax Zones are for use in states with "Destination based tax", which is when the customer is taxed by where they live, or where merchandise is delivered to instead of where the store is located.

In RTO Pro you can setup tax zones in Store Setup under the Sales Tax tab. You should have a Tax Zone for every area that you deliver to. Generally this is for each city and also a separate county zone for customers who are outside city limits.

Below is a screen shot of Setup Tax Zones form. The top line with the "*" to the left of it is where you enter new zones. Any of the zones already loaded can also be edited from this screen by clicking on the field you wish to edit and simply typing the changes and then pushing enter.

The City State and County rates must equal the total rate. The Other Taxable is to set whether other charges are taxable for this zone.

If you fill in the City, County and State amounts correctly the [Sales Tax Report](rto_pro_manual_sales_tax_report.md) in RTO Pro will break down the amounts collected into amounts collected for each of these regions which will make it easier to fill out tax reports.

Description of fields:

Tax Zone: This is a number to represent the Tax Zone, it can be up to 5 numeric characters. Zip codes are commonly used as the Tax Zone.

Description: This is the description of the Tax Zone. Up to 35 alphanumeric characters.

Total Rate: This is the total tax rate for this tax zone. Entered in the format ".07" for 7%. Note that this is the total tax rate, including any state, county and city rates.

State Rate: This is the portion of the total rate that is the state rate.

County Rate: This is the portion of the total rate that is for the county, if any.

City Rate: This is the portion of the total rate that is for the city, if any.

Other Taxable: If other charges (late fees, delivery/processing fees) are taxable in this tax zone check this box.

State: This is to enter the state this tax zone is in. If this field is filled in the [Sales Tax Report](rto_pro_manual_sales_tax_report.md) will subtotal by state if you have more than 1 tax zone in a state.

If you have Tax Districts enabled you will also have the fields below (Enable by clicking Function Keys > Enable Tax Districts):

TD1: Tax District 1 description, code, number etc. Whatever you want to identify the tax district by.

TD1Rate: Tax rate for tax district 1.

TD2: Tax District 2 description, code, number etc. Whatever you want to identify the tax district by.

TD2Rate: Tax rate for tax district 2.

TD3: Tax District 3 description, code, number etc. Whatever you want to identify the tax district by.

TD3Rate: Tax rate for tax district 3.

Tax districts are for states such as Texas that have state, county, city and special tax districts that you have to collect and remit tax for. Please note sales tax reports will have totals for matching tax district, so for instance any tax zone that contains a tax district "100" for instance, no matter which tax district space it is put in, all revenue and tax collected for districts matching "100" would be added together and totaled on the report.

![image44](image44.jpg)

Below is a screen shot of the form you use to select a Tax Zone while loading a new transaction. It is the same as the form above except it is not in edit mode so you cannot make any changes to the zones or add new zones unless you push F5 to turn edit mode on.

You can sort by any field by clicking on the header for the field you wish to sort by. Clicking on the header again will switch the sort method from descending to ascending.

To select a zone simply highlight the zone and push enter or double click on it with your mouse.

![image47](image47.jpg)
