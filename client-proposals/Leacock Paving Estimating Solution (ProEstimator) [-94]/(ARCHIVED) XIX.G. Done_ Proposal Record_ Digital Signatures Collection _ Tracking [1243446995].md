19.7. Done: Proposal Record: Digital Signatures Collection / Tracking

  


Requirements

The following feature could be added to facilitate digital signatures on Proposals sent to Customers. This would not be used for all Proposals, as some Customers would still sign paper copies. 

  


Estimated Cost: TBD once design is finalized, but ballpark estimates are included with the options below

  


Initial Spec / Ideas: 

  * Option 1: (Manual) Use a service such as Adobe Acrobat Sign or PandaDoc, separate from the ProEstimator Solution. Each Proposal record in ProEstimator would include a link to the eSignature service. The user would open this link, manually upload the Proposal Printout PDF to the service, and send it to the customer. Once signed, the user would document it in ProEstimator (check a checkbox and download a copy of the signed PDF and upload it into ProEstimator). 
    * [X] Add the following new custom System Switch:
      * Label: "Proposal eSignature URL"
        * Code: "ProposaleSignatureURL"
        * Field Type: Plain text
        * Description: "Specifies the URL for the eSignature provider for Proposals."
        * Value / set to: TBD
        * Other Notes: 
          * Editable
    * [X] Add the following to the Proposal record:
      * Open eSignature Service (link; visible if __; opens the eSignature provider used by Leacock Paving, based on the URL set in the "Proposal eSignature URL" System Switch (see corresponding spec))
      * Proposal Signed (checkbox + date, which toggle; visible if __; any user can set this to document when the signature was received)
    * [X] Additional Notes:
      * A copy of the signed Proposal printout can be uploaded via the existing "Documentation" feature for the Proposal (this is utilizing the existing features to avoid additional cost for the ; note that if an additional field is added to store the Proposal, it would incur additional cost)
    * [X] Ballpark pricing: 
      * Upfront: $300-500 
      * Annual Maintenance: N/A for Silverloom + any service provider charges



  


_VA: Tim Reitz 07/03/2025: Client wants to move forward with Option 1 for Phase 1.

  


  


  


  * Option 2: (Automated) Integration with a service such as Adobe Acrobat Sign or PandaDoc, via an API. Much more design would be required for this, but it would likely include the same "Proposal Signed" checkbox + date, which could be set automatically, and the signed Proposal could potentially be uploaded automatically as well.
    * Ballpark pricing: 
      * Upfront: $5,000-10,000 
      * Monthly Maintenance: $50-150 + any service provider charges



  


_VA: Tim Reitz 07/03/2025: Let's write up a CR for Option 2.

Tim Reitz 07/03/2025: Done here: [[[IN11673](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11675&)]] - ZLP - Consider Integration with eSignature Provider.

  


Development Specification

_EM: Tim Reitz 01/29/2025: There was a note in the HLD review call about doing digital acceptance: Send a link to the customer with the Proposal, for them to provide and e-signature. You mentioned that we're done this for other clients. (approx. 20:30 in the review call recording). What would this look like? 

Tim Reitz 05/14/2025: Maybe include just some basic details & price ballpark for now, to be specced out if/when needed. 

  


_PRICING: Tim Reitz 05/22/2025: I added the 3 "Ideas" above. Are all of those reasonable to put on the table?

Ellis Miller 05/06/2025: _VA: I changed it to TODO _PRICING and I' will discuss with Josh.

Tim Reitz 06/26/2025: Client sees this as a pretty important feature of the software, and would like a ballpark price.
