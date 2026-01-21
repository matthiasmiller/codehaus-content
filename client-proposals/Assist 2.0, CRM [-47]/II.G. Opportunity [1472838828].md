2.7. Opportunity

  


Requirements

Opportunity

  * Contact
  * Opportunity
    * Description
    * Lead Source (user-owned list; can add new items but they won't show up in the master list without approval); list of:
      * Phone
      * Email
      * Website
      * Saw a Lot
      * Print Ad
      * Billboard
      * Referral
    * Referral Source (text)
    * Marketing (section)
      * UTM Source (text)
      * UTM Medium (text)
      * UTM Campaign (text)
      * UTM Term (text)
      * UTM Content (text)
      * Search Engine Term (text)
    * Status; automatic
      * Unclaimed
      * Not Yet Quoted
      * Quoted
      * Won
      * Lost
      * Abandoned
    * Origination Date (default to today's date)
    * Follow-up Date
    * Follow-up Task (text field)
    * Closed checkbox (sets Date to today)
    * Closed Date
    * Closed Reason (Won / Lost / Abandoned; required if closed)
  * Estimates / Sales Orders (list of links to the Estimates / Sales Orders)



  


Sales Portal

Opportunities are assigned based on the Contact's assignment. With the exception of new communication entries, it can only be edited if the salesperson has claimed the contact. This would have a read-only checkbox showing whether it's been claimed, along with a button to claim/unclaim the contact from the opportunity record. (NOTE: This means that if one salesperson is covering for another salesperson, they would have to claim the opportunity before making any changes.)

  


If the salesperson has NOT claimed the contact, allow them to add a Communication with notes for the sales person. The followup date would automatically be set to today's date. This allowed other salespeople to easily leave messages for other sales people.

  


All unclaimed or unquoted opportunities would be visible to everyone in the district. Once that lead is quoted, the opportunity would only be visible to the person who's assigned to it.

  


The opportunity will also have a section for Duplicate Contacts, allowing them to be merged directly through the opportunity, in the same was as the Contact record.

  


Development Specification

[ ] For Lead Source, allow AddToList, but the helper list will only show active items.

  


[ ] On the Estimate / Sales Order, add a hidden field that links back to the opportunity. I'm thinking we use a custom DB level (numeric ID). We should add a link to the sales order to "View Opportunity". We need to coordinate with Josh to pass this opportunity ID to the visualizer. Add the field, then let Josh know that we need to pass this through.

  


[ ]  I don't care whether Closed Reason is the same or different list from Status. I'm fine with the same list but filtering it down.

  


[ ] Consider a Warning on Save on the Sales Order if the linked opportunity is Won but does not have any completed sales orders.

  


[ ] The Estimates / Sales Orders can be a link in AppHosting. We'll embed it in the sales portal.
