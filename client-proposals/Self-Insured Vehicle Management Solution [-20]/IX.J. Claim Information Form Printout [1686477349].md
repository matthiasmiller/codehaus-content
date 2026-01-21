9.10. Claim Information Form Printout

  


Requirements

*Done. 

  


Purpose/Overview: The Claim Information Form custom printout is used as an informational document by the Agent and the Client when a claim is generated.

  


Printed From: Claim Record: "Claim Information Form" link

  


File Format/Name: 

  * PDF: "Claim Information Form -<Claim ID> (exported on <current date in the yyyy-mm-dd format>)"



  


Fields to be Filled: 

  


  * Heading: 
    * "<contents of the "Plan name" System Switch, in bold font>" 



  


  * Claim Info fields:
    * Client ID: "<Claim Client's Contact ID #>"
    * Claim ID: "Claim ID>"
    * Entered: "<Date that the Claim record was created, in the mm/dd/yyyy format>"



  


  * Client Information fields:
    * INSURED section:
      * "<Claim Client LastName, FirstName>" 
      * "<Claim Client address, in standard format, up to 3 lines>" 
    * Phone 1: "<Claim Client phone; the top non-fax phone number from the Client's Contact record>"
    * Phone 2: "<Claim Client phone; the 2nd non-fax phone number from the Client's Contact record, if applicable>"
    * Fax: "<Claim Client fax; the "Fax"-type phone number from the Client's Contact record, if applicable>"
    * Email: "<Claim Client email; the top/Primary email address from the Client's Contact record, if applicable>"
    * Client Notes: "<Claim Client Notes memo contents, from the Client's Contact record, with formatting>" 



  


  * Agent Information fields:
    * AGENT box:
      * "<Originating Agent LastName, FirstName>" 
      * "<Originating Agent's current address, in standard format, up to 3 lines>" 



  


  * Additional Client Information fields: 
    * Client Status: "<Current Status of the Claim Client's Contact record>" 
    * Client Is: "<Claim Client's current Contact Type"
    * High Risk Driver: "<Yes/No, based on whether the Claim Client is a High Risk Driver>" 
    * Entry Date: "<Date that the Claim Client's Contact record was created, in the mm/dd/yyyy format>" 



  


  * Driver and Vehicle Details fields: 
    * Our Driver: "<Claim Driver>" 
    * Year: "<Vehicle Year>"
    * Make: "<Vehicle Make>" 
    * Model: "<Vehicle Model>" 
    * Liability: "Active <first part of Vehicle Type>" (if Liability coverage currently is active) or "Inactive" (if Liability coverage currently is inactive) 
    * <Alternate text for Collision - Short label>: "Active <first part of Vehicle Type>" (if Collision coverage currently is active) or "Inactive" (if Collision coverage currently is inactive) 
    * Cargo: "Active <first part of Vehicle Type>" (if Cargo coverage currently is active) or "Inactive" (if Cargo coverage currently is inactive) 



  


  * Accident Details fields:
    * Date of Accident: "<Date of Accident from the Claim record, in the mm/dd/yyyy format>"
    * Time of Accident: "<Time of Accident from the Claim record>"
    * INJURY NOTES: "<Injury Information memo contents, from the Claim record, with formatting>"
    * LOCATION OF ACCIDENT: "<Location of Accident memo contents, from the Claim record, with formatting>"
    * DETAILS OF ACCIDENT: "<Details of Accident memo contents, from the Claim record, with formatting>"
    * FOLLOW-UP / MISCELLANEOUS NOTES: "<Follow-up / Misc Notes memo contents, from the Claim record, with formatting>"



  


  * Settlement Details fields:
    * SETTLEMENT DETAILS: "<Settlement Details memo contents, from the Claim record, with formatting; truncated to approx. 60-65 characters>"
    * Liability 1: "<Liability 1 amount from the Claim record>"
      * Include in Release: "<Yes / No, based on the corresponding checkbox selection on the Claim record>" 
    * Liability 2: "<Liability 2 amount from the Claim record>"
      * Include in Release: "<Yes / No, based on the corresponding checkbox selection on the Claim record>" 
    * Towing / Storage / Other: "<Towing / Storage / Other amount from the Claim record>"
      * Include in Release: "<Yes / No, based on the corresponding checkbox selection on the Claim record>" 
    * Pain & Suffering: "<Pain & Suffering amount from the Claim record>"
      * Include in Release: "<Yes / No, based on the corresponding checkbox selection on the Claim record>" 
    * Medical: "<Medical amount from the Claim record>"
    * <Alternate text for Collision - Short label>: "<Collision amount from the Claim record>"
    * Total Release: "<Total Release amount from the Claim record>"
    * Total Settlement Paid: "<Total Settlement amount from the Claim record>"



  


  * Other Party / Vehicle Details fields:
    * Other Driver: "<Other Driver from the Claim record>"
    * Description of Other Vehicle: "<Description of Other Vehicle memo contents, from the Claim record, with formatting; truncated to approx. 40-45 characters>"



  


  * Other Party box:
    * Name: "<Other Party Name from the Claim record>"
    * Address: "<Other Party Address from the Claim record, up to 3 lines>" 
    * Phone 1: "<Other Party Phone 1 from the Claim record>"
    * Phone 2: "<Other Party Phone 2 from the Claim record>"
    * Email: "<Other Party Email email from the Claim record>"
    * Notes: "<Other Party Notes memo contents, from the Claim record, with formatting>"



  


  * Their Insurance Info box:
    * Name: "<Other Party Insurance Name from Claim record>"
    * Address: "<Other Party Insurance Address from the Claim record, up to 3 lines>"
    * Contact: "<Other Party Insurance Contact from the Claim record>"
    * Phone 1: "<Other Party Insurance Phone 1 from the Claim record><, Ext. <Extension> visible if an Extension is specified on the Claim>"
    * Phone 2: "<Other Party Insurance Phone 2 from the Claim record><, Ext. <Extension> visible if an Extension is specified on the Claim>"
    * Fax: "<Other Party Insurance Fax from the Claim record>"
    * Email: "<Other Party Insurance Email from the Claim record>"
    * Notes: "<Other Part Insurance Notes memo contents, from the Claim record, with formatting>"
    * Policy: "<Other Party's Policy # from the Claim record>"
    * Claim: "<Other Party's Incident / Claim # from the Claim record>"



  


Handling Page Breaks: N/A (this printout always fits on a single page)

  


Other Notes:

  * Includes the standard "Powered by Silverloom Business Suite" footer.



  


Development Specification

Sample(s): 

  * Tim Reitz 08/28/2024: 
    * Template as of today: [[File:Std Print Claim Information Form.r21 (1).rtf]] 
    * Sample file from test system as of today: [[File:3663-50-20210615-REITI (exported on 2024-08-28) (2).pdf]]



  


  


Change Requests:

  * Tim Reitz 03/14/2025: [[[IN10412](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10414&)]] - ZWA - Claim Information Form Printout - Changes for "Collision" Terminology
  * Tim Reitz 08/20/2025: [[[IN11314](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11316&)]] - ZWA Multi-State Feature - Umbrella Incident


