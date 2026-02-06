7\. Workflow: Pickup

  


Requirements

Once an invoice has been created for an order, the order will automatically reflect the "Pickup" workflow and will start the scheduling process. The scheduling process will be tracked on a per-invoice basis.

  


Once the invoice is created, the text messages will automatically be sent out, as long as they have opted-in for those. The text message will be something like this (wording can be customized):

  


Your Deer #123 and #124 is/are ready for pickup at Log City Meats. Please reply with YES to acknowledge or with the keyword STOP to opt out. For questions, call (123) 456-7890.

  


If they reply YES, respond with:

  


When will you pick it up? Please reply with TODAY, TOMORROW, or a day of the week (e.g. FRIDAY). If you would like to wait more than a week, please reply with the full date (i.e. 9/5/2019). For questions, call (123) 456-7890.

  


We will track on the invoice any outreach actions, include:

  * Sent SMS (the reminder has been sent)
  * Confirmed SMS (SMS acknowledgment has been received)
  * Left Voicemail (left a voicemail for the customer; requires manual entry)
  * Confirmed Call (confimed with the customer via phone call; requires manual entry)



  


We will provide a Reminders report. This will show a list of completed orders, sorted by invoice date (earliest first). Show a column with the status, such as "Sent SMS" or "Confirmed SMS" or "Confirmed Call". Show a Scheduled Date column.

  


Sales Counter

At the sales counter, they will be able to look up invoices by customer name. They will mark the invoice as paid, then print off a copy for the customer. This will flag the order as "complete".

  


Development Specification

Matthias Miller 06/10/2019: 

  * CCI - 3 days
  * Matthias - 2 days



  


Have a trigger report that kicks off an x30 to create outbound SMS

  


Have an RG:

  * put an auto entry when sending the SMS
  * put an auto entry when confirming the SMS
  * put in new entries when making calls



put scheduled date on the order -- basically snoozes until then.

  


Ellis Miller 06/03/2019: The example date should always use the current year. It could always be 9/5, but next year it should be 9/5/2020, etc. (Or maybe do it Today+7.)

  


Ellis Miller 06/10/2019: 

RG Fields:

  * InvoiceReminderAction (sent SMS, Confirmed SMS, Left Voicemail, Confirmed Call....) TODO: Need list
  * InvoiceReminderDate (date the action took place)



InvoiceScheduledPickupDate -- the date user specified, no history on this....

  


  


Ellis Miller 06/10/2019: Matthias, do you want us to provide reports that give you this wording and SMS'es to send? We should definitely control as much of this as possible from expressions.

Matthias Miller 06/10/2019: Yes, but let me talk this over more specifically with Josh. I'm thinking something like:

  * Cell #
  * Message



Matthias Miller 06/11/2019: Josh is asking for $20/mo (so he gets $16/mo), unless we want to round it up to $25/mo
