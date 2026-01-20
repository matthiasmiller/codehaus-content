# https://rtopro.com/help/importing_customer_info.htm

# Importing Customer Info from a CSV file

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Importing Customer Info from a CSV file

# 

|  [](mobile_collections_app.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](ss_command_line.md "Next Topic")  
---|---  
  
You can import customer information from a CSV file. Below is a sample command line you could use to import customer info from a CSV file.

"c:\rtowin\rto-win.exe -importcust c:\app.csv"

The command line above would import the file "app.csv" located on the C drive. 

You can include "-noopen" switch in the command line if you do not want the result files opened on completion.

"c:\rtowin\rto-win.exe -importcust -noopen c:\app.csv"

The command line above would import the file "app.csv" located on the C drive and would not display the results files when it is finished. 

With this feature you can import:

1\. Customer info only. 

2\. Customer and contract info.

3\. Customer, contract and the inventory on the contract. 

To see what fields can be imported [click here.](customer_import_fields.md)

[If you want to import inventory ONLY see this help topic.](autoreceivefromxmlfile.md)

Please note in the latest version of RTO Pro, Ver 5.9.142 you can also import a file from Point of Sale Menu > View Web Apps > Import from file(Link at the top of the screen).

Central Server Note

For Central Server companies you can also pass the store number in the command line, like below.

"c:\rtowin\rto-win.exe -importcust -store2 c:\app.csv"

Below is the same command with the -noopen switch

"c:\rtowin\rto-win.exe -importcust -noopen -store2 c:\app.csv"

If the store number is not included in the fields imported the store number passed in the command would be used, if the store field is in the data that store number would be used.

For Central Server the store number must either be a field in the file or passed in the command line.

For Central Server the import file name can not contain the characters "-store", for instance never name an import file "Import -store 2.xml".

The fields in the CSV file can be in any order, the first line of the file must be the field name headers.

To see what fields can be imported [click here.](customer_import_fields.md) If the field names do not match this list, nothing will get imported.

Below is a sample CSV file with 2 records with just a few fields imported, you can have as many records as you want in each CSV file. The field names can be in any order but they have to be the exact field names as shown in the [topic here](customer_import_fields.md) and the file has to contain a header line with the field names in it.

name,address,city,state,zip,work1

"DOE,JOHN","1000 ANY Street","Eustis","FL","32726","7-Eleven"

"SMITH,JOE","1500 Any Street","Eustis","FL","32726","Wal-Mart"

After you have the CSV file ready and saved on your computer follow the steps below to pass a command line to RTO Pro to import the info from the CSV file. The steps below assume RTO Pro is installed in the "C:\rtowin" folder and the CSV file you want to pass is "C:\app.csv". If these values are different on your system change the info below as needed.

1\. Click the Windows Start button, Click All Programs, then Click the "Accessories" folder, under this folder you will see an icon for "Command Prompt", click this icon. This will open a command prompt window.

2\. In the command prompt window type the following command, then press the ENTER key:

c:\rtowin\rto-win.exe -importcust c:\app.csv

This will import the customer info from your CSV file into RTO Pro.

Please note this feature was designed for importing customer info, and optionally agreement and inventory info from a website, so you can build a website that you can accept customer applications and/or load agreements online. Any agreements imported will have a "PENDING" status, and will have to be loaded, like a pre-printed agreement is to make it an "OPEN" active agreement. For any dealers we have a service that allows you to accept applications online without building your own web application. For shed companies we have a service that allows your dealers to do load agreements online, and optionally have customers e-sign them at the dealers lot. 

For more info on our web applications service see this page: <http://www.rtopro.com/import_apps.aspx>

For more information on our Shed Dealer Web Portal see this page: <http://www.rtopro.com/sheddealer.aspx>

* * *

Sample CSV file

Below is a sample CSV file with 2 records, you can have as many records as you want in each CSV file, the header line must be present with the field names, the field names can be in any order but must use the field names as shown above.

name,address,city,state,zip,work1

"DOE,JOHN","1000 ANY Street","Eustis","FL","32726","7-Eleven"

"SMITH,JOE","1500 Any Street","Eustis","FL","32726","Wal-Mart"
