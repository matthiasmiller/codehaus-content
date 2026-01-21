3.5.4. Insurance Card (Front & Back) Printout

  


Requirements

*Documented. Tim Reitz 08/20/2025

  


Make the following changes (full spec included here, with changes noted with blue and strike-through): 

  


Purpose/Overview: The Insurance Card printout is an essential part of the Plan, as it provides clients with proof of coverage for their vehicles. This is a custom printout that is very complex because of the amount of information included and the layout restrictions (1/3 of a standard sheet of paper, printed front and back).

  


Printed From (opens the PDF in the browser, with the option to download or to print): 

  * Home | Resource | Insurance Card (Back) menu option (prints only the back for one card, for users who with to avoid duplex printing) 
    * This is being moved to the new "Insurance Card (Back Only) Printout" spec.
  * Vehicle Record: "Print Insurance Card (Front Only)" link (for an individual client; prints only the front, for users who wish to avoid duplex printing) 
  * Vehicle Record: "Print Insurance Card (Front & Back)" link (for an individual client; prints both the front and back on separate pages, for duplex printing) 
  * Admin | Renewals and Printing | Print Annual Invoices & Insurance Cards - "Link to Print Cards" column (generates the "Front Only" version, for all clients of an agent, for a given period year)



  


  


File Format/Name: 

  * PDF: 
    * For an individual client + vehicle, front only: "Insurance Card for <ClientLastName, ClientFirstName> (Front Only)"
    * For an individual client + vehicle, front and back: "Insurance Card for <ClientLastName, ClientFirstName> (Front & Back)"
    * For all clients of an agent: "Insurance Cards for Agent <AgentLastName, AgentFirstName> (Front Only)" 



  


  


Fields to be Filled: 

  * Front of card: 
    * Card title: 
      * "<PLAN STATE NAME>" PENNSYLVANIA FINANCIAL RESPONSIBILITY IDENTIFICATION CARD (all uppercase; displays the contents of the "Plan State Name" System Switch) 



  


  * Coverage dates:
    * Effective from "<Liability Coverage Start Date for the applicable period, in the mm/dd/yyyy format>" 
    * to "<Liability Coverage End Date for the applicable period, in the mm/dd/yyyy format>"



  


  * Policy #:
    * Policy # "<Policy #> SI 15 (bold; displays the Plan-specific or Client-specific Policy #, based on the "Contact Policy Number" System Switch)
      * Note: Also shift this field to the left, to allow more space for up to 9 characters to be included.



  


  * Vehicle information:
    * Year: "<Vehicle Year>"
    * Make: "<Vehicle Make>"
    * Model: "<Vehicle Model>"
    * Vehicle ID (VIN / Serial #): "<Vehicle VIN or Serial #>"



  


  * Insured information:
    * "<ClientLastName, ClientFirstName, in all upper case letters>"
    * "<Client address, in standard format, up to 3 lines, in all upper case letters>" 



  


  * Agent information:
    * "<AgentLastName, AgentFirstName, in all upper case letters>" 
    * "<Agent address, in standard format, up to 3 lines, in all upper case letters>" 
    * "<Agent phone, displaying the top phone number from the Agent's Contact record>"



  


  * Important Notice message contents: 



The Aid Plan is required by <Plan State Name> Pennsylvania law to send you an I.D. card. The card shows that an insurance agreement has been issued for the vehicle(s) described satisfying the financial responsibility requirements of the law.

  


If you lose the card, contact your local representative of the Aid Plan to request a replacement.

  


The I.D. card information may be used for vehicle registration and replacing license plates. If your liability agreement is not in effect, the I.D. card is no longer valid.

  


You are required to maintain financial responsibility on your vehicle. It is against <Plan State Name> Pennsylvania law to use the I.D. card fraudulently such as using the card as proof of financial responsibility after the insurance agreement is terminated.

  * (both of these display the contents of the "Plan State Name" System Switch) 



  


  * Full Plan Name below vehicle details: 
    * <Full Plan Name>" SI #15 Weaverland Mennonite Vehicle Aid Plan (bold; displays the Full Plan Name, based on the "Insurance Card: Displayed full Plan name" System Switch)



  


  * Optional text to the right of Full Plan Name: 
    * "<Optional text>" NAIC No: S0015 (displays Plan-specific text as desired (or is left blank), based on the "Insurance Card: Optional text to the right of full Plan name" System Switch)



  


  * Optional text below Full Plan Name: 
    * "<Optional text>" The named self-insurer has been granted approval as a self-insurer under 67 PA.C.S. 223.5 (displays the Plan-specific text from the "Insurance Card: Optional text below Plan name" System Switch) 



  


  * Coverage amounts: 
    * Coverage: "<Coverage amounts>" Coverage: $15,000 - $30,000 - $5,000 (displays the Plan-specific amounts, based on the following Silverloom Settings: "Bodily Injury Liability $ (Per Person)", "Bodily Injury Liability $ (Per Accident)", & "Property Damage Liability $ (Per Accident)")



  


  * Authorized Signature:
    * <Authorized Signature image> Hard-coded signature image (displays the "Authorized Signature" from Silverloom Settings; dimensions: 86 x 14 points (note that this is different from the standard 120 x 20 (6:1 ratio) used on other printouts)) 



  


  * Back of card: Most of the text on the back of the card is hard-coded, with the exception of the following:  
    * N/A 
    * Vehicle Code law reference:



NOTE: THIS CARD IS REQUIRED WHEN:

  * You are involved in an auto accident.
  * You are convicted of a traffic offense other than parking offense that



requires a court appearance.

  * Upon the request of a police officer when you are stopped for violating any provision of <Vehicle Code law reference> the Vehicle Code (75 Pa. C.S.) 
    * (displays the contents of the "Insurance Card: Vehicle Code law reference" System Switch)



  


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



  


  


Handling Page Breaks: 

  * If there are more than 3 cards in a file, as with the case of printing cards for all clients of an agent, from the "Renewals and Printing" report, page breaks happen between cards, with up to 3 cards on each page.



  


Other Notes:

  * This printout does not include the standard "Powered by Silverloom Business Suite" footer. 
  * N/A



  


Development Specification

Tim Reitz 08/23/2024: Link to template work in Docs: [https://docs.google.com/document/d/1mw_jOtB479uMxrGEgnN0lWsx3_kH1qqK/](https://docs.google.com/document/d/1mw_jOtB479uMxrGEgnN0lWsx3_kH1qqK/). 

  


Tim Reitz 08/23/2024: Spec copied from ZWA proposal today (8/23/24).

  


Ellis Miller 09/05/2024:

  


2 Days

[ ] NOTE: Because of signatures, we will keep a master template in the "AppHosting Vehicle Insurance" standard folder and exact copies in each of the client folders ZWA / ZWI / etc, with just the signature overridden. Whenever we make a change, we have to copy the results to each client folder and apply the signature again. In the base folder, maybe insert a red cursive Signature Here image so that we don't forget to override it.

BEFORE DOING THIS, LET'S ASK JOHN ALLAN IF HE CAN HELP US FIND A SOLUTION.

[ ] Rename actual template to " \- Signed.r21" so that we remember we need to clone.

[ ] For any templates that have a logo, add "\- Logo.r21"

[ ] If both logo and signed, use "\- Logo - Signed.r21"

  


[ ] Consider an InsCardCoverageAmts macro that formats the "$15,000 - $30,000 - $5,000" as indicated above.

  


Tim Reitz 09/10/2024:  Exclude the "powered by Silverloom" footnote.

  


Sagar Sagar 05/19/2025: CLS job ID - [[PC0178338]]
