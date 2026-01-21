7.2.5. Contact Record - Notifications Section

  


Requirements

  * Notifications custom section (visible if Contact Type = Member; visible to and editable for the corresponding Member and all his uplines):
    * Notification Preferences (embedded spreadsheet with the following:) 
      * Columns: 
        * Notification Name (auto-fills with a row for each notification available to the Member) 
        * In-App Alert (checkbox; column is hidden if Member is not an online user; defaults to checked) 
        * Email/Fax (checkbox; defaults to checked)
        * Text Msg. (checkbox; may be added in the future) 
      * Automatically sorted by: Alphabetically by Notification Name
      * Buttons to insert/append/remove rows: N/A
      * Show 4 rows without scrolling
      * Other Notes:
        * As indicated above, members who are not online users may still receive notifications via email (and/or text message, once that feature is added).
        * The Notifications will be displayed in the following sequence:
          * New Growth Ring Meeting Scheduled
          * Growth Ring Meeting Rescheduled
          * Growth Ring Meeting Canceled
          * Upcoming Growth Ring Meeting
          * Yesterday's Growth Ring Meeting
          * Review New Resources
          * Missing Payments / Confidentiality Agreements
          * Recently Ended Memberships
          * Annual Renewal Notices Due
          * Review / Update Annual Goals
          * Review / Update Annual Goals (Facilitator)
        * Warning on Save if a new row has been added but none of the delivery methods have been selected: "A new Notification has been added, but no delivery method has been selected." 
    * On-screen message in red text if one or more available notifications don't have any notification selections: "One or more available notifications are turned off."



  


Development Specification

Change Requests:

  * Tim Reitz 04/09/2024: [[[IN9044](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9046&)]] - ZSB - Contact Record - Improve User Notifications Interface
  * Tim Reitz 04/09/2024: [[[IN9565](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9567&)]] - ZSB - Contact Record - Clarify Visibility & Editability
  * Ben Reitz 08/01/2025: [[[IN11164](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11166&)]] - ZSB - Notifications - Growth Ring Meeting in 3 Days


