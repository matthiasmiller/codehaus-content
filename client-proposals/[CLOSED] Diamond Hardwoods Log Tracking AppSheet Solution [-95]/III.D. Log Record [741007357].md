3.4. Log Record

Overview: The Species record tracks information about log species, including the species-specific pricing for grades. 

  


Accessed via: 

  


Sections and Fields: 

  * Purchase Batch (auto-set and read-only??)
  * Tag # (filled from the QR code scan; might not have validations against duplicates) 



TODO_AP: Tim Reitz 11/05/2024: Could we have this be unique identifier for the Log record? 

  * Species (required; drop list of Species) 
  * Length (ft) (required; __; this is the length of the log in __)



_DD: feet + inches? 

TODO_AP: Tim Reitz 11/01/2024: Yes, feet + inches. 

Tim Reitz 11/04/2024: what options do we have for this? A combined field, or two separate fields. We would end up converting it to a decimal number for BF calculations. 

  * Diameter (in) (required; __; this is the diameter of the log in inches)



_DD: inches? 

TODO_AP: Tim Reitz 11/01/2024: Yes, inches. 

TODO_AP: Tim Reitz 11/01/2024: No cutback at this point. 

  * BF (auto-calculated and read-only; displays the board feet for the log, calculated via the following formula: "((D-4)^2*L)/16", where "D" = Diameter in inches and "L" = Length in feet (decimals); rounded to the nearest 1 decimal place)
  * Grade (required; drop list of Grades) 
  * Grade Rate $ (auto-set and read-only; number; 3 decimals; displays the Grade Rate for the selected Supplier + Species + Grade; this is the price per Board Foot for the log)
  * Log Value $ (auto-calculated and read-only; number; 2 decimals; displays the value of "BF" * "Grade Rate $"; rounded to the nearest 2 decimal places)  



  


Data Access: N/A (all users can access)

  


Special Considerations: TODO_AP: Tim Reitz 11/04/2024: Is this something to consider for AppSheet?  

  * Copy Record:
  * Delete Record:
  * Merge Record:



  


Other Notes:

  * N/A


