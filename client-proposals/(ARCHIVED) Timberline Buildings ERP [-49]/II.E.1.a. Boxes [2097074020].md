2.5.1.1. Boxes

  


Requirements

The Box SKU category would be used to price the base product.

  


Each Box SKU has a base dimension (width and length). Jobs can extend the box by 2-foot increments. The additional length pricing will be based on 8-foot sections.

  


It would have a materials section with a list of material SKUs included in the building.

  


It would also include:

  * Labor Hours (with rate and total $ automatically calculated)
  * Equipment $
  * Overhead (% and $; automatically calculated)
  * Profit (% and $; automatically calculated)
  * Total Price



  


The Overhead and Profit %'s are calculated from the total price.

  


Development Specification

Total Price = (Material + Labor + Equipment) / (100% - Overhead% - Profit%)

  


TODO_IDD: We will probably need to have a way to update base building prices based on the calculations, since the SKU stores a fixed price.
