
# Backwards Reachability: A Tutorial

  This is a project about safety analysis for safety critical dynamic systems. 
  
  In the context of a dynamic system, the [backwards reachable set][]{:target="_blank"} (BRS) describes all initial states that can reach a given target set of final states within a certain duration of time. If one can efficiently compute such sets, there is potential to use them to make safety guarantees for various autonomous systems, by determining whether some potential unsafe state will, in principle, ever be reached by a given policy. 
  
  In this tutorial, we describe the tools currently available to tackle this problem and how to use them. We also talk briefly about good and bad ways to think about the problem, from our own experience and time spent working on it.

  An additional component of this project is to make BRSs easier to compute for non-linear systems by "linearizing" them using [Koopman operator theory][]{:target="_blank"}.


[backwards reachable set]: https://people.eecs.berkeley.edu/~somil/Papers/Introduction_to_Reachability_to_Share.pdf
[toolbox]: https://www.cs.ubc.ca/~mitchell/ToolboxLS/
[Koopman operator theory]: https://www.mit.edu/~arbabi/research/KoopmanIntro.pdf


## Prerequisites 

- Math 
  - [Linear Algebra][]{:target="_blank"}
  - [Differential Equations][]{:target="_blank"}
    - In terms of the theory, pretty much everything in reachability comes down to solving non-linear (often partial) differential equations. The more comfortable you are with them, the better.     

<!-- &nbsp; -->
- Programming
  - Python (Future toolboxes should have python interfaces)
  - MATLAB (Currently the most well-documented toolbox is in MATLAB)
  - C++ (For the low level implementations of the algorithms and GPU support)


## Resources     
- Control Theory
  - [Control Theory Basics][]{:target="_blank"} (first six videos are relevant)
  - [Dynamical Systems][]{:target="_blank"}

<!-- &nbsp; -->
- Reachability
  - [Hamilton-Jacobi Reachability Tutorial: Basics of HJ Reachability][]{:target="_blank"}
  - [Hamilton-Jacobi Reachability: A Brief Overview and Recent Advances][]{:target="_blank"}
  - [Reachability and Controllability Review][]{:target="_blank"} (you can skim after section 4.5)  
  - [Introduction to Reachability](https://people.eecs.berkeley.edu/~somil/Papers/Introduction_to_Reachability_to_Share.pdf){:target="_blank"}
  - [Comparing Forward and Backward Reachability as Tools for Safety Analysis](https://www.cs.ubc.ca/~mitchell/Papers/myHSCC07.pdf){:target="_blank"}

<!-- &nbsp; -->
- Techniques for "Linearizing" Non Linear Systems:
  - [Dynamic Mode Decomposition][]{:target="_blank"} (to approximate Koopman operator)
  - [Koopman Spectral Analysis][]{:target="_blank"}


  [Dynamical Systems]: https://www.youtube.com/playlist?list=PLqA5alXk-vhjrx1KxRdA2cq-5YnnXSNSK
  [Control Theory Basics]: https://www.youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m
  [Linear Algebra]: https://youtu.be/fNk_zzaMoSs
  [Differential Equations]: https://youtu.be/p_di4Zn4wz4
  [Hamilton-Jacobi Reachability Tutorial: Basics of HJ Reachability]: https://youtu.be/iWsfc107nRc
  [Hamilton-Jacobi Reachability: A Brief Overview and Recent Advances]: https://arxiv.org/abs/1709.07523
  [Reachability and Controllability Review]: http://www.dii.unimo.it/~zanasi/didattica/Teoria_dei_Sistemi/Luc_TDS_ING_2016_Reachability_and_Controllability.pdf
  [Koopman Spectral Analysis]: https://www.youtube.com/playlist?list=PLqA5alXk-vhisuj1TPPxl43__7vza--q0
  [Dynamic Mode Decomposition]: https://www.youtube.com/playlist?list=PLqA5alXk-vhjoCnv4-5Ql_IFRU2xeXyhG

    

## Toolbox Setup

- ### HelperOC toolbox (written by Sylvia Herbert, Mo Chen and others) <br /> [*MATLAB* ]

  This is a MATLAB toolbox (that uses another toolbox) to compute backwards reachable sets. Currently it is the most well documented and easiest to use.

  If you don't know how to install toolboxes in MATLAB you can find [basic MATLAB tutorials here][]{:target="_blank"} but I think you'd be better off just asking someone who knows MATLAB to spend 30 minutes showing you the basics.

  Steps:

  1. Install MATLAB
  2. Follow the instructions to download and install the [levelset toolbox][]{:target="_blank"}
  3. Follow the instructions to download and install the [helperOC toolbox][]{:target="_blank"}
  4. In the helperOC repo, there is a file called [tutorial.m][]{:target="-blank"} that goes through the basics of using the toolbox. You should experiment with it until you feel comfortable.
  
  Here are some questions I asked [Sylvia Herbert][]{:target="_blank"} while I was working on this, you may treat it as a guidance and it may provide some clarifications. 

  [Sylvia Herbert]: http://sylviaherbert.com/ 
  
  ### Short FAQ: 

  - <span style="color:dodgerblue"> *Ali* : </span> You make a cylinder target set and ignore the $\theta$ dimension, but there doesn't seem to be an ignore dimension option while creating other shapes? Is this only an option for cylinders?

    <span style="color:limegreen"> *Sylvia* :</span> Let's say I have a rectangular target set in position space (from -1 to 1), but my state space contains position x and velocity v.  I would make something like `shapeRectangleByCorners(grid, [-1 -inf], [1, inf])`.  I'm essentially saying that this set is between -1 and 1 in position space, and through all of velocity space.  So that essentially ignores the velocity dimension.  If you're ever curious about the shaping functions you can just open the function and take a look--they're generally pretty simple.


  - <span style="color:dodgerblue"> *Ali* : </span> How do I combine shapes? You say in your HJR paper that "the obstacles should then be combined in a cell structure and set to `HJIextraArgs.obstacles`", I'm not sure how to do this.

    <span style="color:limegreen"> *Sylvia* :</span> You can do things like `shapeUnion` and `shapeIntersect`.  You can also create your own signed distance function if you have some really weird shape (again I'd recommend looking into the shaping functions to see how it's done).


  - <span style="color:dodgerblue"> *Ali* : </span> How do I label the axis(s) in the grid object? It's hard to figure out what effect my changes are having when I don't know whats changing.

    <span style="color:limegreen"> *Sylvia* :</span> If you type `edit HJIPDE_solve` into the command like it'll bring up that function.  You'll see at the top we have a lot of instructions on all the bells and whistles you can add to the computation.  One of them is to say (for example) `extraArgs.visualize.xTitle = 'x'; extraArgs.visualize.yTitle = 'v'`.


  - <span style="color:dodgerblue"> *Ali* : </span> Why does it make the corkscrew pattern? The dubins car only has an x and y position geometrically so like, shouldn't it just make a bigger cynlinder around the target cylinder?

    <span style="color:limegreen"> *Sylvia* :</span> Great question! Let's consider a particular slice in x and y at $\theta$ = 0 (i.e. the car is pointed to the right).  If the car is to the left of the set and pointing to the right, it's headed straight for the target set (and therefore will enter the target set, making this initial state part of the reachable set).  However, if the car is to the right of the target set, it's facing away from the set and will need more time to turn around and head for the set.  Therefore, at different orientations (i.e. different slices of $\theta$) the initial positions that will enter the target set in the time horizon are different. 

- ### Optimized DP  (by Mo Chen and others) Using BEACLS (by Ken Tanabe, Somil Bansal and others) <br />  [*Python interface, C++ implementation* ]

  This Python project is currently in a work in progress, and the C++ library called BEACLS (which is just a C++ version of the helperOC + LevelSet toolboxes with GPU support) that it is based on is relatively recent, and does not have comprehensive tutorials as of yet. So there's a fair amount of trial and error here, but it's most likely the way forward in the long term.

  I'd recommend creating a new Python virtual environment with conda for using this tool as well. If you don't know what those are, you should [really][]{:target="_blank"} [change that][]{:target="_blank}.

  1. Clone the [optimized_dp][]{:target="_blank"} repo and follow the instructions in the readme
  2. You'll need to install [HeteroCL][]{:target="_blank"} library as well (the virtual env comes in handy here)
  3. Define your problem in the user_definer.py and then run solver.py. <br />
    NOTE: The solver.py file launches a web browser to plot the result and it may be unable to do so if you run it from an integrated terminal like in VSCode. It's really tragic, but you gotta open a normal terminal and run it there :(

  As mentioned before, this is still a work in progress so be prepared to have things not work exactly and to experiment. 








[basic MATLAB tutorials here]: https://www.mathworks.com/help/matlab/getting-started-with-matlab.html
[levelset toolbox]: https://www.cs.ubc.ca/~mitchell/ToolboxLS/
[helperOC toolbox]: https://github.com/HJReachability/helperOC
[tutorial.m]: https://github.com/HJReachability/helperOC/blob/master/tutorial.m

[really]: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
[change that]: https://towardsdatascience.com/virtual-environments-104c62d48c54
[optimized_dp]: https://github.com/SFU-MARS/optimized_dp
[HeteroCL]: http://heterocl.csl.cornell.edu/doc/installation.html




# Reachability Notes 

## What is Reachability?

Reachability formalizes the idea of 

**"what states in the _configuration space_ can you reach as time passes".**

### Configuration space?

A mistake I made when first trying to understand this was that I thought about this purely geometrically. As in, only thinking about location, and not _configuration_. A good counterexample is to think of the reachability sets of Rubick's cube configurations. Here the set is discrete, discontinuous and it doesn't make sense to describe it with Euclidean space. Yet you can still perform reachability analysis on it.


![Rubicks](https://media.giphy.com/media/kFuavIYvRQZGg/giphy.gif)

That being said, most reachability problems will involve navigating some physical space.

## In two (simple) dimensions...

Here is a simple geometric example involving a [Dubin's Car][]{:target="-blank"}: You can see the set of all the possible "locations" that are reachable increase as time increases. 

In this example, the green box represents the set of all possible initial positions, and as time passes, the blue "box" representing the set of all points reachable by starting from somewhere in the green box grows. So when **t = N seconds**, the blue box represents all the points you could possibly reach in **N seconds**, if you started at somewhere in the green box. 

You can read more about a Dubin's Car in Steve LaValle's [Planning Algorithms textbook][]{:target="_blank"}

Example 1: 
![Reach](https://i.imgur.com/OPUjO6G.gif)

## Okay, but...

But this example just begs the question **"How exactly does the set grow with respect to time?"** <br /> (You might even question the assumption that the set should always grow ( which it does *not* )).

### What determines the set?

There are two main things that determine the transformation of the reachable set with respect to time. The **_dynamics_** of the system, and the **_policy_**. <br />
(Again, you may interject with "Isn't the policy technically just a part of the dynamics?" and in a sense, yes, that's a perfectly valid way to think about it but for the purposes of this project it is useful to treat them as separate)

### What do we mean by policy?

The word policy depends on context. 

Typically in reinforcement learning, we think of policies as a **function**, as in, given a state, it picks *exactly one* action to take. 

In reachability analysis, what is typically meant by policy is a [*bang bang policy*][]{:target="_blank"}, which essentially means you go full speed in the optimal direction. It's called bang bang because it switches abruptly between (usually) two states, such as go left and go right.

For the purposes of this project, policy can mean either of those things. Here we think of policies simply as **_restrictions placed on the agents movement through the configuration space_**. 

A policy could be "stay at least two feet away from the walls", such a policy would forbid picking an action that gets you too close to a wall in the environment, but otherwise doesn't choose one action over another. The restriction may be "use a heuristic to compute a reward for each possible action, and pick the action with the highest reward (ties can be broken randomly)", this is a restriction that narrows down your options to exactly one for each state, and therefore results in a function. 

The example above has no meaningful policy. Any action in the action space is allowed, so the dynamics are the only restriction, hence the set grows sharply in all directions, limited only by the speed of the car and its turning radius.

[*bang bang policy*]: https://en.wikipedia.org/wiki/Bang%E2%80%93bang_control#Bang%E2%80%93bang_solutions_in_optimal_control

## Different Policies?

Here is another example where the policy is "go straight" (or "don't turn").

Example 2: 
![WithPolicy](https://i.imgur.com/ZDNcL7T.gif)

As you can see, it gets us a very different reachable set. For one, this policy **_is_ a function**, meaning that given a state, it only ever returns one action; i.e. Go one step backwards in the x direction from wherever you currently are.

In example 1, there are many (technically infinitely many) actions the policy could choose;  For example: "go right", "go left", "go a little bit left", if the dynamics allow it, even ["turn right to go left"][]{:target="_blank"}

## Noise / Disturbance 

Something else you might notice if you look closely at example 2 is that the boundary of the set gets "smoother" with time, this is because of noise (tiny disturbances in your input and output that inevitably affect your system in the real world). You can add more or less noise to the dynamics in either toolbox as a parameter.

This brings me to my next point, which is that one can also leave the policy constant and change the dynamics, which is why it's useful to think of them as separate. 

## Different Dynamics?

In example 3, the policy is simply "always turn right", in example 4, its the exact same policy, but with a lot more noise.

Example 3: 

![swirly](https://i.imgur.com/B8tjlmn.gif)

Example 4: Lots of noise

![damped_swirly](https://i.imgur.com/xAugfTf.gif)

## But you said *backward*...

At this point you may be wondering **"Okay, but why is it called _backward_ reachability?"**

The unsatisfying answer is that for this project, we're focused on extrapolating backwards from unsafe states. The satisfying answer is because backwards and forward reachability are essentially the same thing.

### The same, really?

It is easy to miss the profundity of this statement. The fact that the dynamical laws of physics — with one small exception — seem to be [symmetrical with respect to time][]{:target="_blank"} is something that really surprised me when I first found out about it,and frankly it continues to surprise me to this day. It's also important to remember that time is simply how we measure causality, and doesn't exist in any meaningful way *in and of itself*. 

[*Crazy*, I know.][]{:target="_blank"}

[*Crazy*, I know.]: https://i.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy-downsized-large.gif


Anyways, given that backwards reachability analysis is essentially the same as forward reachability analysis, there is a lot of potential to leverage the backwards version in solving problems regarding safety critical systems.

### If they're the same, what's the difference?

You can think about forward reachability as determining to *what* states in the *future* is your current policy going to take you, and whether those states are good or bad.

You can think about backward reachability as: *given* a certain good or bad future state, what *previous* states would you have to cross to get there, and whether or not you should seek or avoid such states, respectively.

From a computation perspective, its pretty much identical.

[symmetrical with respect to time]: http://math.ucr.edu/home/baez/time/

## What now?

After this, you can start messing around to get a feel of what's possible with the toolboxes. Here's a personal favorite.

Example ???:

![crazzy](https://i.imgur.com/ETmNGj7.gif)

## Real Life Applications 

These examples are obviously just for demonstration, when you're actually working on applications, several things are likely going to be different. For one, you're going to have a more complicated policy, you'll be working in higher dimensions, and you may have more than one moving part/ agent in the system. 

Here is an example from [Sylvia Herbert's website][]{:target="_blank"} who has some great [reachability tutorials][]{:target="_blank"} there as well.


![3d](https://bit.ly/32A9AQi)

# Conclusion 

I hope by this point you have a basic understanding of what this problem is, and why it's difficult. The papers linked to in the resources section paint a much more detailed picture, especially when it comes to the math, and the implementation of the math. I avoided that here on purpose, as showing someone the math for something before giving them a high level conceptual explanation of what the math is describing can often be counterproductive. 

But now, dear reader, you are ready. You should have a much easier (and frankly much saner) time reading through the literature on this topic, and making progress on this very cool and very interesting problem. 

I don't know much about partial differential equations, lagrangian mechanics or hopf-lax formulas, but I can offer you a kernel of wisdom that often helps me put things in perspective: 

> "It might be well for all of us to remember that, while differing widely in the various little bits we know, in our infinite ignorance we are all equal." <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Karl Popper, Conjectures and Refutations

Good luck.








[Dubin's Car]: https://gieseanw.wordpress.com/2012/10/21/a-comprehensive-step-by-step-tutorial-to-computing-dubins-paths/

[Planning Algorithms textbook]: http://planning.cs.uiuc.edu/node657.html#sec:wheeled
["turn right to go left"]: https://youtu.be/-7Ra1LMYphM
[Sylvia Herbert's website]: http://sylviaherbert.com/
[reachability tutorials]: http://sylviaherbert.com/reachability-decomposition


<!-- 

Links
-----

For a URL or email, just write it like this:

<http://someurl>

<somebbob@example.com>


To use text for the link, write it [like this](http://someurl).

You can add a *title* (which shows up under the cursor), 
[like this](http://someurl "this title shows up when you hover").

Reference Links
---------------

You can also put the [link URL][1] below the current paragraph like [this][2].

   [1]: http://url
   [2]: http://another.url "A funky title"

Here the text "link URL" gets linked to "http://url", and the lines showing 
"[1]: http://url" won't show anything.


Or you can use a [shortcut][] reference, which links the text "shortcut" 
to the link named "[shortcut]" on the next paragraph.

   [shortcut]: http://goes/with/the/link/name/text


## Welcome to GitHub Pages


You can use the [editor on GitHub](https://github.com/rvl-lab-utoronto/backwards-reachability/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown file(sss).

### Markdown

Markdown is a lightweight and easy-to- for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block
```
# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)


For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/rvl-lab-utoronto/backwards-reachability/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out. -->
