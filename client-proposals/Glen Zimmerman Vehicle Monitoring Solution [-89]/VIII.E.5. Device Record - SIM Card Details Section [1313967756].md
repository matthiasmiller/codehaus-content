7.6.5. Device Record - SIM Card Details Section

*Done. 

  


  * SIM Card Details section (visible if "Device Type" = "OBD-II"):
    * ICCID (required; number; 0 decimals; wide enough for 20 digits; used to document the unique ID for SIM, which can be found below the barcode on Hologram SIMs)
    * SIM Name (read-only macro; displays the contents of the "Device ID" for the current record; for the user to set as the SIM Name in Hologram; note that in the future, this could be set in Hologram automatically)
    * Security Sticker Code (optional; plain text field; this can be used to document a code on a security sticker that is placed over the SIM slot on the OBD)
    * Manage SIM Card (link; opens the URL specified in the "Manage SIM Card URL" System Switch; this allows the provider easy access to log into the online account to manage the SIM card) 



  


  


  * Other Notes Regarding SIM Management for Phase 1:
    * For Phase 1, the <Service Name> main office would manage SIMs and the Hologram account. The SIM management workflow would look something like the following: 
      * Main office orders SIM cards from Hologram (may be in bulk)
      * Main office activates the SIM cards and pairs them with OBD Devices, documenting in the <Service Name> Solution 
      * When a Reseller or Group Admin request devices, the main office pulls OBD devices from inventory, sets the "Assigned Reseller" in the Solution, and passes the devices with the SIM cards (probably already installed) on to the Reseller / Group Admin. 
      * This would not be a "bring your own SIM" service. 
      * At some point in the future, "organizations" could be set up in the Hologram account, to give the Resellers access to manage SIMs for the Devices that they manage. See the following notes from some research on Hologram's features: 
        * Each account can have multiple "organizations". 
        * Each "organization" has a name and can track logins with varying permissions - this could work well for the Resellers to manage SIMs for their own devices. 
        * Resellers would have the ability to add additional SIMs, pay for the SIMs under their management, etc. 
        * SIMs can be transferred from one "organization" to another. 
    * Hologram offers batch pricing (they call it "custom" pricing) -- see [https://www.hologram.io/pricing/](https://www.hologram.io/pricing/). Notes from the Hologram website: 
      * Data pools
      * Custom network configurations
      * Zero fees for inactive SIMs
      * Multi-year prepaid
    * At some point, we could consider adding the "Device Name" to the SIM Name, in addition to the "Device ID". This could be done when Resellers are given access to Hologram, or when an API integration is set up with Hologram.


