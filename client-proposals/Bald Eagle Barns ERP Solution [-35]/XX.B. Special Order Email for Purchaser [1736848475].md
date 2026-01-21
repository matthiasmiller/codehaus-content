20.2. Special Order Email for Purchaser

TODO_TR: scrap this

  


  


Overview/Purpose: This automated email would serve as a "daily digest" for the Purchaser of all Special Order items that need to be ordered as of the time of sending the email. If there are no such items, the email would not send. 

  


Title (can be an expression?): Special Order item(s) need to be ordered

Text (can be include expressions): 

Hello <Name>, 

  


The following Special Order items need to be ordered: 

<display the items (extract from report) TODO_TR

  


<link to Special Order Items report> 

  


\- The AppHosting.Zone Bot 

  


Trigger: Send daily at ___ if there are unordered Special Order items on Sales Orders TODO_JM: what time? end/middle of day? night/early morning? 

Action: Clicking the link opens the Special Order Items report

User(s) to notify: Purchaser DONE_CH: how to define/determine this?

  * TODO_TR: A checkbox on the contact record called "Notify for Special Order Items"?



Internal Name (not visible to the user):
