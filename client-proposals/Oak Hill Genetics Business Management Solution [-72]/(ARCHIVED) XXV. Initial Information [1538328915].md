25\. Initial Information

  


Requirements

TODO_HLD: Tim Reitz 03/24/2023: This section can be archived now. I've moved items out of here. 

  


Tim Reitz 03/16/2023: From the Sales Opp: 

Good Afternoon,

  


Anthony Martin had recommended your company to us. We are looking to add some features to our program. I’m assuming you are familiar with our system and can continue working with what Anthony has built?

  


Thanks,

•Justin Burkholder

•CCO

•Oak Hill Genetics, LLC

  


Ben Reitz 01/26/2023: Replied.

  


Ben Reitz 01/27/2023: Lead responded:

Hi Ben,

 

Sounds great!

 

  * We have around 12 employees.
  * Yes we have fiber internet at our business.



 

Thanks,

 Justin Burkholder

  


Sent the scheduler link for him to connect with Ian.

  


Ian Miller 02/09/2023: 

Tell me a little more about your business--what do you do, what services do you provide? 

  * We raise animals for medical research
  * We use software that others helped us get started with; Anthony with Paragon Solutions ([https://goparagon.com/](https://goparagon.com/)) built it around our company as we grew
  * Everything we're doing is built on Microsoft Access
    * We currently use it for animal inventory - medications they received, reports on sales, shipment paperwork; health reports; USDA forms, state forms; pushing information into QuickBooks for the invoice
  * We just built a facility which houses animals for other people
  * We need to track everything for each animal that we house for others--everything from daily observation, health check, medication we administered the animal, etc. 
    * Each action includes a billable item so that we can keep track of what needs to be billed; ability to mass assign medication to groups of animals at once; we want inventory tracking as well
    * We don't want to mix that in with our current system for our animals



  


What are the challenges or problems you're facing? What are you looking to solve? 

  * Anthony doesn't have bandwidth to continue adding features for us
    * They have basically "divorced" themselves from us
  * Our program isn't online, and we'd like to move that way
  * Wanting to be able to integrate with other programs; currently integrating with QuickBooks; would need to continue doing that



Tim Reitz 03/22/2023: What integrations do you want?

  * QuickBooks
  * Outlook



  


  * Want to be able to run the software on tablets so that employees in the buildings can pull it up when they're checking on the animals and enter data directly without having to use clipboards, and then re-enter the data when they go to the office



  


  


Offline support:

Tim Reitz 03/22/2023: This is pretty low priority for the client regarding the office use. Not needed at all for mobile use.

  


  


Standardizing terms:

Tim Reitz 03/22/2023: Client is fine with standardizing Dog/Pig and Canine/Porcine. We should settle on one.

  


  


Tracking litters:

Tim Reitz 03/22/2023: Yes, they track litter information (see around minute 48 in the first 3/22 Zoom recording). Each puppy born, info about it, various metrics about the litter, etc.

Ben: Something to note: might not be a bad idea to make sure we have numbers running alongside their litters so they can easily keep a count of number born vs number survived

  


Multi-line text fields:

Tim Reitz 03/22/2023: Currently they have multiple fields that are multi-line plain text. Doe they want to switch them to formatted text memos?

Client likes the idea of formatted text - said it would be useful.

  


  


Dog record:

Tim Reitz 03/22/2023: There are items like Rabies Certificate, Dog History Report: These are file reports that are sent with the dog when they are delivered. But they rarely use the individual ones on the dog record. Generally they are batch printed from the order for all animals in the order. But sometimes they would want to be able to print out an individual form for one animal (like if there's a last-minute change and they don't want to reprint the whole order).

  


Invoices:

Tim Reitz 03/22/2023: Printing in Access. Click on the Invoice feature, creates the invoice & pushes it to QB, gets pushed back from QB, can be printed from Access.

  


  


*Other System* Animal Inventory Tracking / SKUs:

Tim Reitz 03/22/2023: This is a whole other feature that doesn't exist yet. They recently bought a housing facility for their customers. They desperately need software for that as well (currently running on Excel). This is a completely separate feature, but Justin does want to work on design for this now as well as the main software.

Overview:

  * Animals are only housed OR bred and housed
  * Housed:
    * Entry Date
    * Daily Observation/actions
    * Exit Date
    * Vaccinations
  * Housed and litter birthed there:
    * Track mother
    * Track litter
  * Inventory tracking:
    * Facility has 6 big rooms
    * They know approximately how much room each room can hold, but would like to be able to track how many animals each room has and how much space is available (assign an animal to a room and go from there).



  


  


Animal orders vs. Transport orders: 

Tim Reitz 03/22/2023: "Animal" is for OH's own animals; "Transport" is for other animals. The two companies coexist and the orders coexist. 

Orders can be shipped in multiple shipments. 

It sounds like two separate tables for the two order types. 

Transport order has less info pulled from the database. More manual entry. 

  


Matthias Miller 03/22/2023: Rare that they need to split it into two orders,. But may have two stops on a single order, would be ideal.

  


Transport Tasks -- could assign any myriad of combinations to that....

Matthias Miller 03/22/2023: Do NOT want to autocreate these tasks, and there are a pretty unlimited amount of scenarios, they go to specific cities every week, but one week might have dogs and rabbits (preditor/prey) etc...if you want to autocreate, you'll have to have alot of roles

Matthias Miller 03/22/2023: Order entry is one step of the process, and then it goes over to the logistics team to schedule.

Matthias Miller 03/22/2023: DONE_MM - split apart the transport information from the order information

  


  


Standard Questions for Each Design: 

  


Included in email: 

Tim Reitz 03/16/2023: Ben is sending today. 

Ben Reitz 03/17/2023: Client responded. I'm placing his answers in blue after the corresponding question.

  


[X] 1\. On a scale of 1 to 10, how important is it to access the software from a mobile device, such as a phone or tablet? #8. This is fairly high on my list.

Matthias Miller 03/21/2023: Big difference between phone vs tablet.

Tim Reitz 03/22/2023: Discussing elsewhere.

  


[X] 2\. Do you want to import data from an existing software system or spreadsheets? If yes, what data (i.e. contacts, sales items, invoices, etc.)? Yes, we will need to bring across all the animal information and customer information. Invoices are made in our program but are stored in Quickbooks so they won't need to be imported.

Tim Reitz 03/22/2023: Discussing elsewhere.

  


[X] 3\. We offer two options for login format: A quick login using Gmail/Google accounts, and a username/password login. It can also be set up so that some users use one and others use the other. Which format would you prefer? Username/password login.

  


[ ] 4. Will you want to restrict access to certain portions of the system from some users? If so, you can be thinking through what groups of users you will want to have and what portions of the system you would like them to be able to access. Yes we will need restrictions.

  


[ ] 5. Do you want to use time tracking for employees? Will need to discuss the functionality of this before I can give an answer.

  


[X] 6\. We offer two formats for date fields: A simple date field where you type in the date and a calendar date picker that opens a small calendar where you can select a date. Which would you prefer? Calendar date picker.

  


Ask on call: 

  


[ ] What types of contacts will you be tracking in the system (Contact Types)?  

  


  


TODO_: Create sections & document the answers as needed.

  


  


Tim Reitz 03/23/2023: TODO_HLD: Client is interested in our Sales Opportunity feature. Justin has been looking for a sales management software to track workflow, stay on timelines, etc. 

  


Tim Reitz 03/23/2023: TODO_HLD: Client is also interested in the Time Cards. Lower on the list of priorities. Would want to consider how to have safeguards, like only allowing employees to clock in/out from the office. Maybe a time card machine, or a dedicated time card user (with the employees not able to edit time cards from their own user profile).

  


Development Specification

Tim Reitz 03/22/2023: Mobile Use: Tablet use is where they'd like to start. At some point they might want to build out something for phones.

Client is interested in improving things on the logistics side. Not so interested in cool features; interested in fixing problems. But he doesn't know what he doesn't know.

  


Tim Reitz 03/22/2023: Pain point: Struggling with managing where the drivers are at, when are they available next, and what are they available for. And same for the vehicles. It needs to be in a visual overview so you don't have to do do mental math, etc. (maybe Gantt)

* We could consider building it out ourselves or doing an integration.

  


Matthias Miller 03/22/2023: Worlds of opportunity for improvement -- doesn't just want to do cool features DONE_BR -- Send NHM to them
