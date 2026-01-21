4.3.4. NG Customer Record

  


Requirements

Overview: This record is a read-only copy of the data from the NexGen Customer record.

  


This is a custom list-tied record that's keyed off the NexGen key (externalRef).

  


Read-Only NG Fields:

  * externalRef (UID)
  * Active
  * Name
  * First Name
  * Last Name
  * Address 1
  * Address 2
  * City
  * State/Province
  * Country
  * Phone
  * Mobile
  * Fax
  * Email
  * Price Level (pending Easy Automation adding this to the endpoint)



  


Development Specification

TODO_IDD: Tim Reitz 04/30/2024: We don't have direct one-to-one matching between the QB Contact and the NG Customer records, so we will need to match on name (maybe + phone or something like that).
