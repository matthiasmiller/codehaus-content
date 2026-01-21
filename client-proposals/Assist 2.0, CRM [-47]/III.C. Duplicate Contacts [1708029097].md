3.3. Duplicate Contacts

  


Requirements

Deduplicating Contacts

This is a two-pane report. The left pane shows all contacts for a salesperson that had activity for the prior week, and that share a name, email, address, or phone number with another contact. The right pane shows those secondary possible contacts, using the same columns as the duplicate contacts spreadsheet on the Contact record. The salesperson will have the opportunity to select two contacts, then click Merge. This behavior will work the same as on the Contact screen above.

  


Development Specification

All we need for now is the subset.

  


Macros:

ContactIDsByContactInfo. Takes pipelist of addresses, emails, phones, and exclude IDs.

ContactIsDuplicate: calls the above with current record data.
