11.9. Distributions Record

  


Requirements

Accessed via: FaithBuilders Scholarship Services | School | School Distributions

  


TODO_AP: Tim Reitz 02/24/2025: Bring in the Record Snippet for the standard pieces for this overview section. Also update the record sections below as able/needed.

  


  


Niccolas Miller 10/28/2025: Overview of some distribution logic from client from 10/28/25:

  * Minimum distribution is all funding that arrived before the start of the current fiscal year.
  * Starting balance is all available funding, whether it arrived during the current fiscal year or prior.
  * As soon as you create a distribution and put in the DistYear, the minimum distribution fills to the correct number. I’ve not seen any issues with this number being incorrect on distribution records, although I don’t think I’ve created multiple distribution records for a school this year.



  


I should maybe clarify minimum distribution: it is all available funding that arrived before the start of the current fiscal year; that is, if a school carries forward a balance from the prior fiscal year, then that balance is their minimum distribution. We have a lot of schools with no carried-forward funding from the prior fiscal year, thus no minimum distribution.

  


In subsequent distributions, minimum distribution would need to reflect the remaining balance of carried-forward funding, if there is any. For example, School X started the year with $89,900 from contributions given the prior fiscal year, which constitutes their minimum distribution. Their first distribution was $79,000. When a subsequent distribution was created, it showed minimum distribution to be 20,900.

  


In another example, school Y had $78,000 minimum distribution and distributed $78,000 in the first distribution. A subsequent distribution was created to help a late enrolled student, and the school authorized us to distribute some of the funds from the current fiscal year. The minimum distribution was $0, but the $1,700 they issued decreased the minimum balance for the next year’s distributions.

  


Development Specification

Change Requests:

  * Ben Reitz 06/24/2025: [[[IN11379](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11381&)]] - XFB - Distribution record - Update Funds section (part 1 of State Reports feature)
  * 


  


Matthias Miller 04/06/2018:

  * The VIrtual RG should include items from the stored RG, even if they would not otherwise be in the list of students. Then we should warn if the receiving student is inactive/ineligible.



  


[ ] Vivian - what EITC fund should get defaulted, Pre-K or K-12?

Matthias Miller 04/25/2018: This is moot issue b/c we never would do both.

  


  * Should we have a report that shows them the age of the money, for things close to the 2 years? --- (If there were no more distributions, when would the balance hit zero or negative, and what's the time?)
    * Matthias Miller 04/25/2018: She does it school by school, and says "you have this amount of money that came in last fiscal year, and you must use this money and you must use it."
    * Matthias Miller 04/25/2018: Per Vivian, another option would be to have a report that would show contributions that have not been used up (with the amount remaining), either sorted or filtered by date of contribution (for fiscal year)
    * Matthias Miller 04/25/2018: Per Vivian --- the report that gets sent to schools w/ their contribution information -- we would show:
      * contributions sorted by date (and grouped by fiscal year)
      * available/carryover balance



  


[ ] Vivian - what if on the distribution we had a grid showing:

  * Matching contributions
  * Contribution date
  * Contribution type (OSTC/EITC/Etc)
  * full contribution amount
  * Remaining contribution balance
  * Age of contribution



Then on the distribution, show balance OF THE CURRENT DISTRIBUTION, as well as age of money, and we could also show the corresponding contributions

  


[ ] Later, we could add validation for the age of money
