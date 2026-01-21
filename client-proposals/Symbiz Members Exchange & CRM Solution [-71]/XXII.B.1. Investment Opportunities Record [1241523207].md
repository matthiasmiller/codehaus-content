22.2.1. Investment Opportunities Record

  


Requirements

Tim Reitz 04/06/2023: Per the client today, this can be a Phase 2 (or later) item. They want to make sure the core of the system is working (members, groups, etc.) first. 

  


Overview: This record stores information about Investment Opportunities that are created and shared by members.

  


Accessed via: TODO_IDD

  


Sections and Fields: 

  * Investment Opportunity Overview section:
    * Status (auto-set and read-only; Submitted/Approved/Archived)
    * ID (auto-set and read-only; unique identifier for the record)
    * Investment Opportunity Title (single-line; required)
    * Member Name (automatic and read-only; user who created the opportunity; copies name, phone number, email, mailing address, and bio onto the investment opportunity)
    * Member Phone
    * Member Email
    * Member Address
    * Member Bio 



  


  * Sponsor Details section:
    * Sponsor Name (text)
    * Sponsor Phone Number (text)
    * Sponsor Email (text)
    * Sponsor Address (text)
    * Sponsor Bio (memo)
    * View X Other Opportunities (link that opens the Investment Opportunities report, filtered to this Sponsor)



  


  * Opportunity Details section:
    * I Have (memo)
    * Plans / Vision for this Opportunity (memo)
    * ROI (single-line)
    * Term Length (single-line)
    * Date Funds Needed (single-line)
    * References / Referrals (memo)
    * Experience (memo)
    * Hard assets / collateral (memo)
    * Investor Benefits (memo)
    * Report Performance at end of Term Length (memo)
    * Approved (checkbox + automatic/read-only Approved By and Approved Date; editable by facilitators and admins)
    * Created Date (auto-set and read-only)
    * Closed (checkbox and date)



  


  * Discussion section: 
    * Displays details for all Discussion Threads linked to the opportunity and option to comment (details TBD)
    * New Discussion Thread (link) 



  


Data Access

  * Visible to all users if Approved
  * Always visible/editable for sponsor, facilitators, or admins



  


Special Considerations: 

  * Copy Record: 
  * Delete Record: 
  * Merge Record: 



  


Other Notes:

  * Investment Opportunities should automatically be closed out if the linked Contact ("Member Name") is inactive.



  


Development Specification

For reference, view: [https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=0%3A1&node-id=646%3A4753&scaling=min-zoom&starting-point-node-id=9%3A3](https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=0%3A1&node-id=646%3A4753&scaling=min-zoom&starting-point-node-id=9%3A3)
