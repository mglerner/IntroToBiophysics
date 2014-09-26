Introduction To Biophysics (PHYS 225/BIOL 225) (SI non-lab, A-QR)
========================================================

**TODO** revamp for two 80 minute class per week, rather than three 50
  minute classes.

When people ask me what it means to be a Biophysicist, my stock answer
is "I like to think like a physicist, but am fascinated by problems
that come from biology." **Introduction to Biophysics** is an
introduction to that mindset, summed up wonderfully by the back-cover
of [Physical Biology of the Cell][PBoC]:

> *Physical Biology of the Cell* maps the huge and complex landscape
> of cell and molecular biology from the distinct perspective of
> physical biology. As a key organizing principle, the proximity of
> topics is based on the physical concepts that unite a given set of
> biological phenomena. Herein lies the central premise: that the
> appropriate application of a few fundamental physical models can
> serve as the foundation of whole bodies of quantitative biological
> intuition, useful across a wide range of biological problems.

What sorts of patterns do we expect to find in biology? Can physics
let us determine whether a process in the cell is governed by random
diffusion, or whether active transport (molecular motors) are needed
to move things from one part of a cell to another? How does dialysis
work (spoiler: entropy!)? What are the main forces governing protein
folding? We'll develop a small number of fundamental physical models,
and apply them to a broad range of biological problems. These physical
models give us both a new perspective on biology and a way of gaining
quantitative biological intuition across that range of problems.

## Learning Goals ##

In addition to specific content-related learning objectives, the
course has several non-content, "course-scale" learning
objectives. During this course, successful students will

  * Develop problem solving skills and the ability to connect
    concepts between physics, biology, chemistry and mathematics to
    understand how biological systems function.
  * Use simple physical models to provide quantitative insight into
    biological systems.
  * Gain exposure to the important questions in the modern field of
    molecular biophysics and evaluate current research on a system
    of their choice.
  * Mature in knowledge organization and communication, gaining in
    ability to justify and explain approches and solutions to
    problems, either in written or oral form; be able to articulate
    big ideas from each content area.

## Textbook(s) ##

I'm still deciding on the main (*required*) textbook. There are three
front runners at the moment:

 * [Biological Physics][BiolPhys]
 * [Physical Biology of the Cell, Second Edition][PBoC]
 * [The Molecules of Life][MolLife]

[Nelson][BiolPhys] is a most definitely physics book, but it's less math-intensive
and more readable that many other physics texts. It's the most likely
choice at this point.

Whichever we choose, we'll use the others as significant secondary
resources. We'll use PBoC's
[companion site](http://microsite.garlandscience.com/pboc2/).

Phil Nelson has some great material on his
[website](http://www.physics.upenn.edu/~pcn/), especially the recent talks.

We will not cover the whole book; see below for a list of topics. Other people
have taught similar courses, and some have been kind enough to put
their course materials online
(e.g. [SFU](http://www.sfu.ca/phys/347/),
[Cambridge](http://www.damtp.cam.ac.uk/user/gold/teaching_biophysicsIII.html)).

For more supplemental information, we'll use Phil Nelson's
(in-progress) book [Physical Models of Living Systems][PMLS], the
whole of which is absolutely worth reading, but is more suited to an
upper-level class.

You may be surprised to learn that some of the most famous physicists
were also *Biophysicists*! Einstein's "Miracle year" (1905) is
so-called because of the four papers he wrote. One of those papers
explained for the first time the connection between the macroscopic
motion of particles in a fluid (diffusion) and the microscopic motion
of individual molecules buffeted by thermal forces. Believe it or not,
this was one of the main pieces of work that convinced physicists and
chemists to believe in *atoms*! Schrodinger's classic short book
[What is Life? (free PDF)][WhatIsLife] has inspired countless
scientists, and Watson and Crick both
[credit](http://www.human-nature.com/nibbs/04/erwin.html) it with
motivating their famous discovery of the structure of DNA!

William Bialek's Biophysics:
[Searching for Principles](http://www.princeton.edu/~wbialek/PHY562.html)
is a graduate-level text, but is nice and free online.

Duke's [Biophysics](http://www.phy.duke.edu/learning-about-biophysics)
website has a nice set of pointers to other resources.

[PBoC]: http://www.garlandscience.com/product/isbn/9780815344506 "Physical Biology of the Cell"

[BiolPhys]: http://www.physics.upenn.edu/~biophys/ "Biological Physics"

[MolLife]: http://www.garlandscience.com/product/isbn/9780815341888 "The Molecules of Life"

[PMLS]: http://www.physics.upenn.edu/biophys/PMLS/index.html "Physical Models of Living Systems"

[WhatIsLife]: http://whatislife.stanford.edu/LoCo_files/What-is-Life.pdf "What is Life?"



## Prerequisites ##

* **One semester of calculus-based physics is required.** We'll be
  asking the question "what are the physical concepts that unite a
  given set of biological phenomena," and we'll find that a
  surprisingly small number of physical models can give us a
  shockingly good quantitative biological intuition. We do need to
  know some physics as background, and we will need to discuss rates
  of change. To be clear about the mathematical level here, we will
  spend most of our time using beautiful formulas to understand
  nature; later physics classes will give you a chance to look deeply
  and carefully at the detailed derivations of those formulas.
  Students who have taken (non-Calculus based) physics 120 and a
  calculus class (in high school or college) need the consent of the
  instructor.

* Biol 112, "Cells, Genes and Inheritance" is *recommended* as a
  pre-requisite or co-requisite, but is **not required**. It will give
  you a broader background (and a different perspective) on the
  subject, but we'll introduce the biology as it comes up throughout
  the course.

* Computer models are becoming more and more important in modern
  science across the board. These days, tools like
  [IPython Notebooks][IPyNBG] make it surprisingly easy to create,
  tweak and share computational models. We'll be *using* and playing
  with models that I create throughout the course. However, you have a
  great opportunity to learn how to *create* these things yourself:
  Earlham is hosting a two-day Python Bootcamp, led by
  [Software Carpentry](http://software-carpentry.org/). It'll be
  hosted on Earlham's campus, January 11-12, 2015 (that's the
  Sunday/Monday before Spring classes, so housing should not be a
  problem). The ability to build and tweak simple computational models
  *greatly* expands the types of questions you can ask (and answer!)
  by yourself. This two-day bootcamp will teach you all the Python you
  need to get started right away, and it's **completely free**! To be
  clear: this is *recommended* but **not required**.  If you're
  interested, but absolutely can't make it to the bootcamp, you can
  discuss working through the bootcamp lessons (or the
  [Code Academy][CodeAcademy] lessons) independently.

[IPyNBG]: https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks "IPython Notebook Example Gallery"

[CodeAcademy]: http://www.codecademy.com/ "Code Academy"


## Course Structure and Grades ##

  * Reading assignments and Moodle participation: 10%. This course
    covers a fantastically wide variety of topics, and students come
    from a wide variety of backgrounds with a corresponding variety of
    interests. All of that means that we'll want to have great
    in-class discussions, and focus on the most important/interesting
    parts. We can only do that if you've done the reading ahead of
    time. To ensure that you're prepared for class, and to ensure that
    I'll be able to focus on the parts that are giving you the most
    trouble, you will be **required to post to the Moodle site by 8PM
    the night before each class**. Your post should include what you
    thought was most interesting and most important from the
    reading. You should also be sure to mention any parts of the
    reading that were particularly hard to understand.

  * Clicker questions and participation: 5%. We'll use clicker
    questions, think-pair-share, and other active learning techniques
    to supplement in-class discussion. These are designed to assess
    the overall class and to inspire discussion; your grade on this
    portion will be based on the percentage of the questions that you
    answer.

  * Research project: 15%. One of the main goals for the class is to
    get you to the point where you can read about current, active
    research topics. Your research project consists of two parts: a
    paper and a presentation. Each student will choose a biomolecular
    system that is interesting to her/him, and search the modern
    biophysical literature for 2-3 papers that use experimental and/or
    theoretical methods to address the structure, function, and/or
    dynamics of the system.  The paper should be approximately 7-8
    pages in length (including a couple of figures and a
    bibliography). Proposals for the project will be due half way
    through the course, and 1-2 rough drafts will be required. The
    presentation should be 15 minutes in length.  Questions that
    should be addressed in both the paper and the presentation include
    (but are obviously not limited to):

      * Why is this system important and interesting?

      * What were the methods used in the studies?

      * How do these studies complement each other?

      * What did the studies find, and how does that relate to
        things we've learned in class?

      * What are the outstanding questions that these studies have
        left, and how could those questions be answered?

  * Homework: 35%. Homework will be assigned at the end of each
    chapter, and you'll have approximately one week to complete each
    assignment. You can turn in an assignment up to one class day late
    for 80% credit, and up to a week late for 50% credit. After that,
    you may receive 25% credit for the assignment, but the grading
    will be significantly less detailed. When calculating your
    homework grade, I will drop the worst single assignment grade
    (e.g. if there are 10 assignments, I'll average the best
    9). Homework problems will be graded on the same scale used in
    Physics 125 and 235:

      * **5 points** Correct or close-to-correct solution with maybe
        a small sign or arithmetic error.

      * **4 points** Correct reasoning for the solution with maybe
        an algebra error.

      * **3 points** Small or single mistake in reasoning for
        solution, but correct follow-through.

      * **2 points** Large or multiple mistakes in reasoning for
        solution, or substantive but incomplete problem-solving.

      * **1 point** Some (written) attempt at problem solving.

      * **0 points** No attempt.
  
  * Exams: 35%. The final will be worth 15% of your grade. The other
    two midterm exams will combine for 20%, but I'm kind in the
    weighting: if you do better on one of the midterms, I will
    retroactively make it worth 15%, while your lower score becomes
    worth 5%. The re-weighting is done on a per-student basis, and
    won't be done if it lowers your grade instead of raising
    it. Further, students can **redo** missed exam problems to earn
    extra credit on their overall homework grade.

## Modules/Topics ##

We'll follow Nelson in order, although we'll pick and choose among the
chapters and sections based both on my opinions and *your*
interests. As described above, a research project (paper and
presentation) is a key component of the class. We expect to cover the
majority of Chapters 1-8 and selected sections from chapters 9
and 10. As a biophysicist, chapters 9, 10, 11 and 12 are near and dear
to my heart, and make a great set of ideas for your independent
projects!

Even though this is not a lab class, it's grounded in the physical
world, and we will collaborate with a lab at South Dakota State
University to watch *individual* lipids diffusing in a membrane. We'll
compare these to both our theoretical results and some simple
computational models of diffusion.

### Introduction to physical principles and cellular/molecular biology ###

**Mysteries, Metaphors and Models** The first two chapters, "What the
Ancients Knew" and "What's Inside Cells" set the stage for the whole
course. What do we care about here, and how will we approach
problems? Ballpark estimate: 4 class days.

### "Heat" is molecules moving ###

Chapter three asks "what's the ideal gas law, and where does it come
from?" This will give us a chance to learn a bit about probability and
make sure we understood the kinetic theory of gas as it was presented
in intro physics. If you took physics 125, this will almost all be
review! Ballpark estimate: 2 class days.

### Random Walks, Friction and Diffusion ###

Chapter four gives us our first real shot at taking a physicist's
perspective on biology, and it's full of good stories. We use Brownian
motion (random walks) to build up a model of diffusion and friction,
and start asking questions like: a single-celled bacterium living in a
lake needs oxygen to survive. Given that, is there a physical limit on
how big a bacterial cell can actually be? Ballpark estimate: 6
class days.

### Diffusion in membranes ###

(Instructor-provided materials) Somewhat shockingly, the physics
governing diffusion in two dimensions is significantly different from
the three-dimensional laws. Since cell membranes are so thin as to
essentially be two-dimensional, it seems like we ought to figure
something out about how diffusion works in 2D. We'll cover some
theory, and we'll also team up with Adam Hoppe at South Dakota State
University to actually measure *individual* lipid molecules diffusing
in membranes. Will the real data match our theory?  Ballpark estimate:
2 class days.

### On a small scale, viscous forces *dominate* inertial forces ###

(Chapter 5) Cells moving around in a fluid environment see a
*fundamentally* different physical world than you do. On a pool table,
the inertial forces we learned about in the mechanics part of intro
physics tell you everything you need to know. For a bacteria swimming
in a lake, inertial forces are far less important than viscous
forces. The **Reynolds number** is a relationship between speed, size,
density and viscosity that characterizes the relationship between
these types of forces. We'll learn just how different the world is at
low Reynolds number, and how life manages to deal with it. Ballpark
estimate: 5 class days (more depending on how much interest there is
in additional applications).

### Disorder, Entropy and "Free Energy" ###

Chapter 6 is one of the real gems of the book. We've been talking
about energy since the first day of our first physics class, but the
real world has a secret for us: not all energy can be converted into
useful work. "Free energy" is the energy available to do useful work,
and it's direly important in analyzing and understanding biological
systems. This chapter is a bit more mathematically demanding than the
previous ones, and we want to understand the math well enough that
it's an aid to the rest of the book, rather than an impediment. So,
we'll slow down a bit and work (ha! ha!) through these pages
carefully. Ballpark estimate: 6 class days, including additional notes
on biological applications of free energy differences.

### Entropic forces at work ###

(Chapter 7) Entropy seemed like an abstract concept at first, but here we learn
that it's the main driving force for many biological processes. How
does osmosis work? How does dialysis work? What's so special about
water and how does that influence the stability and thermodynamics of
biomolecules?  (If there is time, we'll cover section 7.4, a
discussion of electrostatic interactions in ionic
environments). Ballpark estimate: 6 class days.

### Chemical forces and self assembly ###

We talk a lot about equilibrium in physics, but a lot of physics (and
**all** of biology) takes place far from equilibrium (not to put too
fine a point on it, but, in equilibrium, we're all dead). Chapter
eight asks how this deviation from equilibrium can do work, and how
different biochemical systems interact with each other. To this end,
we introduce the ideas of chemical potentials and forces, as well as
the concept of self assembly. The plan is to cover this in roughly
four days (1.5 on chemical potential and forces, a second 1.5 on self
assembly, with some time left for computer models), but I could be
persuaded to give up some of the later material and spend more time
here. Ballpark estimate: 4 days.

### Protein Folding ###

Protein folding is one of the fundamental unsolved problems of modern
biophysics. We'll discuss the forces involved and try our hand at some
online-tools for poking at this problem. Ballpark estimate: 3 days.

 * [Protein Folding Dynamics in the Cell](http://pubs.acs.org/doi/abs/10.1021/jp501866v)
 * [Fold.it tutorials](http://fold.it/portal/)

### Elastic Network Models ###

Despite our earlier focus on complex physics, it turns out that models
based on the springs we learned about in our very first semester of
physics can explain an almost unreasonable amount about how proteins
move and interact. Demian Riccardi (from the Chemistry department)
will give a guest lecture for this. Ballpark estimate: 1 day.

### Remaining Topics ###

The remainder of the course will be spent on topics from chapters
9-12. We'll nail down exactly which topics will be covered in class
after you've chosen your independent project topics (i.e. you get
first choice for your own projects). The above ballpark time estimates
are just rough estimates, so it's possible that we'll cover all or
none of these.

#### DNA cooperativity, stiffness and stretching ####

The first four sections of chapter 9 give us some basic polymer
physics, and a surprisingly good model of DNA. Ballpark estimate: 3
days.

 * [DNA: Flexibly flexible](http://www.cell.com/biophysj/abstract/S0006-3495(14)00611-0)

#### Cooperativity in other biomolecules ####

The remainder of chapter 9 extends these ideas to protein structure
and allostery. Ballpark estimate: 1-2 days.

#### Molecular machines ####

Molecular motors and other types of cellular machinery, from chapter
10 and instructor-provided materials. Ballpark estimate: 2 days.

#### Ion pumps ####

One of the mainstays of biophysical theory and experiment. Ballpark
estimate: 5 days.

#### Molecular Dynamics ####

Computers are often used to simulate biomolecules, and we can do
state-of-the-art simulations on our very own campus supercomputing
clusters. This may get folded (ha! ha!)
into the Protein Folding section. Ballpark estimate: 2 days.

#### Quantum Mechanical Simulations ####

Molecular dynamics allows us to look at an amazing variety of
processes, but it has some very important limitations. The most
obvious of those are (1) it cannot simulate the making or breaking of
bonds (2) it is bad at simulating most metals and multivalent
ions. For this, you need quantum mechanics (possible guest lecture
from Lori)! Ballpark estimate: 2 days.

#### Neurons, action potentials, neuroscience ####

Hodgkin-Huxley at least (maybe a guest lecture from Kat Bartlow). I
have a feeling that this will be taken as a project, but there are
some great resources
online, especially for computational neuroscience. E.g. Paul Gribble's Computational Modeling in Neuroscience
[course](http://gribblelab.org/compneuro/index.html) (the Oct 1-4
lectures in particular), some powerful modeling
[code](http://nbviewer.ipython.org/github/brian-team/brian-material/blob/master/2013-CNS-tutorial/03-model-fitting/slides.ipynb)
using [Brian](http://briansimulator.org/), and
[several](http://nbviewer.ipython.org/github/vargaslo/model_fitting/blob/master/model_ionic_gating_nlopt.ipynb)
[other](http://nbviewer.ipython.org/github/forrestsheldon/neurodynamics/blob/master/week_3_Dynamical_systems.ipynb)
[IPython](http://nbviewer.ipython.org/gist/coderforlife/6473989)
[notebooks](http://nbviewer.ipython.org/github/forrestsheldon/neurosci/blob/master/Stim_Cancellation_in_Cerrebellum.ipynb)
depending on your level of comfort/experience.

#### Structure and dynamics of cell membranes #######

Kalani Seu is a local experimental expert here. We may ask him to give
a guest lecture, or an interested student could interview him as part
of an individual project.


### Project presentations ###

The plan is to have 15-minute presentations, allowing three
presentations per class period. I've blocked out three days for
presentations. If we have more than nine people enrolled, we'll have
to consider shorter presentations or extra class times. Ballpark
estimate: 3 days.

## Acknowledgements ##

Both [Jeff Wereszczynski](http://mypages.iit.edu/~jwereszc/) and
[J.C. Gumbart](http://simbac.gatech.edu/) have graciously provided 
information and examples relating both to the syllabus and to the
content. 
