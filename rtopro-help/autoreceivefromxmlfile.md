# http://www.rtopro.com/help/autoreceivefromxmlfile.htm

# Auto receive / import inventory from XML or CSV file

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** »No topics above this level« 

# Auto receive / import inventory from XML or CSV file

# 

|  [](welcome_welcome_1.md "Parent Chapter")  
---|---  
  
To receive inventory from a file you can use a command line(see below) or go into RTO Pro > Inventory Menu > Receiving > Receive from CSV or XML File, then browse and select the file.

Example of using the auto receive inventory by XML file passed as switch to RTO Pro. Note CSV files can also be used now, [click here for info on receiving by CSV file.](autoreceivefromxmlfile.md#autoreceivebycsvfile)

Below is an example of the command line you would use to pass the file containing the inventory data to RTO Pro. The "c:\xmlfiles\myxml.xml" would be changed to the actual path to your file.

rto-win.exe -r c:\xmlfiles\myxml.xml

Add "-noopen" switch if you want the report to not display after the process runs, like:rto-win.exe -r --noopen c:\xmlfiles\myxml.xml

Below are the field names and descriptions, with a * are required, the fields can be in any order, field names are not case sensitive

<model> *Model alphanumeric 15 characters max

<serial> *Serial alphanumeric 30 characters max. If this is for a non serialized item the serial number must be passed as "NON SERIALIZED".

<stock> Stock number numeric 15 characters max (if auto stock numbers are set in RTO Pro this will be generated if not passed otherwise 0 if not passed)

<daterec> Date received, defaults to today if not passed, please note this date must be in US format such as "12/31/2013" or "12-31-2013"

<cost> Inventory cost

<balance> RBV Tax, defaults to cost if not passed

<rbvbook> RBV Book, defaults to cost if not passed

<description> Description alphanumeric 250 characters max

<invoice> Invoice number alphanumeric 15 characters max

<brand> Brand or manufacturer. alphanumeric 15 characters max

<category> Inventory category, defaults to "NONE" if not passed 31 characters max(15 main category, 15 sub category with a : separating for instance "APPLIANCE:WASHER", sub category is optional)

<vendor> Vendor for this item alphanumeric 15 characters max

<AGENT> FP agent, defaults to "NONE" if not passed. alphanumeric 15 characters max

<BOR> BOR YES or NO defaults to YES if not passed

<RENTALRETAIL> Rental or RETAIL, defaults to RETAIL if not passed (rental would make the item show as idle BOR retail would not)

<QUANTITY> Quantity for non serialized or pieces for serialized

<STORE> Store number, defaults to current store if not passed

<RETAIL> Retail price

<RTO> RTO$ field (not used by most but some use it to store total RTO price). alphanumeric 15 characters max

<dealer> Dealer name 75 alpha numeric characters maximum. The Dealer to save for the inventory item. If the dealer does not exist in the dealer table it will be added.

Below is an example of how the XML file should look

<rtoproinventory>

<record>

<model>T1000</model>

<serial>T1000SER</serial>

<stock>1000</stock>

<daterec>1/17/2011</daterec>

<cost>100</cost>

<balance>100</balance>

<rbvbook>100</rbvbook>

<description>T1000 test load</description>

<invoice>1000</invoice>

<brand>BRandT1000</brand>

<category>WASHER</category>

<vendor>TvENDOR</vendor>

<AGENT>RENTALAGENT</AGENT>

<BOR>YES</BOR>

<RENTALRETAIL>RENTAL</RENTALRETAIL>

<QUANTITY>1</QUANTITY>

<STORE>1</STORE>

<RETAIL>300</RETAIL>

<RTO>100</RTO>

</record>

<record>

<model>T1000</model>

<serial>T1000SER1</serial>

<stock>1001</stock>

<daterec>1/17/2011</daterec>

<cost>100</cost>

<balance>100</balance>

<rbvbook>100</rbvbook>

<description>T1000 test load</description>

<invoice>1000</invoice>

<brand>BRandT1000</brand>

<category>WASHER</category>

<vendor>TvENDOR</vendor>

<AGENT>RENTALAGENT</AGENT>

<BOR>YES</BOR>

<RENTALRETAIL>RENTAL</RENTALRETAIL>

<QUANTITY>1</QUANTITY>

<STORE>1</STORE>

<RETAIL>300</RETAIL>

<RTO>100</RTO>

</record>

<record>

<model>T1000</model>

<serial>T1000SER2</serial>

<stock>1002</stock>

<daterec>1/17/2011</daterec>

<cost>100</cost>

<balance>100</balance>

<rbvbook>100</rbvbook>

<description>T1000 test load</description>

<invoice>1000</invoice>

<brand>BRandT1000</brand>

<category>WASHER</category>

<vendor>TvENDOR</vendor>

<AGENT>RENTALAGENT</AGENT>

<BOR>YES</BOR>

<RENTALRETAIL>RENTAL</RENTALRETAIL>

<QUANTITY>1</QUANTITY>

<STORE>1</STORE>

<RETAIL>300</RETAIL>

<RTO>100</RTO>

</record>

</rtoproinventory>

Below is an example of how the result file will look: c:\rtowin\AutoReceiveresult.txt (c:\rtowin if default folders were used in install)

01/17/2011 03:18 PM

0 <Received count

3 <Skipped count

Record below skipped, model / serial combination exists in database already.

Model:T1000 Serial:T1000SER Stock: 1000

Record below skipped, model / serial combination exists in database already.

Model:T1000 Serial:T1000SER1 Stock: 1001

Record below skipped, model / serial combination exists in database already.

Model:T1000 Serial:T1000SER2 Stock: 1002 

Auto receive by CSV file

You can also auto receive inventory in a CSV file below are the specs and requirements:

Command line:

rto-win.exe -r c:\csvfiles\mycsv.csv

Add "--noopen" switch if you want the report to not display after the process runs, like:rto-win.exe -r -noopen c:\csvfiles\mycsv.csv

When receiving by CSV file a log file will be saved in the local C:\rtowin\logs folder, named with the date, time and "Inv Import.csv", like "2022-11-08 14-09 Inv Import.csv". This file will be the same as the import file, except it will have a new column added in the first column position "Result_Status" that will either have "received" in it or the reason the item was not received.

The field names and descriptions are the same as XML files (see above). A sample of what the file will look like is below, the fields can be in any order. Note the example below only includes 13 fields, all 19 fields are available but not required.

model,serial,category,description,invoice,stock,vendor,agent,cost,retail,rto,brand,store

BARN,32396,BARN,5-B-32396-1016-070911-VA,0811VA,473,MY VENDOR,MY AGENT,2752.00,2752.00,4586.67,MY BRAND,1

GARDEN SHED,31981,GARDEN SHED,5-GSX-31981-1420-063011-VA,0811VA,473,MY VENDOR,MY AGENT,5206.00,5206.00,8676.67,MY BRAND,1
