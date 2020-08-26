
## Prerequisites 

- [Control Theory
  Basics](https://www.youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m)
  (first six videos are relevant)


- Math 
  - [Linear Algebra](https://youtu.be/fNk_zzaMoSs)
  - [Differential Equations](https://youtu.be/p_di4Zn4wz4)
  - Koopman Spectral Analysis (recommended order below)
    1. [Overview](https://www.youtube.com/watch?v=J7s0XNT96ag&list=PLqA5alXk-vhjOeNKanHLgKhww_nCJ_bxu&index=8)
    2. [Control](https://www.youtube.com/watch?v=dx2f4exDZnU&list=PLqA5alXk-vhjOeNKanHLgKhww_nCJ_bxu&index=9)
    3. [Koopman Observable Subspaces & Finite Linear Representations of Nonlinear Dynamics for Control](https://www.youtube.com/watch?v=K5CRbC4yqnk&list=PLqA5alXk-vhjOeNKanHLgKhww_nCJ_bxu&index=10)
    4. [Koopman Observable Subspaces & Nonlinearization](https://www.youtube.com/watch?v=pnGsQAt0od4&list=PLqA5alXk-vhjOeNKanHLgKhww_nCJ_bxu&index=11)
    5. [Koopman Operator Optimal Control](https://www.youtube.com/watch?v=qOdwRel-1xA&list=PLqA5alXk-vhjOeNKanHLgKhww_nCJ_bxu&index=12)
    6. [Representations](https://www.youtube.com/watch?v=--J7F6khJD0&list=PLqA5alXk-vhjOeNKanHLgKhww_nCJ_bxu&index=13)
    7. [Continuous Spectrum](https://www.youtube.com/watch?v=JJaxltAN9Ug&list=PLqA5alXk-vhjOeNKanHLgKhww_nCJ_bxu&index=16)
    8. [Multiscale Systems](https://www.youtube.com/watch?v=J1MIaTdOL5A&list=PLqA5alXk-vhjOeNKanHLgKhww_nCJ_bxu&index=17)


- Programming
    - Python (Future toolboxes should have python interfaces)
    - MATLAB (Currently the most well-documented toolbox is in Matlab)
    - C++ (For the low level implementations of the algorithms and GPU support)
    - 
    - 


- Recommended Reading
    - [Hamilton-Jacobi Reachability: A Brief Overview and Recent
      Advances](https://arxiv.org/abs/1709.07523)
    

## Setup

- ### HelperOC toolbox

    1. Install matlab
    2. Follow the instructions to download the levelset toolbox [here](https://www.cs.ubc.ca/~mitchell/ToolboxLS/)
    3. Follow the instructions to download the helperOC toolbox [here](https://github.com/HJReachability/helperOC)
    4. You may find [this tutorial](https://youtu.be/iWsfc107nRc) helpful

# Reachability Notes 

Reachability formalizes the idea of 

**"what states in the _configuration space_ can you reach as time passes".**

A mistake I made when first trying to understand this
was that I thought about this purely geometrically. As in, only thinking about
location, and not _configuration_. A good counterexample is to think of the
reachability sets of rubick's cube configurations. Here the set is discrete, and
it doesn't make sense to describe it with Euclidean space.

![Rubicks](https://media.giphy.com/media/kFuavIYvRQZGg/giphy.gif)

Here is a simple geometric example involving a [dubin's car](https://gieseanw.wordpress.com/2012/10/21/a-comprehensive-step-by-step-tutorial-to-computing-dubins-paths/): You can see the set of all the possible
"locations" that are reachable increase as time increases.  

![Reach](https://i.imgur.com/OPUjO6G.gif)



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
