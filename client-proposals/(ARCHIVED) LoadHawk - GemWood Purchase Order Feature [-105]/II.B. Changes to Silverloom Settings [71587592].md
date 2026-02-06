2.2. Changes to Silverloom Settings

  * Email Settings section (custom):



  


Not copying in the full section spec. 

  


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
