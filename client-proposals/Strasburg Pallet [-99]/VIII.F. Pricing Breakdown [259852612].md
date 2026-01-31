8.6. Pricing Breakdown

PART 1: Lumber Pricing

  


LUMBER RAW MATERIAL

  


Step 1: Round to Standard Dimensions

  * Actual dimensions → rounded up to Standard Dimensions (Actual) for pricing



  


Step 2: Determine Kerf %

  * Look up Kerf % for Pricing based on Dimensional Lumber vs Cants (from Lumber Size record; only calculated if priced using Board Feet With Kerf)



  


Step 3: Calculate BF for Pricing

  * Start with rounded dimensions from Step 1
  * If  the raw material is Dimensional Lumber, adjust the board footage based on Nominal Dimensions instead of Actual Dimensions
  * Apply Kerf %
  * (Only calculated if UOM is Board Feet With Kerf or Board Feet Without Kerf)



  


* NOTE: Mathematically, it doesn't matter whether we first adjust from Actual to Nominal Dimensions, or first we apply Kerf.

  


Step 4: Calculate # of Units

UOM| # of Units  
---|---  
Linear Feet| Length (from dimensions for pricing)  
Board Feet With KerfBoard Feet WIthout Kerf| BF value from Step 3  
Each| N/A (handled as total count in Other Material Costs)  
  
  


Step 5: Lumber $

Lumber $ = (# Units × $/Unit) + Setup Cost

  


LUMBER SAWING

  


Step 6: Calculate Sawing BF

  * Calculate the number of saws (include the sizer)
  * Multiply that by the actual board footage
  * ❓ TODO: Should this use rounded dimensions for pricing instead of actual?
  * ❓ TODO: With or without kerf?



  


Step 7: Sawing $

  * NOTE: Sawing has a blended rate that includes both labor and machine overhead:



Sawing $/BF = (Annual Sawing Labor + Annual Sawing Machine Cost) ÷ Annual Sawing BF Processed

  


  * Then:



Sawing $ = Sawing BF × Sawing $/BF

  


Step 8: Specialty Cuts

  * # Angle cuts × $/ea (including Angle cut setup time if used)
  * # Bevel cuts × $/ea (including Bevel cut setup time if used)
  * # Holes × $/ea (including Boring setup time if used)



  


Step 9: Total Raw Material + Sawing

= Lumber $ + Sawing $ + Specialty Cuts $

  


(NOTE: Panels priced by Each—handled in Part 3)

  


PART 2: Other Material Costs

Step 10: Additional Costs

  * Fasteners $
  * Heat Treating $
  * Panels $ (Each-based lumber)



  


PART 3: Assembly Pricing

Step 11: Setup Time / $

  * Base Setup Time
  * \+ MAX of adders for: Max Outside Dimension, # of Parts, # of Fasteners
  * × Assembly $/Hr (blended rate including labor + machine overhead)
  * ÷ Order Qty for Pricing (spread across units)



  


Step 12: Cycle Time / $

  * Trained formula → per-item cycle time (mins)
  * × Assembly $/Hr (same blended rate)



Assembly $/Hr = (Annual Assembly Labor + Annual Assembly Machine Cost) ÷ Annual Assembly Hours

  


PART 4: Final Overhead

Step 13: Non-Production Overhead

  * Covers: Occupancy, Admin, Insurance, Technology, Marketing/Sales, Employee Benefits, Transportation, Depreciation
  * Applied as a percentage on top of total cost:



Final Price = Total Cost ÷ (1 - Overhead %)

  


Open Questions

  * Sawing BF basis (Step 6): Actual BF or rounded/pricing BF?
  * Kerf in Sawing (Step 6): With or without kerf?
  * Pricing for Dimensional Lumber: Do you want to do this by linear feet or by nominal board feet? (i.e. 2x4 BF vs. 1.5x3.5 BF)


