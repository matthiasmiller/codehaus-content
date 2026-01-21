25.0.1. Delivery Ticket - (OLD) Member Overview Section

  


Requirements

  * Member Overview section: 



  


  


Tim Reitz 11/22/2024: All fields from this section have been moved to other sections, specifically: 

  * Delivery Ticket Overview 
  * Documentation 
  * Member Financials



Archiving this old section.

  


Development Specification

Ticket #: 

Tim Reitz 10/17/2024: Per Ellis, to find the most recently-entered Ticket #, use DeliveryTicketsByMemberAndSysIDLastKey(MemberKey+"...", DeliveryTicketNum) 

Tim Reitz 10/30/2024: Have the following: 

  * Field: TicketNumStr (stored, to support legacy Member prefixes) 
  * Field: TicketNumNumeric



  


_VA: Matthias: I think we have an underlying Ticket Number Digits Only field, and the editable expression can be the Member Identifier Prefix + the Digits Only. The OnChange sets the member and the underlying Digits field to KeepOnlyDigits( NewValue). Give an error with an invalid member prefix.

_EM: Tim Reitz 10/22/2024: Does this still sound right?

Tim Reitz 10/30/2024: Reviewed with Ellis today. He's planning to clean up this spec when he does pricing.
