19.4.0.1. Silverloom-Supplied Lead Source Records

  


Requirements

_EM: Tim Reitz 06/18/2025: Note that I've added spec for these to the "Lead Source Record" main spec, based on your comments below and our conversation today. Planning to archive this section once you see this note. 

  


  


  


The following Lead Source item(s) are hard-coded and included in the system automatically, with the "Name" field read-only and any other fields editable: 

  


  * "Previous Customer": 
    * Explanation: This lead source is used for times when a lead has been a customer of Leacock Paving in the past. 
    * Spec:
      * Lead Source section:
        * Active: Checked (editable)
        * Name: "Previous Customer" (read-only)



  


  * "Referral": 
    * Explanation: This lead source is used for times when a lead has been referred to Leacock by another party (another customer, etc.). 
    * Spec:
      * Lead Source section:
        * Active: Checked (editable)
        * Name: "Referral" (read-only)



  


  * "Other": 
    * Explanation: This lead source is used for times when the a lead gives a reason that isn't on the Lead Sources list, especially one that isn't worth adding to the list.
    * Spec:
      * Lead Source section:
        * Active: Checked (editable)
        * Name: "Other" (read-only)



  


Development Specification

_VA Ellis Miller 06/02/2025: Minor note -- if shipped list items are completely default records (besides name which is in the list), then we don't have to spec out the individual shipped records. Not a big deal either way.

\\_PRICING: Tim Reitz 06/11/2025: Got it, makes sense. 

\- On a related note, I saw your commend here in the dev spec about having these be Investortools-owned list items. What if this record ends up being expanded in the future, to include more fields that would need to be specced out for shipped records? Is it straightforward enough to switch to shipped records at that point? 

_VA Ellis Miller 06/18/2025: We can switch later.

  


\- Also, should I remove referenced to these being "shipped", or just keep that as generic terminology for hard-coded records/items?  

_VA Ellis Miller 06/18/2025: Avoiding shipped is nice. Maybe Silverloom-supplied records or Records for Silverloom list items or for readonly list items.

  


Ellis Miller 06/10/2025: 

[ ] Just make these Investortools-owned list items, not shipped records.

Included above
