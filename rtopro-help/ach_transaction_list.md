# http://www.rtopro.com/help/ach_transaction_list.htm

# ACH Transaction List  
  
# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# ACH Transaction List

# 

|  [](commitments.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](rto_pro_information_using_ms_word_for_letters_invoices_or_contracts__1.md "Next Topic")  
---|---  
  
The ACH Transaction List Screen will list all ACH transactions. To view the ACH transaction list click the green "View ACH Transactions" (see image below) button on the Autopay screen. You select the status's you want to view by clicking the option boxes at the top left. Below is a description of each status type and what operations can be done to the transactions in each type.

To perform a function on a transaction click the transaction and then click "Edit" on the top left or you can right click on a transaction and the menu will display.

Unsent

Unsent transactions are ones that have been entered in RTO Pro but have not been sent to the ACH system through your ACH provider (Profituity or IcheckGateway). 

Unsent transactions can be deleted, which would prevent them from being sent through the ACH system (the customer would not be charged).

Unsent transactions can also be flagged as SENT. This can be used in an instance where the transaction was sent previously but for some reason was not flagged as sent.

Unsent transactions bank account / route number can be edited. This is useful when a number was entered incorrectly and the payment processed but the ACH transaction not sent to server yet. Please note editing the bank account / route number from here only affects this transaction, the saved bank account info for the customer will not be updated with any change you make here.

Pending

Pending transactions are ones that have been sent through the ACH system but have not cleared or returned yet. 

Pending transactions can be flagged as Cleared. If a transaction cleared but still shows in pending you can flag it as cleared.

Pending transactions can be flagged as Returned. If a transaction was returned but still shows in pending you can flag it as returned.

A transaction that was returned, then flagged as "Resubmitted through ERS" will also show in this list as it will be waiting to clear again after it was resubmitted.

Cleared

Cleared transactions are ones that have been sent and cleared (you have been paid for them). No functions can be performed on cleared transactions.

Returns

Returned transactions are ones that have been sent and returned, because of NSF or other reason (you will not be paid for them). 

The following functions can be performed on Returns:

1\. Returned transactions can be reversed in RTO Pro (original transaction reversed). You can perform this function from this screen so the record will be flagged as reversed, so you know it has been handled.

2\. Check if transaction was already reversed. This will look at the history records and see if it was reversed already (using the normal reverse process instead of through this screen), if it was reversed it will be flagged as reversed.

3\. Load as an NSF. You can perform this function from this screen so the record will be flagged as Loaded as NSF, so you know it has been handled. The NSF load screen will be brought up with most info filled in already.

4\. 1 Click Load as NSF. This function will load all selected returned transactions as NSF's without any further prompts. The default NSF fees will be used and no NSF letters will be printed if you use this option.

5\. Flag as already loaded as NSF. If the item was loaded as an NSF manually you can flag it as such with this option. 

6\. Flag as resubmitted through the CheckAssist ERS website (If you use Profituity as your ACH provider, see line below if you use ICheckGateway). You can resubmit a return through the ERS website for several reasons, such as a return due to wrong account number, you could log into the ERS website, correct the account number and resubmit. The Profituity ERS website is: <https://quickcheckinc.com>. You will need your user name and password Profituity assigned you to log on.

![ACH Search](hmfile_hash_62bbdd0f.png)

Transaction search feature

You can search ACH transactions by customer account number. When you search by account number all transactions for that customer will display no matter what status list you are on when you start the search. Also all dates will display, not just the past 180 days.

For ICheckGateway users: At the time of this writing ICheckGateway does not have a feature to resubmit returns through their website, any resubmits would have to be done through RTO Pro by reversing the payment and reprocessing the payment by ACH or loading as NSF then paying the NSF by ACH.

![autopayscreen2](autopayscreen2.jpg)
