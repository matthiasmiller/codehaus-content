9.5. Insurance Card (Front & Back) Printout

  


Requirements

*Done. 

  


Purpose/Overview: The custom Insurance Card printout is an essential part of the Plan, as it provides clients with proof of coverage for their vehicles. This is a custom printout that is very complex because of the amount of information included and the layout restrictions (1/3 of a standard sheet of paper, printed front and back).

  


Printed From (opens the PDF in the browser, with the option to download or to print): 

  * Vehicle Record: "Print Insurance Card (Front Only)" link (for an individual Client; generates only the front, for users who wish to avoid duplex printing) 
  * Vehicle Record: "Print Insurance Card (Front & Back)" link (for an individual Client; generates both the front and back on separate pages, for duplex printing) 
  * Admin | Renewals and Printing | Print Annual Invoices & Insurance Cards - "Link to Print Cards" column (generates only the front, for all Clients of an Agent, for a given Period Year)



  


File Format/Name: 

  * PDF: 
    * For an individual client + vehicle, front only: "Insurance Card for <ClientLastName, ClientFirstName> (Front Only)"
    * For an individual client + vehicle, front and back: "Insurance Card for <ClientLastName, ClientFirstName> (Front & Back)"
    * For all clients of an agent: "Insurance Cards for Agent <AgentLastName, AgentFirstName> (Front Only)" 



  


Fields to be Filled: 

  * Front of card: 
    * Card title: 
      * "<PLAN STATE NAME>" FINANCIAL RESPONSIBILITY IDENTIFICATION CARD (all uppercase; displays the contents of the "Plan State Name" System Switch) 



  


  * Coverage dates:
    * Effective from "<Liability Coverage Start Date for the applicable period, in the mm/dd/yyyy format>" 
    * to "<Liability Coverage End Date for the applicable period, in the mm/dd/yyyy format>"



  


  * Policy #:
    * Policy # "<Policy #> (bold; displays the Plan-specific or Client-specific Policy #, based on the "Contact Policy Number" System Switch)



  


  * Vehicle information:
    * Year: "<Vehicle Year>"
    * Make: "<Vehicle Make>"
    * Model: "<Vehicle Model>"
    * Vehicle ID (VIN / Serial #): "<Vehicle VIN or Serial #>"



  


  * Insured information:
    * "<ClientLastName, ClientFirstName, in all uppercase letters>"
    * "<Client address, in standard format, up to 3 lines, in all uppercase letters>" 



  


  * Agent information:
    * "<AgentLastName, AgentFirstName, in all uppercase letters>" 
    * "<Agent address, in standard format, up to 3 lines, in all uppercase letters>" 
    * "<Agent phone, displaying the top phone number from the Agent's Contact record>"



  


  * Important Notice message contents: 



The Aid Plan is required by <contents of the "Plan State Name" System Switch> law to send you an I.D. card. The card shows that an insurance agreement has been issued for the vehicle(s) described satisfying the financial responsibility requirements of the law.

  


If you lose the card, contact your local representative of the Aid Plan to request a replacement.

  


The I.D. card information may be used for vehicle registration and replacing license plates. If your liability agreement is not in effect, the I.D. card is no longer valid.

  


You are required to maintain financial responsibility on your vehicle. It is against <contents of the "Plan State Name" System Switch> law to use the I.D. card fraudulently such as using the card as proof of financial responsibility after the insurance agreement is terminated.

  


  * Full Plan Name below vehicle details: 
    * <Full Plan Name>" (bold; displays the Full Plan Name, based on the "Insurance Card: Displayed full Plan name" System Switch)



  


  * Optional text to the right of Full Plan Name: 
    * "<Optional text>" (displays Plan-specific text as desired (or is left blank), based on the "Insurance Card: Optional text to the right of full Plan name" System Switch)



  


  * Optional text below Full Plan Name: 
    * "<Optional text>" (displays the Plan-specific text from the "Insurance Card: Optional text below Plan name" System Switch) 



  


  * Coverage amounts: 
    * Coverage: "<Coverage amounts>" (displays the Plan-specific amounts, based on the following Silverloom Settings: "Bodily Injury Liability $ (Per Person)", "Bodily Injury Liability $ (Per Accident)", & "Property Damage Liability $ (Per Accident)")



  


  * Authorized Signature:
    * <Authorized Signature image> (displays the "Authorized Signature" from Silverloom Settings; dimensions: 86 x 14 points (note that this is different from the standard 120 x 20 (6:1 ratio) used on other printouts)) 



  


  * Back of card: Most of the text on the back of the card is hard-coded, with the exception of the following:  
    * Vehicle Code law reference (see "< >" portion):



NOTE: THIS CARD IS REQUIRED WHEN:

  * You are involved in an auto accident.
  * You are convicted of a traffic offense other than parking offense that



requires a court appearance.

  * Upon the request of a police officer when you are stopped for violating any provision of <contents of the "Insurance Card: Vehicle Code law reference" System Switch> 



  


  * Plan details (displays the "Plan Identifying Details", with the following):
    * Plan Name (bold; from the "Plan name" System Switch)
    * Plan Name Subtitle (italics; from the "Plan name subtitle" System Switch)
    * Plan Address (bold; from Silverloom Settings)
    * Plan Phone (bold; from Silverloom Settings)



  


  


Handling Page Breaks: 

  * If there are more than 3 cards in a file, as with the case of printing cards for all clients of an agent, from the "Renewals and Printing" report, page breaks happen between cards, with up to 3 cards on each page.



  


Other Notes:

  * This printout does not include the standard "Powered by Silverloom Business Suite" footer.



  


Development Specification

Sample(s): 

  * Tim Reitz 08/23/2024: 
    * Template as of today: [[File:Std Print Insurance Card (Front & Back).r21.rtf]] 
    * Sample file as of today: [[File:Insurance Card for Smith, Arthur (Front & Back).PDF]]



  


Change Requests: 

  * Tim Reitz 08/20/2025: [[[IN11314](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11316&)]] - ZWA Multi-State Feature - Umbrella Incident


