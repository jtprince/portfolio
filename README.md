# John T. Prince

A few significant or interesting projects.  Unless noted, all data visualizations are my work.

See also:

* [Curriculum Vitae](http://tiny.cc/jtprince-cv)
* [Résumé](http://tiny.cc/jtprince-cv)
* [Publications on Pubmed](http://tiny.cc/jtprince-publications) (34)
* [Software Development and Data Analysis Philosophy](https://github.com/jtprince/portfolio/blob/master/philosophy.md)
* [Favorite Tools](https://github.com/jtprince/portfolio/blob/master/favorite_tools.md)

# Work which I primarily authored

### Out of Stock Risk

Developed custom Holt-Winters (triple exponential) forecasting:

* Custom algorithmic development:
    * can handle non-uniform data
    * heuristic to select optimal seasonalities
    * integrate with probabilistic model to better predict low count data
* Implemented in python/numpy/scipy
* *Currently in production use at Doba Inc*

[in-house project presentation](https://www.dropbox.com/s/k5niyn4kwm1jwze/OOS_Risk_Presentation.pdf?dl=0)

<table border="0">
<tr>
<td><a href="media/oos-risk/categories.png"><img src="media/oos-risk/categories.png" width="400"/></a></td>

<td><a href="media/oos-risk/final-example.png"><img src="media/oos-risk/final-example.png" width="400"/></a></td>
</tr>

<tr>
<td><a href="media/oos-risk/integration-types.png"><img src="media/oos-risk/integration-types.png" width="400"/></a></td>

<td><a href="media/oos-risk/nonuniform-data.png"><img src="media/oos-risk/nonuniform-data.png" width="400"/></a></td>
</tr>
</table>

### RESTful architecture

Co-designed the Crux-Connect RESTful interface.

See [docs.cruxconnect.com](docs.cruxconnect.com) for public endpoints. I assisted with creation of the jekyll documentation, but I designed and built all the endpoints described by the documentation.

<a href="media/restful-architecture/sku-example.png"><img src="media/restful-architecture/sku-example.png" width="900"/></a>

### Stateful Elasticsearch-based Search

Architected entire elasticsearch search for product and autocompletion.

Created stateful faceted and filtered search.  The entire UI (which I did not
build) was driven by the data returned from stateful API calls.

* Dozens of unique filters and facets
* Handles complete category heirarchy
* Custom analyzers and normalizers for intuitive text search
* Dual text/keyword indexing for text search and keyword-based sorting

<a href="media/stateful-search/basic-search-interface.png"><img src="media/stateful-search/basic-search-interface.png" width="900"/></a>

<a href="media/stateful-search/more-filters.png"><img src="media/stateful-search/more-filters.png" width="200"/></a>

### Rubabel

Wrapped Open Babel (cheminformatic model toolkit) with ruby.  I did not create
the below image, but I was responsible for coding most of the library.

[Journal of Cheminformatics 2013 5:35](https://jcheminf.biomedcentral.com/articles/10.1186/1758-2946-5-35)

<a href="media/rubabel/object-model.png"><img src="media/rubabel/object-model.png"/></a>

### rserve-simpler (Ruby R-serve wrapper)

Built convenient interface to Rserve (a binary R server) for ruby.

[rserve-simpler](https://github.com/jtprince/rserve-simpler) (github)

### ruby histogram

Histogram solution for ruby featuring auto-bin and various bin methods (Scott, Sturges, FD, etc), multiple datasets, and weights

Suggested and then accepted as answer to [this stack overflow question](https://stackoverflow.com/questions/19101167/how-to-create-a-histogram-from-a-flat-array-in-ruby).

[histogram](https://github.com/jtprince/histogram) (github)

### Obiwarp

Dynamic programming and bijective warping solution for chromatographic alignment of complex LC-MS datasets.

* [Analytical Chemistry 2006 78:6140-52](https://pubs.acs.org/doi/abs/10.1021/ac0605344) ([alternate link](https://www.dropbox.com/s/natjcxrha9w0m0y/obiwarp.pdf?dl=0))
* Default method in XCMS ([retcor.obiwarp](https://rdrr.io/bioc/xcms/man/retcor.obiwarp-methods.html))

<a href="media/obiwarp/obiwarp.png"><img src="media/obiwarp/obiwarp.png"/></a>

## Mspire - Mass Spectrometry Proteomics in Ruby

* MS and proteomic object models for ruby
* Direct access to data in large, binary indexed xml files.
* Reverse engineered the closed .srf format.

<a href="media/mspire/mspire.png"><img src="media/mspire/mspire.png"/></a>

### Django-gtin-fields

Provides django model fields to store and validate commonly used GTIN related product identifiers (like UPC).

[django-gtin-fields](https://github.com/CruxConnect/django-gtin-fields) (github)

## State machine citation parsing

State machine parsing to efficiently extract citations from large ascii doc dataset.

[extrac_sources.rb](https://github.com/wordtreefoundation/book-of-mormon/blob/master/src/extract_sources.rb)

```ruby
...
  state_machine :state, initial: :in_verses do
    event :start_margin do
      transition :in_verses => :in_margin
    end

    event :end_margin do
      transition :in_margin => :in_verses
    end

    event :start_source do
      transition :in_margin => :in_source
    end

    event :end_source do
      transition :in_source => :in_margin
    end

    state :in_margin do
      def parse(line)
        if line == END_MARGIN
          if @source_lines.size > 0 && @source_lines.any? {|line| !line.strip.empty? }
            @sources.push(*Source.many_from_lines(@source_lines))
            @source_lines = []
          end
          end_margin
        elsif line == SOURCE_DELIMITER
          @source_lines = []
          start_source
        else
          @source_lines << line
        end
      end
    end
...
```

