# http://www.rtopro.com/help/excel_files_using_scientific_q.htm

# Excel files using Scientific Notation

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Excel files using Scientific Notation

|  [](help_desk_run_time_error_9_subscript_out_of_range_when_running_a_depreciation_report_.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](help_desk_macro_can_not_be_found_or_is_disabled_message.md "Next Topic")  
---|---  
  
This is more of a fix for Excel than RTO Pro. Often when files are opened by Excel it will try to determine the format of a column and format the column accordingly. For fields such as serial number or any other numeric fields, or fields that have some values that are numeric, Excel will decide to treat the entire column as numeric instead of text. The problem with Excel and number is that Excel, in an attempt to save space, will convert a long number such as "1222222244566" to "1.22222E+12", the scientific notation for that number. This "space saving feature" of Excel saves very little screen space and makes the data basically useless unless you are a genius and can do scientific notation in your head. 

This worked for me in Excel 2010 and newer. Just select the column, right click > Format cells, choose Custom and choose the option that says 0 (second option below General). 

This will make Excel display the actual numbers instead of scientific quotation.
