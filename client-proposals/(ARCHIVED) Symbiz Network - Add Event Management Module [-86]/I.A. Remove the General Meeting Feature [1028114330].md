1.1. Remove the General Meeting Feature

  


Requirements

*Documented 

  


As mentioned in the Overview, the existing General Meetings feature is being replaced in this process, either by building out the existing feature and renaming it to "Events", or by removing it and replacing it entirely. 

  


Note that any existing General Meeting events in the live system should be documented prior to running the update, so that they can be entered as Events after this feature is deployed. This could be done manually or via an export/import -- details to be determined at the time of deployment, based on what would be most cost-effective and efficient.

  


Development Specification

Tim Reitz 04/29/2024: Note that we are replacing the existing (very simple) General Meeting record with the (much more complex) Event record. We can reuse pieces / features from the General Meeting record as needed if that is helpful.

Ellis Miller 06/20/2024: Likely easiest to completely pull and then start from scratch. Proposing to delete the General Meeting level and follow the errors.  3 Hours.

_EM: Tim Reitz 07/03/2024: There actually are some General Meetings in the live system now (see the report: [https://symbiz.silverloom.io/Reports/Standard/Std_General_Meetings?Asks=...&State=pa4IpoPlMj0](https://symbiz.silverloom.io/Reports/Standard/Std_General_Meetings?Asks=...&State=pa4IpoPlMj0)). Does this change our approach, or should we continue with just removing the feature? (from where I sit that still seems simplest). 

  


I'm thinking we should have them manually re-enter the items as Event records. Or we could potentially give them an export / import (maybe for an extra cost) if there are a lot of General Meetings at the time of deployment.

TODO_VA: Tim Reitz 07/04/2024: Per Ellis, let's create a user report with all the General Meeting fields (customized version of the existing standard report). Then they can export before the update, then manually re-enter in the new feature. 

  


  


Tim Reitz 05/09/2024: We need to remove the following: 

  * [X] General Meeting Record 
  * [X] General Meetings Report 
  * [X] Menu sections / options that reference General Meetings: 
    * Admin | General Meeting Management | New General Meeting
    * Admin | General Meeting Management | View General Meetings
    *     * Any others 
  * [X] User Notifications:



Remove the existing "New General Meeting" notification:

6\. Name: New General Meeting

Record Type: General Meeting

Date: Created Date

Trigger / Scheduled Task Details: On save, for new records only. 

Scheduled Task: N/A

Format: Member's choice

Send To: All Members who have the notification enabled

Subject / Message:

Subject: New General Meeting Scheduled

Message: Hello, <Member FirstName>, 

  


A new General Meeting has been scheduled. Here is the information:

Date: <mm/dd/yyyy>

Description: <Meeting Description> 

Virtual Meeting: <Yes/No>

Meeting Link: <link; if Virtual Meeting>

In-Person Meeting: <Yes/No>

Location: <Location; if In-Person Meeting>

Address: <full address; if In-Person Meeting> 

Link to Meeting record: <link>

  


Remove the existing "New Industry-Specific Meeting" notification:

7\. Name: New Industry-Specific Meeting

Record Type: General Meeting

Date: Date that a relevant Industry is selected on a scheduled General Meeting, or date that an Industry matching a scheduled General Meeting is selected on the Contact record.

Trigger / Scheduled Task Details: On save, if one of the following criteria is met: 

  * A relevant Industry is selected on a scheduled General Meeting, or 
  * An Industry matching a scheduled General Meeting is selected on the Contact record.



Scheduled Task: N/A

Format: Member's choice

Send To: All Members in the selected industry(ies) who have the notification enabled

Subject / Message:

Subject: New Industry-Specific Meeting Scheduled

Message: Hello, <Member FirstName>, 

  


A new industry-specific General Meeting has been scheduled for your industry. Here is the information:

Date: <mm/dd/yyyy>

Description: <Meeting Description> 

Industry: <Industry(ies)> 

Virtual Meeting: <Yes/No>

Meeting Link: <link; if Virtual Meeting>

In-Person Meeting: <Yes/No>

Location: <Location; if In-Person Meeting>

Address: <full address; if In-Person Meeting> 

Link to Meeting record: <link>

  


[X] Data Access Control: 

General Meeting| Everyone| All Regional Reps + All Super Admins  
---|---|---  
  
  


[X] Other / Misc.: 

  * [X] Contact Record | Notifications section / RG: Remove the following items: 
    * New General Meeting
    * New Industry-Specific Meeting
  * [X] Dashboard: Remove the references to General Meetings (to be replaced with Events)
    * Label: "Other Upcoming Events:" (displays the next three General Meeting events, chronologically; this includes any non-industry-specific meetings as well as industry-specific ones that match the industries on the current user's Contact record.)
      * List Item: <Meeting Name: date (link to meeting)>


