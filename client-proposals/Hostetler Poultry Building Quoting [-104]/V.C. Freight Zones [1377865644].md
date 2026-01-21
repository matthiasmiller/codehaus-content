5.3. Freight Zones

  * Name: string (auto-generated, read-only) Format: "Zone {Zone Number} ({Min Miles}-{Max Miles} miles)" OR "Zone {Zone Number} ({Min Miles}+ miles)" OR Example: "Zone 2 (101-300 miles)" OR "Zone 5 (751+ miles)"
  * Zone Number: integer (required)
  * Min Miles: integer (required)
  * Max Miles: integer (optional)
  * Base Price (number; 2 decimals)
  * Cost / Mile (number; 2 decimals)
    * TODO_HS - Earl will get us the spreadsheet OR confirm the pricing structure



  


NOTE: Warn if:

  * The mileage range overlaps with another freight zone.
  * The minimum miles is non-zero, and there's no other freight zone with a Max Miles that is 1 below the current freight zone's minimum.
  * The maximum miles is non-zero, and there's no other freight zone with a Max Miles that is 1 below the current freight zone's minimum.



  


Example Records

#  
| Name| Min. Miles| Max. Miles| Notes  
---|---|---|---|---  
0| Zone 0 (0-30 Miles)| 0| 30| Enforces min. freight  
1| Zone 1 (31-100 miles)| 31| 100|   
  
2| Zone 2 (101-300 miles)| 101| 300|   
  
3| Zone 3 (301-500 miles)| 301| 500|   
  
4| Zone 4 (501-750 miles)| 501| 750|   
  
5| Zone 5 (751+ miles)| 751| 9999|   
  
  
  

