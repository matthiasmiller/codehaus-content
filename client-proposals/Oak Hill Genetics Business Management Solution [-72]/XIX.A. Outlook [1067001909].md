19.1. Outlook

  


Requirements

We have the following options for Outlook integration:

  


  * The simplest is changing the attachments to be links, and simply embedding the link into the email contents.



  


  * We may be able to provide a link to download a draft email and simply click it to open it in Outlook (or any email software).



  


  * We can provide the ability to send emails within the software, providing limited editability of the message contents.



  


  * We can provide the ability to send emails within the software, with full editability of the email and contents.



  


The specifics will be determined in the in-depth design.

  


Development Specification

email.Generator

  


Email Settings: In the existing software this looks like basic email fields: To, Subject (can include expressions), Body (can include expressions), Attachments.
