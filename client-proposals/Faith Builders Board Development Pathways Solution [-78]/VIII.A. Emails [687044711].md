8.1. Emails

  


Requirements

The main emails (other than system notifications) probably will be managed with email templates / records (like the SPE software). This allows for setting up an initial customized template, and also allows for adjustments to the template by FB personnel along the way.

  


These templates allow for expressions so that customized text can be included on a per-recipient basis.

  


Email participants have option to reply all to the email to send comments/take-aways to the other board members who also received the email. 

  


It would be nice to maintain a record in the database of who has replied, so that the board chairman can see who has replied. This probably will be done by incorporating a CC in the initial email, set to an FB email address that is integrated with the Solution. The tracking will only work automatically for members who include that FB email address in their replies, but replies could be documented manually in the software as well.

  


Development Specification

TODO_IDD: Response tracking: 

  * In the email template: Include a CC to a set FB email
  * with email imports “[done@fbboarddevtrack.com](mailto:done@fbboarddevtrack.com)” that flags it as being completed
  * $25-$50/month for the integration
  * Have an RG on the Subscription 
    * One row for each Lesson + Participant that replies
    * Allow manual editing


