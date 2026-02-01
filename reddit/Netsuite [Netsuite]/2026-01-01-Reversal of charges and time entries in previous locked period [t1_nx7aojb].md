Someone asked this question:

> Title: Reversal of charges and time entries in previous locked period
>
> Hi team,
> 
>   
> A little bit stumped on how to proceed correcting this mess.
> 
>   
> For context we have a lot of projects running simultaneously under a single customer. Our developers often don't know which project their work is for and rely on a team to assist with where to put their time (highly inefficient and under review but it is what it is for now). What has happened is a number of developers had created their time, the time was charged using a charge rule creating an invoice which was subsequently paid. The problem is, the project is incorrect meaning the time, charge and invoice is incorrect. - all of this happened 3 periods ago and has only just been noticed during a quarterly review.
> 
>   
> The invoice can be credit memo'd (and has been) but that is as far as I get before getting stumped. I know we can create negative charges but these cannot be time based as there is no time entries to put against it. I cannot delete the previous charges as they have been invoiced. I could create a negative charge using fixed date but would that create an issue on the revenue side? and it still does not correct the time entries. 
> 
>   
> My other option is to open the periods up, delete the credit memo, invoice and charges. This would allow me to edit the time entries and put under the correct project and create a new invoice in that past period which would keep the overall accounting impact the same. - is this best practice in this situation or is there a process to correct this that I am unaware of?
> 
>   
> Any insight would be appreciated


Here was my response:

> The software companies I've worked with have time tracking tied into their SDLC, then push time codes from there into their accounting software (either automatically or manually). The time tracking is literally tied to the same ticket that has the requirements for whatever changes that they're making (which are also tied to their commits), so except for developers getting lazy, there's zero reason for anything to get billed wrong. Ever. Plus, having a senior dev or PM put in time estimates provides secondary checks &amp; balances for errors.
> 
> I can understand why most service-based companies might not want to do this. Less sure about developers, since they're the ones who can actually solve these problems themselves. ;-)