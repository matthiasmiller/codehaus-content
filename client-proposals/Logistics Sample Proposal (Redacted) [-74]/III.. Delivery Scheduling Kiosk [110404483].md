3.30. Delivery Scheduling Kiosk

  


Requirements

We will have a Delivery Scheduling kiosk. This will be a tablet with a screen that prompts for:

  * Cashier Initial
  * Item Number
  * Item Name



  


When clicking continue, it will show a follow-up screen:

  * Name
  * Address
  * Phone Number
  * How should we confirm the schedule?
    * Text Me
    * Call or Email
  * Email
  * Delivery Date (availability is determined by zip code, per settings above)
  * Comments



  


This would get emailed to a list of contacts defined in the AppHosting.zone settings. It would NOT get sent to the guest.

  


The email will include a link to approve the request. This would walk through a similar process as approving an online pickup request. The scheduler will be responsible for confirming the delivery with the guest through the standard confirmation process.

  


Development Specification

Matthias Miller 09/10/2020: Ask Josh re tablet
