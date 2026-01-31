2.3. Changes for Coverages

*Documentation N/A

  


Entry Fees: The Solution can be set to use or not use Entry Fees for Collision/VLS and Cargo coverages, to be set on a Plan-by-Plan basis. If set to not use Entry Fees, only the annual Premium is charged to the clients. This is based on the following System Switches, which are set by CCI as part of the system setup:

  * Config_VPlanUsesColEntryFee
  * Config_VPlanUsesCargoEntryFee



  


Calculating Annual Premiums: The Solution can be set on a Plan-by-Plan basis to use different methods for calculating and charging Collision/VLS and Cargo annual premiums:

  * Flat fees
  * Percentage of the entered Coverage Amount
  * Flat Fee + percentage of the Coverage Amount



  


This is based on the following System Switches, which are set by CCI as part of the system setup:

  * Config_VPlanColPremiumUsesFlatFee
  * Config_VPlanColPremiumUses%
  * Config_VPlanCargoPremiumUsesFlatFee
  * Config_VPlanCargoPremiumUses%



  


Once the System Switches have been set appropriately, the flat fee amount and/or percentages are configured on the Vehicle Type records, and can be set differently for different Vehicle Types if desired. Note that annual premiums for Liability coverage always is a flat fee, which also is configured on the Vehicle Type records.
