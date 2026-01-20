# http://www.rtopro.com/help/help_desk_error_75_path_file_access.htm

# Error 75 Path / File Access error when running Overdue Customer List with the "Runsheet Type Report" checked.

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Error 75 Path / File Access error when running Overdue Customer List with the "Runsheet Type Report" checked.

|  [](help_desk_error_75_path_file_access_error_when_running_on_screen_account_manager_.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](help_desk_error_75_path_file_access_error_during_transfers.md "Next Topic")  
---|---  
  
Problem : When running the Overdue customer list with "Runsheet Type Report" checked you get the following error: Error 75 Path / File Access error.

Cause: This has been reported by 1 user where the file "run.tmp" was somehow changed to "Read-Only" by Windows not allowing access to a needed file to RTO Pro.

Fix: Delete the file "run.tmp" which will be in the "C:\RTOwin" folder by default. This is only a temporary and will be recreated the next time you run the Overdue Customer List.
