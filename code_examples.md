## Code Examples

I've written dozens of packages (many quite extensive) for different languages (e.g., Ruby and Python) and hundreds of scripts.  Most of them can be found at [my github page](https://github.com/jtprince) or [my lab's github page](https://github.com/princelab).

### Out-of-stock risk

Some of the best data science/engineering code that I've written lately is proprietary.  A good example of such a project is out-of-stock risk prediction which I've briefly described with images [on my portfolio page](https://github.com/jtprince/portfolio/#out-of-stock-risk).  Coded mainly using numpy/scipy.

### Django-gtin-fields

I've written a ton of python code for Doba and CruxConnect over the past 4.5 years, but almost all of it is proprietary.

I was given permission to open-source this package, which is solid, unexiting python/django code.

Interesting features: concise/readable UPCA -> UPCE conversion.

Potential improvements: Could use a bit more modularization in spots.

[django-gtin-fields](https://github.com/CruxConnect/django-gtin-fields)

* [validators.py](https://github.com/CruxConnect/django-gtin-fields/blob/master/gtin_fields/validators.py)
* [converters.py](https://github.com/CruxConnect/django-gtin-fields/blob/master/gtin_fields/converters.py)

### Screenshot - concise standalone script

High-level control over screenshots in 90 lines of source code.

Interesting features: compact help message which also uses color to distinguish some options.

Potential improvements: If I were using more color then I would use a library for that purpose (e.g., colorize or highline)

[screenshot](https://github.com/jtprince/dotfiles/blob/master/bin/sc)

Easy to take a screenshot of this one:

![example](media/code-examples/sc-example-2019-04-03--01-14-10.png)

### MSabundanceSIM - small science project

My collaborator, Rob Smith (a National Science Career Award recipient and CS professor at the University of Montana) , had written some idea code  and asked for my help making it production ready. I refactored and polished it up a bit and wrote some tests around it.  This was a personal project (wrote this at night after day job at Doba).

Interesting features: Rob wanted the code to be usable as a single, standalone file, and as a gem executable.

Potential improvements: More modularization (i.e., shorter code blocks; single purpose) and more/better tests.

### Savgol

The Savitsky-Golay filter does a much better job at smoothing most data than, say, a moving average which tends to depress extrema.  I wanted to be able to use it with zero dependencies in Ruby.

Interesting feature: I also wrote a polynomial regressor for this package to handle unevenly spaced data but with the same interface as the digital savgol filter.

Potential improvements: More modularization (i.e., shorter code blocks; single purpose).

[savgol](https://github.com/princelab/savgol)

* [savgol.rb](https://github.com/princelab/savgol/blob/master/lib/savgol.rb)

### Rserve-simpler - simple R interface

Wrapper around the fairly performant Rserve library for binary communication with an R server.

[rserve-simpler](https://github.com/jtprince/rserve-simpler)

* Example usage in [mspire-lipid](https://github.com/princelab/mspire-lipid/blob/master/lib/mspire/lipid/search/probability_distribution.rb)

### Diadem - large project built on top of libraries I authored

I wrote this package to do analyeses for the JC Price at BYU. The package facilitated calculation of various mass isotopomer distributions.

Potential improvements: More modularization.

[diadem](https://github.com/princelab/diadem)

* [calculator.rb](https://github.com/princelab/diadem/blob/master/lib/diadem/calculator.rb)
* [isotope_distribution.rb](https://github.com/princelab/diadem/blob/master/lib/diadem/isotope_distribution.rb)

### A few other projects of note

* mspire: [pubmed](https://www.ncbi.nlm.nih.gov/pubmed/18930952) | [rewrite](https://github.com/princelab/mspire) - library to handle major mass spectrometry data formats, including features like random access to massive, indexed xml files.
* rubabel: [pubmed](https://www.ncbi.nlm.nih.gov/pubmed/18930952) | [repo](https://github.com/princelab/rubabel) - ruby interface (and many add-on features) to the openbabel gem.
* mspire-molecular_formula: [repo](https://github.com/princelab/mspire-molecular_formula) - DSL for molecular formulas and tons of useful calculations and some basic manipulation.
* mspire-obo: [repo](https://github.com/princelab/mspire-obo) - generic handling of ontology files for mass spectrometry terms.
* ruby-emass: [repo](https://github.com/princelab/ruby-emass) - ruby implementation of the emass, an ultra-high accuracy isotope peak mass calculator.
* obiwarp: [pubmed](https://www.ncbi.nlm.nih.gov/pubmed/16944896) | [repo](https://sourceforge.net/projects/obi-warp/files/obiwarp/) | [integration into R](https://rdrr.io/bioc/xcms/man/retcor.obiwarp-methods.html)
* histogram: [repo](https://github.com/jtprince/histogram) - Generates histograms similar to R's hist and numpy's histogram functions and has implementations for common auto-bin algorithms.
* binneroc: [repo](https://github.com/jtprince/binneroc) - constant time binning.
