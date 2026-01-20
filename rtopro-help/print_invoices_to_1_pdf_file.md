# http://www.rtopro.com/help/print_invoices_to_1_pdf_file.htm

# Print Invoices to 1 PDF file

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Print Invoices to 1 PDF file

# 

|  [](help_desk_deleting_data_after_running_fake_info_for_testing_prior_to_actual_data_being_installed_.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](help_desk_contract_addendums.md "Next Topic")  
---|---  
  
Starting in version 5.9.371 of RTO Pro it is possible to save all invoices that would be printed to a single PDF file. This option is on the billing page, when checked all invoices will be saved to 1 multi page PDF file in your local "C:\RTOwin\Reports" folder. The PDF file will be saved with the date and time it was created like "2023-10-19 15-22-33 Merged Invoices.pdf".

Below is the setting found on the billing screen.

![pdf single setting](hmfile_hash_27d3f0c7.png)

This feature is used by companies who outsource their printing/mailing of invoices.

Below are other ways you can accomplish the same thing if you want to use a PDF printer to do it instead or have an older version than 5.9.371

* * *

Using some PDF printers it is possible to print all invoices to one multi-page PDF file. This is useful for companies who outsource their mailing of invoices. This is probably possible with other PDF software also, but we will go over how to set it up with Bullzip PDF Printer, which we have tested and verified works.

1\. Install Bullzip PDF Printer, this is their website: <http://http://www.bullzip.com>

2\. In RTO Pro, Printer / Forms Setup, choose Bullzip PDF Printer as the printer to use for invoices.

3\. Set up Bullzip PDF like this page describes: [http://www.bullzip.com/kb/append-to-pdf-without-dialogs/ ](http://www.bullzip.com/kb/append-to-pdf-without-dialogs/)

4\. Change the port settings for Bullzip like this page describes: [http://www.bullzip.com/phpBB/viewtopic.php?f=6&t=57738&p=72366&hilit=append#p72366 ](http://www.bullzip.com/phpBB/viewtopic.php?f=6&t=57738&p=72366&hilit=append#p72366)

and this page: <http://www.biopdf.com/guide/port_settings.php>

That's it! When you print invoices they will all be appended tot he same PDF file. Be sure to delete the file after you are finished or the next time you print invoices they will get appended to previous invoices.

* * *

Below is from the page referenced above in #4, in our testing we used -1 as the port setting with success with Bullzip PDF Writer

All these settings are located under the printer's private registry key:

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Print\Printers\PDF Writer - bioPDF

The last part of the key name depends on the printer name.

GUITimeout

The GUITimeout setting controls how the printer port starts the gui.exe process. This process is where the actual conversion from Postscript to PDF or image formats take place. Conversion is started by the port when the Postscript is spooled. By default, the port continues with the next print job as soon as the gui.exe process is started.

Using the GUITimeout setting you can change this behavior. The value of GUITimeout is a number of milliseconds to wait for the gui.exe process to finish. In case the gui.exe process has not finished within this time limit, an error is reported by the port. Specifying -1 as the timeout value will make the port wait forever for the process to terminate. That will make sure that no more than one process is running at any given time. This can be used if you automate a sequence of appended print jobs with the Append If Exists feature.

GUITimeout defaults to 600000 (10 minutes) if the setting is not found in the registry. 

Before version 10.24 the default was 0 (zero).

Value Meaning

0 The port continues with the next job as soon as the gui.exe process is started. Multiple conversions can run simultaneously.

-1 The port waits until the gui.exe process has terminated before starting the next print job from the spooler queue.

> 0 The port waits the number of milliseconds specified in the value. An error is reported and the gui.exe is terminated if it runs longer than the specified timeout.

Warning: If you specify -1 then the gui.exe process can stop the printing process if it hangs for any reason. In a fully automated setup, you might prefer to specify a sufficiently high timeout that makes sure that the job is finished if everything run as planned. At the same time, it makes sure that a faulty print job does not hang the system.

The GUITimeout is specified in the computer registry under the key shown below.

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Print\Printers\PDF Writer - bioPDF

It is a string value named GUITimeout and the content is an integer.

GUITimeout Registry Image

![clip0031](clip0031.png)
