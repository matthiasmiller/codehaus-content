7.1.3.1. Shipped Member Payment Terms Records

  


Requirements

The following Payment Terms for Members are hard-coded and included in the system automatically ("shipped"), with the "Payment Terms Name" field read-only and the other fields editable: 

  


  * Shipped Payment Terms: 



  


  * "Early Pay Option":   
    * Explanation: GemWood has the option to pay the Member within 10 calendar days of the Ticket Date for a 2% discount (in addition to and after the GemWood Lumber Brokerage Fee).  If GemWood does not pay within 10 days, the full amount is due within 3 business days of the "Buyer Settlement Date". 
    * Spec:
      * Payment Terms Overview section:
        * Active: Checked  
        * Available For: "Member" (read-only)
        * Name: "Early Pay Option" (read-only)
        * Description: Blank (can be configured as needed in the Solution)
      * Early Payment section:
        * Uses Optional Early Payment: Checked
        * Early Pay Window [   ] Calendar Days from Ticket Date: "10"
        * Early Pay Discount %: "2.00"
      * Due Date section:
        * Payment Due In: "3"
        * Day Type: "Business"
        * Date Baseline: "Buyer Settlement Date"



  


  * "After Buyer Settlement": 
    * Explanation: GemWood waits to pay the Member until after receiving payment from the Buyer for the load. This is a net payment to the Member, due within 3 business days of the "Buyer Settlement Date", with no additional fee or discount taken off. 
    * Spec:
      * Payment Terms Overview section:
        * Active: Checked  
        * Available For: "Member" (read-only)
        * Name: "After Buyer Settlement" (read-only)
        * Description: Blank (can be configured as needed in the Solution)
      * Early Payment section:
        * Uses Optional Early Payment: Not checked
        * Early Pay Window [   ] Calendar Days from Ticket Date: N/A (not visible)
        * Early Pay Discount %: N/A (not visible)
      * Due Date section:
        * Payment Due In: "3"
        * Day Type: "Business"
        * Date Baseline: "Buyer Settlement Date"



  


Development Specification

BID: 3 Hours

  


TODO_VA: Tim Reitz 07/28/2025: Let's update this documentation. Client has changed at least the Early Pay Option (Due Date settings) in the live system. Let's note here what the original settings were, and that they may be changed.
