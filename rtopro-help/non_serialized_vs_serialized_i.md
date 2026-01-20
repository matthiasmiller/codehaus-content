# http://www.rtopro.com/help/non_serialized_vs_serialized_i.htm

# Non Serialized VS Serialized Inventory

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Non Serialized VS Serialized Inventory

|  [](exporting_data_from_rto_pro.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](late_fees_by_state.md "Next Topic")  
---|---  
  
This topic will explain the differences between serialized and non-serialized inventory. Non-serialized means more than just an item that does not have a serial number, if you are receiving items without a serial number you should review the differences below and decide if you want to use serialized or non-serialized. If you decide to receive items as serialized that do not have a serial number you can always make one up or have RTO Pro generate serial numbers for you.

Serialized inventory

* Can be tracked individually.

* You can see where each one has been, a complete history of transactions.

* You can see how much income each one has.

* Can be depreciated in RTO Pro.

Non-serialized

* Can NOT be tracked individually.

* You can NOT see where each one has been, there is no complete history of transactions for each individual item.

* You can NOT see how much income each one has.

* Can NOT be depreciated in RTO Pro.

Think of non-serialized like cans of soup at your favorite grocery store. They do not track each can individually and there is no unique number on each can, they all have the same UPC number. The grocery store does not care where can #4 went, they only care about quantity, they purchased 100 cans and sold 4 so they should have 96 left. This is the way non-serialized works in RTO Pro, you start with the quantity you receive and as you sell or rent them the quantity on hand is reduced. You can have 1000 of the same non serialized item and they are all represented by 1 inventory record that says the quantity is 1000.

To get your cost of sale for non-serialized inventory, since they cannot be depreciated you would either run a "Non serialized Cost of Sale" report, inventory menu option 8 or you would expense them when you purchase the items instead of when you sell them.
