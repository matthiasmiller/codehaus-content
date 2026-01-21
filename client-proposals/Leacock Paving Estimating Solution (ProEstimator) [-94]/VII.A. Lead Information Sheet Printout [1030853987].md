7.1. Lead Information Sheet Printout

  


Requirements

Purpose/Overview: This is a basic internal-facing PDF of all the Customer Information details on a Proposal record.

  


Printed From: 

  * "Print Lead Information Sheet" link on the Proposal record



  


File Format/Name: PDF:

  * If "Job Type" = "Residential": "Lead Info <Proposal #> \- <Customer Last Name>, <Customer First Name> (<Address Line 1>; <Job Type>)"
    * Example: "Lead Info 15001 - Byler, John (1234 Some St; Residential)"
  * If "Job Type" = any other: "Lead Info <Proposal #> \- <Customer Name> (<Job Name>; <Job Type>)"
    * Example: "Lead Info 15002 - ABC Builders (Ephrata Community Park; Commercial)" 



 

Fields to be Filled (note that if any fields are blank on the Proposal record, they also are blank on this printout) 

  


  * Internal Details Section: 
    * Proposal/Lead # (displays the "Proposal #") 
    * Received Date (displays the "Received Date")  
    * Received By (displays the "Received By") 



  


  * Sales Rep (displays the name of the Sales Rep in the "FirstName LastName" format)  
  * Appointment Date (displays the "Appointment Date") 
  * Appointment Time (displays the "Appointment Time") 



  


  * Customer Details Section: 
    * Customer Name (displays the name of the Customer, with the following details / behaviors: 
      * for Organizations: displays the "Name" from the Contact record (not the Display Name); 
      * for Individuals: displays the name from the Contact record in the "FirstName LastName" format (not the Display Name)) 
    * Previous Customer (displays "Yes" / "No", based on the corresponding checkbox)
    * Customer Address (displays the "Customer Address", in the standard multi-line format without the addressee name) 



  


  * Customer Phone (displays the "Customer Phone") 
  * Customer Email (displays the "Customer Email") 
  * Preferred Contact Method (displays the "Preferred Contact Method") 



  


  * Job Details Section: 
    * Job Type (displays the "Job Type") 
    * Job Name (displays the "Job Name") 
    * Job Contact Name (displays the "Job Contact") 
    * Job Contact Phone (displays the "Job Contact Phone") 
    * Job Contact Email (displays the "Job Contact Email") 
    * Job Address (displays the "Job Address", in the standard multi-line format without the addressee name) 



  


  * Paved Before (displays "Yes" / "No", based on the corresponding checkbox selection) 
  * Pavement Age (displays the "Pavement Age") 
  * Pavement Condition (displays the "Pavement Condition") 
  * Stone Base Good (displays "Yes" / "No", based on the corresponding checkbox selection) 
  * Have Drawings (displays "Yes" / "No", based on the corresponding checkbox selection) 
  * Grading Required (displays "Yes" / "No", based on the corresponding checkbox selection) 



  


  * Additional Lead Details Section: 
    * Lead Source (displays the "Lead Source") 
    * Referring Party (displays the "Referring Party") 
    * Referring Party Address (displays the "Referring Party Address", in the standard multi-line format without the addressee name) 
    * Lead Source Note (displays the "Lead Source Note", with text wrapping) 



  


  * Ideal Project Timeframe (displays the "Ideal Project Timeframe") 
  * Decision Process (displays the "Decision Process" selection(s); comma-separated if there are multiple) 
  * Decision Process Note (displays the "Decision Process Note", with text wrapping) 



  


  * Additional Lead Notes (displays the "Additional Lead Notes", with formatting and text wrapping; note that since this printout never is more than one page long, these notes will be cut off at the bottom of the page) 



  


Handling Page Breaks: N/A (always single page) 

  


Other Notes:

  * This was referred to as the "Call Sheet" or "Call Information Sheet" in the Power App. 
  * Includes the default "Powered by Silverloom Business Suite" footnote at the bottom of the page. 
  * Note that printout templates may be subject to limitations of the PDF templating library. CCI will communicate with the client in places where the template library requires significant changes from the original design.



  


Development Specification

Mockup:

  * Docs: [https://docs.google.com/document/d/1GYYknYXIWAwY_yXhJ-f_jqMEN0X1_PoLoOnih916csg/edit?tab=t.0](https://docs.google.com/document/d/1GYYknYXIWAwY_yXhJ-f_jqMEN0X1_PoLoOnih916csg/edit?tab=t.0)
  * Sheets (old) [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1578163735#gid=1578163735](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1578163735#gid=1578163735)



  


Sample Call Sheet from the Power App solution: [https://drive.google.com/file/d/12hoaaeQR1aiRHqwbgVVbG2Z29i6e7jsY/view?usp=sharing](https://drive.google.com/file/d/12hoaaeQR1aiRHqwbgVVbG2Z29i6e7jsY/view?usp=sharing) .

  


  


Ellis Miller 06/17/2025: 

[ ] Note that we want to use the same macro expression for the core of this as for the lead information child screen. Create a ProposalFormattedLeadInfo macro that returns all of this in a large RTF memo.

[ ] Use FormattedCell to do your layout 

[ ] Use "None" for borders

[ ] Add macros that set font, width, and borders to make this easier:

[ ] ProposalLeadInfoSectionHdg( vText) - wide row for section headings

[ ] ProposalLeadInfoLabelCell( vText) - bold text for a label cell

[ ] ProposalLeadInfoValueCell( vText) - regular text for the field value cell

[ ] The Additional Lead Notes can just be appended below the table, doesn't have to be in a cell.

  


BID: 4 HOURS
