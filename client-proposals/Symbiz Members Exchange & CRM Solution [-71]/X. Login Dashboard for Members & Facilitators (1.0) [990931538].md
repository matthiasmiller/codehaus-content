10\. Login Dashboard for Members & Facilitators (1.0)

  


Requirements

Welcome Banner / Header:

  * Symbiz logo 
  * "Powered by Silverloom" (label) 
  * "Welcome to the Members Exchange, <first name of logged-in user>" (label) 
  * "View Profile" (link to Contact record for logged-in user)  
  * "Main Menu" (link to the main Members Menu at [https://symbiz.silverloom.io/](https://symbiz.silverloom.io/)) 



  


  


Meetings & Events Tile:

  * "My Next Growth Ring Meeting:" (label; displays details for the next meeting with a date of today or in the future that has a status of tentative or scheduled and the current user's Contact is in attendance.)
    * Details: (read-only field; link; in the following format: <meeting date and time, link to meeting record>) 
    * Location: (read-only field; link; in the following format: <meeting location or meeting link>)
    * Resource: (read-only field; link; in the following format: <meeting resource, truncated with ellipsis to 60 characters, link to record>)
  * Print Book/Impact Worksheet (button; opens the PDF from the "Book/Resource Impact Worksheet" memo on the Silverloom Settings page)
  * Label: "Other Upcoming Events:"



TODO_VA: Tim Reitz 03/29/2025: In the Events feature proposal, we were planning to remove the word "Other" from this label since this has been changed specifically show Event records. 

Tim Reitz 07/10/2025: This has not been removed (see [https://testsymbiz.silverloom.io/Integrations/homepage.htm?_=lKaNA&](https://testsymbiz.silverloom.io/Integrations/homepage.htm?_=lKaNA&)), so we should write up a CR to knock it out. 

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



  


  


My Current Goals Tile:

  * List Items: <Life Branch: Goal description> (looks at the Growth Ring Goals record for the current user and the next upcoming Growth Ring Meeting; displays the details for all Life Branches that have a goal set, and displays blank for empty items)
  * Message: "No goals set for the upcoming Growth Ring Meeting." (visible if there are no goals set for the current user for the next upcoming Growth Ring Meeting) 
  * Button: "View/Edit Goals" (if one or more goals are set) / "Create Goals" (if there are no goals set): (link to the Growth Ring Goals record that has filled in the Goals tile; creates a new record if the tile is blank / if no current Goals exist.)
  * Button: "Print Meeting Goals Worksheet" (opens the "Print Meeting Goals Worksheet" prompt screen - see corresponding spec)



  


  


My Life Vision Tile:

  * Field: <contents of Life Vision Statement from the current user's Contact record>
  * Button: Print My Life Goals (prints the filled-out goals for the current user)
  * Button: Print Blank Worksheet (prints the blank worksheet)



  


  


Community Tile: Note that this tile includes various buttons and the News Feed feature, which is a scrolling list of new items from the past X days (the number to be set via the "Days for Dashboard News Feed" field on the Silverloom Settings page).

Included items: 

  * <#> Members (button; opens the Member Directory report)
  * <#> Groups: (button; opens the All Groups report)
  * <#> Resources: (button; opens the Development Resources report)
  * "News Feed:" (label for the scrolling news feed feature, with the following items included:



TODO_VA: Tim Reitz 03/29/2025: I don't see this "News Feed" label - could/should we add it?  

  * Newly-scheduled Events: 
    * Conditions: Event records that have been marked as Scheduled within the set number of days. 
    * Preceding icon image: Calendar
    * Display format: <Event ID>" (with link to the record) 
  * New Development Resources: 
    * Conditions: Development Resource records marked as Approved within the set number of days. 
    * Preceding icon image: Book
    * Display format: <Resource Description>" (with link to the record) 
  * New Groups: 
    * Conditions: Growth Ring Group records created within the set number of days, with at least one linked Member. 
    * Preceding icon image: Person 
    * Display format: <Group Description>, <Facilitator State>" (with link to the Group record) 
  * New Members: 
    * Conditions: Member-type Contact records with memberships that have been activated or reactivated within the set number of days. 
    * Preceding icon image: Group of people
      * Display format: "<FirstName MiddleName LastName>, <City, State>" (with link to the record) 



  


Additional News Feed details: 

Group by: 

  * First by date: Greatest/current date at the top, with a bold label in the following format: "MMMM DD, YYYY"
    * Note that if there are no new items for a day, that group will simply be hidden. 
  * Second by record / item type: In the following sequence, with the same labels as the subgroup labels; note that if there are no new items for a day, that sub-group will simply be hidden: 
    * Resources 
    * Groups
    * Members



  


Sort by: Chronological order, based on the following: 

  * Resources: Approved Status Date + Status Time (most recent at the top) 
  * Groups: Created Date (most recent at the top)
  * Members: Membership Activation Date & Time (most recent at the top) 



  


Example: 

May 2, 2024: 

  * [icon] The Five Dysfunctions of a Team, Patrick Lencioni
  * [icon] Reset, David Murray
  * [icon] Group 51, Pennsylvania
  * [icon] John A. Doe, Myerstown, Pennsylvania
  * [icon] James B. Smith, Myerstown, Pennsylvania
  * [icon] John A. Doe, Myerstown, Pennsylvania
  * Etc.



  


Other Notes: 

  * N/A



  


Development Specification

Change Requests: 

  * Tim Reitz 05/06/2024: [[[IN9857](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9859&)]] - ZSB - Dashboard - Add "Main Members Menu" Link
  * Tim Reitz 05/06/2024: [[[IN9828](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9830&)]] - ZSB - Dashboard Testing 
  * Tim Reitz 07/20/2024: [[[IN9836](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9838&)]] - ZSB - Dashboard - Add Scrolling News Feed
  * Tim Reitz 03/29/2025: [[[IN10119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10121&)]] - ZSB - Dashboard - Update Scrolling News Feed with Events Items
  * Ben Reitz 08/01/2025: [[[IN11205](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11207&)]] - ZSB - Dashboard - Add "Print Book/Impact Worksheet" button (prev. Resource - Add "Print" button)
  * Ben Reitz 09/17/2025: [[[IN10074](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10076&)]] - ZSB - Growth Ring Goals - Add "Meeting Goals Worksheet" printout (prev. Add "Print Goals" button)
  * 


  


  


Tim Reitz 11/07/2023: See: 

  * The CR: [[[IN8898](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8900&)]] - ZSB - Login Dashboard for Members & Facilitators.
  * Our mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=344805851](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=344805851)
  * Rubico's wireframe: [https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=0%3A1&node-id=9-2&scaling=min-zoom&starting-point-node-id=9%3A3](https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=0%3A1&node-id=9-2&scaling=min-zoom&starting-point-node-id=9%3A3)


