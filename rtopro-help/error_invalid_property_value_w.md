# http://www.rtopro.com/help/error_invalid_property_value_w.htm

# Error Invalid Property Value when trying to print invoice

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Error Invalid Property Value when trying to print invoice

# 

|  [](help_desk_not_able_to_add_categories_after_deleting_all_data_.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](issue_server_running_slow.md "Next Topic")  
---|---  
  
When trying to print an invoice for a customer with multiple agreements, you may see this error "Invalid property value (1-3211)":

![Invalid Propery value](hmfile_hash_69014fc6.png)

This is caused by certain fields being in the wrong place on the invoice form. When editing invoices, some fields must be in the same row for the invoice to print correctly, as explained in the screen shot below, the field list form (push F4 to list fields when editing forms):

![Invoice Editor Fields](hmfile_hash_7bb1714e.jpg)

To correct the problem, open the invoice form in the Editor under Printer/Forms Setup and rearrange fields as needed. After editing the invoice form click File>Save to save your changes.

Below is an example of how these fields must be used, the {contractd1} and {desc1} must be in columns in one table in the same row. Any other field names that end in "1" must be in columns in their own table in a single row.

![Invoicefieldsclip](invoicefieldsclip.png)
