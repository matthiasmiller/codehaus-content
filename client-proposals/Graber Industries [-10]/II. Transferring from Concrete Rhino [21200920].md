2\. Transferring from Concrete Rhino

  


Requirements

Concrete Rhino is the whole batch system. It runs on a Linux computer, and its information needs to be pushed across into the accounting system. Currently, this is done through email attachments that can be imported into QuickBooks.

  


Rhino products will be transferred across as sales items, along with their short codes. Any modifications to these sales items in the AppHosting system will be overwritten during the nightly sync.

  


The following information needs to be transferred across to invoices:

  * Name & Billing Address
  * Invoice PO (from the job's PO)
  * Invoice Date (from the Delivery Date)
  * Item / Description
  * Quantity
  * Rate
  * Amount
  * Tax % -> based on the 3 checkboxes in Rhino



  


The invoices will be created based on all loads with a completed delivery. We will copy across any items, quantities, etc associated with that load. We will only copy across new invoices, leaving existing invoices untouched.

  


The tax % will be based on the % configured in the AppHosting database.

  


Development Specification

I'm thinking we'll just have a cron that dumps data from the sqlite database. When I did some digging on the backup, I found that it sends this request:

  


[http://localhost:8080/controlclient/export/rhino_backup.db](http://localhost:8080/controlclient/export/rhino_backup.db)

  


All that does is runs the following commands:

  


$  cp /opt/alogic/dat/sys.db /opt/alogic/wwwroot/controlclient/export/rhino_backup.db

  


We can just write a Python script that points to the source database, copies it to a working folder, then use sqlite to suck out the data.

  


QUESTIONS

[ ] Do you ever mark a load completed the day after?
