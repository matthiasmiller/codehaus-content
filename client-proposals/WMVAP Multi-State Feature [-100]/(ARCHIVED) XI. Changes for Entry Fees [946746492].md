11\. Changes for Entry Fees

_EM: Tim Reitz 07/24/2024: How to spec out these changes? Copy in the living spec notes and add blue like below? 

_VA: Tim Reitz 07/24/2024: Should be fine to add the visibility condition to the spec in parentheses. 

  


[X] The Solution can be set to use Entry Fees for Collision and Cargo coverages, or to not use Entry Fees (only charging the annual Premium). This is based on the following System Switches, which are set by CCI as part of the system setup:

  * Config_VehiclePlanUseCollisionEntryFee
  * Config_VehiclePlanUseCargoEntryFee



  


Items affected:

  * [X] Vehicle Type Record: Show/hide the following fields:  
    * Collision Entry Fee % (__; visible if the Solution uses Collision Entry Fee)
    * Cargo Entry Fee % (__; visible if the Solution uses Cargo Entry Fee)



  


  * [ ] Vehicle Types Report: Show/hide the following columns:  
    * Collision Entry Fee (%) (__; visible if Solution uses Collision Entry Fee)
    * Cargo Entry Fee (%) (__; visible if Solution uses Cargo Entry Fee)



  


  * [X] Vehicle Record:   
    * Vehicle Owner and Status section: 
      * Transferring Ownership Process: ___ 
        * _EM: Tim Reitz 07/24/2024: Do we need to have special handling to exclude Entry Fee details from the calculation? 
          * _VA: Tim Reitz 07/24/2024: "add Entry Fee if Solution uses __ Entry Fees"
    * Collision Coverage section: 
      * _VA: Tim Reitz 07/24/2024: "add Entry Fee if Solution uses Collision Entry Fees"
        * Tim Reitz 08/01/2024: Actually, I don't think there are any references to Entry Fees here. 
    * Cargo Coverage section: 
      * _VA: Tim Reitz 07/24/2024: "add Entry Fee if Solution uses Cargo Entry Fees"
        * Tim Reitz 08/05/2024: Actually, I don't think there are any references to Entry Fees here
    * Fees & Credits section: Show/hide the following:
      * "Entry Fee" list item on the "Fee Type" drop list for rows with "Coverage Type" = "Collision" (included if Solution uses Collision Entry Fee)
      * "Entry Fee" list item on the "Fee Type" drop list for rows with "Coverage Type" = "Cargo" (included if Solution uses Cargo Entry Fee)



  


  * [ ] Invoice Record: Show/hide the following: 
    * "Collision Entry Fee" list items in the drop list for Sales Items (included if Solution uses Collision Entry Fee)
    * "Cargo Entry Fee" list items in the drop list for Sales Items (included if Solution uses Cargo Entry Fee)



  


  * [ ] Income Report: Show/hide the following:
    * Collision Entry Fee Units column (visible if Solution uses Collision Entry Fee)  
      * _VA: Tim Reitz 07/19/2024: Note that we're reworking this report in [[[IN9647](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9649&)]] - ZWA - Income Report - Add Pane for Units. [so things might change]


