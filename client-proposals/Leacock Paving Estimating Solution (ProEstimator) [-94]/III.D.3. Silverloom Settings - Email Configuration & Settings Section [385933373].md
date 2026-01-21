3.4.3. Silverloom Settings - Email Configuration & Settings Section

  


Requirements

  * Email Configuration & Settings section (custom):  
    * Proposal to Customer Email (button; opens a child screen with the following: 
      * Default Text for Proposal to Customer Email (multi-line plain text field that supports expressions; with the following details / behaviors: 
        * technical notes: 
          * expressions are evaluated on Proposal records; 
          * plain text is used here to facilitate sending the email via the mailto feature; 
        * this is used for setting & storing the default text for the email that is sent with the Proposal Printout PDF - see corresponding spec; 
        * warning required on Save if blank; 
        * to be initially set to the following at deployment of the Solution, but may be edited by Leacock Paving or CodeCrafters: 



Hello, <Job Contact Name>,

  


Attached please find the complete proposal for the "<"Job Name">" project.

  


Please review this and let us know if you would like to proceed.

  


Thank you,

<"Short Display Name" for the Sales Rep> 

  


  


  * Job Awarded Email (button; opens a child screen with the following: 
    * Default Recipient for Job Awarded Email (email field; with the following details / behaviors:
      * warning on Save if blank;
      * to be initially set to the following at deployment of the Solution, but may be edited by Leacock Paving or CodeCrafters: [info@leacockpaving.com](mailto:info@leacockpaving.com))
    * Default Text for Job Awarded Email (multi-line plain text field that supports expressions; with the following details / behaviors: 
      * technical note: expressions are evaluated on Proposal records; 
      * this is used for setting & storing the default text for the internal email that is sent when a Proposal is marked as awarded - see corresponding spec; 
      * warning on Save if blank;
      * to be initially set to the following at deployment of the Solution, but may be edited by Leacock Paving or CodeCrafters: 



This proposal has been awarded. Please open the following link and enter the proposal details into QuickBooks: <link to the corresponding Proposal record>

  


Thank you!

  


  


  * Work Order Email (button; opens a child screen with the following: 
    * Default Text for Work Order Email (multi-line plain text field that supports expressions; with the following details / behaviors: 
      * technical note: expressions are evaluated on Proposal records; 
      * this is used for setting & storing the default text for the internal email that is sent - see corresponding spec; 
      * warning on Save if blank;
      * to be initially set to the following at deployment of the Solution, but may be edited by Leacock Paving or CodeCrafters: 



This proposal has been awarded.

  


View Proposal: <link to the corresponding Proposal record>

  


View Work Order PDF (complete): <link to the "Work Order Printout" PDF in the Solution for the corresponding Proposal record>

  


Thank you!

  


  


  * Jobs Awaiting Scheduling Email (button; opens a child screen with the following: 
    * Default Text for Jobs Awaiting Scheduling Email (multi-line plain text field that supports expressions; with the following details / behaviors:
      * this is used for setting & storing the default text for the internal email that is sent - see corresponding spec; 
      * warning on Save if blank;
      * to be initially set to the following at deployment of the Solution, but may be edited by Leacock Paving or CodeCrafters: 



One or more jobs have been awarded and are ready for scheduling.

  


View Report: <link to the "Jobs Awaiting Scheduling" report>

  


Thank you!

  


Development Specification

Change Requests:

  * Tim Reitz 11/25/2025: [[[IN11677](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11679&)]] - ZLP - Job Scheduled Tracking
  * 


  


  


Email Settings section (custom)

[ ] 3 simple child screens with expression fields. We are not adding warning Report Alerts for failures at this point:

  * The email to clients is previewed in the user's email client
  * The other two emails are internal only and so broken expressions aren't a big deal



[ ] All expression fields are evaluated at the Proposal level.

3 Hours
