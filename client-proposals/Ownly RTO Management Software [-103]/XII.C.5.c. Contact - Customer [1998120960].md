12.3.5.3. Contact - Customer

The Contact record also includes the following custom section and fields for customer type contacts: 

  


  * SSN (custom; plain text; visible for non-organization customers; auto-formats with dashes; error on save if not nine digits long or contains invalid characters) 



Seth Miller 09/03/2025: TODO_Permissions. PII

  * Previous Account # (custom; plain text; visible for customer type contacts; validation against duplicate previous account #s for customers with the same rental company)



  


Contracts section

  * Contracts (virtual RG)
    * Contract #
    * Create Date
    * Status
    * Start Date
    * "View" link



  


  * Driver's License section (Visible if "Contact Type" = Customer and Customer is not an organization and the user has permission to "view PII")
    * License ID (text field)
    * State (droplist of states, required if License ID is specified.)
    * Upload Driver's License (link to upload image; only visible if no image is uploaded)
    * Download Driver's License (link to view/download image; only visible an image is uploaded)
    * Delete Driver's License (link to delete image; only visible an image is uploaded)



  


  * Helpful macros
    * ContactContractsToArray


