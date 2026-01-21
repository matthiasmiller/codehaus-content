8.4. User Alerts Notification (Report Alert)

  


Requirements

TODO_VA: report alert

  


  


  * When a user has unread messages, they will see a red button at the bottom of the menu that reads "Unread Message for [User Name]", as well as a red notification square on the bottom left of every screen.
  * When the user clicks this button, it will show a list of all unread messages if the user has multiple messages. Otherwise, it will immediately open the unread message.
  * When the user reads the message, the notification will disappear. If the user wants to keep the message for future reference, they must click the Mark Unread button at the top of the message.



  


  


When a user has unread messages, they will see a red button at the bottom of the menu that reads "Unread Message for [User Name]", as well as a red notification square on the bottom left of every screen.

  


When you click this button, it will show a list of all unread messages if you have multiple messages. Otherwise, it will immediately open the unread message.

  


When you read the message, your notification will disappear. If you want to keep the message for future reference, click the Mark Unread button at the top of the message.

  


Development Specification

Matthias Miller 07/20/2020: Make this be a generic feature.

  * Call the underlying message User Alert.
  * Use a System Notification (report alert) to show these messages.
  * Rely on detail screen unread marks to determine which ones to display
  * For now, have a title and message field. Include a read-only "To" expression control that is set to "Everyone". Eventually, we can expand this to send to a user group, etc.
  * Include a Sent that is a Date/Time the record was saved.


