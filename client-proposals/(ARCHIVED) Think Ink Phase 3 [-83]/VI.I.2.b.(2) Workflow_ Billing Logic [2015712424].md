6.9.2.2.2. Workflow: Billing Logic

For annual billing, the first invoice would be a partial year, starting on the nearest 1/4 month in the future until the end of the 11th month in the future. 

  * Examples:
    * Today is October 3, 2023. The start date would be October 8, 2023 and the end/renewal date would be September 30, 2024. The Agreement would be renewed, starting October 1, 2024.
    * Today is October 25, 2023. The start date would be November 1, 2023 and the end/renewal date would be October 31, 2024. The Agreement would be renewed, starting November 1, 2024.



  


DONE_JM: Tim Reitz 07/27/2023: How do you bill for a new device that is added to an agreement in the middle of a billing cycle? 

TODO_IDD: Tim Reitz 08/24/2023: Can install any time (and set the Install Date accordingly). For billing, always round to the next 1/4 month, always in the customer's favor (assuming a 28-day month, so if there are 10 days left in the month, bill the customer for .25 month / 7 days) (1st, 8th, 15th, 22nd) 

TODO_EM: Tim Reitz 09/21/2023: Thoughts on how to do this? Or should we save it for Phase 4?
