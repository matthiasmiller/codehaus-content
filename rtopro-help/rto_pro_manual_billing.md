# http://www.rtopro.com/help/rto_pro_manual_billing.htm

# Run Billing / Invoices

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** RTO Pro Manual >

# Run Billing / Invoices

# 

|  [](rto_pro_manual_create_central_file_mail_list.md "Previous Topic") [](welcome_welcome_1.md "Parent Chapter") [](rto_pro_manual_delinquency_analysis_report.md "Next Topic")  
---|---  
  
Customer Menu Option "7"

If you are going to send invoices to your customers, either by email or regular mail it is best to send invoices out once a week. If you have customers due at all different times of the month you should send invoices out weekly. The default options are set up for weekly invoicing. With the default settings invoices will be sent out between 14 and 21 days before a customer is due, this gives them time to get the invoice and get a payment back to you before their due date. There are a lot of other ways you can set invoicing up, the options are listed below, but if you want to do weekly invoices you can just keep the default settings and pick a day of the week and always run invoices on that day every week

More details and different options are outlined below.

Any rental account can be set up to be billed. When loading the contract select yes under billing, (See [New Rentals and Leases](rto_pro_manual_new_rental_lease_contracts.md)).

The contracts that are due to be billed will be when you run the Billing (Customer Menu option 7). How often the billing will be run depends on what you put in the Run Billing For __ Days box. However, if you load a new contract that needs to be billed right away the next time you run On Screen Account Manager it will be billed even if billing is not due to be run.

The sample invoice is designed with the customer address positioned so it can be put in a window envelope for mailing. The contract information, amount due, next due date etc. will be printed automatically on the invoice. You can customize the invoice in Printer Setup. The invoices will be printed to the printer you have selected in Printer Setup. The recommended settings for billing / invoicing are to check the lines that are underlined below and have a n beside them, the recommended days are 7 and 14 as shown below.

Below are descriptions of the fields / buttons on the Billing screen:

Run Billing For  7  Days: This is for how often you run billing, if you print invoices every week set it to 7. If you set it to 7 every 7 days you will be asked if you want to print invoices when you run the On Screen Account Manager (If that option is set in Store Setup). This number is also added to the next number below to get the total days out to bill customers.

Bill Customers  14  Days Before Due: This is for how many days before a customer is due you wish to bill them. Typically this is set to 14. This number is also added to the Run Billing For number to get the total days before due to bill customers. For instance if these 2 numbers are set to 7 and 14 every 7 days you will be prompted to print invoices and invoices would be printed for anybody due in the next 21 days. These 2 numbers together should never add up to more than 30. If you run billing only 1 time per month the numbers should be set to 30 and 0.

The two numbers above are also used to determine how much to bill the customer for, for instance if the #'s are 7 & 14 the amount that would be billed is the amount the customer would owe 21 days from now.

When a contract is billed it is flagged with the date last billed, if they do not pay and you have rebilling enabled they would not be billed again until at least 25 days later.

n "Only print 1 Invoice each month" With this option checked each customer would only be invoiced 1 time per month. If this is not checked with the default number of days settings if a customer was billed and did not pay they would be billed every 21 days, with this checked they would not be billed again until 21 days before their next scheduled due date. Below is an example of the difference with this checked and unchecked for somebody due 1/21 who does not pay until 2/2 (note this example assumes Re-Bill monthly even if overdue is checked).

With this box checked: They would be billed on 1/1 and then billed again on 2/1.

Without this checked: They would be billed on 1/1 and then again on 1/22 and then not billed again until 21 days after 1/22.

n "Re-Bill Monthly even if overdue" Check this box if you want to re-bill customers who were billed previously and has not paid since they were billed (check this box if you want to keep mailing invoices to customers who are late). If this box is not checked invoices will not be mailed to overdue customers.

n "For overdue customers Email an Invoice EVERY billing run" If you check this box and a customer is overdue and you have their Email address everytime you run billing they will be EMAILED an invoice only. Note this only applies if "Only Print 1 Invoice each Month" is checked, on their normal billing date they will be printed an invoice..

Â¨ "Let me enter the info below instead of handling automatically" "Do Not bill customer that have been billed in the past number of days?" Check this box and enter the number of days if you want to determine the number of days to not bill a customer that has been billed in that number of days in the past. If you enter a number here such as 21, anybody who has been billed in the past 21 days will not be billed no matter what.

There are a couple of instances listed below where you may want to enter a number here instead of letting the software handle this for you automatically

1\. If you want to bill everybody even if they have been billed say for instance last week you may want to enter a small number here such as 6, that way anybody due in the billing range would be billed even if they were already billed 7 days ago.

2\. If you only want to mail out invoices once each month to customers you may want to enter a large number here like 25, that way nobody would ever be mailed an invoice more than one time every 26 days.

The default handling for number of days will rebill customers who have been billed but have paid after the last invoice went out but did not pay enough to catch up or did not pay enough to move their due date beyond the billing range. For instance if a customer is due on 1-1 and you invoiced them on 1-5, they paid one payment on 1-15 if you run billing on 1-16 the default handling would invoice them on 1-26 whereas if you enter the number for this option as 21 and run billing it would not print them an invoice since they have been billed in the past 21 days.

Â¨"Only Report what would be billed. Do not print invoices" checkbox: Check this box if you only want to see a report of who is due to be billed with the current settings instead of printing the invoices.

"Cancel Last Billing Run" button: This button will undo the last billing ran so you can re-run the same billing again if you need to.

Print / Email options

o Print Invoices Only: If you select this option invoices will be printed for all customers except for customers who are marked to email invoices only. Customers can be marked to email invoices only in "Customer Maintenance" (Payment screen > F11).

o Print and Email Invoices: If you select this option invoices will be printed and any customer who has an email address on file will have an invoice emailed to them also.

o Email Invoices Only: If this option is checked all invoices will be emailed unless a customer does not have an email in their records, in that case it will be printed.

Note: You can mark customers to be billed by Email ONLY. This is done from the customer maintenance screen (F11 from payment screen) or on the customer application screen. If you mark a customer to be billed by Email only they will be handled according to the rules below:

1\. If You run invoices as "Print Only" the customer marked to bill by email only would be billed (invoice would be printed).

2\. If you run invoices as "Print and Email Invoices" that customer's invoice would be emailed only unless their email address was missing or an error prevented the email of the invoice, then their invoice would be printed.

3\. If you run invoices as "Email Invoices Only" that customer's (and all other customers) invoices would be emailed only unless their email address was missing or an error prevented the email of the invoice, then their invoice would be printed.

Â¨Ignore all other settings and just invoice ALL customers setup to be billed. (For once a month invoices).: If this box is checked all of the settings that limit who gets billed are ignored, ALL customers who are flagged to be billed will be sent an invoice, no matter when they were previously invoiced or what their due date is. If you want to send 1 invoice every month to ALL of your customers this option can be used.

Â¨Order invoices by ZIP CODE: If this box is checked the invoices are printed (or emailed) ordered by zip code instead of alphabetically.

Â¨Print Invoices for customers paid ahead also: If this box is checked any contract that has a due date beyond the normal billing date that has not been billed in the last 20 days will be billed.

Â¨Include customers with back rent due even if their due date is beyond billing range: If this box is checked any contract that has back rent due will be billed, even if the due date is beyond the normal billing range, unless they have been billed in the last 20 days.

Â¨Use Alternate Billing Logic checkbox: Check this box if you want to use the alternate way of determining who gets billed. The way it determines who gets billed is described below.

Example of how the alternate billing method works with the following sample #'s in the fields.

Run Billing For  7  Days

Bill Customers  14  Days Before Due

Bill anybody due on any month within the dates: 1-15

If the contracts due date is beyond todays date + 21 days the contract WILL NOT BE BILLED (unless."Print invoices for customers paid ahead also" is checked).

If the contract was billed in the past 15 days it WILL NOT BE BILLED. (the 15 days is an internal # that cannot be changed)

If either of the 2 calculations above determine the contract should not be billed then it will not be billed no matter if it meets the requirement below or not.

If the day of month due falls from 1 to 15 it WILL BE BILLED, no matter what month they are due.

The alternate billing method works best for stores that only print invoices 1 or 2 times a month. If you print invoices weekly the normal method works best.

Note: If you only print invoices once a month and want to send an invoice to ALL customers who are marked to be billed check the alternate logic box, put 1-31 in the date box, check re-bill monthly even if not paid and check print invoices for customers paid ahead also. This will print an invoice for all customers marked to be billed unless they were already billed in the past 15 days.

Â¨Only Print Invoices for due dates in the range below: If you only want to print invoices for customers that are due in a given date range check this box and enter the date range. With this option checked only customers with due dates in the given date range that have not been billed in the last 20 days will be billed.

CSV Export Options

![Billing CSV export options](hmfile_hash_7d8e420b.png)

Below are the options for creating CSV export files with the billing information. These files could be used to send to a 3rd party billing company to print and mail invoices for you. 

Please note the only invoice information exported is for invoices that would be printed, if an invoice would be emailed only it will not be included in the export file. This feature was designed for stores that want to email their invoices themselves, but use an outside company to print and mail any that would be printed.

* No CSV Export: Check this box and a CSV export file will not be created.

* Print and Export: Check this box if you want to print/email invoices as well as create a CSV export file.

* Export Only: Check this box if you want to email invoices, but any invoices that would be printed to be included in the CSV export file only, not printed. Any invoices that are set to be emailed would be emailed like normal, they would not be included in the export file if they are set to be emailed only.

* Send file to Mail Service: Check this box if you want to send the CSV export file to the AccuSent Mail Service(info below). 

The CSV file is saved in your local RTO Pro install folder in the sub folder "exported data". It is named as follows store name year-month-day hour-minute-seconds.csv, example path and file name below:

c:\rtowin\exported data\RTO Pro Software 2024-08-20 09-45-15.csv

Mail Service

AccuSent Mailing is providing custom invoice processing. We utilize the data from your current RTO Pro billing and design, print and mail for you. Working in conjunction with the United States Postal Service, we ensure that your invoices get to your customers. Donât use valuable time printing, folding, stuffing and stamping when you have more important tasks to address. Contact AccuSent today to discuss how we can benefit your business. (660) 888-8429 or [info@accusent.net](mailto:info@accusent.net)

![AccuSent](accusent.png)
