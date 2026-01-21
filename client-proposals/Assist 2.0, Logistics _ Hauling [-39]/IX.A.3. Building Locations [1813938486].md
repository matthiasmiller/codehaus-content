9.1.3. Building Locations

The Building Locations will have additional columns:

  * Miles (number; 2 decimals)
  * Mileage Cost (number; 2 decimals)
  * Reimb $ (number; 2 decimals)
  * Invoiced Date (checkbox + date; default to today when checking it)



  


To calculate mileage cost:

  * Multiply the square feet by the AppHosting.zone Settings "Hauler Sq Ft Price"
  * Multiply the miles, the length of the building, and the AppHosting.zone Settings "$ / linear ft / mi"
  * Add them together, enforcing at least the Hauler Minimum based on the haul type


