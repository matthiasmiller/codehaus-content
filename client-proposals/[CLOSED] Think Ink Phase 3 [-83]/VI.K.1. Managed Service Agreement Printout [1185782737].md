6.11.1. Managed Service Agreement Printout

  


Requirements

Purpose/Overview: This is a customized PDF printout of the Managed Service Agreement, including customer information, device information, and agreement details.

  


Printed From: 

  * Print Agreement (PDF) on the Manage Service Agreement record
  * Print Agreement (Word) on the Manage Service Agreement record



  


File Format/Name:

  * PDF: <Customer Name> \- <Agreement #>.<Revision #>
  * Word: <Customer Name> \- <Agreement #>.<Revision #>



TODO_IDD: Tim Reitz 08/08/2023: review how the revision # works on the agreement record. Update on the header as well.

  


Sections and Fields to be Filled: 

  * "Billing Details" section" (all pulled from the "Billing Details" section on the Agreement record):
    * Customer
    * Address
    * City
    * State
    * Zip
    * Phone
    * Fax
    * Email



  


  * "Equipment Location (if different)" section (all pulled from the "Equipment Location Details" section on the Agreement record):
    * Customer 
    * Address 
    * City 
    * State
    * Zip
    * Phone 
    * Fax 
    * Email



  


  * "Section A - Included Devices" section (pulled from the Included Managed Devices table on the Agreement record):
    * Table with the following (wrap the title row text to help the columns fit with a vertical layout):



TODO_IDD: try to get all of this to fit on a vertical page

  * Device ID
  * Model Description (wrap text to multiple lines if needed)
  * Serial #
  * Maint Only



TODO_IDD: update here after we settle on the Agreement record. 

  * Install Date
  * Initial Page Count
  * Base Charge
  * Included Black Pages
  * Black Overage $
  * Included Color Pages
  * Color Overage $


  * Total Base Charge $



  


  * "Section B - Special Terms" section:
    * Agreement Special Terms (box with text; pulls the text from the "Special Terms" memo on the Managed Service Agreement record)
    * Device Special Terms (box with text; pulls the text from the "Special Terms" memos on any of the included Devices, on separate lines, in the order in which they appear on the Billing Group table; in the following format: "<Device Description>: <Special Terms>")



  


  * "Section C - Agreement Details" section:
    * Agreement Details (text box; pulls the text from the Agreement Text memo on the AppHosting.Zone Settings page, with expressions filled in appropriately) 
    * Sales Rep (displays the Agreement Sales Rep from the Agreement record)
    * Date (displays the current date when the printout is generated)



  


Template: 

  * Header (page 1 only): 
    * Think Ink logo
    * Think Ink address:
      * 2401 County Rd 144, Sugarcreek, OH 44681
    * Think Ink Contact info:
      * T: 330.674.2251
      * F: 330.674.0033 
      * E: [support@thinkinkllc.com](mailto:support@thinkinkllc.com)
    * "Managed Service Agreement"
    * "Agreement ID: <Agreement ID>.<Revision #>
    * "Effective Start Date: <mm/dd/yyyy"



  


  * Footer: 
    * "Current Revision Date: <mm/dd/yyyy>"
    * "Page <X> of <Y>"



  


Handling Page Breaks: 

  * All pages include the full header and footer.



TODO_IDD: Ben Reitz 08/11/2023: Discrepancy. Template above says header for Page 1 only. Here it says full header for all pages.

  * Page break can be made in the middle of Section A if needed.
  * Page break can be made before Section B if needed (don't split this section).  
  * Always have a page break before Section C (always on its own page).



  


Other Notes:

  * N/A



  


Development Specification

Mockup: [https://docs.google.com/document/d/1AeTv-KF43Okc2WBYbpVeJ9-41geRU9RqmiBFVp5206Y/edit](https://docs.google.com/document/d/1AeTv-KF43Okc2WBYbpVeJ9-41geRU9RqmiBFVp5206Y/edit)

  


Sample from the client:

  * Full printout (some text cut off): [https://drive.google.com/file/d/1V6IUuQnQ3HpbFq7wXSe9J3CX_ovn_raA/view?usp=drive_link](https://drive.google.com/file/d/1V6IUuQnQ3HpbFq7wXSe9J3CX_ovn_raA/view?usp=drive_link) 
  * Page 2 (agreement text): [https://drive.google.com/file/d/1RyzPyCL14j9Qxl6EAG94-BO767YDhsWE/view?usp=drive_link](https://drive.google.com/file/d/1RyzPyCL14j9Qxl6EAG94-BO767YDhsWE/view?usp=drive_link)



  


TODO_EM: Tim Reitz 08/01/2023: Do you want the client to provide a letterhead or will we build out the full PDF template?
