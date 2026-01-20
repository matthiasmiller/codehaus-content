# http://www.rtopro.com/help/help_desk_run_time_error_6_when_pulling_up_a_customer_in_payments.htm

# Run time Error 6 when pulling up a customer in payments or when running a customer listing or overdue report

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Run time Error 6 when pulling up a customer in payments or when running a customer listing or overdue report

|  [](help_desk_run_time_error_6_overflow_when_receiving_non_serialized_inventory.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](help_desk_run_time_error_9_subscript_out_of_range_when_running_a_depreciation_report_.md "Next Topic")  
---|---  
  
Problem: Run time Error 6 when pulling up a customer in payments or when running a customer listing or overdue report

Cause: This is usually caused by a customer having a due date that is way off, like 5-5-300. This due date can be set wrong accidentally when moving a due date and hitting an extra character in the year place.

Fix: Pull up the customer under Contract Maintenance (Point of Sale menu option 3), verify the due dates on all contracts for the customer. The date 5-5-300 is displayed as 5-5-00 in RTO Pro so the dates may not look wrong. If the date displays incorrectly hit F11 and correct. If the date looks correct push F11 and just push enter to save, in the above example the displayed date of 5-5-00 will automatically change the year of the due date to 2000 instead of 300 when you save it.
