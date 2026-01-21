3.8. SMS - Prior Day Confirmation

  


Requirements

If a guest has opted in to text notifications, send them a message on the day before their scheduled delivery/pickup. The times could be customized as needed in the Scheduled Tasks settings.

  


The text message should be able to reference:

  * First Name
  * Stop type (pickup/delivery)
  * Time (morning, around noon, afternoon)



  


The time should be:

  * "morning" before 11am
  * "around noon" from 11am to 1pm
  * "afternoon" after 1pm



  


The default message can be:

  * "[FirstName], you are scheduled for a [stop type] [time]. Reply Y to confirm, R to reschedule, or N to cancel your [stop type]. Call ____ for personalized service."



  


If they reply Y, send a message such as, "Thank you! We look forward to seeing you tomorrow."

  


If they reply R, send a message such as, "Thank you! We will call or text you for a new time for your [stop type]."

  


If they reply N, send a message such as, "Got it! Your stop has been canceled, Call or text if you have any questions."

  


Any unrecognized messages would show up as an alert, and could be addressed separately.

  


Development Specification

[ ] Create a scheduled task so times can be adjusted.
