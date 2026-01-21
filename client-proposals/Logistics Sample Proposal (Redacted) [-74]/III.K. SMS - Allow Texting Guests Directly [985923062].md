3.11. SMS - Allow Texting Guests Directly

  


Requirements

We will provide an online chat screen to allow you to view and send text messages.

  


We will provide real-time notifications using an application to install on the scheduling computer. It will require a user name and password to be specified. It will show alerts on the screen when a new text message is received. Clicking the alert will open the web browser to view and respond to those text messages.

  


Development Specification

Matthias Miller 08/19/2020:

[ ] We will have a Mobile view that shows all prior phone numbers on the left, lookup names based on contact info, and have an option to send a new message

[ ] Sneding a message would close out all existing conversations (ending all automation)

[ ] All unrecognized messages would show up as unread

[ ] Have a report alert to show when there are unread SMS messages.

  


Matthias Miller 08/19/2020: Or:

[ ] Have a multipane report

[ ] Left pane = all numbers previously texted

[ ] Right pane = all messages sent and received

[ ] Left Pane has button to send new message -- prompts for contact and message

[ ] Right pane has a button to reply -- prompts for message

  * This runs an x30 that closes out all prior conversations and creates a new one to send them outbound message



  


[ ] You would have a catch-all message handler that would somehow trigger an alert for this message (not sure how this would work??)
