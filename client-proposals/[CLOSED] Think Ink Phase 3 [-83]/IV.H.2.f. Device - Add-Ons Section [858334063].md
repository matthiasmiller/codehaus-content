4.8.2.6. Device - Add-Ons Section

  * Add-Ons section (visible if Type is or previously was "Leased Printer" or "Leased Other")
    * Included Add-Ons (embedded spreadsheet with the following:) 
      * Columns: 
        * Description (required; drop list of Add-ons for the selected Model; defaults to blank)
        * Monthly Charge (required; number field with 2 decimals; default to the Default Monthly Charge on the selected item from the Model record; editable to allow overriding the default if desired)
        * Install Date (required; date; defaults to the current date) 
        * Billing Start Date (required; date; defaults to the ___



TODO_IDD: Tim Reitz 09/07/2023: Round to the nearest 1/4 month in the future, same as the Devices. Update here once we have details finalized there. 

  * Automatically sorted by: alphabetically
  * Buttons to add / remove rows ("+" / "-")
  * Show 6 rows without scrolling 
  * Other Notes: 
    * Note that changes to the editable fields will not be tracked directly on the record (though they can be retrieved from Modification History). 



  


Other Notes:

  * When an Add-On item is added to or removed from a Device, it results in a revision to the Agreement (since Add-Ons are included in the Agreement itemization).



  


Other Notes for Phase 4:

  * Any items included with the Device should be included on the initial invoice as separate line items & $0.00 charges.
  * For the monthly invoice, the total could just be lumped together (would not need to include line items for the add-ons)


