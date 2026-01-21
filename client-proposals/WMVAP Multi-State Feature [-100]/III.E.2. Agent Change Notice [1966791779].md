3.5.2. Agent Change Notice

  


Requirements

*Documented. Tim Reitz 08/19/2025

  


Purpose/Overview: To be sent to clients whose agent is being changed from one to another.

  


Printed From:

  * "Print Agent Change Notice" link on the Contact record (visible after "Client's Agent" has been changed - see corresponding spec)
  * "Print Agent Change Notices" button on the "Change Agents" report (visible if Change Agent button is used - see corresponding spec)



  


File Format/Name: PDF:

  * When printed for an individual Contact: "Agent Change Notice for <Client "Display Name" LastName FirstName> (exported on <current date in the YYYY-MM-DD format>)" (example: "Agent Change Notice for Doe John (exported on 2025-05-14)") 
    * Note that due to a platform limitation, this file name does not include a comma between the Last and First names for individuals. However, this hopefully will be fixed at some point. 
  * When printed from the "Change Agents" report: "Agent Change Notices for Clients of <Prior Agent "Display Name"> \- <Prior Agent "Agent Code">" (example: "Agent Change Notices for Clients of Cummins, Bartholomew - CUMBA") 



  


Fields to be Filled:

  * Plan details:



Weaverland Mennonite Vehicle Aid Plan

of the Weaverland Mennonite Conference Body

395 Cherry Hill Road. Richland, PA 17087

Phone: 717-933-4817

  *  Displays the "Plan Identifying Details", with the following:
    * <Plan Name> (bold; from the "Plan name" System Switch) 
    * <Plan Name Subtitle> (italics; from the "Plan name subtitle" System Switch; displayed if non-blank) 
    * <Plan Address> (bold; from Silverloom Settings) 
    * <Plan Phone> (bold; from Silverloom Settings) 



  


  * Prior Agent section:
    * "<Prior Agent "Display Name", in all upper case letters>" 
    * "<Prior Agent address, in standard format, up to 3 lines, in all upper case letters>"



 

  * Date (displays the "Agent Change Date")



  


  * Client section:
    * "<Client "Display Name", in all upper case letters>"
    * "<Client's Mailing (or Primary if no Mailing) address, in standard format, up to 3 lines, in all upper case letters>" 



  


  * Printout Body section:



"<contents of the "Agent Change Notice Printout Body" memo in Silverloom Settings>"

  


  * New Agent:
    * "<Current Agent "Display Name", in all upper case letters>" 
    * "<Current Agent address, in standard format, up to 3 lines, in all upper case letters>"



 

  * Authorized Signature:
    * <Authorized Signature image> Hard-coded signature image (displays the "Authorized Signature" from Silverloom Settings; dimensions: 120 x 20 points (6:1 ratio)) 



  


Template: "Std Print Agent Change Notice"

  


Handling Page Breaks: 

  * One page per client affected by the agent change.



  


Other Notes:

  * Includes the standard "Powered by Silverloom Business Suite" footer.
  * N/A



  


Development Specification

Sagar Sagar 05/20/2025: CLS job ID - [[PC0179031]]

  


Tim Reitz 05/20/2025: See note under file name / format: "When printed for an individual Contact...": This note is referring to [[PC0179190]] - Detail Screen - File Name does not Support Comma with OutputFile.
