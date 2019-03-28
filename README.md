# portfolio

Simple demonstration and description of my significant or otherwise
interesting projects.  Unless noted, all work shown is my own.

## Out of Stock Risk

Developed custom Holt-Winters (triple exponential) forecasting:

* Custom algorithmic development:
    * can handle non-uniform data
    * heuristic to select optimal seasonalities
    * integrate with probabilistic model to better predict low count data
* Implemented in python/numpy/scipy
* *Currently in production use at Doba Inc*

[in-house project presentation](https://www.dropbox.com/s/k5niyn4kwm1jwze/OOS_Risk_Presentation.pdf?dl=0)

<a href="media/oos-risk/categories.png"><img src="media/oos-risk/categories.png" width="400"/></a>

<a href="media/oos-risk/final-example.png"><img src="media/oos-risk/final-example.png" width="400"/></a>

<a href="media/oos-risk/integration-types.png"><img src="media/oos-risk/integration-types.png" width="400"/></a>

<a href="media/oos-risk/nonuniform-data.png"><img src="media/oos-risk/nonuniform-data.png" width="400"/></a>


## RESTful architect



## Stateful Elasticsearch-based Search

Architected entire elasticsearch search for product and autocompletion.

Created stateful faceted and filtered search

* Dozens of unique filters and facets
* Handles complete category heirarchy
* Custom analyzers and normalizers for intuitive text search
* Dual text/keyword indexing for text search and keyword-based sorting
