20.1.4.1. Generating Emails

  


Requirements

To generate email communications, run the appropriate menu from Faith Builders SPE | Communications. This will generate draft emails, which can be viewed from the View/Send Emails menu item under the Communications tab.

  


Development Specification

[ ] Each of the email communications will be driven by multiple r20s that get fed into the same x30.

  


[ ] Add a macro to evaluate the template subject from an email.

  * If it evaluates based on the email record, evaluate from that context.
  * Otherwise, do a LookupLevelField to evaluate the record from the appropriate context



[ ] Add a macro to do the same thing for the body

  


[ ] Std Notify Contacts.x30

  * Ask Prompt (Template)
  * Column 1 - Recipient



It will create a new email record for each row, setting the From to the correct value, filling in the To, and evaluating/populating the subject/body.

[ ] Create a series of reports for each Contact notifications that returns a single column with the recipient contact. Consider naming these consistently, such as "Std Notify Contacts - Soliciting of Applications", etc.

  


[ ] Std Notify Member Applications

  * Same as above, except:
  * Column 1: Recipient
  * Column 2: Member Application



  


[ ] Std Notify SPE Approvals

  * Same as above, except:
  * Column 1: Recipient
  * Column 2: SPE Approval
  * Column 3: Pipe-delimited list of schools



The x30 should only try to populate the list of schools if it's non-blank.
