# http://www.rtopro.com/help/customer_import_fields.htm

# Customer Import Fields

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Customer Import Fields

# 

|  [](web_customer_applications.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](webpay_setup.md "Next Topic")  
---|---  
  
Customer / Agreement / Inventory data that can be imported into RTO Pro.

Please note the field names must match the names exactly as they are below, they are NOT case sensitive.

Note the fields below are laid out in 3 sections, but any data imported must be included in ONE file. Below is a list of what can be imported

1\. Customer info only. 

2\. Customer and contract info.

3\. Customer, contract and the inventory on the contract. 

[If you want to import inventory ONLY see this help topic.](autoreceivefromxmlfile.md)

You can require any data you wish on your web applications page or import file, however the only data RTO Pro requires is the "NAME" or "FIRST" AND 'LAST" fields. 

Please note all date fields must be formatted "m/d/yyyy" or "m-d-yyyy". All dollar value fields must be passed without a dollar sign and without commas, for example pass $1,000.00 as "1000.00". 

Ref# | Field Name | Max characters and type | Description  
---|---|---|---  
1 | ACCOUNT | 10 numeric | Note this will be generated for new customers automatically, this should NEVER be passed for NEW customers. For existing customers this should be passed if known. If this is not passed a social security number search will be performed, if a match is found with the same SS# and last name the existing record will be used. No changes to the existing record will be made, any address or other info will have to be updated manually.  
2 | NAME | 35 alphanumeric | Full name formatted: LAST,FIRST. The first and last name can be sent separately instead, see below.  
3 | FIRSTNAME  | 35 alphanumeric | First name if sending first and last separate.  
4 | LASTNAME | 35 alphanumeric | Last name if sending first and last separate.  
5 | ALTNAME | 35 alphanumeric | Co-Renter or spouse full name formatted: LAST,FIRST The first and last name can be sent separately instead, see below.  
6 | ALTFIRSTNAME | 35 alphanumeric | Alternate first name if sending first and last separate.  
7 | ALTLASTNAME  | 35 alphanumeric | Alternate last name if sending first and last separate.  
8 | ADDRESS | 35 alphanumeric | Customers street or mailing address  
9 | APT | 35 alphanumeric | Apartment info  
10 | CITY | 20 alphanumeric | Address city  
11 | STATE | 4 alphanumeric | Address state  
12 | ZIP | 10 alphanumeric | Zip or postal code  
13 | HMPHONE  | 12 characters  | Home Phone # (formatted like 3523839375 or 352-383-9375)  
14 | WKPHONE | 12 characters | Work Phone # (formatted like 3523839375 or 352-383-9375)  
15 | MESS | 12 characters | Message phone # (formatted like 3523839375 or 352-383-9375)  
16 | CELL | 12 characters | Cellular phone # (formatted like 3523839375 or 352-383-9375)  
17 | PHONE5 | 12 characters | Other phone # (formatted like 3523839375 or 352-383-9375)  
18 | WORKEXT | 5 alphanumeric | Extension for work #  
19 | DIRECTIONS  | 140 alphanumeric | Directions to home or physical address.  
20 | ZONE | 15 alphanumeric | This is the customer zone / route.  
21 | RATING | 5 alphanumeric | If this value is not passed the default value for pending applications will be assigned to all imported applications, you set this up in Store Setup under the "Other" tab.  
22 | SS1 | 11 numeric | Primary social security number. Please note if SS1 is passed a check will be performed to see if there is a matching SS1 and last name in your customer records, if a match is found a new customer record would not be added. This can be formatted 111223333 or 111-22-3333  
23 | SS2 | 11 numeric | Co-renter / spouse social security number. This can be formatted 111223333 or 111-22-3333  
24 | DOB1 | date | Date in format MM/DD/YYYY Primary date of birth  
25 | DOB2 | date | Date in format MM/DD/YYYY Co-renter / spouse date of birth  
26 | DL1 | 25 alphanumeric | Primary drivers license #  
27 | DL2 | 25 alphanumeric | Co-renter / spouse drivers license #  
28 | EMAIL | 50 alphanumeric | Email address  
29 | LANGUAGE | 10 alphanumeric | Language spoken by customer  
30 | ACHACCT | 17 numeric | Customer bank account number if they are setting up ACH payments  
31 | ACHROUTE | 9 numeric | Customer bank route number if they are setting up ACH payments  
32 | ACHACCTTYPE | 2 characters | Customer bank account type if they are setting up ACH payments (must be one of the following "PC" = personal checking, "BC" = business checking, "PS" = personal savings, "BS" = business savings)  
33 | AUTOCHARGEFORM | 1 character | 0 = Autopay to be paid by Credit Card, 1 = Autopay to be paid by ACH (If customer's agreement(s) setup for Autopay) Note this field was added 12/17/2013  
34 | HOWLONGCURRENT | 10 alphanumeric | How long at current address, can be a date or something like "5 years"  
35 | RENTERSEX | 1 character | Sex of renter (M or F)  
36 | CORENTERSEX | 1 character | Sex of co-renter (M or F)  
37 | RENTERHEIGHT | 4 alphanumeric | Height of renter... 5'11 for example  
38 | CORENTERHEIGHT | 4 alphanumeric | Height of co-renter  
39 | RENTERWEIGHT | 4 alphanumeric | Weight of renter  
40 | CORENTERWEIGHT | 4 alphanumeric | Weight of co-renter  
41 | RENTEREYES | 4 alphanumeric | Renter eye color  
42 | CORENTEREYES | 4 alphanumeric | Co-renter eye color  
43 | LANDLORDORMORT | 35 alphanumeric | Landlord or mortgage company name  
44 | LANDLORDADDRESS | 35 alphanumeric | Landlord / mortgage address line 1  
45 | LANDLORDADDRESS2 | 35 alphanumeric | Landlord / mortgage address line 2 (city, state, zip)  
46 | LANDLORDPHONE | 12 characters | Landlord / mortgage phone number  
47 | PREVADDRESS | 35 alphanumeric | Renters previous address  
48 | PREVCITYSTZIP | 35 alphanumeric | Renters previous address line 2 (city state zip)  
49 | HOWLONGPREVIOUS | 10 alphanumeric | how long at previous address  
50 | WORK1 | 35 alphanumeric | Renters work place  
51 | WORKADD1 | 35 alphanumeric | Renters work address  
52 | WORKADD21 | 35 alphanumeric | Renters work address line 2 (city, state, zip)  
53 | WORKPH1 | 12 characters | Renters work #  
54 | WORKEXT1 | 8 characters | Extension for work #  
55 | WORKSUPER1 | 35 alphanumeric | Work supervisor  
56 | WORKSTARTED1 | 15 alphanumeric | When renter started this job  
57 | OCCUPATION1 | 15 alphanumeric | Renters occupation / job title  
58 | HOURS1 | 15 alphanumeric | work hours  
59 | PAYDAY1 | 15 alphanumeric | pay day  
60 | WORK2 | 35 alphanumeric | Co-renter work place  
61 | WORKADD2 | 35 alphanumeric | Co-renter work address line 1  
62 | WORKADD22 | 35 alphanumeric | Co-renter work address line 2  
63 | WORKPH2 | 12 characters | Co-renter work #  
64 | WORKEXT2 | 8 characters | Co-renter work extension  
65 | WORKSUPER2 | 35 alphanumeric | Co-renter work supervisor  
66 | WORKSTARTED2 | 15 alphanumeric | Co-renter work started  
67 | OCCUPATION2 | 15 alphanumeric | Co-renter occupation / job title  
68 | HOURS2 | 15 alphanumeric | Co-renter work hours  
69 | PAYDAY2 | 15 alphanumeric | Co-renter pay day  
70 | CAR1 | 30 alphanumeric | Vehicle #1 info  
71 | LPLATE1 | 15 alphanumeric | Vehicle #1 license plate  
72 | CAR2 | 30 alphanumeric | Vehicle #2 info  
73 | LPLATE2 | 15 alphanumeric | Vehicle #2 license plate  
74 | COMMENTS | 1000 alphanumeric | This could be used to hold order info or requested merchandise, prices etc.  
75 | PAYPERIOD | 15 alphanumeric | pay period for renter  
76 | PAYAMT | numeric decimal(18,2) | Pay amount for renter, per pay period  
77 | ADSOURCE | 15 alphanumeric | ad source... where did they hear about you  
78 | BANKNAME | 20 alphanumeric | Bank name for non ACH purpose  
79 | BANKPHONE | 12 characters | bank phone #  
80 | BANKACCT | 20 alphanumeric | bank account number for non ACH purpose  
81 | CCACCT | 50 alphanumeric | This is for when passing a credit card token ONLY, it must be formatted "token~~cclast4", for instance "78fhg656ern~~5746"  
82 | CCEXP | 4 numeric | Credit card expiration formatted MMYY, so for instance "0623" for expiration June 2023  
83 | CCTYPE | 1 numeric | Credit card type 1 character, V, M, D or A (Visa, MC, Discover, Amex)  
84 | CCSTREET | 10 alphanumeric | Billing street number for the CC address, number only, not the street name. For instance 1500 W Main St you would pass "1500" only  
85 | CCZIP | 5 alphanumeric | Billing zip code for the credit card token passed  
86 | CELLOPT | 1 numeric | 2 = opted in for SMS, 3 = opted out for SMS  
87 | CELLOPT2 | 1 numeric | 1= Phone5 is a cell, 2 = opted in for SMS and is a cell number, 3 = opted out for SMS and is a cell number  
88 | COUNTY | 20 alphanumeric | The County for the customers address  
89 | EMAILINV | 1 numeric | 0 = Customer is not invoiced by email only, 1 = Customer IS invoiced by email only (added in update 11/27/2023)  
  
Reference info

Ref# | Field Name | Max characters and type/ Description  
---|---|---  
90 | REFERENCE1  | max 35 characters reference #1 name  
91 | REFADD1  | max 35 characters reference #1 address  
92 | REFADD21 | max 35 characters reference #1 address line 2  
93 | REFRELATION1 | max 15 characters reference #1 relation to renter  
94 | REFPHONE1 | max 12 characters reference #1 phone number  
  
the fields above can be repeated for up to 6 references, the 2 at the end below (highlighted in yellow) can be changed to 3,4,5 or 6.

REFERENCE2

REFADD2

REFADD22

REFRELATION2

REFPHONE2

Agreement and inventory info that can be imported into RTO Pro

Please note all value fields below such as "PMT", "AMTPAID" must be passed without a dollar sign and without commas, for example pass $1,000.00 as "1000.00". Note there are no minimum requirements for agreement info, agreement info does not have to be passed at all to just load a pending customer without a pending agreement attached.

Ref# | Field Name | Max characters and type | Description  
---|---|---|---  
95 | CONTRACT | 10 alphanumeric | Contract or agreement number. Note this will be generated automatically if not passed.  
96 | DUEDATE | Date | The contracts next due date after any down payment  
97 | CONTRACTDATE | Date | The date of the agreement, starting date  
98 | PMT | Numeric | The total pre-tax rent only amount of the payment. Note if you are including inventory items in the imported data send the rates in the individual items(see "rate1-10" below) and leave this as 0.00.  
99 | GRP | Numeric | DWF / LDW amount per term, commonly known as Damage Waiver  
100 | CONTRACTAMT | Numeric | Total contract amount (pmt x payments). This will be calculated automatically if not passed  
101 | AMTPAID | Numeric | Total regular paid down, including rent, DWF, club, other charges and tax. Customer deposit IS NOT included. Extra money paid down is NOT included in this figure.  
102 | OTHERPAID | Numeric | Other charges paid down, delivery + any processing fee etc.  
103 | CLUBPAID | Numeric | This field holds the portion of "OTHERPAID" that was delivery charge. So if they paid 5 processing + 10 delivery, OTHERPAID = 15, CLUBPAID = 10  
104 | EXTRARENT | Numeric | For stores that accept "Deposits", you would pass the deposit amount paid down in this field.  
105 | PAIDDOWN | Numeric | For stores that accept extra money paid down to reduce the payment amount or term this is where you would pass the extra amount or down payment that was paid.  
106 | OTHERDUE | Numeric | Any other charges that will be payable next payment  
107 | CHARGESDUE | Numeric | Number of payments paid down (note this will be calculated automatically from AMTPAID, no need to send both).  
108 | CONTYPE | 1 Character | Contract type R, L, T, G or O (R for Rent to Own will be default if not passed).  
109 | TERM | 1 Character | Payment term W = weekly, M = monthly, B = bi-weekly, S = semi-monthly  
110 | PAYMENTS | Numeric | Total number of payments entire contract  
111 | BILLED | See Description > | 1 = This contract should be billed or invoiced automatically (12/31/1899 can also be passed to mean the same thing also, any other date passed would mean the last date this contract was invoiced).  
112 | CASHPRICE | Numeric | Total cash price for ALL inventory on the contract  
113 | SACDATE | Date | Same as Cash expiration date  
114 | CLUBFEE | Numeric | Club fee per payment  
115 | PAYOFFDISCOUNT | Numeric | Payoff discount (discount off balance for EPO (.4 = 40% discount off balance) or % of rent that comes off cash for EPO calculation (.6 = 60% of rent comes off cash price), depending on your store settings). Only needed when you have different discounts for different contracts.  
116 | SALESMAN | 15 Alphanumeric | Max 15 characters. Salesman who sold the agreement, should be the employees 3 character employee ID normally.  
117 | AUTOCHARGEPMTS | See Description> | 1 = this agreement will be setup for Autopay  
118 | AUTOCHARGEB4DUE | See Description> | If setup for Autopay, how many days before the due date should it be paid on (1 = pay 1 day BEFORE due date, -1 = pay 1 day AFTER due date)  
119 | TAXRATE | Numeric | The tax rate that applies to this agreement .06 = 6%  
120 | TAXZONE | 15 Alphanumeric | This is the tax zone record identifier in RTO Pro for this agreement (only required for destination based sales tax states).  
121 | STORE | Numeric | Store # this agreement is for. Only needed for central server systems.  
122 | BOTHSIGN | numeric | not passed or =0 means the renter is signing only. =1 means the co-renter is signing also. This only takes affect when RTO Pro generates a contract on import(that can be set up in Store Setup, and is also used for web dealer e-signing center)  
123 | DEALERID | Numeric | This is an internal field used by the RTO Pro web applications/Dealer E-signature service. It is passed from the dealer e-signature service to identify the dealer who handled the contract. It cannot be used for other import purposes, it links the dealer by the field "dealertable.webid". Please note starting version 5.9.423 if dealerid is passed any inventory included will be assigned to the passed dealer also, unless it is already in your system and has a dealer attached already.   
124 | EPOMETHOD | Numeric | Early Payoff Method. This is optional and can only be included if you have the feature enabled to allow multiple EPO methods within a store. 0 Use Store Default 1 Balance X (1 - Discount) = EPO, 2 Cash - (Amt Paid X Discount) = EPO, 3 Cash X (Remaining Pmts / Total Pmts) = EPO  
  
| The fields below are for importing delivery address and or ship from/source addresses if you use that feature in RTO Pro. The delivery address is for when the delivery is to a different address than the customer address, the ship from or source address is for when the delivery is from a different address than the store address. This can only be passed along with agreement info. This is for sales tax tracking, primarily for use with TaxJar.  
125 | del_address1 | 35 alphanumeric | Delivery address   
126 | del_address2 | 35 alphanumeric | Delivery address line 2  
127 | del_city | 20 alphanumeric | Delivery city  
128 | del_state | 4 alphanumeric | Delivery state  
129 | del_zip | 10 alphanumeric | Delivery zip code  
130 | from_address1 | 35 alphanumeric | Ship from or source address   
131 | from_address2 | 35 alphanumeric | Ship from or source address line 2  
132 | from_city | 20 alphanumeric | Ship from or source city  
133 | from_state | 4 alphanumeric | Ship from or source state  
134 | from_zip | 10 alphanumeric | Ship from or source zip code  
  
* * *

The fields below are to identify inventory on contracts. Up to 10 inventory items can be included for each contract. Each field should be followed by a number 1-10 to specify which line number it is on the agreement (MODEL1, MODEL2 ... MODEL10 etc.) For example the field names for the the 1st inventory item on the contract would be "MODEL1", "SERIAL1", "RATE1", "DATEREC1" etc.

MODEL1-10 | max 15 alphanumeric characters. | Model number of inventory rented 1 - 10.   
---|---|---  
SERIAL1-10 | max 30 alpha characters | Serial number of inventory rented 1 - 10. Note if model is passed but not serial number a purchase order item will be generated. If model and serial is passed and the item is not present in inventory it will be received. If this is for a non serialized item the serial number must be passed as "NON SERIALIZED".  
DESCRIPTION1-10 | max 250 characters. | Description of inventory rented 1 - 10. If not passed description will be retrieved from master model records, if present.  
RATE1-10 | Numeric | Payment amount for each inventory item. Note if you are including inventory items in the imported data pass the rates here only and leave the "PMT" field see above) as 0.00.  
STOCK1-10 | Max 15 numeric | Stock number for the inventory (optional)  
BRAND1-10 | Max 15 alphanumeric | Brand or manufacturer of the inventory  
DATEREC1-10 | Date | Date received. This will be set as today's date if not passed.   
VENDOR1-10 | 15 alpha-numeric characters. | Vendor or supplier of the product.  
COST1-10 | Numeric | Cost of the inventory (your cost, what you paid for it)  
AGENT1-10 | 15 Alphanumeric | Floor plan agent, for depreciation purposes. If not passed the only allowed agent or last agent used will be used (see store setup for only allowed agent setting).  
BOR1-10 | YES or NO | YES is the default if not passed. Yes = this item counts toward BOR numbers, No= it does not.  
CATEGORY1-10 | See > | Category for the inventory. Up to 15 alpha characters. If it is a sub-category up to 31 characters formatted like "MAIN:SUB".  
INVOICE1-10 | 20 max alphanumeric | Invoice number for this inventory.   
RETAIL1-10 | Numeric | Retail or Cash price for this item.   
RTO1-10 | 15 max alphanumeric | RTO field. [See the help topic here for more info on how this field is used.](rto_pro_manual_receiving.md)  
INVCOMMENTS1-10 | 200 max alphanumeric | Inventory comments.  
CONDITION1-10 | 15 max alphanumeric | Normally one of the following: "EXCELLENT", "GOOD", "FAIR", "POOR". Optional and only needed for USED merchandise.
