# http://www.rtopro.com/help/help_desk_deleting_data_after_running_fake_info_for_testing_prior_to_actual_data_being_installed_.htm

# How to: Delete Data after running fake info for testing, prior to actual data being installed.

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# How to: Delete Data after running fake info for testing, prior to actual data being installed.

|  [](help_desk_how_to_print_an_nsf_letter.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](print_invoices_to_1_pdf_file.md "Next Topic")  
---|---  
  
Version 4.2.11 and After do the following:

From registration enter "delete data" in the name

You will be asked "Are you sure you want to delete databases? If you answer yes data cannot be recovered. Answer YES.

Then you will be prompted for a password, enter "yes".

Empty databases will be created and old data will be overwritten.

For network version do this from server only.

Warning: This will delete all existing data, only use after testing prior to real data being entered.

In versions before 4.2.11 do the following:

Deleting Data after running fake info for testing, prior to actual data being installed.

2.Reinstall RTO Pro CD,. Or create a file named "demodata.exe" in the rtowin directory.

3.Delete "register.dat" in the RTO Pro directory.

4.Start RTO Pro then goto Setup> Store Info Setup> click on Register.Enter name and reg. # and push Enter, you will be asked if you want to delete the demo data or the local databases YES, if network you will be asked if you want to create data on this computer, if it is the server answer YES.

Warning: This will delete all existing data, only use after testing prior to real data being entered.
