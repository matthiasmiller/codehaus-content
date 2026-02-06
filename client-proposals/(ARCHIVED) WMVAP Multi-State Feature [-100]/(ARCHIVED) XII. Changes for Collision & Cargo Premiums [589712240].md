12\. Changes for Collision & Cargo Premiums

_VA: Tim Reitz 07/26/2024: Add new items and visibility condition to the spec in parentheses. 

  


[X] The Solution can be set to use different methods for calculating and charging Collision and Cargo annual premiums:

  * Flat fees
  * Percentage of the entered Coverage Amount
  * Flat Fee + percentage of the Coverage Amount



  


This is based on the following System Switches, which are set by CCI as part of the system setup:

  * Config_VehiclePlanCollisionPremiumShowFlatFee 
  * Config_VehiclePlanCollisionPremiumShow%
  * Config_VehiclePlanCargoPremiumShowFlatFee 
  * Config_VehiclePlanCargoPremiumShow%



  


Once the System Switches have been set appropriately, the flat fee amount and/or percentages are configured on the Vehicle Type records, and can be set differently for different Vehicle Types if desired. Note that annual premiums for Liability coverage always is a flat fee, which also is configured on the Vehicle Type records.

  


  


Items affected:

  


  * Collision:
    * [X] Vehicle Type Record: Show/hide the following: 
      * Collision Premium $ (existing field; visible if Solution uses Flat Rate)
      * Collision Premium % (new field; visible if Solution uses Percentage; __



  


  * [ ] Vehicle Types Report: Show/hide the following:
    * Collision Premium ($) (existing column; visible if Solution uses Flat Rate)
    * Collision Premium (%) (new column; visible if Solution uses Percentage; __



  


  * [X] Vehicle Record:
    * Collision Coverage section: __
      * Existing "Premium" macro would stay and show the appropriate calculations for any of the 3 situations (Flat Rate or Percentage or Flat Rate + Percentage) 
        * _VA: Tim Reitz 07/24/2024: 1 for all 3
    * Fees & Credits RG: 
      * Amount: _Tim Reitz 07/24/2024: Let's clearly state in the spec for this field that it is prorated. 
  * Other??



  


  * Cargo:
    * [X] Vehicle Type Record:
      * Cargo Premium $ (existing field; visible if Solution uses Flat Rate)
      * Cargo Premium % (existing field; visible if Solution uses Percentage)



  


  * [ ] Vehicle Types Report:
    * Cargo Premium ($) (existing column; visible if Solution uses Flat Rate)
    * Cargo Premium (%) (existing column; visible if Solution uses Percentage)



  


  * [ ] Vehicle Record:
    * Cargo Coverage section:
      * Existing "Premium" macro would stay and show the appropriate calculations for any of the 3 situations (Flat Rate or Percentage or Flat Rate + Percentage) 
        * _VA: Tim Reitz 07/24/2024: 1 for all 3
    * Fees & Credits RG: 



  


  * Other??


