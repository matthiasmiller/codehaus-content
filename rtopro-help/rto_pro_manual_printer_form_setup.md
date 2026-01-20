# http://www.rtopro.com/help/rto_pro_manual_printer_form_setup.htm

# Printer / Form Setup

<< [Click to Display Table of Contents](index.md) >> **Navigation:** RTO Pro Manual >

# Printer / Form Setup

|  [](performance-report.md "Previous Topic") [](welcome_welcome_1.md "Parent Chapter") [](rto_pro_manual_f5_printing_utility.md "Next Topic")  
---|---  
  
Main Menu Option "5" Setup Option "2"

This is to setup the printers and forms (agreements, invoices etc.) on your system.

![printer-form-setup](printer-form-setup.png)

The Contracts/Main tab, which is displayed above is where you setup the files you will be using for Contracts and other forms which can be printed through RTO Pro.

To create a form or to edit an existing one, click on the form you want to work with and click on the red button. To select a file that has been saved on your computer you can click on the green button and select the file through a file browser.

With each form you can choose the printer to use, you can have 2 different printers for different forms. To choose which printer for each form click on the form line and press 1 to use printer #1 or 2 to use printer #2.

When you click on the red button the RTO Pro Word Processor will be started and either the form previously saved or a sample form will be displayed, you can also double click the form you wish to edit or create. When the form is opened you will notice there are field boxes, these fields are codes enclosed in {}. These fields are filled in automatically with the customerâs information when the form is printed. To add additional fields you put the cursor where you want the field to be and click the F4 key to see a list of fields. After you are finished editing the form save it and exit the RTO Pro Word Processor. The file name that you saved will automatically be put in the form file name box in RTO Pro. Make sure you push F12 after you return to RTO Pro to save these settings.

The other tabs in printer setup are to setup printing for the other functions in RTO Pro.

For Cash Advance Loans you can print a check to be given to the customer instead of cash when a new Cash Advance contract is loaded. The checks which are compatible with this feature are standard laser type checks which are available from many office supply stores. They are also available from Inform Business Systems Item # L-3001. You can reach Inform at 888-786-3676.

After setting all options push F12 to save

Use file SACcontract.rtf if same as cash on contract: If you check this box and the RTO agreement you load has the Same as Cash option the form in "C:\rtowin\docs\SACcontract.rtf" will print instead of the standard contract form.

Print Inventory Category Addendums (See help F1): If you check this box any addendum you have made for inventory will print. For instance if you want to print an addendum for any inventory in the category "COMPUTER" you would save a file named "computer addendum.rtf" in the docs folder on your server computer (default location is "C:\rtowin\docs". Any categories with a ":" in them replace that character with a "-", for instance for an addendum for the category "APPL:DRYER" the file name would be "C:\rtowin\docs\appl-dryer addendum.rtf". To use this feature you will have to create and manipulate the files manually, there is no automated way of handling or creating them. They can contain all the same fields as a normal RTO contract.

Please note the "Inventory Addendum" form in the form list is not for category addendums, this form is for contracts only list a couple of items on the first page of the contract, and has a 2nd page for the addition items to be listed. Do not save your category addendums in this location or they may print with every contract. The category addendum keys off fields in the form to determine when there are enough items that it should be printed.

Use different ACH Auths for different customer zones: If you check this box you can save different ACH Authorization forms named as follows: "zone ACH Authorization.rtf" replacing "zone" with the actual zone number. IE: "32726 ACH Authorization.rtf". If there is no form found for the customers zone the default form would be used. These forms have to be saved in the "Docs" subfolder under the servers data folder (C:\rtowin\docs is the default location).

Auto select agreement to print for Rent to Own contracts by state (For multi-state stores): If you check this box the agreement file would be chosen by the state the customer is in. For instance if the customers state is "FL" the agreement printed would be the file "FL agreement.rtf". These forms have to be saved in the "Docs" subfolder under the servers data folder (C:\rtowin\docs is the default location). If a form is not found with the customers state the normal form will be used. 

.

FORMS INCLUDED WITH RTO PRO

All forms included with RTO Pro including agreements, contracts, letters, price tags and labels are provided as SAMPLES only. RTO Pro does not warrant them to be legal in any given state or jurisdiction. It is your sole responsibility to ensure the forms and agreements you use meet the requirements for your state and or jurisdiction.
