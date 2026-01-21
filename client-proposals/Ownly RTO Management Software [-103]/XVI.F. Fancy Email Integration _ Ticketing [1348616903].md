16.6. Fancy Email Integration / Ticketing

For Now:

  


  


[cricketvalley@ownlyrto.com](mailto:cricketvalley@ownlyrto.com)

  * Set up Mailgun
  * Set up Mailgun routes for forwarding -> gmail
  * Set up gmail to use this as the sending address - [https://support.google.com/mail/answer/22370](https://support.google.com/mail/answer/22370)



  


  


  


  


Email:

  * [autoimport@myrtocompany.com](mailto:autoimport@myrtocompany.com)
    * All emails get imported into the system
    * All emails get auto-assigned based on current contacts in the system
    * Unassigned/unrecognized emails get put somewhere
      * OR, we never assign, and we just search for all messages to all phone #s and emails linked to the account and don't care about duplicates
  * [mycompany@myrtocompany.com](mailto:mycompany@myrtocompany.com)
    * include a forwarding rule that sends it to autoimport@....



  


  * autocreate emails like:
    * [myaccountnumberis+HashedOrMaskedAccountNumber@mycompany.com](mailto:myaccountnumberis+HashedOrMaskedAccountNumber@mycompany.com)



  


Setup:

  * Sending SMTP
  * Inbound SMTP
  * Automatically forward all outbound emails to [autoimport@myrtocompany.com](mailto:autoimport@myrtocompany.com)


