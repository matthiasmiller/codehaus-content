9.9. Loss Payable Clause Printout

  


Requirements

*Done. 

  


Purpose/Overview: The Loss Payable Clause custom printout serves as the official statement to indicate if someone other than the insured driver is the beneficiary.

  


Printed From: 

  * Vehicle Record: "Print Loss Payable Clause" link (visible if a Loss Payee is selected for the Vehicle)



  


File Format/Name: 

  * PDF: "Loss Payable Clause for Vehicle <Vehicle record ID>"



  


Fields to be Filled: 

  * Plan details (displays the "Plan Identifying Details", with the following):
    * Plan Name (bold; from the "Plan name" System Switch)
    * Plan Name Subtitle (italics; from the "Plan name subtitle" System Switch)
    * Plan Address (bold; from Silverloom Settings)
    * Plan Phone (bold; from Silverloom Settings)



  


  * Policy Number:
    * POLICY NO: "<Plan-specific or Client-specific Policy #, based on the "Policy Number" System Switch>"



  


  * Optional text below the Policy Number: 
    * "<Plan-specific text as desired (or is left blank), based on the "Loss Payable: Optional text above Vehicle details" System Switch, in bold font>"



  


  * Vehicle information:
    * Year: "<Vehicle Year>"
    * Make: "<Vehicle Make>"
    * Model: "<Vehicle Model>"
    * Vehicle ID (VIN / Serial #): "<Vehicle VIN or Serial #>"



  


  * Insured (client) information:
    * "<ClientLastName, ClientFirstName, in all uppercase letters>" 
    * "<Client address, in standard format, up to 3 lines, in all uppercase letters>" 
    * "<Client phone, displaying the top phone number from the Client's Contact record>"



  


  * Loss Payee information:
    * "<Payee Name, in all uppercase letters>"
    * "<Payee address, in standard format, up to 3 lines, all uppercase letters>"
    * "<Payee phone, displaying the top phone number from the Payee's Contact record, does not display a number if the top number is a Fax number>"



  


  * Coverage information:
    * <"Alternate text for Collision - Legal label"> Coverage: "<displays the Vehicle Collision Coverage>" less "<displays the Coverage Deductible Amount from Silverloom Settings>"
    * Comprehensive Coverage: "<displays the Vehicle Collision Coverage>" less "<displays the Coverage Deductible Amount from Silverloom Settings>"



  


  * Agent information:
    * "<AgentLastName, AgentFirstName, in all uppercase letters>" 
    * "<Agent address, in standard format, up to 3 lines, in all uppercase letters>" 
    * "<Agent phone, displaying the top phone number from the Agent's Contact record>"



  


  * Authorized Signature:
    * <"Authorized Signature" from Silverloom Settings; dimensions: 120 x 20 points (6:1 ratio) >



  


  * Plan Representative Signature Line: 
    * <contents of the "Plan name" System Switch> 



  


Handling Page Breaks: N/A (this printout always fits on a single page)

  


Other Notes:

  * Includes the standard "Powered by Silverloom Business Suite" footer.



  


Development Specification

Sample(s): 

  * Tim Reitz 08/27/2024: 
    * Template as of today: [[File:Std Print Loss Payable Clause.r21.rtf]] 
    * Sample file from test system as of today: [[File:Loss Payable Clause for Vehicle 3741.PDF]]



  


Change Requests:

  * Tim Reitz 03/14/2025: [[[IN10227](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10229&)]] - ZWA - Loss Payable Clause Printout - Changes for "Collision" Terminology
  * Tim Reitz 08/20/2025: [[[IN11314](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11316&)]] - ZWA Multi-State Feature - Umbrella Incident


