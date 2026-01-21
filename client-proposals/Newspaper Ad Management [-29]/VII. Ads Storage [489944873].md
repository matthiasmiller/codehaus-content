7\. Ads Storage

  


Requirements

The plan is to use Amazon S3 for the storage of the ad files. CCI/CH set up integration between S3 and AppHosting to upload, download, preview, and email the ad files through the ads management database. 

  


John Lapp/PNP would be responsible for setting up the Amazon S3 account and providing login access to CCI/CH. CCI/CH would set up the account details, storage, and integration. Billing for the storage would go directly to John/PNP rather than through AppHosting.

  


Development Specification

Restrictions for accessing ads files:

  * Full Admins: Full access
  * Publication Admins: Full access for assigned publication
  * Standard Users: Full access for assigned publication


