9.2.1. Payment Portal

Jonathan Bergen 10/30/2025: DONE_IDD: How should we validate that all of the payment rows on contracts for a certain payment match the payment's total?

Matthias Miller 12/16/2025: I'm going to assume we're going to have some kind of Accounting Exception report alert that this would show up in. TODO_JB / TODO_SETH

Matthias Miller 01/20/2026: Better yet, pull 1 total from the payment and another total from the linked rows, so that it blows up when trying to create the accounting transaction. We could theoretically do it from both sides:

  * Contract uses Payment amount for A/P
  * Payment uses Contract amount for A/P


