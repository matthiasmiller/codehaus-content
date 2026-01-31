3.5.8. Loss Payable Clause Printout

  


Requirements

*Documented. Tim Reitz 08/20/2025

  


Make the following changes (full spec included here, with changes noted with blue and strike-through): 

  


Purpose/Overview: The Loss Payable Clause serves as the official statement to indicate if someone other than the insured driver is the beneficiary.

  


Printed From: 

  * Vehicle Record: "Print Loss Payable Clause" link (visible if a Loss Payee is selected for the Vehicle)



  


File Format/Name: 

  * PDF: "Loss Payable Clause for Vehicle <Vehicle record ID>"



  


Fields to be Filled: 

  


  * Plan details:



Weaverland Mennonite Vehicle Aid Plan

of the Weaverland Mennonite Conference Body

395 Cherry Hill Road. Richland, PA 17087

Phone: 717-933-4817

  *  Displays the "Plan Identifying Details", with the following:
    * Plan Name (bold; from the "Plan name" System Switch)
    * Plan Name Subtitle (italics; from the "Plan name subtitle" System Switch)
    * Plan Address (bold; from Silverloom Settings)
    * Plan Phone (bold; from Silverloom Settings)



  


  * NAIC No: S0015 (being replaced with conditional text, and moved to below the Policy Number)



  


  * Policy Number:
    * POLICY NO: "<Policy #> SI 15 (displays the Plan-specific or Client-specific Policy #, based on the "Policy Number" System Switch)



  


  * Optional text below the Policy Number: 
    * "<Optional text>" (bold; displays Plan-specific text as desired (or is left blank), based on the "Loss Payable: Optional text above Vehicle details" System Switch) 



  


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
    * <Collision - Legal label> Coverage: "<displays the Vehicle Collision Coverage>" less "<displays the Coverage Deductible Amount from Silverloom Settings>"
    * Comprehensive Coverage: "<displays the Vehicle Collision Coverage>" less "<displays the Coverage Deductible Amount from Silverloom Settings>"



  


  * Agent information:
    * "<AgentLastName, AgentFirstName, in all uppercase letters>" 
    * "<Agent address, in standard format, up to 3 lines, in all uppercase letters>" 
    * "<Agent phone, displaying the top phone number from the Agent's Contact record>"



  


  * Authorized Signature:
    * <Authorized Signature image> Hard-coded signature image (displays the "Authorized Signature" from Silverloom Settings; dimensions: 120 x 20 points (6:1 ratio)) 



  


  * Plan Representative Signature Line: 
    * <Plan name> Weaverland Mennonite Vehicle Aid Plan Representative (displays the contents of the "Plan name" System Switch)



  


Handling Page Breaks: N/A (this printout always fits on a single page)

  


Other Notes:

  * Includes the standard "Powered by Silverloom Business Suite" footer. 
  * N/A



  


Development Specification

Tim Reitz 08/27/2024: Link to template work in Docs: [https://docs.google.com/document/d/1kNabtpm5HZEP8w9NrdN2OzjASsD6iZ-P/edit](https://docs.google.com/document/d/1kNabtpm5HZEP8w9NrdN2OzjASsD6iZ-P/edit).

  


[ ] Rename actual template to " \- Signed.r21" so that we remember we need to clone. Will need to clone.

  


[ ] As spec'ed.

[ ] Also footer.

  


1 Day
