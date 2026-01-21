18.6.1. Automatic Email Manager

TODO_JM: is this something you currently have?

  


TODO_CH: spec this out?

  


Matthias Miller 05/19/2022: Waiting to hear back from John Allan on attachments. This will need to be a lightweight application running on one of their computers, that will poll for new attachments, then download and print. On the AHZ side, I think this can be as simple as an index of all emails that have attachments, with a subset that take a prior email ID, and looks for subsequent emails. The client app would memorize the last processed email. It would never download full history. The first time you run it, it would check the latest email ID, and go from there.

Matthias Miller 05/19/2022: This is in discussion with Josh. I'm thinking attachments get pushed to S3, and the links/keys get stored in AHZ.
