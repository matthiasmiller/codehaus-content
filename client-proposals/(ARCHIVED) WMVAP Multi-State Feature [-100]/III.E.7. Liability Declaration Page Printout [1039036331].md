3.5.7. Liability Declaration Page Printout

  


Requirements

*Documented. Tim Reitz 08/20/2025

  


Make the following changes (full spec included here, with changes noted with blue and strike-through): 

  


Purpose/Overview: The Liability Declaration Page printout serves as an official statement of the Liability coverage for a certain Vehicle in a specified policy period.

  


Printed From: 

  * Vehicle Record: "Print Liability Declaration Page" link



  


File Format/Name: 

  * PDF: "Liability Declaration Page for <Year> <Make> <Model> <VIN / Serial #>



  


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



  


  * Policy Number:
    * POLICY NO: "<Policy #> SI 15 (displays the Plan-specific or Client-specific Policy #, based on the "Policy Number" System Switch)



  


  * Optional text below the Policy Number: 
    * "<Optional text>" NAIC No: S0015 (bold; displays Plan-specific text as desired (or is left blank), based on the "Insurance Card: Optional text to the right of full Plan name" System Switch)



  


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
    * "<Optional text>" "The named self-insurer has been granted approval as a self-insurer under 67 PA.C.S issued by the PA Department of Transportation on July 23rd of 1975 to Glenn Zimmerman, Administrator." (displays the contents of the "Insurance Card: Optional text below Plan name" System Switch)



  


  * Liability Benefits: 
    * "(Limited Tort)" (visible or hidden based on the "Liability Declaration: Includes "(Limited tort)" text" System Switch)
    * Bodily Injury Liability (displays the following values)
      * $<Amount> 15,000 Per Person (displays the value set in the "Bodily Injury Liability $(Per Person)" field in Silverloom Settings)
      * $<Amount> 30,000 Per Accident (displays the value set in the "Bodily Injury Liability $ (Per Accident)" field in Silverloom Settings)
    * Property Damage Liability $<Amount> 5,000 Per Accident (displays the value set in the "Property Damage Liability $ (Per Accident)" field in Silverloom Settings)



  


  * First Party Benefits: (visible or hidden based on the "Liability Declaration: Includes "First Party Benefits" section" System Switch)
    * "(Limited Tort)" (visible or hidden based on the "Liability Declaration: Includes "First Party Benefits" section" System Switch and the "Liability Declaration: Includes "(Limited tort)" text" System Switch)
    * Medical Expense Benefit $<Amount> 5,000 Per Person (visible or hidden based on the "Liability Declaration: Includes "First Party Benefits" section" System Switch; displays the amount from the "Medical Exp. Benefit $ (Per Person)" field in Silverloom Settings)
    * Uninsured Motorist Property Damage $<Amount> 5,000 Per Accident (visible or hidden based on the "Liability Declaration: Includes "First Party Benefits" section" System Switch; displays the amount from the "Unins. Motorist Prop. Dmg. $ (Per Accident)" field in Silverloom Settings)



  


  * Authorized Signature:
    * <Authorized Signature image> Hard-coded signature image (displays the "Authorized Signature" from Silverloom Settings; dimensions: 120 x 20 points (6:1 ratio)) 



  


  * Agent information:
    * "<AgentLastName, AgentFirstName, in all uppercase letters>" 
    * "<Agent address, in standard format, up to 3 lines, in all uppercase letters>" 
    * "<Agent phone, displaying the top phone number from the Agent's Contact record>"



  


Handling Page Breaks: N/A (this printout always fits on a single page)

  


Other Notes:

  * Includes the standard "Powered by Silverloom Business Suite" footer. 
  * N/A



  


Development Specification

Tim Reitz 08/26/2024: Link to template work in Docs: [https://docs.google.com/document/d/1q88YAJBIDglWDOyndMG7i2ZhV2SL11Wl/edit](https://docs.google.com/document/d/1q88YAJBIDglWDOyndMG7i2ZhV2SL11Wl/edit). 

  


Tim Reitz 08/26/2024: Spec copied from ZWA proposal today (8/26/24).

  


Ellis Miller 09/05/2024:

  


[ ] Rename actual template to " \- Signed.r21" so that we remember we need to clone. Will need to clone.

  


[ ] As spec'ed.

[ ] Also footer.

  


1.5 Day

  


Murshid Rahman 05/27/2025: CLS job ID [[PC0178340]].
