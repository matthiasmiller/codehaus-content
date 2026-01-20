# http://www.rtopro.com/help/importing_payment_transactions.htm

# Importing Payment Transactions

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Importing Payment Transactions

# 

|  [](ss_command_line.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](exporting_data_from_rto_pro.md "Next Topic")  
---|---  
  
Importing Payment Transactions

To import payment transactions you will go to Point of Sale Menu > click the Web Payments button, then click the highlighted link as it shows below "Import a Transaction file". 

Note this feature was added to give you the ability to import payment transactions similar to how webpay payments are handled. Transactions imported through this process will be saved to the webpayments table, the same as regular webpay payments. This feature is offered as-is and we do not provide any other support for using this feature other than this help topic. This feature has a very limited use case, you should test it thoroughly to see if it will work for what you are trying to accomplish before using it in your live processes.

Please note. this is for importing payments for OPEN, active agreements only.

![clip0019](clip0019.png)

Below are file specs for creating XML files for importing payment transactions. See below for a sample XML file.

Below lists the required fields that must be sent as well as optional fields in XML format. In XML the data starts with the field name enclosed in brackets "<>", then the field value then the field name in closing brackets "</>". Like below where "account" is the field name and "101" is the value:

  
| Sample data line | Description of field  
---|---|---  
| <account>101</account> | < Customer Account number  
| Â <contract>110</contract> | < Customers agreement number  
| <transdate>1/19/2010</transdate> | <Transaction date for payment  
| <otherpaid>0.00</otherpaid> | *(optional)<Other charges paid, late fees etc. INCLUDING TAX IF APPLICABLE, if set to be taxable taxes will be taken out when processed. This field is optional, other charges are calculated automatically normally, see the "creditcardnumber" field below for a way to pass other charges instead of them being calculated automatically. There is also an option in Store Setup under the "Other" tab in the Webpay section you can check that would make any money passed here a transaction or convenience fee instead of normal other charges.  
| <totalpaid>1.00</totalpaid> | <Total Paid, this is the grand total paid including rent, all other charges and taxes.  
| <email>ron@rtopro.com </email> | *(optional)<Customer Email  If an email address is passed and the email in RTO Pro system is empty it will be set to the passed email Â   
| <trackingnumber>1263932875454</trackingnumber> | (REQUIRED) <This can use any numbering system you wish but they must be unique numbers. A transaction number can never be re-used in future imported transactions for this store. Please note if you use our webpay service and this feature to import payments there could be a possibility of same tracking numbers being used by the webpay system and your numbering system. When RTO Pro imports payment transactions through this feature it searches for matching records in the webpayments table by contract and trackingnumber. If you try to import a transaction for example for contract "100" and a trackingnumber of 100, and there is a record already present with those values, the transaction would not be imported.  
| <paymentmethod>Credit</paymentmethod> | <Payment method (Credit, ACH or Check)  
| <paymentsubmethod>Visa</paymentsubmethod> | For Credit: Visa, MasterCard, American Express, Discover Â  For Check, check number can go in this field(optional) Â  For ACH  Business =Business checking Checking = Personal Checking Savings = Personal Savings -noprocess = If you have already processed the ACH payment we do not send it through the ACH system on our end.  
| <creditcardnumber>****************</creditcardnumber> | *<The CC number is never actually contained in this file. Due to PCI regulations credit card payments have to be processed on your end (the program / system that creates these files must process the credit card). Â  RTO Pro customers who use Xcharge can save customers credit cards so it would be possible for us to charge to a credit card the customer has on file if this is an option you would like to have. Â  Since the credit card number is never passed we will use this field for the following optional switch: -mylate If you pass this switch late fees will be entered based on the what you send in "otherpaid", without this switch late fees(if any are due) are always collected first and the balance of the payment is applied to rent. For instance if a customers payment = 10 and they have 5 in late fees and you pass a 10 payment with 0 in "otherpaid" without the -mylate switch, 5 would be applied to rent and 5 to late. With the -mylate switch all 10 would be applied to rent and 0 in other.  
| <creditcardexpirydate>08/2011</creditcardexpirydate> | *(optional)<CC exp not required  
| <bankroutingnumber>063000021</bankroutingnumber> | For ACH this would be passed ONLY if you want the ACH to be processed at the store level. Also if you do not want the ACH to be processed on our end you must pass "-noprocess" in paymentsubmethod (see above)  
| <bankaccountnumber>2020000333333</bankaccountnumber> | ââÂ ââ  
| All the fields below are not required and do not have to be sent  | Â   
| <firstname>RON</firstname> | *<Customers first name  
| <lastname>GANUS</lastname> | *<Customers last name  
| <address>PO Box 926</address> | *<Address  
| <city>New Market</city> | *<City  
| <state>MD</state> | *<State  
| <zip>21774</zip> | *<Zip  
| <branch>0033</branch> | *< Store number   
| <duedate>1/16/2010</duedate> | *<Due date at the time of payment  
| <nextdue>1/30/2010</nextdue> | *<Next due date after payment was paid  
| <rentpaid>1.00</rentpaid> | *<Base rent paid ... not required, total rent paid is calculated automatically based on total amount paid.  
| <taxpaid>0.00</taxpaid> | *<Tax paidâ¦ not required total tax is calculated when processed  
| <dwfpaid>0.00</dwfpaid> | *<This holds any deposit money paid, usually extra money paid above normal rent amount that is to be added to the customers deposit amount instead of applied to rent.  
| Â  | * = optional Â   
  
Please note. this is for importing payments for OPEN, active agreements only.

Below is a sample of how an XML file should be formatted for importing into RTO Pro. The sample below has 1 payment transaction in it.

<?xml version="1.0" encoding="utf-8" ?>

<RTOPRO>

<History>

<historydata>

<account>20892</account>

<contract>C3000</contract>

<transdate>07/21/2011</transdate>

<totalpaid>29.00</totalpaid>

<otherpaid>0.00</otherpaid>

<paymentmethod>ach</paymentmethod>

<paymentsubmethod>-noprocess</paymentsubmethod>

<trackingnumber>114</trackingnumber>

<creditcardnumber>-mylate</creditcardnumber>

</historydata>

</History>

</RTOPRO>

Below is a sample with 2 payment transactions in it.

<?xml version="1.0" encoding="utf-8" ?>

<RTOPRO>

<History>

<historydata>

<account>20892</account>

<contract>C3000</contract>

<transdate>07/21/2011</transdate>

<totalpaid>29.00</totalpaid>

<otherpaid>0.00</otherpaid>

<paymentmethod>ach</paymentmethod>

<paymentsubmethod>-noprocess</paymentsubmethod>

<trackingnumber>114</trackingnumber>

<creditcardnumber>-mylate</creditcardnumber>

</historydata>

<historydata>

<account>20900</account>

<contract>C3150</contract>

<transdate>07/21/2011</transdate>

<totalpaid>35.00</totalpaid>

<otherpaid>0.00</otherpaid>

<paymentmethod>ach</paymentmethod>

<paymentsubmethod>-noprocess</paymentsubmethod>

<trackingnumber>115</trackingnumber>

<creditcardnumber>-mylate</creditcardnumber>

</historydata>

</History>

</RTOPRO>
