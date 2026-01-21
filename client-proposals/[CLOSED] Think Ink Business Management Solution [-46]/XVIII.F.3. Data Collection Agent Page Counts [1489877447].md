18.6.3. Data Collection Agent Page Counts

  


Requirements

The page counts will be imported from the DCA either via an API or through CSV exports.

  


Tim Reitz 04/07/2022: Probably starting out with CSV exports from the MPS service, imported into the Solution. Maybe API integration in the future. 

TODO_JM: what needs to be imported? 

TODO_JM: sample CSV file? 

  


  


DONE_TR: I suspect that Net Gateway is the piece that allows some level of automation, and there's a question between using an API (i.e. integrating directly with it) or CSV (import). Could also be Manual vs Automatic.

  


Development Specification

x30 Matching on Serial number(?), 

Create new RG Row, filling in 

  * Entry Date
  * Black
  * Color
  * Source (API)



  


HL Est: 16 Hours
