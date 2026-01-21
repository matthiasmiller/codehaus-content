5.4. Silverloom Settings

  


Requirements

The standard Silverloom Settings page, accessed from Advanced | Admin | Silverloom Settings, includes the following custom sections and fields for various configuration settings. It also may include standard sections & fields. 

  


  * GemWood Settings section (custom; visible to and editable for users with the "Manage Financials" Permission)
    * GemWood Lumber Brokerage Fee % (number; 2 decimals; used to calculate the portion that GemWood retains for their brokerage fee, out of the Total Load Value for a Delivery Ticket (including both lumber and Other Line Items, as applicable); defaults to blank, but the current percentage is 4.00%; warning on Save if blank) 
    * Default Salesperson (drop list of active "Internal"-type Contacts; warning on Save if blank) 
    * Internal Fee Payouts Configuration (embedded spreadsheet with the following; used for tracking internal GemWood payouts of the brokerage fee: 
      * Columns: 
        * Payee (required; drop list of all active Internal-type Contacts; validate against duplicates - error message on the field: "Duplicate Payees are not allowed.")
        * Division (required; drop list of GemWood Divisions list items; used for tracking & reporting on Internal Fee Payouts) 
        * Fee Payout % (required; number; 2 decimals; defaults to 0.00; this is the percentage out of the "GemWood Lumber Brokerage Fee %" that the Payee receives) 
        * % of Total Load Value (read-only macro; number; 2 decimals; displays the calculated value of "GemWood Lumber Brokerage Fee %" * "Fee Payout %"; i.e. if "GemWood Lumber Brokerage Fee %" = 4% and "Fee Payout %" = 25%, this would = 1%)
      * Automatically sorted by: Payee (alphabetically) 
      * Buttons to insert/append/remove rows: "+" / "-"
      * Show 10 rows without scrolling 
      * Other Notes: 
        * N/A
    * % of Lumber Brokerage Fee Used (read-only macro; number; 2 decimals; displays the sum of "Fee Payout %" values; i.e. if "Fee Payout %" items = 25.00%, 10.00%, & 10.00%, this would = 45.00%) 
    * "This configuration does not account for Sales Commission or profits, which also come from the Lumber Brokerage Fee of <%>%." (visible if "GemWood Lumber Brokerage Fee %" is not blank; on-screen message in black font, as a reminder to users that the Brokerage Fee % should not all be allocated, to account for Commission and profits) 



  


  * Email Settings section (custom): 
    * Configure Salesperson Invoice Review Email (button; opens a child screen with the following:)
      * Default Text for Salesperson Invoice Review Email (memo that can include expressions; defaults to blank; the contents of this memo are used as the template for the "Salesperson Invoice Review Email"; warning on Save if blank; contents to include are as follows: 



  


Hello, #ContactField( TktGWFinSalesperson, ContactFirstName)#,

  


The following Buyer Invoice is ready for your review and approval.

  


Buyer: #TktBuyer#

Invoice #Chr( 35)#: #TktBFinBuyerInvoiceNum#

Invoice $: #TktBFinBuyerInvoice$##IncludeIf(TktBFinIsApprovalDenied)#

  


You previously denied approval for this invoice, based on the following comments:

#TktBFinApprovalDeniedComments##IncludeEnd#

  


To approve and send it to the Buyer, follow [[#ComponentWebUrl( "MainDir::\Standard\Std Approve or Deny Invoice.x30|?vAskDeliveryTktID="+String(TktInternalID)+",vAskApproved="+AddQuotes("Yes"))# this link]].

  


To deny approval and leave comments, follow [[#ComponentWebUrl( "MainDir::\Standard\Std Approve or Deny Invoice.x30|?vAskDeliveryTktID="+String(TktInternalID)+",vAskApproved="+AddQuotes("No"))# this link]], and email Dane to let him know.

  


Link to Delivery Ticket: #ComponentWebUrl( "MainDir::\Standard\Std Autopush Open Delivery Ticket.r20|vAskTicketNum="+String(TktInternalID))#

  


Link(s) to original Delivery Ticket scans from the Member (links expiring in 180 days): #ConcatRG( TktDeliveryTicketFileUploadKey, "[[" \+ WSGI_RedirectURL( RedirectReportPath, TktDeliveryDownloadUploadedFileURL) + " " \+ AttachmentName( TktDeliveryTicketFileUploadKey) + "]]", ", ")#

  


Link(s) to original PO documents from the Buyer (links expiring in 180 days): #PurchaseOrderField( TktBuyerPurchaseOrderID, ConcatRG( POFileUploadKey, "[[" \+ WSGI_RedirectURL( RedirectReportPath, PODownloadUploadedFileURL) + " " \+ AttachmentName( POFileUploadKey) + "]]" , ", "))#

  


Thanks!

The GemWood Solution Bot

  


  * Configure Buyer Invoice Email (button; opens a child screen with the following:)
    * Default Text for Buyer Invoice Email (memo that can include expressions; defaults to blank; the contents of this memo are used as the template for the "Buyer Invoice Email"; warning on Save if blank; contents to include are as follows: 



  


Hello, 

  


Please see the attached invoice from GemWood. 

  


Link(s) to original PO documents (links expiring in 180 days): #PurchaseOrderField( TktBuyerPurchaseOrderID, ConcatRG( POFileUploadKey, "[[" \+ WSGI_RedirectURL( RedirectReportPath, PODownloadUploadedFileURL) + " " \+ AttachmentName( POFileUploadKey) + "]]" , ", "))#

  


Thank you!

  


  * Configure GemWood Purchase Order Email (button; opens a child screen with the following:)
    * Default Text for GemWood Purchase Order Email (memo that can include expressions; defaults to blank; the contents of this memo are used as the template for the "GemWood Purchase Order Email"; warning on Save if blank; contents to includes are as follows:) 



  


Hello, 

  


Please see the attached purchase order.

  


Thank you!

  


  * Configure Member Payment Issued Email (button; opens a child screen with the following:)
    * Default Text for Member Payment Issued Email (memo that can include expressions; defaults to blank; the contents of this memo are used as the template for the "Member Payment Issued Email"; warning on Save if blank; contents to includes are as follows: 



  


Hello, 

  


Payment has been issued by GemWood via ACH for this delivery ticket. Please see the attached documents for details.

  


Thank you! 

  


  


Data Access:

  * Visibility: Visible to all users (standard), with section(s) and/or field(s) limited to certain users based on Permissions (custom) 
  * Editability: Editable for users included in the "Custom_CanEditSilverloomSettings" macro, which defaults to "Administrator"-type Users only (standard) 



  


Other Notes:

  * CCI can assist with generating the expressions to be used in the "Default Text" for email body fields. 
  * The Solution will display an alert if an expression in an email template fails to evaluate when the email is sent.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1449376467#gid=1449376467](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1449376467#gid=1449376467)

Tim Reitz 01/02/2025: Updated

  


  


Change Requests:

  * Ben Reitz 10/08/2025: [[[IN11670](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11672&)]] - ZGW - Add "Internal Fee Payout Sent" and "Sales Commission Paid" emails
  * Ben Reitz 10/08/2025: [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature
  * 


  


Tim Reitz 10/21/2024: Per Ellis, let's make the following CORE change, to base editability on the following macro; 

[ ] New macro: 

[ ] Custom_CanEditSilverloomSettings

[ ] Defaults to UserIsAdministrator

[ ] For GemWood, set it to the "Manage Financials" Permission.

Tim Reitz 01/29/2025: After talking with Jisan today, we're allowing all Administrators to edit. 

Jisan Mahmud 01/30/2025: Just to clarify, to edit the GemWood Settings section, user still needs to have the "Manage Financials" permission.

  


Ellis Miller 12/13/2024: 

[ ] Add fields

[ ] Add RG

[ ] Report alert for inactive contacts

[ ] Add multiple memos with #expr# parsable expr fields (include report alerts on failures).

BID 2 days
