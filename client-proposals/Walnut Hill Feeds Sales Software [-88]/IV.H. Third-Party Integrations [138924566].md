4.8. Third-Party Integrations

  


Requirements

CodeCrafters will provide software to run on-premise to sync data from QuickBooks Enterprise and NexGen. Walnut Hill has an on-call IT person who can provide support to get this set up and configured.

  


Development Specification

This could either be GitHub + Python, OR ship as py2exe binary w/ config file for input file upload secret key, and probably EAI base URL, user name, and password

  


Proposed Design (pending Josh's stamp of approval):

  * Create temp folder
  * Call Transaction Pro command line to export QuickBooks information ([https://tprosupport.rightworks.com/kb/article/531-automate-rightworks-transaction-pro-exports-for-quickbooks-desktop/](https://tprosupport.rightworks.com/kb/article/531-automate-rightworks-transaction-pro-exports-for-quickbooks-desktop/)) 
  * Call EAI API (perhaps via a wrapper) to export all data files from everywhere
  * Upload all data to files to Silverloom using a utility and/or endpoint that Josh(?) supports.
  * Could use HMAC with date + secret key for authentication + prevening replays. (Alternatively, we could do date+time, and prevent uploading any duplicates or anything prior to the latest upload time.)
  * On Silverloom, create a scheduled task with all the input files and have it wait for all input files to run. This allows us to archive input files if an import breaks, making it easier to support.


