6.8.1.4. Buttons

  


Requirements

Buttons: The buttons will vary based on the selected Payment Type filter:

  


  * Send Landowner Summaries for Selected (visible if Payment Type = "Landowner %"; clicking the button prepares the Landowner Payment Summary Email for the selected paid Payments in the left pane; any selected unpaid payments will be skipped; see corresponding section of this proposal) 



  


  * Send Logger Summaries for Selected (visible if Payment Type = "Logger"; clicking the button prepares the Logger Payment Summary Email for the Payees on the selected paid Payments in the left pane; any selected unpaid payments will be skipped; see corresponding section of this proposal)



  


  * Send Yard Tally Summaries for Selected (visible if Payment Type = "Vendor"; clicking the button prepares the Vendor Yard Tally Summary Email for Payees on the selected Payments in the left pane; see corresponding section of the proposal)



  


  * Print Summaries for All Unpaid (visible if Payments Status = "Unpaid + Paid Today" and Payment Type = "Vendor"; clicking the button prepares the Vendor Yard Tally Summary PDF for all Yard Tallies associated with all unpaid Payments in the left pane, with all of the Yard Tally Summaries combined in one PDF, sorted by Payee then Yard Tally ID; see corresponding section of the proposal)



  


  * Print Summaries for Selected Unpaid (visible if Payments Status = "Unpaid + Paid Today" and Payment Type = "Vendor"; clicking the button prepares the Vendor Yard Tally Summary PDF for all Yard Tallies associated with the selected unpaid Payments in the left pane, with all of the Summaries combined in one PDF, sorted by Payee then Yard Tally ID; see corresponding section of the proposal)



  


  * Create Missing Payments (visible if Payments Status = "Unpaid + Paid Today"; runs the "Create and Link All Payments" background process to create Payment records for any items that are missing them (Down Payment rows, Expense Withholding rows, Yard Tally records, Pulpwood Load records)



  


Development Specification

Ellis Miller 12/22/2022: 

[ ] Use Open with Selected Values for each of these options, passing in a pipe-delimited list of payment ID's.

BID: 4 HOUR 

  


  * Print Yard Tally Summaries (visible if Payment Type = Vendor; clicking the button prepares the Vendor Yard Tally Summary PDF for Payees on the selected Payments in the left pane, with a separate file for each Payment; see corresponding section of the proposal)



DONE_DM: Tim Reitz 01/26/2023: how many of these would you be doing at a time? (similar consideration as the Booking Summary - zip file vs. one at a time in the browser) (could be row-by-row, or select multiple, or both)

DONE_CH: follow up: Client's ideal:

  * [X] links in-line for each individual
  * [X] Button at top to "Print All Unpaid...", generates one PDF with all tallies together
    * [ ] OR could be zip file if we can't do all together



DONE_MM: Tim Reitz 01/31/2023: "separate file for each Payment" \- but these printouts are on a per-Tally basis. We need to think through how it work if there are multiples Tallies on one Payment.

DONE_MM: Tim Reitz 01/31/2023: Client would like to batch them all together into one PDF and print with one click (rather than printing all of them individually).

DONE_CH: Tim Reitz 01/31/2023: we can write up a proposal for "Print for Unpaid..." w/out page numbers, and have Ellis review it. 

DONE_Ellis: Tim Reitz 01/31/2023: Could you review the updated design below and give your thoughts? The client would like to be able to print the Tally Summaries both on an individual/Payment basis and on a batch basis, and it's pretty important to them to be able to have just one PDF to print if they do the batch generation (rather than printing 25 separate PDFs at the end of the day). They are OK with the zip file and printing individually if we can't combine them all into one PDF. 

TODO_CH: Ellis Miller 02/03/2023: Yes, this works fine. I'm noting it. I am planning to use a single complex template that will be used for the Unpaid Yard Tally Printouts, Single Payment Printouts, and Yard Tally Printouts. This means that we will not show page numbers for the Payment Summary or Yard Summary exports.

TODO_EM: Tim Reitz 02/03/2023: Does this mean that the Landowner % Payment Summary and Logger Payment Summary printouts won't have page numbers?
