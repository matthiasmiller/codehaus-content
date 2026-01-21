7.1.3.2. Shipped Buyer Payment Terms Records

  


Requirements

The following Payment Terms for Buyers are hard-coded and included in the system automatically ("shipped"), with the Payment Terms Name field read-only and the other fields editable: 

  


  * "2/10 net 30":
    * Explanation: The Buyer has the option to pay GemWood within 10 calendar days of the Ticket Date to receive a discount of 2% off of the "Buyer Grade $" (initially estimated from the "Buyer Invoice $"). If paid with the discount after 10 calendar days, the Buyer Payment will give a warning on save to confirm that the details are correct - see corresponding section of the proposal. If the Buyer does not pay within 10 days, the full amount is due within 30 calendar days of the Ticket Date.
    * Spec:
      * Payment Terms Overview section:
        * Active: Checked  
        * Available For: "Buyer" (read-only)
        * Name: "2/10 Net 30" (read-only)
        * Description: Blank (can be configured as needed in the Solution)
      * Early Payment section:
        * Uses Optional Early Payment: Checked
        * Early Pay Window [   ] Calendar Days from Ticket Date: "10"
        * Early Pay Discount %: "2.00"
      * Due Date section:
        * Payment Due In: "30"
        * Day Type: "Calendar"
        * Date Baseline: "Ticket Date"



  


  * "1/10 net 30": 
    * Explanation: The Buyer has the option to pay GemWood within 10 calendar days of the Ticket Date to receive a discount of 1% off of the "Buyer Grade $" (initially estimated from the "Buyer Invoice $"). If paid with the discount after 10 calendar days, the Buyer Payment will give a warning on save to confirm that the details are correct - see corresponding section of the proposal. If the Buyer does not pay within 10 days, the full amount is due within 30 calendar days of the Ticket Date.
    * Spec:
      * Payment Terms Overview section:
        * Active: Checked  
        * Available For: "Buyer" (read-only)
        * Name: "1/10 Net 30" (read-only)
        * Description: Blank (can be configured as needed in the Solution)
      * Early Payment section:
        * Uses Optional Early Payment: Checked
        * Early Pay Window [   ] Calendar Days from Ticket Date: "10"
        * Early Pay Discount %: "1.00"
      * Due Date section:
        * Payment Due In: "30"
        * Day Type: "Calendar"
        * Date Baseline: "Ticket Date"



  


  * "Net 5":
    * Explanation: The Buyer must pay GemWood the full "Buyer Grade $" or "Buyer Invoice $" amount within 5 calendar days of the Ticket Date, with no early pay discount option.
    * Spec:
      * Payment Terms Overview section:
        * Active: Checked  
        * Available For: "Buyer" (read-only)
        * Name: "Net 5" (read-only)
        * Description: Blank (can be configured as needed in the Solution)
      * Early Payment section:
        * Uses Optional Early Payment: Not checked
        * Early Pay Window [   ] Calendar Days from Ticket Date: N/A (not visible)
        * Early Pay Discount %: N/A (not visible)
      * Due Date section:
        * Payment Due In: "5"
        * Day Type: "Calendar"
        * Date Baseline: "Ticket Date"



  


  * "Net 10":
    * Explanation: The Buyer must pay GemWood the full "Buyer Grade $" or "Buyer Invoice $" amount within 10 calendar days of the Ticket Date, with no early pay discount option.
    * Spec:
      * Payment Terms Overview section:
        * Active: Checked  
        * Available For: "Buyer" (read-only)
        * Name: "Net 10" (read-only)
        * Description: Blank (can be configured as needed in the Solution)
      * Early Payment section:
        * Uses Optional Early Payment: Not checked
        * Early Pay Window [   ] Calendar Days from Ticket Date: N/A (not visible)
        * Early Pay Discount %: N/A (not visible)
      * Due Date section:
        * Payment Due In: "10"
        * Day Type: "Calendar"
        * Date Baseline: "Ticket Date"



  


  * "Net 30":
    * Explanation: The Buyer must pay GemWood the full "Buyer Grade $" or "Buyer Invoice $" amount within 30 calendar days of the Ticket Date, with no early pay discount option.
    * Spec:
      * Payment Terms Overview section:
        * Active: Checked  
        * Available For: "Buyer" (read-only)
        * Name: "Net 30" (read-only)
        * Description: Blank (can be configured as needed in the Solution)
      * Early Payment section:
        * Uses Optional Early Payment: Not checked
        * Early Pay Window [   ] Calendar Days from Ticket Date: N/A (not visible)
        * Early Pay Discount %: N/A (not visible)
      * Due Date section:
        * Payment Due In: "30"
        * Day Type: "Calendar"
        * Date Baseline: "Ticket Date"



  


Development Specification

BID: 4 HOURS
