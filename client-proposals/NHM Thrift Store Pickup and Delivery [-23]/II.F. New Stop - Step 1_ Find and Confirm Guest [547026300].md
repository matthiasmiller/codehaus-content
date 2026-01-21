2.6. New Stop - Step 1: Find and Confirm Guest

  


Requirements

We will have a New Stop link on the menu. When clicked, it will prompt for:

  * Name
  * Address
  * Address Type
  * Apartment/Lot # (visible and required for Apartment/Lot)
  * City
  * State
  * Zip
  * Mobile phone
  * Home phone
  * Work phone
  * Email address



  


It will search for all contacts, and show similarity based on:

  * Name, Email, and Phone Number (heaviest weighting - 4x)
  * Street Address (secondary weighting - 2x)
  * City, State, and Zip (third weighting - 1x)



  


It will show a list of the first 15 guest, sorted by similarity. Phone numbers will match with other phone numbers, regardless of type. (For example, searching for a mobile number of 719-276-2676 will match on an existing contact that has a work number of  719-276-2676.)

  


It will also show a New Guest button that will pre-populate the new contact with a Pickup & Delivery Type and all specified fields.

  


The Guest screen will embed a map showing the location of the address. This will closely model the behavior in the prior system.

  


Development Specification

Matthias Miller 08/18/2020: This entire section will be handled by Matthias. He will coordinate with John Allan on the customer matching.

  


[ ] Can we optimize this to use a StrikeAMatch implementation without severe performance cost?

[ ] Can we have the bottom pane be an auto-push report that opens an integration to show the map? Or...

  


Required Validation:

[ ] Validate against unicode spellings of Canon City, etc?

[ ] Allow generating the following URLs:

  * geo - geo:%(lat)s,%(lng)s?q=%(addr)s
  * apple - [http://maps.apple.com/?ll=%(lat)s,%(lng)s&daddr=%(addr)s&dirflag=d&address=%(addr)s](http://maps.apple.com/?ll=%\(lat\)s,%\(lng\)s&daddr=%\(addr\)s&dirflag=d&address=%\(addr\)s)
  * google - [http://maps.google.com/maps?ll=%(lat)s,%(lng)s&daddr=%(addr)s](http://maps.google.com/maps?ll=%\(lat\)s,%\(lng\)s&daddr=%\(addr\)s)



  


Tim Reitz 09/14/2020: Should we include screenshots from the existing system, or provide access to it for me and the developers?

  


Matthias Miller 09/04/2020: We shluld embed this either as an integration.
