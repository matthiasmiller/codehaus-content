12.8.0.1. Duane's Notes

Matthias Miller 07/28/2025: Due Dates: TODO_DB_THINK: Do you like these calculations? [https://testownly.silverloom.io/Reports/User/Personal/Duane.Burkholder/Due_Date_Calculations](https://testownly.silverloom.io/Reports/User/Personal/Duane.Burkholder/Due_Date_Calculations)

  


  


THOUGHTS:

  


  * Online portals/app and handling customers that want to pay more then what they owe. 
    * pay ahead or decrease contract balance without moving due date far into the future.
    * put money in the deposit (How do we validate and communicate to the customer for states that do not allow increased amount in the deposit account)
    * 


  


\----

  


  


  * RG of notes on the contact record:
    * When a note is checked for "Needs Follow up", an assignee is required and follow up date (i.e. due date).
    * When note is checked for "Needs Follow-up" their needs to be a completed checkbox that when check logs on the record who completed it and the date of completion
    * When we build dashboards these follow-up assignments should have a place on the dashboard
    * Could this be expanded to be a stand alone thing that you could tie a note to just about any record that may need review and follow up?
      *   * DASHBOARD
    * Duane Burkholder 07/24/2025: TODO_MM:I want to understand the capabilities of a standard dashboard and how much flexibility a user has to customize their dashboard and it stay that way.
    * Duane Burkholder 07/24/2025: TODO_MM: Is there a way to define, maybe on the user record, where a person lands when logging on? I would like to for a user to define where they land every time they log in after a logout cycle or maybe an inactive time frame.
    * Duane Burkholder 07/24/2025: TODO_MM can we define a log out point for anyone that is inactive for a certain amount of time?
  * RTO Pro Database connector/Migration
    * Duane Burkholder 07/24/2025: TODO_MM: in a conversation with Josh on Wednesday morning he mentioned that we need to get started on data migration sooner than later. Thoughts?
    * Maybe it is that we set a point in the future that we must start working on this



  


  


  * Hauling Calculation (% of the price of the building) - TODO_DB_DONE/TODO_IDD - Need to map out hauling charges incurred



Duane Burkholder 07/18/2025: TODO_IDD I do not particularity remember what this was in relation to but I am going to take a stab at what I think this was about. 

  


This field will be on the manufacturer record and is a place to store what was agreed upon between the Rental Company and the manufacturer. We currently do these calculations in spreadsheets now where we create a vendor invoice for the person that did the hauling. I think I want to talk about invoice generation workflow whereby the Rental Company can generate a vendor invoice for the hauling company and pay it without any interaction from the hauling company. This keeps haulers really happy if they don't have to do paperwork. I do worry about non usage of a feature like this.

  


There may be some value in having it be an RG with:

  * Date field 
  * Percentage field 
  * Simple notes field 



  


I am thinking that we may need to be a bit more complex and do something like:

  * Date
  * Type: Percentage, mileage
  * Numerator
  * Simple notes



  


TODO_MM this reminds me that we will need to talk about hauler contact records as a part of logistics which may be the other place we store the hauling calculation.

  


  


  


  


Matthias Miller 07/25/2025: TODO_IDD: Sales Tax - uploadable table of sales tax zones, and option for TaxJar

  


  


  


TODO_IDD - design recurring notes (like Recurring VIs in Assist??)

  


  


TODO_DB: Build out the details for the welcome email note

  


TODO_IDD - Email Reminders
