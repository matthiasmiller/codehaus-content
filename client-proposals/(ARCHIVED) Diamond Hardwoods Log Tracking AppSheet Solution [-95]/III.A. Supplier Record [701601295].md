3.1. Supplier Record

Overview: The Supplier record tracks information about log sellers / suppliers, including the supplier-specific pricing for grades. 

  


Accessed via: 

  


Sections and Fields: 

  * Name (required) 



TODO_AP: Tim Reitz 11/01/2024: client would like to be able differentiate between individuals & businesses. Is this hard in AppSheet? 

  * Description (optional; plain text field) 
  * Default Location (optional; address) 
  * Pricing fields (repeat for as many grades as there are): 
    * Grade G1 $/BF (required; number; 2 decimals) 
    * Grade G2 $/BF (required; number; 2 decimals) 
    * Grade G3 $/BF (required; number; 2 decimals) 
    * Grade G4 $/BF (required; number; 2 decimals) 
    * Grade G5 $/BF (required; number; 2 decimals) 
    * Grade G6 $/BF (required; number; 2 decimals) 
  * TODO_AP: Tim Reitz 11/01/2024: Possibly also a grade description. (TBD)
  * TODO__ Also would need to account for per-Species pricing. 



  


  


Data Access: N/A (all users can access)

  


Special Considerations: TODO_AP: Tim Reitz 11/04/2024: Is this something to consider for AppSheet?  

  * Copy Record:
  * Delete Record:
  * Merge Record:



  


Other Notes:

  * N/A


