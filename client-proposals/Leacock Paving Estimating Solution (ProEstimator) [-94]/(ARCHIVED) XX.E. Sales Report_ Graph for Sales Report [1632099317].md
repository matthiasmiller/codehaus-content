20.5. Sales Report: Graph for Sales Report

  


Requirements

_SM: Tim Reitz 07/07/2025: Let's write this up as a "future" CR. 

Sean Miller 07/07/2025: [[[IN11680](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11682&)]] - ZLP - Sales Report: Graph for Sales Report

  


An additional pane could be added to the Sales report with one or more graphs to help visualize the data in the left pane.

  


Estimated Cost: TBD (once designed) 

  


Initial Spec:

  * Graph Type: Bar Graph (vertical bars) 
  * Graph Title: Proposals by Sales Rep 
  * Prompts: N/A
  * Legend: N/A
  * Colors: Default
  * Y Axis Label: "Proposals"
  * Y Axis Value: Scale (automatic) 
  * X Axis Label: "Job Types"
  * X Axis Value: Columns for each Job Type
  * Series: single, based on Sales Rep
  * Other Notes:
    * Each bar includes data for both created and awarded Proposals: 
      * Full length of the bar represents "# Proposals Sent" (in green or blue)
      * Section withing the bar represents "# Proposals Awarded" (in gray) 
    * The actual number is listed at the end of each bar



  


Development Specification

Tim Reitz 06/26/2025: Client likes the idea of this, but let's hold off for now.
