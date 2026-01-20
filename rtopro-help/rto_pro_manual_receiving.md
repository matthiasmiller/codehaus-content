# http://www.rtopro.com/help/rto_pro_manual_receiving.htm

# Inventory Receiving

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** RTO Pro Manual >

# Inventory Receiving

# 

|  [](rto_pro_manual_inventory_inquiry_and_maintenance.md "Previous Topic") [](welcome_welcome_1.md "Parent Chapter") [](rto_pro_manual_master_model_category_maintenance.md "Next Topic")  
---|---  
  
Inventory Menu Option "2"

[Watch a demo video on our website on how to receive inventory.](http://www.rtopro.com/index_videolb/player.swf?url=video/receiving_new.mp4&volume=100)

There are 2 types of inventory to choose from when you go into receiving, serialized or non serialized. Non serialized is for items that are not tracked individually, do not use this for items you want to depreciate or for items that you want to track the charge off the cost of when sold. For items that do not have an actual serial # if you want to be able to depreciate or track the item individually you should make up a serial # and load it as serialized. [See this topic for more info about non serialized inventory](non_serialized_vs_serialized_i.md). 

After selecting serialized or non-serialized a box will come up for model #. This box has accelerated recall which means as you type in characters a list will come up with previously entered model #âs listed alphabetically and the closest match alphabetically will be on the line you are typing in. If the model # you want comes up on the line your typing in push ENTER to accept that selection or if the model you want is in the drop down list you can push the down arrow to highlight your selection and ENTER to select. If the model you are typing in does not match a model # previously entered then you will be told that this is a new model # and you will be asked if you want to add it to the master model list. (See Master Model List below.) You can also select a model # from a complete list of Master Model #âs previously entered by pushing F5.

The next step after selecting a model is to enter the cost of the item, the invoice # and the Floor Plan Agent . (See [Special Considerations for Multiple Stores](rto_pro_manual_special_considerations_for_multiple_stores.md) and [Instructions for Setting up Depreciation](rto_pro_manual_instructions_for_setting_up_depreciation.md).) You can also change any of the default items for this model. After all information is entered push ENTER then you will be able to enter Serial #âs and Stock or ID #âs for each piece being received. You can receive as many as 20 pieces at a time. To receive the items push F6.

Master Model List

The master model list stores information about each model so that the next time you go to receive this model it will automatically fill in most of the information about the model in receiving. When you go to add a new model the first thing you do is select a Category. A category is a general description for this type of inventory like APPLIANCES, FURNITURE or VCR. You can have unlimited categories and sub categories. To create a new category see the section below. The categories are used in the BOR Report to show the breakdown of your BOR per category. The next thing you enter is a description for this model, this can be more specific than the category. Then you select if you want this model # to be listed as BOR and if it is Retail or Rental inventory. Remember what you enter here will come up automatically every time you receive this model from now on. You can edit the Master Model Record See [Master Model Maintenance](rto_pro_manual_master_model_category_maintenance.md).

Creating a new category

To create a new category push F5 when the category list is showing. This can be done when loading a new model # in master model or from the secondary receiving screen where it shows the category. To add a new category from the secondary receiving screen tab to the category field, push any key, then push F5. After pushing F5 the New Category screen will come up. Enter the category name then if you want it to be a sub category select the master for it from the list and click on the Make This a Sub Category of checkbox. Push Enter to save the new category.

Description of fields entered when receiving inventory:

Model: Model number of the inventory item. For items that do not have a model number you could make up a short descriptive one for it such as "SOFA" or "12x10 PORTABLE". Model numbers can be up to 15 alphanumeric characters.

What is a model number? A model number is the number or name the manufacturer uses to describe an item. For instance "Malibu" is a model of a car made by the manufacturer "Chevy", "TSP100" is a model number of a printer made by the manufacturer "Star". If you were are in the business you should be able to look at a model number and have some idea of what it is. There are usually lots of inventory items with the same model number, Chevy does not only make one car called "Malibu", they make thousands a year, each will have a model of "Malibu", and each will have another number that identifies each specific car, for cars that is a "VIN" number, for almost everything else that is a "Serial" number (see below).

Serial: Serial number for the inventory item. A serial number is normally a unique number that identifies each inventory item. For items without a serial number you should make one up or have RTO Pro auto-generate one by clicking on "Auto-generate serial number". Generally it is a number such as "100152". It can also contain letters such as "D4790Y". Serial numbers can be up to 30 alphanumeric characters.

Stock#: This is an optional number that is usually an internal number to track inventory. Stock numbers can be left blank and you can also have RTO Pro generate you stock #'s automatically (See Store Setup > Other Tab). Stock numbers can be up to 15 characters and can only be numeric characters (0-9).

Cost: This is what the item cost you, what you paid for it or what it cost you to manufacture it. This will be the basis for any depreciation.

Description: This can be up to 250 characters, an example could be "43" LCD TV WITH STAND". Note that the first 35 characters of the description is all that prints on contracts and many reports.

Invoice: This is the invoice # where you purchased the item. When you purchase inventory you will usually get an invoice for the purchase, the invoice number represents the order the item came from.

F/P Agent: The F/P Agent determines the depreciation type you wish to use for this item, most stores only need one F/P Agent and for example a store named "ACE Rentals" could use "ACE RENTALS" as the agent name. By using different agent names you can group inventory that needs to be depreciated with different depreciation methods, if you need this functionality. See [Instructions for Setting up Depreciation](rto_pro_manual_instructions_for_setting_up_depreciation.md) for more info about agents and depreciation.

Retail: This is the retail price you would sell this item for in a cash sale. (optional)

RTO$: This can be used 3 different ways, listed here from most common to least common.

(1) Not at all, leave it blank (RTO prices can be generated automatically by setting up category markups or an individual rate table for each item, see [Pricing Setup.](help_desk_pricingsetup.md)). 

(2) Can be used to hold the total contract amount for RTO (If you use it for the total contract you can use this field to generate prices when loading an agreement and on price tags using this field, make sure you check the appropriate box in store setup under the "Contract" tab if you wish to use this field this way, see [Pricing Setup](help_desk_pricingsetup.md).).

(3) You could use it just as a lookup reference such as "$10 WK 52 WKS". If used this way it would not fill in pricing on a contract automatically, it would only be on the inventory inquiry screen for your reference only.

Category: This is a general description of the kind of inventory, you can have as many or as few categories as you like. An example of a category could be "APPLIANCES", "FURNITURE", "ELECTRONICS", or you could get more descriptive and have separate categories such as "WASHERS", "DRYERS", "DISHWASHERS". You can run inventory and revenue reports by category so keep that in mind when you create your categories, anything that you need to know how much income you are getting should have a separate category. For instance if you want to know how much income you are getting on say DVD Players then you should make sure you have a category just for DVD Players.

You can also have categories with sub categories, such as "APPLIANCES:WASHERS". To create a category with a sub category first create the main category ("APPLIANCES"), then create the sub category ("WASHERS") as a sub of the main category.

Date Received: This is the date you receive it in your store.

Rental/Retail: Everything is generally loaded as retail if it is new, when it is rented out it is automatically changed to rental. When an item is listed as "RETAIL" it is not counted as idle BOR on the BOR Report.

Pieces (If group): If the inventory you are receiving is a group or has multiple separate pieces that are all going to have 1 model / serial / stock number enter the number of pieces here. For instance if you have a living room group that has couch, chair and coffee table all with the same model and serial number then the pieces would be 3.

B.O.R.: This stands for balance on rent (an industry term that really doesn't describe what it means). Total BOR represents the number of items you have on rent. If you receive an item and set BOR to "NO" it would not be counted toward the number of items you have on rent on reports that show BOR figures. Generally everything is counted as BOR except for maybe small items such as lamps or accessories.

Brand: This is the manufacturer or brand of the item.

Vendor: The vendor is the supplier you purchased the inventory from, for instance Kenmore could be the brand but Sears may be the vendor you purchased it from. Many shed rental companies use the vendor field to track what lot the building is at. Inventory reports can be ran based on vendor. To edit your Vendor list go to Inventory Menu > Master Model / Category > Click Function keys(menu at top left) > Edit Vendor List

Rental Rates grid: The rental rates grid (pictured below) allows you to enter the # of payments and the payment amounts that you wish to rent this item out for. Note this is only to be used when you wish to use individual pricing instead of category markup to determine payment amounts on this item you are receiving. If this is left blank pricing will default to pricing by Category Markup method.

Always start with the shortest term and then longer terms (# of payments) as you work down. You can list up to 6 different terms for monthly and weekly payments. See [Pricing Setup](help_desk_pricingsetup.md) for more info about how pricing works in RTO Pro.

![image31](image31.gif)
