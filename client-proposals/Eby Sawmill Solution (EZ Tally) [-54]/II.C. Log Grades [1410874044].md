2.3. Log Grades

  


Requirements

Logs are graded to determine their quality. Grades are listed as two or three-digit numbers. This will be based off of two lists: 

  * Base Grades: numbers 0-5
  * Subgrades: number 0-9 and 10-99 



  


Standard grades: For most logs, the first digit (called the Base Grade) reflects the number of blemish-free sides, from 0 to 4. The second digit (Subgrade) reflects the relative quality within the Base Grade.

  


Examples: 

  * 09:  no blemish-free sides, but a high quality log within the base grade
  * 40: four blemish-free sides, but a low quality log within the base grade



  


Veneer grade: If a log has exceptional quality, it is flagged as a Veneer log. The Base Grade digit is a 5, and the Subgrade consists of 2 digits that reflect the price (in thousands of dollars per thousand board feet; can also be interpreted as dollars per board foot). 

  


Examples: 

  * 510: veneer log at $1000/mbf
  * 545: veneer log at $4500/mbf



  


Note that this may be adjusted in the future to handle an additional incremental price (see the Veneer Pricing section of the living spec). 

  


Other notes: 

Previously, Eby's used letters for their subgrade. They will change their grades away from letters to purely numbers to simplify the usage in the software. It also allows easy data entry when scaling, since the scaler can enter the grade using a simple number pad. It's also a simpler scale, since both the Base Grade and Subgrade use ascending values. (Previously 0 meant the lowest grade, but A meant the highest subgrade.)

  


The previous 0A through 4H grades will use 00 through 49 instead. A log previously graded at 0A will be graded at 09.

  


The previous V10 through V99 grades will use 510 through 599.

  


This change of scale will affect both data entry and printouts (printouts will display the Base Grade and Subgrade separated by a hyphen, such as "4-1" or "5-40"). 

  


The EZ Tally Solution will include an unchangeable list for all Grades, containing items from "00" through "49" and "510" through "599".

  


Development Specification

List: LogGrades, Unchangeable.

BID: 2 hours
