9.8. Liability Declaration Page Printout

  


Requirements

Purpose/Overview: The Liability Declaration Page printout serves as an official statement of the Liability coverage for a certain Vehicle in a specified policy period.

  


Printed From: 

  * Vehicle Record: "Print Liability Declaration Page" link



  


File Format/Name: 

  * PDF: "Liability Declaration Page for <Year> <Make> <Model> <VIN / Serial #>



  


Fields to be Filled: 

  * Plan details (displays the "Plan Identifying Details", with the following):
    * Plan Name (bold; from the "Plan name" System Switch)
    * Plan Name Subtitle (italics; from the "Plan name subtitle" System Switch)
    * Plan Address (bold; from Silverloom Settings)
    * Plan Phone (bold; from Silverloom Settings)



  


  * Policy Number:
    * POLICY NO: "<Plan-specific or Client-specific Policy #, based on the "Policy Number" System Switch>"



  


  * Optional text below the Policy Number: 
    * "<Plan-specific text as desired (or is left blank), based on the "Insurance Card: Optional text to the right of full Plan name" System Switch, in bold font>"



TODO_VA: Tim Reitz 08/20/2025: Is this right? 

  


  * Insured (client) information:
    * "<ClientLastName, ClientFirstName, in all uppercase letters>" 
    * "<Client address, in standard format, up to 3 lines, in all uppercase letters>" 
    * "<Client phone, displaying the top phone number from the Client's Contact record>"



  


  * Policy Period information:
    * from "<Liability Coverage Start Date for the applicable period, in the mm/dd/yy format>" 
    * thru "<Liability Coverage End Date for the applicable period, in the mm/dd/yy format>"



  


  * Vehicle information:
    * Year: "<Vehicle Year>"
    * Make: "<Vehicle Make>"
    * Model: "<Vehicle Model>"
    * Vehicle ID (VIN / Serial #): "<Vehicle VIN or Serial #>"



  


  * Optional text below the Vehicle Information: 
    * "<contents of the "Insurance Card: Optional text below Plan name" System Switch>" 



  


  * Liability Benefits: 
    * "(Limited Tort)" (visible or hidden based on the "Liability Declaration: Includes "(Limited tort)" text" System Switch)
    * Bodily Injury Liability (displays the following values)
      * $<value set in the "Bodily Injury Liability $(Per Person)" field in Silverloom Settings> Per Person 
      * $<value set in the "Bodily Injury Liability $ (Per Accident)" field in Silverloom Settings> Per Accident 
    * Property Damage Liability $<value set in the "Property Damage Liability $ (Per Accident)" field in Silverloom Settings> Per Accident 



  


  * First Party Benefits: (visible or hidden based on the "Liability Declaration: Includes "First Party Benefits" section" System Switch)
    * "(Limited Tort)" (visible or hidden based on the "Liability Declaration: Includes "First Party Benefits" section" System Switch and the "Liability Declaration: Includes "(Limited tort)" text" System Switch)
    * Medical Expense Benefit $<amount from the "Medical Exp. Benefit $ (Per Person)" field in Silverloom Settings> Per Person (visible or hidden based on the "Liability Declaration: Includes "First Party Benefits" section" System Switch)
    * Uninsured Motorist Property Damage $<amount from the "Unins. Motorist Prop. Dmg. $ (Per Accident)" field in Silverloom Settings> Per Accident (visible or hidden based on the "Liability Declaration: Includes "First Party Benefits" section" System Switch)



  


  * Authorized Signature:
    * <"Authorized Signature" from Silverloom Settings; dimensions: 120 x 20 points (6:1 ratio) >



  


  * Agent information:
    * "<AgentLastName, AgentFirstName, in all uppercase letters>" 
    * "<Agent address, in standard format, up to 3 lines, in all uppercase letters>" 
    * "<Agent phone, displaying the top phone number from the Agent's Contact record>"



  


Handling Page Breaks: N/A (this printout always fits on a single page)

  


Other Notes:

  * Includes the standard "Powered by Silverloom Business Suite" footer.



  


Development Specification

Sample(s): 

  * Tim Reitz 08/26/2024: : 
    * Template as of today: [[File:Std Print Liability Declaration Page.r21.rtf]]
    * Sample file from test system as of today: [[File:Liability Declaration Page for 2016 Chevrolet BLAZER 1GTV2MEC7GZ298272.PDF]]



  


Change Requests: 

  * Tim Reitz 08/20/2025: [[[IN11314](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11316&)]] - ZWA Multi-State Feature - Umbrella Incident


