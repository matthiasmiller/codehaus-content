6.1. Email Integration for Private Messages

  


Requirements

The CRM system will allow email integration to private messages. The subject line will automatically include the opportunity ID, allowing it to be tied back to the opportunity. The software will have a link to allow opening an email client with the subject and email prefilled.

  


If an email is received without an opportunity ID, it will look for a contact with that email address. If no open opportunity exists, it will create a new opportunity.

  


NOTE: The email integration will be simplest if all emails are with the same provider, such as emailbyfax. If the email is hosted by multiple domains or with other fax bridges, it come at an additional cost.

  


Development Specification

All the domains are bought via Creative Warehouse. They don't foresee using emailbyfax.com right now.

  


TODO:

[ ] Add the Incoming Email catalog to ZFP

[ ] Set up with Josh to start pulling in all emails for all the sales people.

[ ] Create macros to automatically link opportunities

  * Is this email thread already linked to an opportunity. If so, link to that opportunity.
  * Does this email have an opportunity ID in the body? If so, link to that opportunity.



[ ] Create macros to automatically link contacts:

  * If there is a matching opportunity (above), link to that contact.
  * Otherwise, just create a new contact



[ ] x30list

  * Find the contact from above subset. Create one if it doesn't exist. Add an autonumber to the name to force uniqueness.
  * Find an opportunity for that contact, creating one if one doesn't exist.
  * Create an email record with an Opportunity ID that has an OnModify that automatically finds/sets the appropriate opportunity ID (based on above macros)
  * Create a communication record that links to the email record and the opportunity ID



  


  


[ ] When sending an email for an opportunity, add a body that says:

  


  


\--

Please write your message above this line, keeping the code [[OID1234]] in this sentence.

  


(This can be a macro based on the opportunity ID)

  


[ ] TODO: Have an easy way to create a new opportunity from an email (?)

  


[ ] TODO: If the salesperson is inactive, unassign the contact and put it through the dealer round robin.
