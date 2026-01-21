2.2.4. Workflow for Calculating Scholarship Awards

  


Requirements

1\. We determine the available funds to distribute for scholarships.

If the school opts for discretionary funds, the State requires that 80% of the funds must go to tuition. FB enforces a limit of up to 5% (prior to 2024, 13%) of the gross funds (before the management fee) being allocated to discretionary funds.

  


For example, given a gross amount of $100K, the funds will be distributed as follows:

  * A $5K processing fee will be retained by FB.
  * The school will receive notice of $95K awarded
  * Up to $13K will be allowed for a discretionary fund.
  * FB will assess a $13/family charge for all FB-managed applications. This will be withdrawn from the discretionary fund.
  * The remaining $82K will be allocated to tuition.



  


The $13/family fee must be taken from the OSTC fund for any family with OSTC students. All other fees will be taken from the respective EITC fund. (Pre-K and K-12 schools are currently completely separate.)

  


For each of the fund accounts, we will also provide the option to reduce the amount of funds to be distributed. This must be determined before specifying the discretionary funds, since the discretionary funds must be proportional to the tuition funds. (This should be validated.)

  


For each of the fund accounts, we will provide the option to choose between a percentage or dollar value for the discretionary fund. This must not exceed 5% (prior to 2024, 13%) of the gross amount to be distributed (<= Distribution * .13 / .82). We will default these values based on the school's application (either 0% or 5%).

  


Note that FB may override the awards for a specific family, in which case that family will be excluded from the calculations. This allows these funds to be given or taken from all other families with equal fairness.

  


  


2\. We determine the maximum income for each family. 

If the school imposes a stricter maximum income, we respect that. If a family falls within the State limit but not within the school limit, we will not automatically award them funds. However, we will allow manually allocating funds to that family.

  


The dependents are currently calculated as children and do not include the spouse. However, this may change in the future.

  


MaxFamilyIncome = MINIMUM(

SchoolMaxIncomeBase + Dependents * SchoolMaxIncomePerDependent,

GvtMaxIncomeBase + Dependents * GvtMaxIncomePerDependent

)

  


  


3\. We determine which students qualify. 

We will show a list of all qualifying students based on the specified limits.

  


If the family has one or more children with learning disabilities, the entire family will qualify as long as their income is within 150% of the normal maximum family income. This will not affect the amount of award they will receive.

  


  


4\. We determine the ratio between the family's income gap and maximum income. 

For example, if a family makes $60,000 and is eligible up to $80,000 of income, their IncomeGapRatio is 0.25.

  


In some situations, families may have a negative income gap if they have a child with a learning disability and make between 101 and 150% of the maximum income. To normalize this gap, we will enforce a minimum IncomeGapRatio of 0.05.

  


For example:

  


IncomeGap = MaxFamilyIncome - CurrentIncome

IncomeGapRatio = Maximum(

0.05,

IncomeGap / MaxFamilyIncome

)

  


This can also be expressed as:

  


IncomeGapRatio = Maximum(

0.05,

1 - (CurrentIncome / MaxFamilyIncome)

)

  


  


5\. We calculate a weighting based on the student's tuition. 

For example, a student with $5,000 of tuition will be awarded twice as much as a family with $2,500 of tuition.

  


TutitionRatio = StudentTuition / TotalTuition

  


  


6\. We calculate the award weighting, combining the IncomeGapRatio and the TuitionRatio.

  


AwardWeighting = IncomeGapRatio * TutitionRatio

TotalAwardWeighting = SUMALL(AwardWeighting)

  


  


7\. We determine the maximum percentage or dollar value each student may receive, as defined by the school or FB.

  


This includes two requirements:

  * Students can only be rewarded 70% of their tuition. This is to reduce the impact of self-employed families with significant deductions. (This limit only applies to automatic awards.)
  * OSTC's cannot grant more than $8500 per student, or $15,000 per student with learning disability. (This requirement is not currently part of the software and is manually overridden by Vivian.)



  


This maximum percentage is an FB-recommended preference to avoid giving people free rides. This is not a State limit, and schools are welcome to override it, which happens occasionally but very rarely. This limit is usually adjusted when there are a small number of applicants.

  


MaxTuition% = 70% (fixed percentage; non-changeable)

StudentMaxAward$ = StudentTuition * MaxTuition%

StudentMaxAward% = StudentMaxAward$ / TotalAward$

  


  


8\. We distribute awards in order of greatest need (descending order by IncomeGapRatio). 

This allows us to distribute the funds accurately, respecting the maximum award amounts, yet without iteratively calculating values.

  


StudentAward% = MINIMUM(

StudentMaxAward%,

AwardWeighting / SUMALL(AwardWeighting IF OtherIncomeGapRatio >= ThisIncomeGapRatio)

)

StudentAward$ = MINIMUM(

StudentMaxAward$,

(SchoolFunds - SUMALL(StudentAward$ IF OtherIncomeGapRatio < ThisIncomeGapRatio)) * StudentAward%

)

  


(NOTE: We will likely need a tie-breaker for the income gap ratio. This is only required so that we can correctly identify other rows and should not affect awards.)

  


All awards will be rounded to the nearest dollar. We will use the final student to fix any rounding errors. (The current solution leaves a few dollars left over for the following year, but it would be nicer if it wouldn't do that. It's important to do rounding to improve perception of the award amounts. Otherwise, it looks like a nickel-and-dime calculation.)

  


9\. We distribute funds first from OSTC, then from EITC, and finally from Non-EITC funds. 

These will be distributed as follows:

  


  * OSTC awards will be distributed proportionally to the entire award. This means that every eligible OSTC student will receive some OSTC awards.
  * All remaining awards will automatically be distributed from the EITC funds (excluding any OSTC and Non-EITC).
  * FB will be required to manually enter Non-EITC Fund amounts.



  


We will validate that the total distribution amounts match the amounts specified for individual student distributions.

  


Development Specification

This is the description that we got from Michael Petersheim:

  


The formula takes into account the max household income + amount per dependent that the state has specified as qualifying an applicant for an award and the max household income + amount per dependent that the school has requested for their patrons (if any). The lesser of these I call the cap. This has to be calculated for each family based on the number of dependents.

  


Then I get a number that I call Percent Deficit, which equals (cap - income)/cap. That is, PerDef_i = (cap - income)/cap. I add up all the PerDef_i numbers for the applicants of a school to get the TotalPerDef. The award for a particular family I call award_i, where i is a different number for each family.

  


The funds available to the school should not include the amount for any fixed awards given to families - those should be subtracted first.

  


award_i = funds available to the school for tuition * PerDef_i/TotalPerDef.

  


Next all award_i are checked to make sure that none of them exceed the max percentage of tuition that is specified by FB or the school, whichever is lower. Any that do are maxed out at that amount. They are then removed from the calculation and all the maxed awards are subtracted from the total funds available.

  


Then new award_i amounts are calculated from the new funds available after the maxed and fixed awards have been subtracted.

  


This process keeps repeating itself until the awards stop changing.

  


If there are several types of funds being awarded, then they are awarded in a certain order. First all the OSTC funds are awarded, then all the EITC, and finally all the non-program funds.
