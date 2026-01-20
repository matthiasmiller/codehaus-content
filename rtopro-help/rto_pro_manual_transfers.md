# http://www.rtopro.com/help/rto_pro_manual_transfers.htm

# Transfers

<< [Click to Display Table of Contents](index.md) >> **Navigation:** RTO Pro Manual >

# Transfers

|  [](rto_pro_manual_non_serialized_cost_of_sale.md "Previous Topic") [](welcome_welcome_1.md "Parent Chapter") [](rto_pro_manual_depreciation_agent_setup.md "Next Topic")  
---|---  
  
Inventory Menu Option "9"

This is to transfer inventory from one store to another in multiple store operations. If the store # in STORE SETUP is set to zero you cannot use this feature.

First select transfer out or transfer in. See the description of each below.

Transfer Out: A screen will come up with an empty list on it and a drive selection box. The drive is for which disk drive on the computer you want the transfer data put on. This is so the disk can be taken to the store the inventory is going to be transferred in. Make sure the drive is correct then push ENTER to begin adding to the list. The inventory search screen will come up select the inventory you wish then it will be added to the list. To continue adding to the list push ENTER, to remove an item from the list hit DEL when the item is highlighted. To complete the transfer hit F12. The inventory records will be deleted from this stores inventory records and all information will be put on the disk to transfer to the other store.

Transfer In: You will be prompted to insert the transfer disk in the drive and select the drive letter, then push F5. A list of the inventory on the transfer disk will come up. Select the items coming to this store by pushing the space bar. Then hit F12 to complete. All inventory detail information from the other store on these items will now show in your store.

Note that you can transfer out to more than one store, each store can select what items they are getting off the list, the items will be removed that are selected and the remaining ones will stay on the disk for the next store to select from. A store that is being transferred to can also transfer items out to the same disk. Think of it like a truck one store can put 5 TVâs on it the truck can go to another store, that store can take 2 TVâs off the truck then put 3 TVâs on the truck, then the truck can go to another store and that store can take the six remaining TVâs off the truck.

Important Note: If you are storing the transfer file on a hard drive you should delete the file after successfully copying to a removable disk or transferring the file to a remote store. If the file is not deleted and subsequent transfers are performed saving the transfer file to the same location the transfer file will contain the old inventory that was transferred previously as well as the new inventory.

Transfers by FTP: If you perform transfers by FTP transfer the sending and receiving of the transfer files are automated, you simply enter the store number the transfer is for and the file will be sent to the correct store automatically. The store transferring in can click a button to sync their transfers files (check for any pending transfer files for them and send any pending files from them) any incoming transfer files will be listed for transfer in.
