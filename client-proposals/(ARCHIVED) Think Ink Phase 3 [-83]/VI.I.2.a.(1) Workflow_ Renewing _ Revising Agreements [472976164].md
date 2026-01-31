6.9.2.1.1. Workflow: Renewing / Revising Agreements

The following changes count as a revision to a Manage Service Agreement record (updating the Current Revision Date):

  * Renewing the Agreement
  * Adding a Device
  * Deactivating a linked Device
  * Unlinking a Device
  * Adding an Add-On to a Device on the Agreement
  * Removing an Add-On from a Device on the Agreement
  * Changing any of the following for a Device on the Agreement:
    * Monthly Service Plan
    * Monthly Base Price
    * Included Black Pages
    * Included Color Pages
    * Terms
    * TODO_JM (once we have updated the mockups)
  * Changing any of the following on the Agreement:
    * TODO_JM (once we have updated the mockups)



  


  


Renewing Agreements:

  * A month before the Renewal Date on the Agreement, the automated Upcoming Agreement Renewal Notice email gets sent to the customer. At the same time, the Agreements Needing Renewal user notification is displayed for the Sales Rep linked to the Agreement Needing Renewal.
  * That Sales Rep should open the Agreements Needing Renewals report and review all of the Agreements Needing Renewal.
  * If an Agreement is ready to be renewed without revisions:
    * the Sales Rep will click the "Renew Agreement" button on the Agreement record.
    * this runs the Renew Agreement background process (see details in the Background Process section of this proposal)
  * If an Agreement needs revisions before being renewed:
    * the Sales Rep will make the necessary changes to the Agreement record and/or Device records
    * the Sales Rep will communicate directly with the Customer about the changes and get the Customer's approval
    * once the Customer gives their approval, the Sales Rep will click the "Renew Agreement" button on the Agreement record
    * this runs the Renew Agreement background process (see details in the Background Process section of this proposal)



  


Revising Agreements:

  * Any time a change is saved on an Agreement record or a linked Device record that constitutes a revision to the Agreement, the Agreement Revision background runs (see details in the Background Processes section of this proposal) 
    * Note that if multiple changes are made on the same day, the Revision Date stays the same and the PDF in the folder is overridden



  


TODO_EM: Ben Reitz 09/19/2023: are you fine with all of the above?
