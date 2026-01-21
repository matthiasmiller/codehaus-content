12.25.3. Contract Definition (RTR)

Seth Miller 11/13/2025: Moving this here to deal with for spring.

  


  * Rent-to-Rent Financials (only visible if "Rental Contract Type" is set to "RTR")
    * Early Termination Fee $ 
    * Matthias Miller 07/25/2025: DONE_DB: Figure out price increases Duane Burkholder 08/21/2025: DONE_MM: I don't know what this was in relation to



Seth Miller 10/20/2025: DONE_DB: this is rent increases. 80% every year??

Duane Burkholder 11/05/2025: TODO_SETH: to clarify this will be for future. RTR is aimed at Fixed storage so you will have a contract which may have language that allows for rate increase based on some time frame. Due to not being able to effectively quantify at this point how that will work I think the best thing would be to have a dated RG for the rent. I am thinking something like the following:

  


Rent RG:

  * Start Date
  * Frequency
    * Monthly
    * Bi-Monthly
    * Weekly
  * $ Amount



  


I could see some sort of maintenance report that would allow you to add an RG row with ask prompts for:

  * Rental Company
  * Start Date - Date field manual input
  * Frequency - Drop down
  * Rent percentage multiplier - number field
  * Rounding options
    * Round Up to whole dollar
    * Round Down to whole dollar



Grouping:

  * Year - Start of Contract



Column:

  * Usual info
  * Current Rent
  * New Rent - based on multiplier



Link action based on selected rows would add a new RG row based on:

  * Start date ask prompt
  * Frequency ask prompt
  * New rent number



Subpane of actual contract for manual input
