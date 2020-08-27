
# Backwards Reachability: A Tutorial

## Project Description
  The [backwards reachable set][]{:target="_blank"} (BRS) describes all initial states that can reach a given target set of final states within a certain duration of time. We hope to use it as a safety guarantee for self-driving vehicles by computing the BRS with control policies from a set of final states that involve accidents and avoiding being in states from the BRS. We utilize Ian Mitchell's level set method [toolbox][]{:target="_blank"} and the HelperOC toolbox by Sylvia Herbert, Mo Chen and others to compute the BRS (instruction below). 

  The second component of this project is to contribute a new way of computing the BRS for nonlinear systems such as for a self-driving car. We would use the [Koopman operator][]{:target="_blank"} to decompose and transform the nonlinear system into special measurement coordinate so it appears to be a linear system. We would then compute the BRS for the linear system that the nonlinear system has turned into using simple matrix manipulation and multiplication. We should be able to verify the results of this method with the previously mentioned approach that directly computes the BRS for a nonlinear system.  


[backwards reachable set]: https://people.eecs.berkeley.edu/~somil/Papers/Introduction_to_Reachability_to_Share.pdf
[toolbox]: https://www.cs.ubc.ca/~mitchell/ToolboxLS/
[Koopman operator]: https://www.mit.edu/~arbabi/research/KoopmanIntro.pdf


## Prerequisites 

- Math 
  - [Linear Algebra][]{:target="_blank"}
  - [Differential Equations][]{:target="_blank"}
    - In terms of the theory, pretty much everything in reachability comes down to solving non-linear (often partial) differential equations. The more comfortable you are with them, the better.     

<!-- &nbsp; -->
- Programming
  - Python (Future toolboxes should have python interfaces)
  - MATLAB (Currently the most well-documented toolbox is in Matlab)
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

  This is a matlab toolbox (that uses another toolbox) to compute backwards reachable sets. Currently it is the most well documented and easiest to use.

  If you don't know how to install toolboxes in matlab you can find [basic matlab tutorials here][]{:target="_blank"} but I think you'd be better off just asking someone who knows matlab to spend 30 minutes showing you the basics.

  Steps:

  1. Install matlab
  2. Follow the instructions to download and install the [levelset toolbox][]{:target="_blank"}
  3. Follow the instructions to download and install the [helperOC toolbox][]{:target="_blank"}
  4. In the helperOC repo, there is a file called [tutorial.m][]{:target="-blank"} that goes through the basics of using the toolbox. You should experiment with it until you feel comfortable.
  
  Here are some questions I asked Sylvia Herbert while I was working on this, you may treat it as a short FAQ: 

  - <span style="color:dodgerblue"> *Ali* : </span> You make a cylinder target set and ignore the theta dimension, but there doesn't seem to be an ignore dimension option while creating other shapes? Is this only an option for cylinders?

    <span style="color:limegreen"> *Sylvia* :</span> Let's say I have a rectangular target set in position space (from -1 to 1), but my state space contains position x and velocity v.  I would make something like shapeRectangleByCorners(grid, [-1 -inf], [1, inf]).  I'm essentially saying that this set is between -1 and 1 in position space, and through all of velocity space.  So that essentially ignores the velocity dimension.  If you're ever curious about the shaping functions you can just open the function and take a look--they're generally pretty simple.


  - <span style="color:dodgerblue"> *Ali* : </span> How do I combine shapes? You say in your HJR paper that "The obstacles should then be combined in a cell structure and set to HJIextraArgs.obstacles" I'm not sure how to do this.

    <span style="color:limegreen"> *Sylvia* :</span> You can do things like shapeUnion and shapeIntersect.  You can also create your own signed distance function if you have some really weird shape (again I'd recommend looking into the shaping functions to see how it's done)


  - <span style="color:dodgerblue"> *Ali* : </span> How do I label the axis(s) in the grid object? It's hard to figure out what effect my changes are having when I don't know whats changing.

    <span style="color:limegreen"> *Sylvia* :</span> If you type "edit HJIPDE_solve" into the command like it'll bring up that function.  You'll see at the top we have a lot of instructions on all the bells and whistles you can add to the computation.  One of them is to say (for example) extraArgs.visualize.xTitle = 'x'; extraArgs.visualize.yTitle = 'v'


  - <span style="color:dodgerblue"> *Ali* : </span> Why does it make the corkscrew pattern? The dubins car only has an x and y position geometrically so like, shouldn't it just make a bigger cynlinder around the target cylinder?

    <span style="color:limegreen"> *Sylvia* :</span> Great question! Let's consider a particular slice in x and y at theta = 0 (i.e. the car is pointed to the right).  If the car is to the left of the set and pointing to the right, it's headed straight for the target set (and therefore will enter the target.set, making this initial state part of the reachable set).  However, if the car is to the right of the target set, it's facing away from the set and will need more time to turn around and head for the set.  Therefore, at different orientations (i.e. different slices of theta) the initial positions that will enter the target set in the time horizon are different.  I hope that made sense

- ### Optimized DP  (by Mo Chen and others) which uses BEACLS (by Ken Tanabe, Somil Bansal and others) <br />  [*Python interface, C++ implementation* ]

  This Python project is currently in a work in progress, and the C++ library called BEACLS (which is just a C++ version of the helperOC + LevelSet toolboxes with GPU support) that it is based on is relatively recent, and does not have comprehensive tutorials as of yet. So there's a fair amount of trial and error here, but it's most likely the way forward in the long term.

  I'd recommend creating a new Python virtual environment with conda for using this tool as well. If you don't know what those are, you should [really][]{:target="_blank"} [change that][]{:target="_blank}.

  1. Clone the [optimized_dp][]{:target="_blank"} repo and follow the instructions in the readme
  2. You'll need to install [HeteroCL][]{:target="_blank"} library as well (the virtual env comes in handy here)
  3. Define your problem in the user_definer.py and then run solver.py. <br />
    NOTE: The solver.py file launches a web browser to plot the result and it may be unable to do so if you run it from an integrated terminal like in VSCode. It's really tragic, but you gotta open a normal terminal and run it there :(

  As mentioned before, this is still a work in progress so be prepared to have things not work exactly and to experiment. 








[basic matlab tutorials here]: https://www.mathworks.com/help/matlab/getting-started-with-matlab.html
[levelset toolbox]: https://www.cs.ubc.ca/~mitchell/ToolboxLS/
[helperOC toolbox]: https://github.com/HJReachability/helperOC
[tutorial.m]: https://github.com/HJReachability/helperOC/blob/master/tutorial.m

[really]: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
[change that]: https://towardsdatascience.com/virtual-environments-104c62d48c54
[optimized_dp]: https://github.com/SFU-MARS/optimized_dp
[HeteroCL]: http://heterocl.csl.cornell.edu/doc/installation.html




# Reachability Notes 

Reachability formalizes the idea of 

**"what states in the _configuration space_ can you reach as time passes".**

A mistake I made when first trying to understand this was that I thought about this purely geometrically. As in, only thinking about location, and not _configuration_. A good counterexample is to think of the reachability sets of Rubick's cube configurations. Here the set is discrete, discontinuous and it doesn't make sense to describe it with Euclidean space. Yet you can still perform reachability analysis on it.

![Rubicks](https://media.giphy.com/media/kFuavIYvRQZGg/giphy.gif)

Here is a simple geometric example involving a [dubin's car][]{:target="-blank"}: You can see the set of all the possible "locations" that are reachable increase as time increases.  

![Reach](https://i.imgur.com/OPUjO6G.gif)





[dubin's car]: https://gieseanw.wordpress.com/2012/10/21/a-comprehensive-step-by-step-tutorial-to-computing-dubins-paths/




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

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
