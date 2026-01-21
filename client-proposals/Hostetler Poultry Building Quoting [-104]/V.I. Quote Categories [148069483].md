5.9. Quote Categories

Quotes are broken down into multiple categories.

  


Parent Category (list of categories)

  * Example: "Bird Area Equipment > Chain Feeders > Chain Feeders for Layer"



  


Short Name (string)

  * Example: "Winching"



  


Full Name (read-only; Parent Category + Short Name)

  * Example: "Bird Area Equipment > Chain Feeders > Chain Feeders for Layer > Winching")



  


Siblings; embedded table (virtual):

  * Sort Order (editable for current item)
  * Short Name



  


Sort Order (integer; hidden)

  


Include on Cover Sheet (checkbox)

  


Cover Sheet Description (visible & editable if included on cover sheet; quote-level string expression; i.e. "50' x 500' x 9.25' Bird Area")

  


GC Fees (section)

  * Kit GC % (number; 2 decimals)
  * Turnkey GC % (number; 2 decimals)



  


Quantity Label (optional; list of Quote Quantity Labels; blank = no quantity adjustment)

  


Dimensions; embedded table of up to 3 dimensions editable by sales (such as Length, Width, Sidewall Height) and an indefinite number of other dimensions

  * Dimension (list of Quote Dimensions)
  * Editable by Sales (checkbox)



  


Allow customer to supply materials & labor (checkbox; used for concrete)

  


Variables (embedded table)

  * Variable Name
  * Expression (quote-level number expression)
  * *Used for things like "# of Trusses on buildings", etc



  


Example Categories Using Dimensions: These are some example categories that would use dimensions:

  * Egg Room (cooler room, offices, gathering area for packer; sometimes attached or not)
  * Manure Storage (sometimes attached or not)
  * Porch (always attached)
  * Generator Shed (sometimes attached or not)
  * External Service Room (always attached)
  * Bird Area (embedded/inside)



  


Example GC Fees

Category  
| Kit GC %| Turnkey GC %  
---|---|---  
Equipment| 1.5%| 2.5%  
Building | 5%| 5%  
Concrete|   
| 3.5%  
  
  


  


Notes:

  * When renaming, trigger a rename of all descendent categories
  * *NOTE - The Center dimension in the quoting spreadsheet can be handled separately as either sub-items or alternative items.
  * NOTE - The Amish checkbox will a quote item that is not printed on the visualizer sheet.


