# http://www.rtopro.com/help/central-server-mass-move-contr.htm

# Central Server Mass Move Contracts

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** RTO Pro Manual >

# Central Server Mass Move Contracts

# 

|  [](rto_pro_manual_contract_maintenance_and_inventory_switchout.md "Previous Topic") [](welcome_welcome_1.md "Parent Chapter") [](rto_pro_manual_contract_close_and_refunds.md "Next Topic")  
---|---  
  
Central Server stores can move contracts from store to store from contract maintenance 1 contract at a time. If you need to move a lot of contracts from one store to another this feature in Store Setup can do that for you.

This will move contracts from a text file list of contract numbers you create. You will be prompted to select the file, how to handle deposits and what store to move to. 

Screen shot below of where to find this feature, in Store Setup.

![clip0088](clip0088.png)

When you move a contract from store to store the payment history is moved, the contract record, the inventory, everything for the contract from all time. Keep in mind that when you move contracts from store to store it affects past revenue reports and other reports. If you run a revenue report for last month for store 1, then move a contract to store 1 that had a payment for last month and run the revenue report again for last month, it will now include the payment for the contract that was moved, the store it was moved from will no longer show ANY revenue for that contract.

The file with the list of contracts to move must be a plain text file(you can create it with Windows Notepad), with a single contract number on each line, like below.

C100

C102

6789
