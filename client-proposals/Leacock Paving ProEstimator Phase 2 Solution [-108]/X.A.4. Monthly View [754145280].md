10.1.4. Monthly View

  


Requirements

The monthly view includes a calendar for each of the Paving-type Crews. Prep-type Crews are included on the calendar with the Paving Crew to which the main job is assigned. 

  


  * The calendar event Title could be as simple as "<Customer Name> <Job #> <Customer Phone>" 
    * NOTE: We could give an easy way to show the materials on the job. It would be a comma-delimited list with the primary Qty+UOM and description, i.e. "32 tons of 19mm").
    * If the job is missing a deposit, show a "DEPOSIT REQUIRED" in the title.
  * Clicking into the Event would show the "Job Event" screen (see corresponding spec).
  * Note that the heading colors for each calendar section are set on the corresponding Crew record, and the background colors for the Calendar Event Tiles are set on the Calendar Event records.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=422537653#gid=422537653](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=422537653#gid=422537653) 

  


Note that they currently are doing this on an Outlook calendar - see screenshot for example: [https://drive.google.com/file/d/1H96mn6rkizdaFZLgdWVMYAvyKEkbhkC6/view?usp=sharing](https://drive.google.com/file/d/1H96mn6rkizdaFZLgdWVMYAvyKEkbhkC6/view?usp=sharing).

  


TODO_IDD:

TODO_JB: How will it work if another Paving Crew is added? Automatically add another section here in the WSGI, or would it need to be added manually?
