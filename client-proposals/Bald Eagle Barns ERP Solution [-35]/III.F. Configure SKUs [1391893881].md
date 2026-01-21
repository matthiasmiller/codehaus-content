3.6. Configure SKUs

  


Requirements

SKUs will be managed on AppHosting's existing Inventory Management module, with some customizations. 

  


SKUs will be used to track Building Styles, Options, and Materials (see corresponding sections in this proposal). Each of these three categories of SKUs will use a separate "SKU Category". 

  


All SKUs will have the following fields (plus possibly some other standard ones):

  * Is Active (checkbox; defaults to filled) 
  * SKU (required; plain text field; validate against duplicates; this is the "code")
  * Description (required; plain text field)
  * Category (required; drop list of the following options:)
    * Materials
    * Options 
    * Building Styles 
  * UOM (required; drop list of the following:)  
    * Piece 
    * Linear Foot 
    * Square Foot 
  * Sales Price (required; number with up to 2 decimal places; to be used as the Sales Price for all Items; see details below:)
    * For Materials SKUs: Changes to the Sales Price should be updated on all current and future Work Orders/Sales Orders/Buildings EXCEPT for those with a status of Built/Done/Sold and beyond. See also Work Orders documentation.
    * For Options SKUs: This would normally be the same as the Options PWBP. Changes to the Sales Price should be updated on all current and future Buildings and Sales Orders EXCEPT for those with a status of Sold or beyond
    * For Base Building SKUs: This is called the "Building Base Price" throughout the proposal. It is used as the customer price for the building without additional options; changes to the Sales Price should be updated on all current and future Buildings and Sales Orders EXCEPT for those with a status of Sold or beyond)  
  * Cost (optional; number with up to 2 decimal places; would mainly be used for Materials SKUs)
  * Notes (section/memo)



  


Data Access: Editable by Full Admin only

  


Other Notes: 

  * Active SKUs cannot be deactivated if they are being used by one or more of the following: 
    * Active sold, unbuilt Building records
    * Active Building Styles SKUs 
    * Active Material SKUs 



  


*Done.

  


Development Specification

SkuCategoryList will become a lookup type for the standard module. 

Tim Reitz 08/11/2021: We can't remember why we wanted to make it a lookup type. We need to figure out why / whether we actually need to do this.

  


Mockup: Included with the SKU category mockups.
