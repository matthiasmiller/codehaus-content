5.3.1. Proposal - Shared OnChange Actions

  


Requirements

The following Shared OnChange Action(s) are included for the Proposal record: 

  


  * "Clear Fields for All Copies": 
    * Initiated: 
      * When a user clicks any of the "Copy Action" buttons:
        * "Revised Proposal"; 
        * "Change Order";  
        * "Duplicate Proposal"; 
    * Actions: Clears fields in the following sections for all copy types, according to the "Copy Action Details" spec: 
      * "Proposal Finalization" section, 
      * "Print / Emailing" section, 
      * "Customer Acceptance" section, and 
      * "Job Scheduling" section 



  


  * "Set Fields for Revised and Duplicate Copies":
    * Initiated:
      * When a user clicks one of the following "Copy Action" buttons: 
        * "Revised Proposal";  
        * "Duplicate Proposal";  
    * Actions:  
      * Sets fields in the "Proposal Itemization" section, according to the "Copy Action Details" spec.



  


  * "Clear Lead Information Fields for Change Order and Duplicate Copies":
    * Initiated:
      * When a user clicks one of the following "Copy Action" buttons: 
        * "Change Order"; 
        * "Duplicate Proposal"; 
    * Actions:  
      * Clears fields in the "Lead Information" section, according to the "Copy Action Details" spec.



  


Development Specification

Change Requests:

  * Tim Reitz 01/08/2026: [[[IN12362](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12364&)]] - ZLP - Proposal Record: Use Shared OnChanges


