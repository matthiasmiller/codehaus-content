3\. Calendar View

  


Requirements

  * The calendar will be the primary way of editing the schedule.
  * It will be designed for a 4K resolution touchscreen.
  * It will be 5 days wide
  * It will have 5 weeks visible at a time (can drop down to 3 weeks if a second screen is needed; using a 4K resolution)
  * It will allow scrolling to a distant past (configurable # of weeks; large # for now) and up to 1 week past the final scheduled delivery in the future. This allows a blank week.
  * Historical items would be shaded/grayed out.
  * It will allow dragging and dropping between dates, as well as within day.
  * Clicking an item will open it on a new page, with the option to return to the calendar view
  * Will Call items will be shown at the very end of the Calendar View, as a separate week. These can be dragged onto the schedule, and scheduled items can be dragged onto it. They can be edited, just like any other delivery. 
  * Each day will have a + button that will open a new order on a new page, defaulted to that date.
  * This will automatically refresh when other users make changes. It's possible that we'll configure it to go into a "power saver" mode during off hours, where it will blur the schedule and require you to click a button to manually refresh. It would refresh automatically and frequently during business hours.



  


The calendar item will have the following icons at the bottom of the screen, with border colors indicating the current setting:

  * S - Toggles through:
    * Not Set (gray)
    * Set (blue)
  * PE - Toggles through:
    * Neither Permit nor Escort (gray)
    * Permit without Escort (red)
    * Permit with Escort (orange)
  * C - Toggles through:
    * Neither Called nor Confirmed (gray)
    * Called but not Confirmed (yellow)
    * Called and Confirmed (green)
  * M - Toggles through:
    * Not Made (gray)
    * Made (black)



  


Development Specification

Dev Spec: Create an index of ActivityID on all activity records for this level. Use BinStringToNum(LastNdxKey(...)) to detect version/changes. Talk to Josh to make sure he's not concerned about server load.
