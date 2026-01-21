20.1.6.2. Notice of State Approval Received

  


Requirements

Accessed from: Menu

  


Name: Notice of State Approval Received

  


Level: Contacts

  


Subject: SPE Slots Available

  


Attachments:

  * FB SPE Flyer (includes the Operating Agreement and Joinder) 



  


Send To: schools marked Eligible To Receive SPE Donations

  


Body: This email body is configured by the client in the live system.

  


Development Specification

Change Requests: 

  * Tim Reitz 09/13/2024: [[[IN9844](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9846&)]] - XFB - Adding PDF Documents into FBSPE
  * 


  


Ellis Miller 02/15/2021:

  


[ ] One simple macro for amount.

[ ] To recipients will be filtered by the main template export.

[ ] Conditional paragraphs will use something like macros from "     Contact Groups"

       #IncludeIf( ContactIsAccountant (vRecordID))#

....

#EndIf#

  


1 DAY.
