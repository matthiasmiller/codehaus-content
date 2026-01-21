5.10. User Notifications

  


Requirements

The Solution includes the following User Notifications:

  


Misc Notes:

  * If a user does not have an email address set on their Contact record, they will simply be skipped on email notifications that they otherwise would have received.
  * Technical note: Anywhere a specific trigger is mentioned, a Realtime Notification will be used for the in-app notification. A Report Alert will accompany a scheduled task.
  * Notifications with a "Format" = "Member's choice" are configurable on the member's Contact record (see details in the corresponding section of the proposal). If the member is an online user (with a User Profile), they will be able to select in-app alert, an email, or eventually a text message. If the member is not an online user, they will only be able to receive emails (including email-to-fax) or text messages.
  * Note that in a future phase, text messaging probably will be added as an additional option for at least some of the alerts.



  


Development Specification

Change Requests:

  * Tim Reitz 03/07/2024: [[[IN9218](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9220&)]] - ZSB - Change "Members Portal" to "Members Exchange"
  * Tim Reitz 03/29/2024: [[[IN9471](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9473&)]] - ZSB - Growth Ring Meeting - Add Meeting Time
  * Tim Reitz 04/08/2024: [[[IN9522](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9524&)]] - ZSB - User Notifications - Clarify Triggers
  * Tim Reitz 04/08/2024: [[[IN9638](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9640&)]] - ZSB - Various Changes March 2024 (batch 1)
  * Tim Reitz 04/11/2024: [[[IN8960](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8962&)]] - ZSB - Add Features for Symbuzz Extra (prev. called Cross Network Forum)
  * Tim Reitz 06/07/2024: [[[IN9962](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9964&)]] - ZSB - Prepare Symbuzz Extra Posts - wrong file
  * Tim Reitz 06/07/2024: [[[IN9898](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9900&)]] - ZSB - User Notifications - Work on Annual Renewal Notices Due
  * Tim Reitz 06/10/2024: [[[IN9854](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9856&)]] - ZSB - User Notifications - Change "Review New Resources" to "Approve New Resources", etc.
  * Tim Reitz 06/10/2024: [[[IN9817](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9819&)]] - ZSB - Growth Ring Meeting Notifications - Include Resource, Time, and Location
  * Tim Reitz 07/20/2024: [[[IN10206](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10208&)]] - ZSB - User Notifications - Scheduled Task Alert for "Yesterday's Growth Ring Meeting"
  * Tim Reitz 07/20/2024: [[[IN10097](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10099&)]] - ZSB - User Notifications - Scheduled Task Alert for "Growth Ring Meeting Tomorrow"
  * Tim Reitz 07/20/2024: [[[IN9897](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9899&)]] - ZSB - User Notifications - Recently Ended Memberships - Improvements / Fixes
  * Tim Reitz 08/21/2024: [[[IN10425](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10427&)]] - ZSB - Wrong Group Meeting alert
  * Tim Reitz 09/03/2024: [[[IN9889](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9891&)]] - ZSB - Add Time Zone Feature (for Groups & GR Meetings)
  * Tim Reitz 09/03/2024: [[[IN9858](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9860&)]] - ZSB - User Notifications - Add .ics Calendar Invites with New GR Meeting Notification
  * Ben Reitz 05/01/2025: [[[IN9929](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9931&)]] - ZSB - User Notifications - Scheduled Task Alert for PREPARE Symbuzz Extra Posts
  * Ben Reitz 10/08/2025: [[[IN10936](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10938&)]] - ZSB - User Notifications - Scheduled Task Alert for Review / Update Annual Goals (Facilitator)
  * 


  


  


Mockup: N/A

  


  


TODO _PHASE2: Tim Reitz 05/11/2023: When we spec out the text message feature/option, we should consider how to handle the subject line (probably just omit it from the text message?).
