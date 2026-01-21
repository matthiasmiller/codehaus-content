25.5. User Report: Upfront Payments & Member Equity Report

  


Requirements

Tim Reitz 01/23/2025: Removing Upfront Payments today, so I'm archiving this section.  

  


Estimated Cost: $400-800

  


Spec:

Overview: This is a custom user report (not a standard hard-coded report) of equity accumulated by Members, based on Delivery Ticket records. This report specifically includes "Closed" Delivery Tickets with "Member Payment Terms" = "75% Upfront With Equity".

  


Since equity accounts are not anticipated to be kept very long beyond the deployment of the Solution, Phase 1 does not include built-in handling of equity and upfront payments. This report is set up within the Solution at or after deployment and is not interfaced on the menus. A link can be saved in browser bookmarks or in the Solution's standard "Favorites" feature. 

  


Note that this tracks accumulated equity, and does not track draws that the Members may make on their accumulated equity.

  


Accessed from: Shared user folder or link/bookmark/favorite (no menu option) 

  


Title: Upfront Payments & Member Equity

  


Columns: 

  * Ticket # (link to open the record) 
  * Ticket Date 
  * Total Buyer Payment $ (total row shows sum) 
  * Original Member Subtotal $ (total row shows sum)
  * GW Income from Upfront Payment ($) (displays the value of "GemWood Upfront Payment Discount $" or "GemWood Discount $")
  * Upfront Payment Discount % (displays "2.00")
  * Upfront Payment Discount $ (displays the value of 0.02 * "Original Member Subtotal $"; total row shows sum) 
  * Equity % (displays "6.00") 
  * Equity $ (displays the value of 0.06 * "Original Member Subtotal $"; total row shows sum)



  


Grouped by: Member (alphabetically)

  


Sorted by: Ticket # (alphabetically)

  


Filters: 

  * Member (drop list of Member-type Contacts; defaults to blank = all)
  * Ticket Date Start (date; looks at the Ticket Date; defaults to blank = all)
  * End (date; looks at the Ticket Date; defaults to blank = all)



  


Buttons: 

  * N/A



  


Menu Visibility: 

  * N/A (no menu option) 



  


Other Notes:

  * N/A



  


Development Specification

Mockup: __??

_MOCKUPS: Tim Reitz 01/16/2025: should we do a mockup for this?
