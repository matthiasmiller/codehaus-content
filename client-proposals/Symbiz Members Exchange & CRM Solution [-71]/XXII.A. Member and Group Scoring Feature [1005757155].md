22.1. Member and Group Scoring Feature

Tim Reitz 04/11/2023: Per the client today, the scoring feature can be deferred.

  


  


AppHosting.zone Settings page: 

  


Scoring Configurations section: TODO_IDD: Tim Reitz 04/06/2023: work on this OR defer it to a later phase

  * Goal Item Score (single Goal entry)
  * Goal Worksheet Score (single Goal record)
  * Meeting Score (specific Goal meeting)
  * Monthly Group Score (score for a specific group and/or specific Life Branch) 
  * Meeting Attendance (TODO_



  


Notes about scoring: 

  * The current scoring model is as follows:
    * 10 points for completing a goal
    * 5 points for using the Make Up Option ("MUO")
    * 2 points for setting a goal and not reaching it
    * 0 points for not setting any goal
  * There is a rolling 12-month average for each member, based on the past 12 months of meetings. 



  


TODO_ - do you do average score of all members?

  


Life Vision Bonus Points: If a member reviews/updates their Core Values, Life Vision, and Annual Goals once a year, they will receive bonus points added to their monthly score each month for 12 months after the review. 

The bonus points amounts are as follows: 

  * 2 points for each Core Value
  * 10 points for the Life Vision
  * 2 points for each Annual Goal



TODO_IDD: Tim Reitz 04/06/2023: more items in the Scoring Configurations section? 

Matthias Miller 04/13/2023: There are points for goals, and points for Life Vision. These are different. I don't understand the question.

TODO_IDD: Tim Reitz 04/06/2023: Think through how to mark those items as updated so the system can know to apply the points for the next 12 months. 

  


Contact record: 

  * Member Details section: 
    * Monthly Score (
      * TODO_IDD: score for the most recent completed month
      * visible only for member, f, rr, sa
    * Annual Score (
      * TODO_IDD: average score from the past 12 completed months
      * visible only for member, f, rr, sa



  


Growth Ring Group record: 

  * Group Score (auto-calculated and read-only; average of all of the individual members' scores for the most recent completed month)
  * In the Members embedded spreadsheet:
    * Last Score (auto-set and read-only; for the most recent completed month; visible only to growth ring members)
  * Data Access: 
    * Scores: Visible only for group members



  


  


Growth Ring Group Meeting record:

  * Meeting Score (auto-set and read-only; calculated as defined in AppHosting.zone settings)



  


Growth Ring Goal record:

  * Goals table:
    * Score column (auto-set and read-only; based on the selection in Achieved and the scoring model)
  * Total Score (auto-calculated and read-only; sum of all Scores for goals for the month and with Life Vision bonus points)
    * TODO_IDD: Tim Reitz 04/04/2023: work on the bonus points feature (points applied every month if the member has reviewed and updated their annual/life goals in the past year). 
  * Next Month's Goals table: 
    * Score (editable) ?



  


Member Directory Report: 

  * Columns
    * Monthly Score (visible for Facilitators, Regional Reps, and Super Admin users; displays information for their own downlines)
    * Annual Score (visible for Facilitators, Regional Reps, and Super Admin users; displays information for their own downlines)



  


Growth Ring Groups Report: 

  * Columns: 
    * Monthly Score
    * Annual Score



  


Growth Ring Meetings Report

  * Column
    * Meeting Score



  


Growth Ring Goals Report

  * Column
  * Score (total row shows sum)



  


Life Goals Worksheet Printout: 

  * Score section: 
    * Date Last Reviewed
    * Score


