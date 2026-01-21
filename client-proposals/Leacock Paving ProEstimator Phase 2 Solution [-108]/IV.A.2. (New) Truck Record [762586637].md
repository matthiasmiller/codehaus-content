4.1.2. (New) Truck Record

  


Requirements

This tracks the trucks in your fleet so they can be assigned to crews on the daily dispatch sheet, replacing the manual tracking you're doing in Excel.

  


Sections and fields: 

  * Name (automatic & read-only; Tk#116 Optional Desc)
  * Active (checkbox)
  * Truck # (number; 0 decimals; required; must be unique)
  * Description (string)



  


Note that this could be combined with Trailer Record and Equipment Record, to have a single "Fleet & Equipment Asset" record (with types of "Truck" / "Trailer" / "Equipment" / etc.).

  


Development Specification

Mockup: N/A (not needed) 

  


TODO_IDD: Tim Reitz 12/03/2025: I'm wondering if we should just do a single "Resources" / "Vehicles" / "Machinery" record, with Types of "Truck", "Trailer", "Equipment" (would easily allow for additional in the future).

Matthias Miller 12/03/2025: If you want, but then it's an asset. And if you want to distinguish from accounting, it's a Fleet & Equipment Asset.
