6.9.2.3. Agreement - Billing Group Section

  * Billing Group section: 
    * Included Manged Devices (read-only embedded spreadsheet with the following; auto-populates with all Manged Devices linked to Managed Service Agreement:) 
      * Columns: 
        * Device ID (auto-filled and read-only; displays the Device ID from the Device)
        * Description (auto-filled and read-only; displays the Device Description from the Device)
        * Serial # (auto-filled and read-only; pulled from the Device)
        * Type (auto-filled and read-only; pulled from the Device) 
        * Managed (auto-set and read-only; displays "Yes" or "No" based on the Managed checkbox on the Device)
        * View (link; displays as "Link"; opens the corresponding Device record)
        * Install Date (auto-filled and read-only; current install date pulled from the Device; does not update on the Agreement if changed on the Device)
        * Initial Page Count (auto-filled and read-only; pulled from the Device)



TODO_IDD: update here once we have it clarified on the Device.

  * Prepay (auto-set and read-only; displays "Yes" or "No" based on the Prepay checkbox on the Device)
  * Monthly Base Price$ (auto-filled and read-only; pulled from the Device)
  * Included Black Pages (auto-filled and read-only; pulled from the Device)
  * Black Overage $ (auto-filled and read-only; number to 3 decimals; pulled from the Device; blank if the Agreement's Black Meter Type = Per Group)
  * Included Color Pages (auto-filled and read-only; pulled from the Device)
  * Color Overage $ (auto-filled and read-only; number to 3 decimals; pulled from the Device; blank if the Agreement's Color Meter Type = Per Group)
  * Needs Review (auto-filled and read-only; checkbox; pulled from the Device; if one or more Devices in the Billing Group for an Agreement have this checkbox checked, the Agreement is not included in the billing process)


  * Automatically sorted by: Device (alphabetically)
  * Buttons to insert/append/remove rows: N/A
  * Show 15 rows without scrolling



  


TODO_EM: Tim Reitz 10/03/2023: We're selecting the Agreement on the Device, and I think that's the cleanest data model since the only thing that needs to happen on the Agreement when a Device is added is sending the revised PDF. But I wanted to run it by you to confirm.

  


  


TODO_IDD: there should be line items for all of the Add-Ons, tied to their corresponding device

TODO_EM: Tim Reitz 08/31/2023: Should this be a column on the Billing Group RG? (maybe just comma-separated list?)?
