Biophysics (PHYS 3xx/BIOL 3xx) (3 credits, SI non-lab, A-QR, WI)
========================================================

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

What sorts of patterns do we expect to find in biology? Can physics let us determine whether a process in the cell is governed by random diffusion, or whether active transport (molecular motors) are needed to move things from one part of a cell to another? How does dialysis work (spoiler: entropy!)? What are the main forces governing protein folding? We'll develop a small number of fundamental physical models, and apply them to a broad range of biological problems. These physical models give us both a new perspective on biology and a way of gaining quantitative biological intuition across that range of problems. You will get to explore your own interests through a significant independent project.


## Learning Goals ##

In addition to specific content-related learning objectives, the
course has several non-content, "course-scale" learning
objectives. You can see the evolution of one of those goals
[here](http://www.mglerner.com/blog/?p=45).

  * Given a biological system, students will be able to predict relevant
    physical models.
  * Given a biological system and a physical model, students will be
    able to adapt the model to the system through quantitative
    analysis.
  * Students will gain exposure to important questions in the
    modern field of molecular biophysics, and evaluate current
    research on a system of their choice.

The list of learning proficiencies is much larger. Some broad examples include

  * Students will mature in knowledge organization and
    communication, gaining in ability to justify and explain
    approches and solutions to problems, both in written or oral
    form; be able to articulate big ideas from each content area.
  * Students will develop problem solving skills and the ability to
    connect concepts between physics, biology, chemistry and
    mathematics to understand how biological systems function.


## Textbook(s) ##


* Physical Biology of the Cell by Phillips, Kondev, Theriot, and Garcia, 2nd edition (required).
* Physical Models of Living Systems, Philip Nelson (recommended).

## Prerequisites ##

* **Two semesters of calculus-based physics is required.** We'll be
  asking the question "what are the physical concepts that unite a
  given set of biological phenomena," and we'll find that a
  surprisingly small number of physical models can give us a
  shockingly good quantitative biological intuition. 
  Students who have taken non-Calculus based physics and a
  calculus class (in high school or college) need the consent of the
  instructor.

* Biol 112, "Cells, Genes and Inheritance" and Biol 341 are *recommended*,
  but is **not required**. They will give
  you a broader background (and a different perspective) on the
  subject, but we'll introduce the biology as it comes up throughout
  the course.

## Course Structure and Grades ##

|Assignment | points |
|:----------|-------:|
| Reading and participation | 10% |
| Homework | 40% |
| Short Papers | 10% |
| Research Project | 30% |
| Midterm | 10% |

* Reading and participation: 10%. This course
  covers a fantastically wide variety of topics, and students come
  from a wide variety of backgrounds with a corresponding variety of
  interests. All of that means that we'll want to have great
  in-class discussions, and focus on the most important/interesting
  parts. We can only do that if you've done the reading ahead of
  time. To ensure that you're prepared for class, and to ensure that
  I'll be able to focus on the parts that are giving you the most
  trouble, you will be **required to post to the Moodle/Piazza site by 9AM
  the day of each class**. Your post should include what you
  thought was most interesting and most important from the
  reading. You should also be sure to mention any parts of the
  reading that were particularly hard to understand. A significant amount of learning will come from the in-class discussions, and you're expected to attend and participate actively.
  
* Homework: 40%. We'll have 6-8 homework assignments, approximately
  one every other week. These will include visualization analysis of biological structures with the program VMD, pencil-and-paper calculations using equations derived in class, and analysis of simple models using Python (no prior programming experience is needed, and analysis scripts will be provided).
  
* Short papers: 10%. The ability to critically read and digest the scientific literature is a skill that has to be learned. Therefore, we will read a few biophysics papers and devote part of a class day to discussing each. Before we discuss them in class, you will use Heather Lerner's [PaperBox](http://heatherlerner.com/teaching.php) to critique the each article and turn it in at the beginning of class.

* Research project: 30%. One of the main goals for the class is to
  get you to the point where you can read about current, active
  research topics. In the second half of the semester, you will carry out a project in which you model a chosen biophysical phenomenon or system.
  Your research project consists of two parts: a
  paper and a presentation. You will choose either a biological phenomenon (e.g. how do the patterns on the shells of poisonous sea snails form?) or a biomolecular system that is interesting to you. In the former case, you will design and implement a model (including equations and/or code), with which you can produce and analyze output for comparison with real data. In the later case, you will determine a relevant question about the biomolecular system and design a set of molecular dynamics simulations and analysis scripts in VMD to answer that question. You will turn in a project proposal and two rough drafts, and you will give a 15 minute presentation during finals period.
  
* Exams: 10%. There will be one take-home midterm approximately half way through the course, worth 10% of yoru grade. Instead of a final exam, you will be presenting your final project at the end of the semester.

* Late policy: In general, students miss deadlines because you're busy people. Instead of asking you to catch up on such work in the midst of what is almost certainly *still* a busy schedule, I don't ask you to do late work, and I don't accept late work. Instead, I drop approximately one of your homework grades and one of your short paper grades. If you're too busy, *just don't do it*. Give yourself time to do your other work fully. Or turn in a partially-completed assignment. This policy allows you to take charge of your own schedule.
  
## Computer programs ##

To be clear: no previous experience with computer programming or simulations is required! We'll devote as much class time as necessary towards making sure everyone is comfortable with the below tools of computational biophysics.

* VMD: This is a molecular visualization program. We'll use it to look at and analyze protein structures and simulation data. If you have a personal laptop, please download it [here](www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD). If you do not have a personal computer, VMD will be installed on the SciDiv laptops.

* Computer models are becoming more and more important in modern
  science across the board. These days, tools like
  Python/Jupyter notebooks make it surprisingly easy to create,
  tweak and share computational models. **No prior experience is needed!** 
  We'll be *using* and playing with models that the insructor (or the class as a whole) creates throughout the semester. If you have a personal laptop, please install Anaconda as described [here](https://jupyter.readthedocs.io/en/latest/install.html).
  
* Connecting to our computing clusters: for some homework assignments, and perhaps for your final project, you will run short molecular dynamics using the local campus computing resources. If you are on a Mac or Linux, you have everything you need already installed. If you're using Windows, please install [Putty](https://www.putty.org/) and [WinSCP](https://winscp.net/eng/download.php).

## Schedule (very approximate) ##

Here's our tentative schedule of topics. The main text covers more than we can reach in a semester, and there are a many interesting, relevant topics not included in the text. So, we will feel free to modify the schedule based on student interest. For example, we removed some topics in order to spend a week and a half on [Biological Pattern Formation](https://github.com/mglerner/IntroToBiophysics/tree/master/BiologicalPatternFormation) in a previous year.

Papers for discussion:

* [Paper 1](http://simbac.gatech.edu/classes/Phys4251/papers/Gunawardena2014.pdf): Models in biology: ‘accurate descriptions of our pathetic thinking’.
* [Paper 2](http://simbac.gatech.edu/classes/Phys4251/papers/Wang1997.pdf): Stretching DNA with Optical Tweezers,discuss Thurs. Sept. 26
* [Paper 3](http://simbac.gatech.edu/classes/Phys4251/papers/Yildiz2003.pdf): Myosin V Walks Hand-Over-Hand: Single Fluorophore Imaging with 1.5-nm Localization.
* [Paper 4](http://simbac.gatech.edu/classes/Phys4251/papers/Zhao2013.pdf): Mature HIV-1 capsid structure by cryo-electron microscopy and all-atom molecular dynamics
[supplement](http://simbac.gatech.edu/classes/Phys4251/papers/Zhao2013supp.pdf).


| **Week** | **Topic** |
|:--------:|:----------|
| **Week** | **Topic** |
|:--------:|:----------|
| 1 | Introduction to biology: messy, hot, and crowded. Quick and dirty estimation. Four classes of biomolecules. Visualization with VMD. |
| 2 | Statistical mechanics: randomness, distributions, and modeling. |
| 3 | More statistical mechanics, discuss Paper 1 (Gunawardena 2014). |
| 4 | Amino acid properties, pKas, intro to polymer theory. |
| 5 | Polymers: freely jointed chains, worm like chains, and chromatin. |
| 6 | DNA/RNA structure, bending/packing. |
| 7 | Protein folding, discuss Paper 2 (Wang 1997). |
| 8 | Diffusion, crowding, discuss class projects. |
| 9 | More models of diffusion, discuss MGL research. |
| 10 | **Break** |
| 11 | chemical equilibrium, rate equations; cytoskeleton. |
| 12 | molecular motors (ATP synthase, kinesin/myosin). |
| 13 | More molecular motors, discuss Paper 3 (Yildiz 2003). |
| 14 | Protein synthesis; genetics, central dogma. |
| 15 | RNA-Seq, bioinformatics, network models. |
| 16 | Bioelectricity (ion channels, Nernst potential, Hodgkin-Huxley), discuss Paper 4 (Zhao 2013). |

## Acknowledgements ##

[J.C. Gumbart](http://simbac.gatech.edu/), 
[Jeff Wereszczynski](http://mypages.iit.edu/~jwereszc/), 
and [Paul Nerenberg](http://www.psnlab.org/)
have graciously provided 
information and examples relating both to the syllabus and to the
content. 