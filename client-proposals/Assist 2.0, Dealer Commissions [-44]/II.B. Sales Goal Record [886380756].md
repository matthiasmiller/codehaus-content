2.2. Sales Goal Record

  


Requirements

Add a Sales Goal record.

  


Fields:

  * Salesperson (required; list of salespeople)
  * Year (required)
  * Annual Target $ (required)
  * Weekly Goal RG of:
    * Week # (required; number of 1-54)
    * Weight (number; up to 3 decimals)
    * Weekly Goal $ (automatically calculated uses a weighted average)



  


When modifying the year, autopopulate the RG with blank rows, numbered from Week 1-53/54. The # of weeks will be determined by the Week # for December 31 of the year. Ensure that exactly one row exists for all those week #, and no extra rows exist.

  


Development Specification

Matthias Miller 07/27/2021:

  


We could do this one of two ways:

  * Lookup record with a numeric ID, such as SSS-YYYY, where SSS is the zero-padded absolute value of the salesperson's lookup number. Advantages are that it easily prevents defaults, and you can add a macro to easily look up the record.
  * You could also implement this as a custom database level, and just validated against duplicates. I think it's a little more work, but it may be better since it's less clever than the first. Ellis, feel free to weigh in.



Seth Miller 08/13/2021: Ellis said the first option sounds fine.

  


Fields:

  * Salesperson (required; list of salespeople)
  * Year (required)
  * Annual Target $ (required)
  * Weekly Goal RG of:
    * Week # (required; number of 1-54)
    * Weight (number; up to 3 decimals)
    * Weekly Goal $ (automatically calculated uses a weighted average)



  


When modifying the year, autopopulate the RG with blank rows, numbered from Week 1-53/54. The # of weeks will be determined by the Week # for December 31 of the year. Validate Ensure that exactly one row exists for all those week #, and no extra rows exist.

Seth Miller 08/13/2021: I don't think we will ever have 54 weeks in a year unless it's a leap year and we count weekends as weeks (even though no buildings would be sold presumably). 

I'm also not sure we should allow users to edit the week number, but I may be wrong. If we do not allow them to edit week number we should not allow them to create or delete rows. If we allow them to edit week number it calls for more validation. 

Talk with Matthias about this.

Seth Miller 08/17/2021: Yes, it is actually 52 or 53 weeks.

Seth Miller 08/13/2021: How is Weekly Goal $ actually calculated?

Seth Miller 08/17/2021: Annual Target * Weight / Sum of Weight

  


Matthias Miller 08/17/2021: They don't need to add/remove rows, or edit row numbers.

  


For the # of weeks, we can look at the week # for Dec 30. This avoids adding an extra week if the 31st is on a Sunday, and it keeps our number of weeks down to 52 or 53.
