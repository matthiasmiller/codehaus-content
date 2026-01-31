1.0.1. Incident and Wiki Tracking Notifications

  


Requirements

The Solution will include the standard Incident and Wiki Tracking Notifications feature. 

  


The feature allows users to track any Incident or Wiki page in the software via a "Track" checkbox on the record. For Incidents, this checkbox is checked automatically for the incident assignee, and it can be checked manually by other users who wish to track it. For Wiki pages, this checkbox is to be checked manually as desired. 

  


The Solution sends the following email whenever a tracked Incident is assigned to the user or edited by another user or a tracked Wiki page is edited by another user: 

  


Subject: Changes to <[[[IN1234](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-1236&)]] - Sample Title>

  


Body: 

<Receiving User's First Name>, a record you are tracking was changed by <Editing User's User Name>: <[[[IN1234](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-1236&)]] - Sample Title>

  


<link to incident>

  


Other Notes: 

  * This will probably receive customizations at some point in the future, but is being deployed as the standard feature to give Think Ink time to use it as-is.



  


Development Specification

Mockups: N/A

  


Tim Reitz 07/19/2023: In the CR where this feature had been discussed, Ellis had mentioned a $500 initial setup fee: [[[IN7848](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-7850&)]] - ZTK - Email Notifications for Incidents.
