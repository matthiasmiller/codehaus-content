15.0.1. Settings

  


Requirements

Section: Current Period Start Year

Add a setting for the current period start year. 

  * Current Period Start Year (numeric field such as "2020")
  * Period Start Date (automatic; July 1 of the current period start year)
  * Period End Date (automatic; June 30 of the following year)



  


This will be used to determine the current period when printing cards, etc.

  


Section: Liability Fees

Include an embedded spreadsheet:

Liability Code| Annual Premium| Use Classes| Included Classes| Additional Classes ($)| Require VIN & License Plate  
---|---|---|---|---|---  
Auto (same as old system)| 150.00| [ ] |   
|   
| [X]  
Commercial Farm Equipment (new option)| 150.00| [ ] |   
|   
| [ ]  
Farm Equipment (formerly "FrmV")| 40.00| [ ] |   
|   
| [ ]  
Farm Truck (formerly "FrmT")| 150.00| [ ] |   
|   
| [X]  
Commercial Truck (formerly "TrkC")| 150.00| [X] | 3| 20.00| [X]  
  
  


NOTE: ATV will be removed.

  


Section: Collision Fees

  * Annual Fee $ (two decimals)
  * Entrance Fee % (two decimals)



  


Section: Cargo Fees

  * Annual Fee $ (two decimals)
  * Annual Fee % (two decimals)
  * Entrance Fee % (two decimals)



  


Section: Vehicle Transfers

  * Issue Invoices for Credits Over $ (two decimals)



  


Section: Compliance

This would be an embedded spreadsheet of:

  * Liability Code (optional; blank applies to any liability code)
  * Question
  * Statement if Yes
  * Statement if No



  


Murshid Rahman 10/15/2022: The design has changed. See AppHosting Settings and Vehicle Types detail screen.

  


Development Specification

Tim Reitz 08/19/2020: % of what? Same below x2

Matthias Miller 08/20/2020: % fees are calculated based on the coverage amount specified on the vehicle.

  


 Tim Reitz 08/19/2020: In Vehicles it says that Cargo has the same layout as Collision, but Collision does not include this option. Is this correct? 

Matthias Miller 08/20/2020: This is in regards to the Annual Fee %. Collision does not use that.

  


Ellis Miller 08/18/2020: 

  


Coverage Fields (1 day)

  


Compliance RG (1 day)
