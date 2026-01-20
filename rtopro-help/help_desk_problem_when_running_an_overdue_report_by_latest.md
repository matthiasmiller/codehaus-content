# http://www.rtopro.com/help/help_desk_problem_when_running_an_overdue_report_by_latest.htm

# Problem: When running an overdue report by latest not all customer will show up, or when running by an advance date not all showing up.

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Problem: When running an overdue report by latest not all customer will show up, or when running by an advance date not all showing up.

|  [](help_desk_problem_income_and_bor_graph_is_not_displaying_correctly_.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](help_desk_problem_home_office_record_counts_not_matching_with_store_.md "Next Topic")  
---|---  
  
Problem: When running an overdue report by latest not all customers will show up, or when running by an advance date not all showing up.

This problem is fixed in versions after 4.0.11.

This occurs when the last customer alphabetically is due within the report period. Any customer due after the last customer will not show up on report.

To correct this problem in versions prior to 4.0.11 do the following.

Go to Point of Sale > Retail Sales.

Hit F5.

Type ZZ in the name box and push F6, then ESC back to main menu.

This will create a fake last customer which will never be overdue, thus preventing this error to occur.

Or just obtain a new version of RTO Pro after 4.0.11 and the problem will be fixed internally.
