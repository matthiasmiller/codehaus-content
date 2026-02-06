# Systems Deep Dive

1. Introduction  
   1. What do you want to have out of this?  
   2. Two Parts:  
      1. PART ONE \- Instilling a DEEP VISCERAL understanding of systems, how they work, and how to think about them  
      2. PART TWO \- Tactical pieces of how to implement these in your system  
2. Part 1 \- Mindset  
   1. Introduction  
      1. As I was preparing for this, I had a lunch conversation with a friend of mine who asked me, “What do you REALLY do?” We had an intensely creative conversation.  
      2. For the next 48 minutes, I was speaking into my voice recorder, capturing the parallels from my entire career in software and my understanding of business.  
      3. This is going to be my path to UNPACK  
   2. What Are SYSTEM?  
      1. External Inputs (Interruption \+ Information) \-\> Series of Actions / Decision Points \-\> External Output  
      2. A system is only meaningful when it interacts with things OUTSIDE it  
         1. Godel’s Theorem  
         2. Scripture \-...  
         3. A business…  
      3. As simple as a LEVER/FULCRUM  
      4. For example, sitting at the coffee shop, the external event is someone walks in, places an order  
         1. In this case, THEY are making the decision.  
         2. From there, it’s a series of simple steps to make their food/drink based on their decision  
      5. Alarm Clock  
         1. External Input (time of day, etc) … series of items etc …  
      6.   
   3. 3 ways to think about software  
      1. Expression Programming  
         1. if you give me information, I give you new/different information, but I will not DO anything.  
      2. Functional Programming \- Linear / Step by Step  
         1. If you give me information, I may change some things along the way, and I may or may not give you new information  
         2. RETURN-based vs EXCEPTION-based  
            1. I will tell you whether or not it worked  
            2. I will tell you if it DIDN’T work  
      3. Object Oriented  
         1. This is a hierarchical TREE structure, where you have:  
            1. Systems  
            2. Subsystems  
            3. Modules  
            4. Files  
            5. Classes  
            6. Functions  
            7. AND THEN you get to the linear   
         2. But here’s the thing  
            1. EVERYTHING can be represented as a tree structure  
            2. There’s a whole part of linguistics that’s centered around modeling   
            3. Your family is a tree structure  
            4. Your house is a tree structure  
               1. House  
                  1. Kitchen  
                     1. Cabinet  
                  2. Living room  
                  3. Bedrooms  
                     1. Bedroom 1  
                     2. Bedroom 2  
                     3. Bedroom 3  
            5. This is almost everywhere  
   4. How do you traverse TREES?  
      1. The most natural flow of information is up and down the tree, NOT randomly across the tree.  
   5. Trees follow depth of knowledge  
      1. This is what has happened in the evolution   
   6. Knowledge becomes more granular as you go down the tree.  
      1. Software Language – look at what people have called CODING:  
         1. Machine Code (1’s and 0’s)  
         2. Assembler (short abbreviations)  
         3. C (standard C)  
         4. C++ (or object oriented C)  
         5. JavaScript (V8)  
         6. Zapier  
      2. What are the benefits?  
         1. It allows you to turn 10, 100, or 1,000 instructions into 1  
         2. You can tell an entry-level person step by step instructions  
         3. You can tell a manager overall plan  
         4. You can tell a leader the strategic direction  
      3. And encapsulated in your instructions are multiple levels of instruction  
      4. This means that your level of specificity MUST match the level of sophistication of each person. Your PROCESS will be much more terse.   
      5. It also means that if you’re able to find common, repeatable processes, and you’re able to break them down into meticulous instructions, you can offload them to less skilled labor  
   7. When you develop software, you always start with:  
      1. A series of instructions  
      2. YOu allow it to grow  
      3. You recognize the natural divisions  
      4. You split them apart  
      5. *This is how biology works, and this is how organizations grow as well…*  
   8. The same with a business, and a new venture, or ANYTHING that you do…  
      1. You start with a series of steps and tasks  
      2. You look for natural patterns and divisions that emerge  
      3. You separate those so that you can continue to grow without encountering undue complexity  
   9. There are 3 places where these things can break down:  
      1. If you have INACTION, you don’t have any steps/tasks to device  
      2. If you don’t have PATTERN RECOGNITION, you’ll misappropriate tasks OR you’ll continue to evolve into deeper chaos…  
      3. If you don’t have DELEGATION, you can’t split off tasks to continue to multiply  
   10. NOISE is when you have communication without separation.  
       1. There are two types of communication in networking –  
          1. Broadcast (requires users to filter out what is relevant to them)  
          2. Targeted (only sends messages that are targeted)  
       2. Every communication system has a BANDWIDTH issue  
          1. You can only HEAR and UNDERSTAND so much stuff  
          2. (Story of Gox Box?)  
       3. A growing system that does not subdivide, will encounter breakdowns in communication, because people are not able to handle that much information  
       4. Information will actively start getting lost…this is the equivalent of “packets getting dropped”  
   11. Communication  
       1. Targeted communication is high-friction, high-quality, low-bandwidth  
          1. Targetd communication slows down and speeds up based on the communication bandwidth  
       2. Broadcast communication is low-friction, low-quality, high-bandwidth  
          1. Broadcast communication simply gets lost when it exceeds the maximum bandwidth  
       3. Every broadcast medium, such as social media (or to some degree, email) needs to have a filter. If you want something more than just what happens to come at the wrong time, you need to actively WEED OUT invalid information.  
          1. This is why people who are busy with other things are often not able to hear memos from the head office, because they have a hard limit on their bandwidth.  
          2. One of the most 80/20 thing you can do is recognize this limit.  
       4. The problem with your email is that you have BROADCAST and TARGETED communication in one place, which means you are voluntarily dropping information. When you start prioritizing your email, you have a higher quality of information. For example:  
          1. People you MUST absolutely communicate with (spouse, close team members, top clients)  
          2. People you MAY communicate with  
          3. People you SHOULD NOT communicate with  
          4. Subscriptions you MUST read  
          5. Subscriptions you MAY read  
          6. Subscriptions you SHOULD NOT read  
          7. *Note the way that BROADCAST \+ TARGETED COMMUNICATION are mixed into the same medium, which (like packets) SLOWS DOWN even the targeted communication*  
       5. This is why when you send an email asking for volunteers, you don’t get anything, but when you ask people directly, they’ll help you.  
       6. This is why when you send a mass email to people, it goes through a different set of filters. THe power of marketing is in trying to scale something that APPEARS targeted, but as something that is BROADCAST  
   12. This is one of the ways you isolate complexity, because there are two types of communication:  
       1. INTERNAL communication – which are all the things that someone things, or does, that nobody else sees. This applies personally, as a dept, team, business, etc  
       2. EXTERNAL communication – which is how an entity communicates outside of itself  
       3. SIMPLIFICATION comes down to moving as much communication as possible to be INTERNAL, without compromising the utility of the system  
       4. Practical implications  
          1. You have a team member who is asking too many questions, given their role  
          2. You have a team member who is asking TOO FEW questions given their role  
          3. You have to fill out too much information to get a certain amount of feedback  
          4. You have to be too involved in the actual work that needs to be accomplished  
   13. You also reduce complexity by reducing the NUMBER of people you need to communicate with  
       1. If you have a department that talks to EVERYONE, it’s much less efficient than a department that talks to a REPRESENTATIVE  
       2. This does create a point of potential breakage…  
   14. You can reduce the TIMES you need to communicate with people…  
       1. If you have to communicate back and forth more frequently than necessary, it becomes an inefficient approach  
   15. All information should have a SINGLE SOURCE OF TRUTH  
       1. Otherwise, you will be forced to resolve   
3. Trees are inherently **fractal**, and their behavior follows a power curve  
   1. TODO \- Introduce the tool…   
4.   
5. Part 2 \- Tactics  
   1. Checklists  
   2. Templates  
   3. Training  
   4. Knowledge Base  
   5. Simple Repeatable Process  
   6. Software  
   7. Email  
   8. Time X-Ray  
6. Part 3 \- Delegation Revolution

Resources:

* Formula Draft  
  * [https://docs.google.com/document/d/1kLw4YxB9zaLFFLyFq-a7WmSmfemL9JLab17UPfTZUd0/edit\#](https://docs.google.com/document/d/1kLw4YxB9zaLFFLyFq-a7WmSmfemL9JLab17UPfTZUd0/edit#)  
* Systems Lessons from Software  
  * [https://docs.google.com/document/d/1OLLxDGik2PlTPFg5DimUSwupnnghgzZU2HVdFkCK1Uw/edit\#](https://docs.google.com/document/d/1OLLxDGik2PlTPFg5DimUSwupnnghgzZU2HVdFkCK1Uw/edit#)  
* Systems Journal  
  * [https://docs.google.com/document/d/10MD5BYTPfpVdzTCIjWw7ik54fw32KUsLPm0GiHy9rBs/edit\#](https://docs.google.com/document/d/10MD5BYTPfpVdzTCIjWw7ik54fw32KUsLPm0GiHy9rBs/edit#)  
* Optimization  
  * [https://docs.google.com/document/d/1tcNyBEjXFYEoBOZ4Alnvi4U2oF18c9k1YQfCsPMiE7g/edit\#](https://docs.google.com/document/d/1tcNyBEjXFYEoBOZ4Alnvi4U2oF18c9k1YQfCsPMiE7g/edit#)  
* Refactoring  
  * [https://docs.google.com/document/d/1sZ-vi0d8TNaR0qQMTkmFBNj\_elEOaF4e6z8bNn7VqTk/edit?usp=drivesdk](https://docs.google.com/document/d/1sZ-vi0d8TNaR0qQMTkmFBNj_elEOaF4e6z8bNn7VqTk/edit?usp=drivesdk)  
  *   
* [https://zch.apphosting.zone/Detail/Edit/2?RecordType=WikiPages\&NumberID=-241\&State=absb0jn2QnI&](https://zch.apphosting.zone/Detail/Edit/2?RecordType=WikiPages&NumberID=-241&State=absb0jn2QnI&)  
*   
* Risk Free Delegation  
* Rapid Email Triage  
* Inbox Zero Challenge

What we’ve learned:

* Marketing  
  *   
* Sales  
  * What are common objections?  
  * How to frame thinking?  
  * What’s the 80/20 sales training?  
  * Production information  
  * Taking payment  
  * Handoff process  
  * Lead followup  
* Fulfillment  
  * Internal Tasks \- Project Management  
  * Onboarding  
  * Call Agendas / Schedules  
  * Upsell Pricing  
* Client Support  
  * Templates  
  * Product Documentation  
  * Internal Tutorials  
  * Common Issues  
  * ***We ESPECIALLY have documentation for clients who self-host their systems. We are actually MORE careful.***  
* Other Examples  
  * Hiring Process (including Onboarding – which accounts to create, what to do on the first day, etc)  
  * Core Foundations  
* Internal Tutorials  
  * Use of specific software tools  
  * Ongoing processes (PTO, etc etc)  
* Job Descriptions  
* Role Training  
* Virtual Receptionist

# System Optimization

1. Introduction

	a.  What is the tree structure process hierarchical process in optimization?  
b.  2 questions to ask?  
	i. When you go to the first step of any kind of optimization issue, find the worst             case scenario first of all  
		ii. How do you exaggerate the problem? 

2. Part 1  
1. 
