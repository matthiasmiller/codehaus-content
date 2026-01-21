4.5. Order Entry1.0 WALKTHROUGH

Mindy Hilbert 12/23/2020: 

[[File:ASSIST PROJECTS-LIST OF DELIVERABLES.pdf]] 

  


Standard Configuration for All Dealers

  


  


  * Base Configuration
    * Base Price
    * Default Options, including free & discounted options (for example, 1 free, and 1 10% off ?????)
    *   * Options
    * Can be limited to specific building types
    * Can be priced by building size
  * Customizations/Add-Ons
    * Associated with an option (for example, a flowerbox is associated with a window)
    * 


  


>>> For each of these, allow manual per-dealer customizations based on the building and the original price

  


  


Per-Dealer Configuration

  


  


  


  


Per Order Configuration

  


  * Ability to discount base price by $ or %
  * Allow manual line-item adjustments



  


  * Delivery
    * Delivery -- Industry standard is 50mi included in the building, plus a per-mile charge (currently it's as the crow flies, because it's easy to calculate) --- not usually seen this discounteded
    * Give a manual out with line-item adjustment, or with a parsable expression
    * The hauling fee is % of base price --
      * manufacturer to dealer - 5% of base
      * manufacturer to customers - 10% of base
      * adjust the base price to
      * you have the delivery fee that's shown to the customer, but invoice it
      * for the hauler, they'll % of base price,
    * The hauling fee could be different from what the dealer charges...could be out-of-pocket to the company...



  


  


  


Matthias Miller 09/24/2020: Talk this through with Josh.

  


  


Test Folder

  * Customer Orders
  * Vendor Orders



Copy file path of primary folder into spreadsheet

  


  


  


  


Matthias Miller 09/21/2020: This is for a wholesale customer, not for a sales lot. A process for if it's a sales lot, and one for a wholesale ordr....

  * The RE is the retail version for the wholesale dealer buying it from them and selling it to the customer
  * This piece doesn't have the sales/payment options filled in yet.



  


  * The WH one is the one is intended to print out and email them out -- the invoice used to bill them, as well as a Bill of Lading with no prices on it, this gets posted in the building



  


Removed the thought of this Excel being at the retail solution. Not planning to put this there. Only using it internally. The steps are:

  * When you submit order, creates a confirmation that comes to them, that gets forwarded to the customer w/ all the proces
  * The Bill of Lading gets saved in Assist, comes to the builder, and puts into the building.



When it's built, where -Burman creates confirmation for final billing

  


  


  


  


Matthias Miller 09/28/2020: Basic record for building type (lengths it can be, widths it can be)

  


Option records...for example, WINDOW, can go on these types of types, at least these widths, some parameters given a building length, how many you can put on -- 

  


You have add-ons or something that are actually on the options (for example, flower boxes based on the window; can be sized according 

  


Some options have just 1 (floor), others can have multiple (windows), and some can be on multiple sides

  


  


  


Proposal:

  * Option
  * List of Types
  * List of add-ons and availability



  


Walls are an option on the base -- we also have to consider how this affects base pricing for delivery compensation

  


  


  


Matthias Miller 09/28/2020: Do options have different pricings per district?

Matthias Miller 09/28/2020: If so, this means we have to find the builder before we generate the price -- do the dealers have different markup options?

Matthias Miller 09/29/2020: This will be all the same on the manufacturing side.

Matthias Miller 09/29/2020: On the sales side, there will be:

  * Retail dealers (
  * Wholesale dealers (probably 25% reduction) -- but they may sell or mark up from there -- they buy the building, and they handle logistics
  * Corporate Dealers -- the guy on the lot gets paid for selling buildings
  * Commission Dealers -- 10% of every sale; everything else (hauling, etc) is handled by the manufacturer -- inventory is owned by the manufacturer
  * Everything will have a standard MSRP
  * On the dealer portal, they can set their markups and their pricing -- and can even call them by different names. And may want to adjust pricing on a per-dealer basis, for specific options (doors, flower box, etc)
  * Do we need dealer coupon code? Matthias Miller 09/29/2020: Duane doesn't have a clear sense of how we want to do this.....he is going to talk it through with Ivan
    * Minimum Base Price
      * % Discount
      * $ Discount
    * Free Options / Discounted Options /
    * Limit to building types
    *     * Per LeAnn, the latest conversation was that it would be based on square footage of the base...(experimental) -- most buildings = $20/sf, with larger buildings = $19/sf .. OR a designated price by size... this could avoid part of the issue w/ the base price and needing to adjust it
    * They could bill out some of these items, and add a manufacturer discount....
  * Pricing for on-site buildings
    * one price to 50, one to 100, etc



  


Matthias Miller 09/29/2020: Where does distance get calculated from?

  * Doing delivery based on dealership? What about presidential buildings and holding lots?
  * ShedsDirect are paying from manufacturer to holding lot, then holding lot to customer
  * At this point, the free mileage is coming from the holding lot
  * Matthias Miller 09/29/2020: Duane will be getting clarity, as far as what is the calculation point for transportation



  


Matthias Miller 09/29/2020: Haulers don't mind getting paid for traveling distances, as long as they're compensated.

Matthias Miller 09/29/2020: Email these questions to Duane

  


Matthias Miller 09/28/2020: Ask Duane, etc....

  


Matthias Miller 09/29/2020: Provide a virtual lot with each of the types of buildings... drill down by the type, then having a certain set of options...carousel of options

  * Start with A-Frame and Barn-Style ...
  * Matthias Miller 09/29/2020: How do customers think ... about buying it....what do you want to do w/ it?
    * Storage
    * Man Cave
    * She Shed
    * Etc



Matthias Miller 09/29/2020: Even for the dealers, we should have some default options (want to suggest buildings to be built a certain way, because it improves manufacturing process, etc.)

  


Matthias Miller 09/28/2020: Different pricing for differetn dealers -- flat X -- or some that are different per dealer -- or here's the default price, and this is how it's different (add ability to override --- don't want to copy prices for new builders)

Matthias Miller 09/28/2020: Is there an across the board configuration for dealers? 

  


  


  


Matthias Miller 09/28/2020: Tim and I will work on this...then review with Josh and do a screen mockup for ABC
