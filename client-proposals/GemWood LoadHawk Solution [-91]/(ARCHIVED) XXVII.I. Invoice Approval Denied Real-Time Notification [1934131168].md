27.9. Invoice Approval Denied Real-Time Notification

  


Requirements

Sean Miller 04/29/2025: Moved to [[[IN11427](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11429&)]] - ZGW - Invoice Approval Denied Real-Time Notification

  


  


Estimated Cost: Approximately $500

  


Spec: 

  


Overview/Purpose: This is an internal real-time notification to notify users that an invoice has been marked as "Approval Denied". 

  


Details: 

  * Title: "Approval denied for Invoice <Buyer Invoice #>"
  * Text: "Open to view comments and update."
  * Display when: 
    * Record type: Delivery Ticket 
    * Action: Field is changed
    * Condition: "Approval Denied" checkbox is changed from not checked to checked



Notification preference:

  * On (play sound, show banner)


  * Urgent? (notification includes "!"): No
  * Action: Opens the corresponding Delivery Ticket record 
  * User(s) to notify: All users with the "Edit Invoice approval fields on Delivery Tickets" Permission



  


Other Notes:

  * The alert disappears automatically when clicked (standard). 
  * Each user that receives the alert must click on it to dismiss it (standard).



  


Development Specification

Mockup: N/A

  


TODO_PRICING: Tim Reitz 12/10/2024: Not included in the HLD. But the invoice review feature was noted at some point in the "Additional Features to Consider" section, so definitely an extra / add-on / scope creep item.
