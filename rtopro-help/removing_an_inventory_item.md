# http://www.rtopro.com/help/removing_an_inventory_item.htm

# Removing An Inventory Item

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Removing An Inventory Item

|  [](help_desk_sql_strings.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](partial_payment_options.md "Next Topic")  
---|---  
  
Inventory items may be removed from a contract with the Remove Inventory Item button or by pushing Alt+R from contract maintenance.

To remove an item, you will be prompted to enter the line number of the item to remove (1-10). A box will pop up to show you the adjusted payment amount and contract amount, like in the image shown below.

![remove inventory item](hmfile_hash_509585c7.jpg)

After verifying contract changes are correct, select "Yes". This will close out the original contract as Returned and will create a new, adjusted contract with the remaining inventory items. The contract number for the new contract will be the same but with an "-A" added to it (the "A" being progressed alphabetically if it does not create a unique number). Any payments made on the original contract will still be accessible through the original contract History, but will not show in the History of the new "-A" contract. Instead, any previous payments will be factored into the new contract amount.

Please note that Club fees will have to be adjusted manually. You should print this new contract and have it signed.

An example of how a contract is changed when you remove an item:

Agreement terms, $20 a week for 52 weeks = 1040.00 contract amt

2 items $10 a week each

3 payments paid of $20.00 = $60 amt paid, 49 payments remaining.

If you remove one of the items the new agreement with the remaining item will have the following terms:

Agreement terms, $10 a week for 49 weeks = 490.00 contract amt

1 item $10 a week 

0 payments paid, 49 payments remaining.
