5.7. Data Access Controls

  


Requirements

The Solution includes settings that control access to / visibility of various portions of the solution, including reports, records, and parts of records. These roles/permissions are controlled based on a few things:

  * Permissions enabled via User Groups (Super Admins & Regional Reps vs. Facilitators & Standard Members)
  * Organization Roles checkboxes on the Contact record (Super Admins) 
  * Designations on Growth Ring Group and Region records (Regional Reps and Facilitators).



  


Note that users with the "Super Admin" checkbox on their Contact record have full access to the whole system.

  


Each Organization Role has the concept of "uplines" and/or "downlines". Any user can edit any of the information for any of their "downlines". The hierarchy is as follows:

  * All Super Admins
  * Regional Rep
  * Facilitator
  * Standard Member



Note that all Super Admins are uplines to everyone else. A Regional Rep is an upline to all Facilitators in groups in the region(s) for which is a Rep, and all Standard Members in those Facilitators' groups. A Facilitator is an upline to all Standard Members in the group for which he is set as the Facilitator. 

  


The table below lists which individuals can view or edit various types of information in the Solution:

  


Record| Org Roles That Can View| Org Roles That Can Edit  
---|---|---  
Region| Everyone| Super Admins  
Contact Type| Everyone| Super Admins  
Lead Source| All Facilitators + All Regional Reps + All Super Admins| Super Admins  
Church Affiliation| Everyone| Super Admins  
Industry| Everyone| Super Admins  
Growth Ring Group Type| Everyone| Super Admins  
Development Resource Category| Everyone| Super Admins  
Development Resource Media Type| Everyone| All Facilitators + All Regional Reps + All Super Admins  
Knowledge Tree Branch| Member + Uplines| Member + Uplines  
Event Type| Everyone| N/A (not editable in the Solution)  
Contact|   
|   
  
Member Type w/ active membership| Everyone| Member + Uplines  
Member Type w/ inactive membership| All Regional Reps + All Super Admins| All Regional Reps + All Super Admins  
Lead Type| All Regional Reps + All Super Admins| All Regional Reps + All Super Admins  
Member Organization Type | Everyone| All Regional Reps + All Super Admins  
Other Individual Type| All Regional Reps + All Super Admins| All Regional Reps + All Super Admins  
Other Organization Type| All Regional Reps + All Super Admins| All Regional Reps + All Super Admins  
Growth Ring Group| Growth Ring Members + Uplines| Facilitator + Uplines  
Growth Ring Meeting| Everyone (with some sections/fields restricted)| Members (specifically the Meeting Secretary), Facilitator & Uplines   
Growth Ring Goal (for member w/ active membership)| Member + Uplines + concurrent Members of the same Growth Ring Group (based on the Attendance of GR Meetings)| Member + Uplines  
Growth Ring Goal (for member w/ inactive membership)| All Regional Reps + All Super Admins| All Regional Reps + All Super Admins  
  
Development Resource| Everyone| New (unsaved) records: Everyone   
After initial save: Creating Member + All Facilitators + All Regional Reps + All Super Admins  
Development Resource Review (for member w/ active membership)| Everyone (except for private notes, which is for Member + Uplines)| Reviewing Member + Uplines  
Development Resource Review (for member w/ inactive membership)| All Regional Reps + All Super Admins| All Regional Reps + All Super Admins  
Knowledge Tree Entry (for member w/ active membership)| Member + Uplines| Member + Uplines  
Knowledge Tree Entry (for member w/ inactive membership)| All Regional Reps + All Super Admins| All Regional Reps + All Super Admins  
Event|   
|   
  
With Event Visibility = Public| Everyone (with additional visibility restrictions based on Event Status, and some sections/fields restricted to only Regional Reps and Super Admins)| Regional Reps and Super Admins  
With Event Visibility = All Members| Everyone (with additional visibility restrictions based on Event Status, and some sections/fields restricted to only Regional Reps and Super Admins)| Regional Reps and Super Admins  
With Event Visibility = Invitation Only| Members with an Event Registration record for the Event and all their uplines (with additional visibility restrictions based on Event Status, and some sections/fields restricted to only Regional Reps and Super Admins)| Regional Reps and Super Admins  
Event Registration|   
|   
  
Linked to an Event with Event Visibility = Public| Everyone (basic details only; with additional visibility restrictions based on individual sections/fields; more details visible to the Member whose name is in the Registrant Name field & uplines; all details visible to Regional Reps and Super Admins)| Regional Reps and Super Admins  
Linked to an Event with Event Visibility = All Members| Everyone (basic details only; with additional visibility restrictions based on individual sections/fields; more details visible to the Member whose name is in the Registrant Name field & uplines; all details visible to Regional Reps and Super Admins)| Regional Reps and Super Admins  
Linked to an Event with Event Visibility = Invitation Only| Member whose name is in the Name field & all uplines (with additional visibility restrictions based on individual sections/fields; all details visible to Regional Reps and Super Admins) | Regional Reps and Super Admins  
Wiki Pages| Varies by Category, depending on the Restricted Data Policies (see corresponding section of the proposal)| Super Admins  
Email Reminders| Super Admins| Super Admins  
  
  


  


Other Notes:

  * Note that some records have individual sections and/or fields that have additional restrictions, as detailed in the corresponding sections of the proposal.



  


Development Specification

Mockup: N/A

  


Change Requests:

  * Tim Reitz 03/07/2024: [[[IN9262](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9264&)]] - ZSB - Growth Ring Goals - Clarifications / Tweaks
  * Tim Reitz 04/10/2024: [[[IN9074](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9076&)]] - ZSB - Contact Types - Handle Organizations more cleanly
  * Tim Reitz 04/10/2024: [[[IN9697](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9699&)]] - ZSB - Changes to Wiki Module for Non-Admin Users
  * Tim Reitz 04/11/2024: [[[IN8960](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8962&)]] - ZSB - Add Features for Symbuzz Extra (prev. called Cross Network Forum)
  * Tim Reitz 04/16/2024: [[[IN8957](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8959&)]] - ZSB - Add Email Reminders Module (prev. Internally created email reminders)
  * Tim Reitz 04/29/2024: Testing job: [[[IN8331](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8333&)]] - [[PC0156265]] - ZSB - DB Levels: Specify Permissions (T&M)
  * Tim Reitz 07/19/2024: [[[IN9997](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9999&)]] - ZSB - Fix Growth Ring Meeting visibility error
  * Tim Reitz 06/04/2025: [[[IN9119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9121&)]] - ZSB - Add Events Feature (Info Meetings, etc.)
  * 


  


  


  


Matthias's thought on implementing this is to code functions to get uplines/downlines based on a contact. Then, create functions for "who can see" and "who can edit" various records. (Basically, uplines can "impersonate" downlines -- i.e. they have access to anything their downlines have access to.)

  


  * The proposal should refer to specific permissions in the design rather than the user groups that are expected to have that permission.
  * If there is confusion or difficulty thinking in terms of permissions, we may be able to list both permissions and the group names, but this makes it harder to keep the living spec up to date and the coding will be done based on the permissions.



  


CCI: Tim Reitz 05/30/2023: Per Matthias, we should restrict Activity History for any users who don't have access to a full record. 

  


BID:

[ ] UserIsRegionalRepOrSuperAdmin -- used for "RegionalReps + Uplines"

[ ] UserCanViewGroup( vGroup) -- is an active member or has editing permissions for the group

[ ] UserCanEditGroup( vGroup) -- returns true if user is facilitator for the group, a rep for the group's region, or a any super admin. Used for editing Active Members, Growth Mtgs, and Growth Groups.
