13\. Design Notes

_VA: Tim Reitz 08/02/2024: Changing "Collision" references: Let's make sure to follow up with changes to the ZWI spec based on the changes that we're making in [[[IN10155](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10157&)]] - ZWA - Minimize usage of "collision" (Main Job / Instances in Solution) and related jobs. 

Tim Reitz 08/28/2024: Checked in with the ZWA client to see what timeline they would like for the wording changes (email: Timeline & gameplan for "Collision" terminology changes). 

Tim Reitz 08/28/2024: Moving these notes to another section to keep working on them. 

  


_EM: Tim Reitz 07/24/2024: Should we come up with (in connection with PA) a generic name for this Solution? 

_VA: Tim Reitz 07/24/2024: Sure, let's check with the ZWA client & come up with some ideas. 

 DONE_Bruce: Tim Reitz 07/26/2024: Ben, could you send Bruce an email about this?

_VA: Tim Reitz 08/01/2024: Let's consider possible names. Not Weaverland specific.

Tim Reitz 08/21/2024: Sent some to the ZWA client today (email: Software names). 

  * Auto/Aid Plan Manager ("AMS)
  * Auto/Aid Plan Management Software/System/Solution ("APMS")
  * Vehicle Aid Plan Manager 
  * AutoAid Software 
  * DriveCare Software 
  *   * Vehicle Aid Plan Management System 
  * Mutual Benefit Vehicle Aid Plan Manager 
  * SIManager
  * SI Auto Manager 
  * SI Auto Plan Manager 
  * Self-Insured Plan Management System 
  * Vehicle Self-Insured Plan Manager 
  * VSI
  * AidPlan Manager
  * Vehicle Aid Plan Manager 
  * VAP Pro 



Tim Reitz 08/21/2024: The ZWA client replied with this suggestion: 

  * Self Insured Vehicle Management / SIV Management / SIVM



I think calling it the "Self-Insured Vehicle Management Solution" or "SIVM" for short could work. 

  


_VA: Tim Reitz 07/18/2024: What about the "Collision" terminology? PA is looking to move away from that...

_ES: Tim Reitz 07/24/2024: Ben, could you send Elvin an email about this?

_VA: Tim Reitz 07/31/2024: Client thinks they will follow PA's lead on the terminology.

  


  


Silverloom Settings:

TOD_EM: Tim Reitz 07/18/2024: I think we'll want a new section in Silverloom Settings called "State-Specific Settings" or "Organization-Specific Settings". This would include settings that we're discussing below for coverages, as well as official name, address, phone number, email, etc.

  * Plan-Specific Settings section
    * Plan Name (
    * Plan Address:
      * Street Line 1 (
      * Street Line 2 (
      * City (
      * State (
      * Zip (
    * Plan Phone (
    * Plan Email (
  * 


  


System Switches:

TOD_VA: Tim Reitz 07/18/2024: For settings that should be shipped (on a per-plan basis), let's use system switches.

  * Policy #: 
    * Config_VehicleExportedPolicyNum -- string expression evaluated on the vehicle
      * TOD_VA: Tim Reitz 07/18/2024: This sets the approach for the Policy # (one for the whole Plan, or one for each member). 
      * Read-only and hard-coded on a per-plan basis. Configured by CCI for deployement.
      * Can be either one number for the whole policy or one number for each member.
      * TOD_VA: For spec: In the deployment section, note which way it should be configured for each Plan.
  * Insurance Card: 
    * Config_VehicleCardPlanName 
      * TOD_VA: Tim Reitz 07/18/2024: This is the "SI 15 Weaverland..." on the PA Insurance Card...
      * TOD_VA: For spec: In the deployment section, note which way it should be configured for each Plan.
    * Config_VehicleCardRightOfPlanName 
      * TOD_VA: Tim Reitz 07/18/2024: This is the "NAIC No..." on the PA Insurance Card....
      * TOD_VA: For spec: In the deployment section, note which way it should be configured for each Plan.
    * Config_VehicleCardCoverageDisplay 
      * TOD_VA: Tim Reitz 07/18/2024: This is the coverage amount on the PA Insurance Card...
      * TOD_VA: For spec: In the deployment section, note which way it should be configured for each Plan.
  * Vehicle Plan: 
    * Config_VehiclePlanUseCollisionFee
      * TOD_VA: Tim Reitz 07/18/2024: This determines whether or not the whole system uses Collision Entry Fees. 
    * Config_VehiclePlanUseCargoFee 
      * TOD_VA: Tim Reitz 07/18/2024: This determines whether or not the whole system uses Cargo Entry Fees. 
    * Config_VehiclePlanCollisionPremiumShowFlatFee 
      * TOD_VA: Tim Reitz 07/18/2024: This determines whether or not the system includes Flat Fee options for Collision Premium (for PA this would would be set to true; for WI it would be set to false)
    * Config_VehiclePlanCollisionPremiumShow%
      * TOD_VA: Tim Reitz 07/18/2024: This determines whether or not the system includes Percentage  options for Collision Premium (for PA this would would be set to false; for WI it would be set to true)
    * Config_VehiclePlanCargoPremiumShowFlatFee 
      * TOD_VA: Tim Reitz 07/18/2024: This determines whether or not the system includes Flat Fee options for Cargo Premium (for PA this would would be set to true; for WI it would be set to false)
    * Config_VehiclePlanCargoPremiumShow%
      * TOD_VA: Tim Reitz 07/18/2024: This determines whether or not the system includes Percentage options for Cargo Premium (for PA this would would be set to true; for WI it would be set to true)



  


  


  


  * Entry Fees: WI (and the other Midwest groups) do not charge an Entry Fee for Collision and Cargo coverages.
    * _VA: Tim Reitz 07/18/2024: This is based on the System Switches. This would show/hide the following:
      * Vehicle Type Record:
        * __
      * Vehicle Types Report:
        * __
      * Vehicle Record:
        * Collision Coverage section
          * __
        * Cargo Coverage section
          * __
        * Fees & Credits RG
          * Exclude "Entry Fee" from the "Fee Type" drop list for Collision and Cargo
          * __
      * Other?



  


  


  


  * Coverage Premiums:
    * Liability: Same as PA; $150
      * Tim Reitz 07/18/2024: This is configured on the Vehicle Type record and defaults to blank for new records. No change needed here.



  


  * Collision: WI simply charges a % of the Collision Coverage Amount (currently 4%)
    * Would want the ability to configure this.
    * TOD_VA: Tim Reitz 07/18/2024: This is based on the System Switches. This would show/hide the following:
      * Vehicle Type Record:
        * If Flat Rate: Show only existing "Collision Premium $"
        * If Percentage: Show only new "Collision Premium %"
      * Vehicle Types Report:
        * If Flat Rate: Show only existing "Collision Premium ($)"
        * If Percentage: Show only new "Collision Premium (%)"
      * Vehicle Record:
        * Collision Coverage section:
          * Existing "Premium" macro would either stay and show the appropriate calculations or we would have two macros, one for CollisionFlatRatePremium and one for CollisionPercentagePremium, conditionally visible.
      * Other??



  


  * Cargo: WI simply charges a % of the Cargo Coverage Amount (currently 2%)
    * Would want the ability to configure this.
    * TOD_VA: Tim Reitz 07/18/2024: This is based on the System Switches. This would show/hide the following:
      * Vehicle Type Record:
        * If Flat Rate: Show only existing "Cargo Premium $" and "Cargo Premium %"
        * If Percentage: Show only new "Cargo Premium %" (or simply show and use just the existing % field??)
      * Vehicle Types Report:
        * If Flat Rate: Show only existing "Cargo Premium ($)" and "Cargo Premium (%)"
        * If Percentage: Show only new "Cargo Premium (%)" (or simply show just the existing % column??)
      * Vehicle Record:
        * Cargo Coverage section:
          * Existing "Premium" macro would either stay and show the appropriate calculations or we would have two macros, one for CargoFlatRatePremium and one for CargoPercentagePremium, conditionally visible.
      * Other??



  


  


  * WI offers the option to decrease the Coverage Amount over time
    * This is important because the annual fee is based on the Coverage Amount.
    * The current workaround is to essentially cancel the existing coverage and reactivate the coverage for a different amount.
    * This is most easily done at the turn of the period year, rather than mid-year.
    * How should we handle this more effectively?
      * _ES: Tim Reitz 07/18/2024: It looks like our system will already handle this cleanly, as it requires the user to deactivate the coverage before changing the Coverage Amount. It then handles all of the calculations automatically and prepares the fees and refunds to be invoiced.



  


  


  * Policy #: Controlled via system switch.
    * PA: One policy number for the whole plan together.
    * WI: One policy number per member/client
      * TOD_ES: Tim Reitz 07/18/2024: What is the format for this number? Sequential?



  


  


  


  * Existing Authorized Signature (
    * TOD_VA: Tim Reitz 07/18/2024: Remove this memo from AppHostin.Zone Settings, and have it stored on file, on a Plan-by-Plan basis.



  


  * Logo:
    * TOD_VA: Tim Reitz 07/18/2024: Let's have it stored on file, on a Plan-by-Plan basis.


