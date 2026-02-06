8\. Changes to the Dashboard

  


Requirements

*Documented 

  


Tim Reitz 03/29/2025: Note: I documented this in the main living spec today, along with [[[IN10119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10121&)]] - ZSB - Dashboard - Update Scrolling News Feed with Events Items. 

  


  


Make the following changes to the Dashboard (changes noted in blue / strikethrough): 

  


Meetings & Events Tile:

  * Label: "Other Upcoming Events:" (displays the next three General Meeting events, chronologically; this includes any non-industry-specific meetings as well as industry-specific ones that match the industries on the current user's Contact record.)
    * List Item: <Meeting Name: date (link to meeting)>
    * Displays the next three upcoming Scheduled Events that the user can view; they must match the following criteria:
      * Current logged-in user is able to view the record (i.e. Event Visibility = Public or All Members, or Invitation Only and the user has a Registration record for the event), and 
      * Event Status = Scheduled, and 
      * Event Type is:
        * Annual Summit, or
        * Industry Forum and at least one of the selected Industries match one selected on the user's Contact record, or
        * Info Meeting, or
        * Launch Meeting;
      * Sorted by: Event Date (nearest item at the top) then by Event Name (alphabetically); 
      * Displayed in the following format: <Event Name: m/dd/yyyy (link to Event record)>
    * View All (button; opens the Master Events report with Event Date Start filter set to the current day)



  


Development Specification

Ellis Miller 06/22/2024: 

[ ] JonathanB will add this.

  


TODO_VA: Tim Reitz 07/04/2024: Per Ellis, reconsider rules for this: Perhaps display the Annual Summit, even if not one of the next 3. 

  


BID: 1 day
