4.8.2.2.1. Replacing Device Under Warranty Child Screen

Overview: If a Device is replaced under warranty, the second Device's warranty is a continuation of the first. This doesn't happen often but if a Device needs to be replaced under warranty, the User will click the Replace Under Warranty button, which opens this child screen with the following prompts:

  


  * New Device Serial # (required; plain text field; long enough for 20 characters; any validation errors will be displayed after the button is clicked)



TODO_EM: Ben Reitz 08/31/2023: Confirm this behavior for validation errors.  

  * Install Date (required; date field)
  * $0.00 Invoice Needed? (checkbox; defaults to unchecked)
  * Initial Invoice Number (visible if "$0.00 Invoice Needed?" checkbox is checked; optional; plain text field)
  * "Click Continue to create a copy of this Device Record for the new Device, deactivate the old Device, and update the Managed Service Agreement." (message displayed above the Continue button)
  * Continue (button; runs the Replace Device Under Warranty background process - see the details in the corresponding section of the proposal)



  


Other Notes:

  * The $0.00 invoice is only needed for replaced devices when Think Ink provides the replacement device on their own dime (not if the manufacturer provides it under their warranty) 
  * The new Device is automatically added to the same Agreement that the old Device was part of since the Agreement is selected on the new Device record.


