3.1. Email: Amazon Configuration

We will use SES for email.

  


Create the following based on See [https://aws.amazon.com/blogs/messaging-and-targeting/forward-incoming-email-to-an-external-destination/](https://aws.amazon.com/blogs/messaging-and-targeting/forward-incoming-email-to-an-external-destination/):

  * A lambda
  * S3 bucket
  * Policies
  * IAM Role



  


Create two new SNS topics -- one for email and one for notifications.

  * Change the Email to call the lambda
  * Change both to call the ses WSGI entrypoints



  


Set up SES.

  


First, add and verify codehaus.academy for the domain.

  


Then, edit the default rules. Add a Receipt Rule with an S3 type that captures all emails and triggers the Phone_Course_Email SNS topic.

  


Finally, add each of the emails:

  * signup@
  * support@
  * unsubscribe@



  


Configure both the domain AND each of the emails with notifications to the SNS designed for notifiications.
