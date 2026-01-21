15.1.1. Changes to Device Record

  * Prepay? (checkbox; defaults to blank; warning on Save if cleared: "You are turning off Prepay for this Asset. Do you want to continue?") 



TODO_JM: Is it fine to move all Prepay details to the Billing Group/MPS contract instead of it being on a per-device basis?

  * Notes about Prepay:
    * Invoiced on a quarterly basis, with customers paying ahead for the base charge
    * Print count overage still billed like the others (quarterly, post-pay)
    * Currently 5% discount on the base charge (not the page overages) for prepay, but the amount may change on a per-customer basis. The standard rate is set in the AppHosting.Zone Settings page; variations should be
    * Currently very few customers are on a prepay setup (maybe 2%), but Think Ink is interested in expanding this as time goes on
    * It's fine to keep the prepay stuff pretty manual



TODO_JM: are you fine with this semi-manual approach (at least for now)?

DONE_CH: thoughts on this?

TODO_TR: Matthias Miller 05/10/2022: Simple solution is that they put in a $0 base charge for these, then have a Prepay report that they run, where they manually fill in the prepay amount. We could add a single-line textbox called Prepay Notes that allows them to put in information, that would be displayed in the Prepay report. (Notes only visible if Prepay is checked.)

  * Prepay Notes (visible if Prepay box is filled; optional; used for documenting notes regarding price, billing dates, etc.; displays on the Prepay Invoicing Report)
  * Prepay End Date (visible and required if Prepay box is filled; date field; default to blank)



TODO_TR: report alert triggered 1 month before the Prepay Date AND on "today" triggers the Needs Review checkbox 

DONE_CH: good with this? think through details

Matthias Miller 05/10/2022: My proposal is to check the Needs Review box at 30 days, then rely on the weekly alert/email to deal with this. When the user clears the Needs Review without extending the prepay end date past 30 days, show a warning on save, "This device will be flagged for review when prepayment ends on [date]."

  


On the day of (or anytime after), flag Needs Review again. Show a warning on save if Prepay End Date <= Today.
