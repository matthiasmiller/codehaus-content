Someone asked this question:

> Title: Bank rec using power query
>
> I’m a noob to power query so please be gentle with me.
> 
> I have a bank statement in one tab and a list of the payments in the banks nominal download from Sage in the 2nd tab.
> 
> I used to use formulas to return match or not found but it’s unreliable and times consuming still.
> 
> I want power query to show transaction matches between the 2 tabs based on date and amount at least but maybe payment reference too (this bit I find difficult because in the bank statement the reference might say customers name like *Hynes* but the sage download it might say the customer code like *0005336* or it might say *Hyn001* because older customers have numerical customer codes and newer customers have their first 3 digits of their name as part of the code).
> 
> I just want something to help me see matched and unmatched lines and reconcile the 2 lists but so far anyone I ask doesn’t know, and the videos I’ve watched throw me off because I’ll follow the steps and they’ll give lots of info but then they’ll say “but we’re not going to use any of that for this example so delete the last 3 steps” and it throws me off.
> 
> Please can someone be kind and help.
> 
> So far I know to load each tab into query as connection only, and to combine the queries but the “Left Outer” “Left Anti” “Inner” and fuzzy I don’t fully understand


Here was my response:

> Have you tried sitting down with one of the AI tools (ChatGPT, Gemini, Copilot, etc) and talking it through step by step? It honestly might be just as productive as watching YouTube videos.
> 
> Bottom line to your last question:  
> \- left outer: include all rows from the left, and rows from the right if they match  
> \- right outer: include all rows from the right, and rows from the left if they match  
> \- inner: include all rows from left &amp; right if they match  
> \- left anti: include all rows from the left, but only if they don't match  
> \- fuzzy: allow matching on approximate values.
> 
> Do you have more specific questions?