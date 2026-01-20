# http://www.rtopro.com/help/automated_collections_import.htm

# Automated Collections Import

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Automated Collections Import

# 

|  [](excel_export_error_10-2017.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](web_invoice___request_for_paym.md "Next Topic")  
---|---  
  
The ACM import feature will allow you to import a list of account numbers to send text messages or voice broadcasting (call and play recorded message). 

The import file can be created using [SQL strings](help_desk_sql_strings.md) so you can create a call list based on any criteria available with SQL strings. After you create the SQL string for the customers you want you can export it to "Text File" from the records viewer, then import that file here.

The list should be a file with contents like the example below:

account

1002

5003

5897

6598

5874

The "account" header does not have to be present. The account number can have a comma after it also, the SQL record export would place a comma at the end of the number.

When calling and texting from this list all accounts in the list will be called or texted, no matter what their due date is. The only thing that would prevent an account in this list from being called or texted is a non contact status/rating.
