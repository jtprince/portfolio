## Personal Software Development and Data Analysis Philosophy

1. *Keep focused on the goal*
    * The *direct* goal is to create great (correct, maintainable, and efficient) software or analyses.  There is no need to fall prey to sunk cost fallacies or our own egos as we seek this end.  Work in harmony to find the best solutions.
    * The *sustainable* goal (which is generally compatible with the direct goal) is to create software/analyses while building individual skill sets and nurturing a positive culture.  Skilled and happy programmers create great software, but just as importantly, quality work and rich friendships are part of what make life worth living.
1. *Isomorphism is the key to automation*: clear, consistent patterns and abstractions allow a person to automate and change processes quickly and efficiently.  *ad hoc* solutions may be necessary at times but are often more costly than anticipated in software since they cannot easily or typically scale.
1. *Single source (DRY)*: data and code should ideally have a single source.  Creation of all downstream artifacts should be automated.  Single source, along with proper abstractions (see #2), allows many kinds of changes to be made once and completely propagate.
1. *Modular and clean in proportion to anticipated use*: clean and modular take time and effort, so spend more time on the code that is referred to and used most often.
1. *Software is a "living" process*: the processes used are at least as important as the functionality of the code.  Continuous integration (which includes code standards and testing) and deployment should be the default (only failed tests prevent deployment) for live projects.
1. *Write clean code*: single purpose, good names, functional is best, avoid side-effects, use immutable obects when possible.
1. *Use code analysis and code formatting tools*: these should ideally be integrated into a personal workflow (asynchronous evaluation or before every save).
1. *Work _with_ your language*: use your programming language's most effective idioms for solving the most common problems.

I prefer:

* real-time document collaboration to meetings
* good processes over a one-time result and broken processes
* gaining intuition about optimal *potential* solutions through rapid failure
* delivering final software solutions that do precisely what is intended
