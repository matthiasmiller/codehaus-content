9.4. Statement (Unpaid Invoices) Printout

  


Requirements

Purpose/Overview: The Unpaid Invoices printout, more commonly referred to as the "Statement", is a custom PDF printout of unpaid invoices for an Agent's clients within the current Period Year and previous Period Year(s).

  


Printed From (opens the PDF in the browser, with the option to download or to print):

  * Contact Record: "Print Statement" link (for an individual client) 
  * Admin | Renewals and Printing | Print Annual Invoices & Insurance Cards - "Link to Print Invoices column" (for all clients of an agent, for a given period year)



  


File Format/Name: 

  * PDF: 
    * For an individual client: "Statement for <ClientLastName, ClientFirstName>"
    * For all clients of an agent: "Statements for Client(s) of Agent <AgentLastName, AgentFirstName>" 



  


Fields to be Filled: 

  


  * Header:
    * Agent details / return address (note that this information lines up with the return address window in a 5030C window envelope - see details in Other Notes): 
      * "<AgentLastName, AgentFirstName, in all upper case letters>" 
      * "<Agent address, in standard format, up to 3 lines, in all upper case letters>" 



  


  * Client details / mailing address (note that this information lines up with the return mailing address window in a 5030C window envelope - see details in Other Notes): 
    * "<ClientLastName, ClientFirstName, in all upper case letters>"
    * "<Client address, in standard format, up to 3 lines, in all upper case letters>" 



  


  * Plan details (displays the "Plan Identifying Details", with the following):
    * Plan Name (bold; from the "Plan name" System Switch)
    * Plan Name Subtitle (italics; from the "Plan name subtitle" System Switch; displayed if non-blank)
    * Plan Address (bold; from Silverloom Settings)
    * Plan Phone (bold; from Silverloom Settings)



  


  * Statement Date: "<current date, in the mm/dd/yyyy format>" 



  


  * Itemization: 
    * "See attached details." (visible on the first page if there are more than 8 lines in the itemization table, in bold font; the itemization table is then displayed on one or more following pages) 
    * Itemization table (displays one row for each row of all Invoices with Status = "Invoiced" for the Client):
      * Columns:
        * Invoice # column: "<Invoice # from the corresponding Invoice>"
        * Date column: "<line item Date from the itemization table of the corresponding Invoice, in the mm/dd/yyyy format>" 
        * Vehicle column: "<line item Vehicle Name from the table of the corresponding Invoice>" 
        * Description column: "<line item Description text from the table of the corresponding Invoice>" 
        * Amount column: "<line item Amount from the table of the corresponding Invoice>" 
      * Sorted by: Invoice (oldest/lowest ID at the top), then Date (blank at the top, if applicable, then oldest to newest)
    * Total Amount: "<sum of "Total Amount" fields for all unpaid Invoices for this Client; may be positive or negative>" 
      * Note: New field on the printout. 
    * Total Paid <sum of "Total Paid" fields for all unpaid Invoices for this Client>"
      * Note: New field on the printout. 
    * Total Balance Due: <sum of "Due Amount" fields for all unpaid Invoices for this Client; may be positive or negative>"



  


  * Payment Remittance Footer:
    * Agent details: 
      * "<AgentLastName, AgentFirstName, in all uppercase letters>" 
      * "<Agent address, in standard format, up to 3 lines, in all uppercase letters>" 



  


  * Client details: 
    * "<ClientLastName, ClientFirstName, in all uppercase letters>"
    * "<Client address, in standard format, up to 3 lines, in all uppercase letters>" 



  


  * Amount Due: "<sum of "Due Amount" fields for all unpaid Invoices for this Client; may be positive or negative>"



  


  * Make checks payable to: <contents of the "Plan Name" System Switch> 



  


  * CLIENT NO.: "<Contact ID for the Client>"



  


Handling Page Breaks: 

  * If there are 8 rows or fewer on the Itemization table, the entire statement fits onto one page, so no page breaks are needed.
  * If there are more than 8 rows on the Itemization table, the entire table is moved off of the first page to start at the top of the second page. If there are enough rows to require additional pages, page breaks should happen between rows.



  


Other Notes:

  * Note this is not the same as the standard Silverloom Customer Statement printout, which is not used in this Solution.
  * Includes the standard "Powered by Silverloom Business Suite" footer. 
  * As mentioned above, the Agent and Client addresses at the top of the Statement printout are located to be compatible with a 5030C double-window envelope. The details are as follows:
    * Model: 5030C
    * Measurements:
      * Envelope dimensions: 9" x 4-1/8"
      * Top window:
        * Placement: 5/8" from left, 1" from top
        * Dimensions: 3" x 7/8"
      * Bottom window:
        * Placement: 5/8" from left, 7/8" from bottom
        * Dimensions: 4" x 1"



  


Development Specification

Sample(s): 

  * Tim Reitz 08/23/2024: Template as of today: [[File:Std Print Unpaid Invoices Template.r21.rtf]]



  


  


Change Requests: 

  * Tim Reitz 08/20/2025: [[[IN11314](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11316&)]] - ZWA Multi-State Feature - Umbrella Incident


