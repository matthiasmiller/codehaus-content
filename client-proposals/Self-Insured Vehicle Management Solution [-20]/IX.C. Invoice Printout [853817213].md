9.3. Invoice Printout

  


Requirements

*Done. 

  


Purpose/Overview: This printout is generated for an individual Invoice record.

  


Printed From:

  * Invoice record: "View as PDF" and "View in Word" buttons



  


File Format/Name: 

  * PDF
    * File Name: "Invoice <Invoiced Date>"
  * Word
    * File Name: "Invoice <Invoiced Date>"



  


Fields to be Filled: 

  * PDF: This is a customized printout with "INVOICE" displayed in the top right corner:
    * Agent (displays the Client's agent and the agent's address)
    * Bill To (displays the Client's name and Client's billing address)
    * Ship To (displays the Client's name and Client's ship to address)
    * Sales Items (unlabeled table, with one row for each sales item (fee/credit), with the following columns):
      * Date (displays the date from the corresponding column in the Itemization section of the Invoice record)
      * Vehicle (displays the text from the Vehicle Name column in the Itemization section of the Invoice record)
      * Description (displays text from the Sales Item and Description columns in the Itemization section of the Invoice record, in the following format: "<Sales Item> for <Description>", or simply "<Sales Item>" if Description is blank)
      * Price (displays the price from the corresponding column in the Itemization section of the Invoice record)
    * Sub-Total (displays the sum of the Price column)
    * Total Amount (bold font; displays the sum of the Price column)



  


  * Word: Same as PDF. 



  


Handling Page Breaks: Split as needed between rows in the itemization / sales items table.

  


Other Notes:

  * N/A



  


Development Specification

Sample(s):
