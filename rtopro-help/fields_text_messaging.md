# http://www.rtopro.com/help/fields_text_messaging.htm

# Fields available for SMS text messages

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** »No topics above this level« 

# Fields available for SMS text messages

# 

|  [](welcome_welcome_1.md "Parent Chapter")  
---|---  
  
Webpay quickpay link field

If your company uses the RTO Pro Webpay Service you can send text messages with "Quickpay" links embedded in them. This would allow your customers to click the link from the text message on their smart phone and be directed to their account on the webpay site to pay payments, without having to log in or create a login.

To use this feature simply include {WebPayLink} in your text message where you want the link to go. For instance you could have a text message worded like below:

Your account at "Your company Name" is over due, call us at "your number" or click the following link to pay online: {WebPayLink}

Remember text messages can only be 160 characters to be charged as a single text, so you should use no more than 130 in a message like this to leave space for the link that must be embedded. If the length of the text, including the quickpay link goes over 160 characters you will be charged for 2 text charges per message sent that is over 160 characters. The length of the quickpay link can vary depending on the length of the customers account number and your webpay account id. You should send some test messages with the quickpay link to see if they go over 160 characters. 

To use this feature you must be signed up to use the RTO Pro webpay service and you must enter your webpay company ID in store setup, under the other tab. Call 352-383-9375 to get your webpay company ID.

* * *

Account Number Field

Another field that is available for text messages is "{account}". When you put {account} in a text message it will be replaced with the customers account number.

For instance if you had a message like below

Please contact us about your account number {account}

And you sent it to account number 100, they would get the following text

Please contact us about your account number 100

Remember text messages can only be 160 characters to be charged as a single text. If the length of the text, including the quickpay link or account number goes over 160 characters you will be charged for 2 text charges per message sent that is over 160 characters. The length of the quickpay link and account number can vary depending on the length of the customers account number and your webpay account id. You should send some test messages with the quickpay link and or account number fields to verify they do not go over 160 characters. You are solely responsible for all texting charges, including being charged for 2 messages if they go over 160 characters.

* * *

Contract Number Field

Another field that is available for text messages is "{contract}". When you put {contract} in a text message it will be replaced with the customers contract number, for their oldest active contract.

For instance if you had a message like below

Please contact us about your contract number {contract}

And you sent it to account number 100, and they have a contract number C100 they would get the following text

Please contact us about your contract number C100

Remember text messages can only be 160 characters to be charged as a single text. If the length of the text, including the quickpay link or account number goes over 160 characters you will be charged for 2 text charges per message sent that is over 160 characters. The length of the quickpay link and account number can vary depending on the length of the customers account number and your webpay account id. You should send some test messages with the quickpay link and or account number fields to verify they do not go over 160 characters. You are solely responsible for all texting charges, including being charged for 2 messages if they go over 160 characters.

* * *

Store Name Field

Another field that is available for text messages is "{storename}". When you put {storename} in a text message it will be replaced with the current store name.

For instance if you had a message like below

Please contact {storename} about your account number {account}

And you sent it to account number 100, and your store name is Best Rental, they would get the following text

Please contact Best Rental about your account number 100

* * *

Store Phone Field

Another field that is available for text messages is "{storephone}". When you put {storephone} in a text message it will be replaced with the current store's phone number.

For instance if you had a message like below

Please call {storename} at [storephone] about your account number {account}

And you sent it to account number 100, and your store name is Best Rental, phone number 352-383-9375 they would get the following text

Please contact Best Rental at 352-383-9375 about your account number 100

* * *

The Fields Below are only useable for SMS texts sent through the RTO Pro Scheduler

* * *

Scheduled Event Fields

{eventtype} would be replaced with the event type that is scheduled, either Delivery, Pick Up, or Service Call.

{eventdate} would be replaced with the event date

{eventtime} would be replaced with the event schdeuled start time

* * *

Remember text messages can only be 160 characters to be charged as a single text. If the length of the text, including the quickpay link or account number goes over 160 characters you will be charged for 2 text charges per message sent that is over 160 characters. The length of the store name can vary and be longer than the {storename} field holder. You should send some test messages with the store name link to verify they do not go over 160 characters. You are solely responsible for all texting charges, including being charged for 2 messages per text sent if they go over 160 characters.

Fields are NOT case sensitive, {Account}, {ACCOUNT}, {account} will all work.
