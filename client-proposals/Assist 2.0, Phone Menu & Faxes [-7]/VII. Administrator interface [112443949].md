7\. Administrator interface

  


Requirements

The software will provide an online interface for administration and maintenance.

  


This includes managing the overall menu structure, monitoring activity, and overseeing user permissions.

  


USER SPECIFICATION

The online administration interface will have a dashboard that includes the following features:

  


Activity   Recent activity   Activity by user   Search activity   Failed QB uploads (alert)   Newly-created documents (alert)  
| Menu   View menu   Search for document   Deleted items| Users   View all users   View companies   View builder permissions  
  
---|---|---  
Batch reports   View all batch jobs   Recent job runs  
| Documentation   Wiki|   
  
  
  


Activity

The activity section will have interactive reports to monitor recent activity. This would allow the administrator to assist with scanned files (correcting file names, for example), as well as find out when things like the Quickbooks upload fail.

  


Menu

This will allow viewing the phone/fax menu by different views:

  * A summary view only showing the folders.
  * A detailed view showing all the individual documents in the folder structure.
  * A view showing the folders in the hierarchy with permissions. This is to allow a quick manual audit of folder permissions.



It is from this menu report that individual documents can be created and modified, including their names and permissions.

  


Users

This is where individual user accounts will be managed. Each user account can have:

  * One or more telephone numbers tied to it. The user must call from this number to be recognized.
  * One fax number. This is the number to which requested faxes will be sent.
  * An email address for receiving color faxes.
  * A PIN for requesting PIN-protected documents
  * Zero or more companies that the user is a part of.



All of this information can be updated by the administrator after the software has been installed.

  


Batch reports

This section allows the administrator to configure batch jobs (see below.)

  


Development Specification

Do you want to prevent the administrator from seeing some documents? Personnel-related, for example. Josh Nisly 04/19/2018: Answer: the administrator should be able to see metadata, but not actual content. This isn't a very bullet-proof block, since the administrator could simply email the document to herself.

  


Ability to send document to phone/email/zip.

  


Uploading documents: for individual documents, we'll have an "Upload new version" that takes them to a wsgi page. (They'll have to authenticate separately for the wsgi page. It will do OAuth with Google, then validate the username with the system. Only admins can upload???)

  


  


Records

Builder (really, a user profile)

  * Fax #
  * Phone numbers
  * Optional PIN



  


Company

  


40 hours?
