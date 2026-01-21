4.8.2.4.1. Workflow: Prepay Devices

Think Ink offers a a discounted Monthly Base Price on a per-device basis if a customer prepays the base price amount for a full year. When this happens, the Customer is billed upfront for up to a full year of the base price a discounted rate, and is not billed again for base charges until they reach the end of the prepay plan (which can be renewed). The Customer is billed for page count overages like other Customers. 

  


If a Customer signs up for prepay in the middle of a month, ___

TODO_IDD / TODO_BR: Tim Reitz 10/03/2023: nearest 1/4 month - see notes

  


If a Customer signs up for prepay in middle of an Agreement year, ___

TODO_IDD/ TODO_BR: Tim Reitz 10/03/2023: finish out the agreement year, then start over with the agreement for a full 12 months

  


If a Customer switches from prepay to standard monthly billing for a Device,

TODO_IDD / TODO_BR: Tim Reitz 09/19/2023: Normally would happen at annual renewal. If switched earlier, we don't need to worry about handling credit / refund

  


Process for setting up prepay: TODO_IDD / TODO_BR

  * Open the Device record
  * Check the Prepay checkbox in the __ section
  * ___



  


Process for switching from prepay to standard monthly billing: TODO_IDD / TODO_BR

  * ____



  


\----------------

DONE_IDD: Tim Reitz 07/13/2023: work through the logic for this: 

[X] \- Think Ink offers a 5% discount for the base charge if the customer prepays the full base charge (not the page count overages) for a full year. 

[X] \- This would not apply to the email accounts

[X] \- When we add invoicing, we need handle that discount for the base charge - but not too much automation, to allow the user to include an extra deal if desired. 

[X] \- If Prepay is checked, there is no Monthly Base Price until the end date

[X] \- If Prepay End Date is in the past, maybe prevent any billing for the device (base charge and pages)

[X] \- If Prepay End Date is in the past, set the Needs Review checkbox

[X] \- Have a notification when the date is X days in the future, to remind them to revisit and renew it. 

Tim Reitz 09/14/2023: See the "Prepay Plans Ending Soon" notification + x30 + report. 

  


  


TODO_EM: Tim Reitz 09/14/2023: Good with how this is specced out so far? ?
