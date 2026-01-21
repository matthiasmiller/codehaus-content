34\. Automation

  


Requirements

DONE_MM: Tim Reitz 06/01/2023: Do we need this section (it seems like automation is specced out throughout the proposal)?

Tim Reitz 06/06/2023: No.

  


Development Specification

TODO_IDD: Tim Reitz 06/01/2023: If we keep this, we need to make sure it's updated: 

The Member's Portal will automatically create Growth Ring Meeting and Monthly Goal records for active members when a new Growth Ring Meeting is created.

  


TODO_IDD: Tim Reitz 04/18/2023: We need to think through scheduling meetings / setting goals. 

  * currently everyone sends their goals in after this month's meeting, and then the next month's meeting would be set up within a few days. 
  * how to link goals and meetings records? 
  * If it would be easy to toggle back and forth between this month's goals and next month's goals, we wouldn't have to have them on the same page



  


  


DONE_MM: Tim Reitz 04/18/2023: what details do we need to spec out for this?

TODO_IDD: Tim Reitz 04/18/2023: Spec this out: Seven days before this month's meeting, we auto-create an unscheduled meeting for next month and create all the linked goals.

  


  


  


  


  


Spec from Matthias: Confirm details, but something like this: 

  * Have a macro for each growth ring that determines the required goal (month+year). Put this in an index.
  * Create a Growth Ring group that repeats on members.
    * For each group, find the minimum required goal, using the index to make it hyper-fast
    * For each member, find the latest goal (presumably also using an index to make it hyper-fast)
    * Only include rows where the latest goal < minimum required goal
  * Create an X30
    * Create the NEXT missing goal for each of the members in the above report (NOTE: If they fall behind, it's OK -- we'll slowly catch them up, and it shouldn't happen frequently.)
  * Then either:
    * Create a trigger that writes them to file with a scheduled task to sweep them, OR
    * Create a scheduled task that looks for missing changes and sweeps them


