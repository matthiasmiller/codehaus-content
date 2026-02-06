3.3.5. Notification: Event Registration Confirmation

  


Requirements

*Documented 

  


Name: Event Registration Confirmation

Record Type: Event Registration 

Date: When a Contact that has an email address specified is registered for an Event. 

Trigger / Scheduled Task Details: On the first save of an Event Registration record after "Registration Status" is set to "Attending", if the Contact selected in "Registrant Name" has an email address specified and if the "Event Status" = "Tentative" or "Scheduled". 

Scheduled Task: N/A

Format: Email 

Send To: The Registrant on the Event Registration record

Subject / Message:

Subject: Symbiz Event Registration Confirmed

Message: Hello, <Contact FirstName>, 

  


Thank you for registering for the following Symbiz Event: <Event Name>! Your registration has been confirmed in our system. 

  


Here is the Event info:

Date: <mm/dd/yyyy>

Time: <HH:MM AM/PM>

Time Zone: <Time Zone> 

Description: <Event Description> 

Meeting Link: <link> (visible if "Event Format" = "Virtual" or "Hybrid")

Dial-In Number: <Dial-In Number> (visible if "Event Format" = "Virtual" or Hybrid")

Dial-In Meeting ID: <Dial-In Meeting ID> (visible if "Event Format" = "Virtual" or Hybrid")

Dial-In Passcode: <Dial-In Passcode> (visible if "Event Format" = "Virtual" or Hybrid")

Location: <Location> (visible if "Event Format" = "In-Person" or "Hybrid")

Address: <full address> (visible if "Event Format" = "In-Person" or "Hybrid")

  


For more info or to cancel your registration, please contact: <Registration Email> or <Registration Phone>. 

  


Add to Google Calendar (link; see details in corresponding section of the proposal / living spec) 

  


Add to Outlook Calendar (link; see details in corresponding section of the proposal / living spec)

  


View Event details (link; opens the the record in Silverloom)

  


Thanks! 

\- The Symbiz team

  


Development Specification

Change Requests: 

  * Tim Reitz 02/01/2025: Added in [[[IN10973](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10975&)]] - ZSB - Events - Add "Event Registration Confirmation" Email Notification
  * Tim Reitz 03/29/2025: [[[IN11109](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11111&)]] - ZSB - Event Email Notifications - Include call-in info


