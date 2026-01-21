7.10.3. Incident - Child Job Details Section

Add the following new custom section: 

TODO_SG: Tim Reitz 04/11/2024: Do you want this? 

  


  * Child Job Details section (visible only for parent incidents if Type = Work Order): This custom section displays read-only information about all child jobs of a parent incident, for quick reference without needing to open the child incidents separately.
    * Child Incident Summary (read-only embedded spreadsheet with the following:) 
      * Columns: 
        * ID & Title (<[[IN0000]] - Incident Title>)
        * Status (<Incident Status>)
        * Est. Hours (<Estimated Hours>)
        * Act. Hours (<Actual Hours>)
        * View (cell displays "Link"; opens the child incident)
      * Automatically sorted by: Incident ID (lowest ID at the top) 
      * Buttons to insert/append/remove rows: N/A (rows are automatically added/removed based on incident linking) 
      * Show 5 rows without scrolling 
      * Other Notes: 
        * N/A
    * Child Incidents Details (read-only memo; displays the following information from all child incidents, in the following format, sorted by Incident ID (lowest at the top): 



Incident ID & Title: <[[IN0000]] - Incident Title> (Note that the ID number is a link to open the incident) 

Status: <Incident Status> 

Estimated Hours: <Estimated Hours>

Actual Hours: <Actual Hours>

Work Requested: <Work Requested contents>  

Work Performed: <Work Performed contents>
