# cluster-review-vectors

This resource contains utilities for clustering (semantic) vectors with Python. To get started, We created vectors as used in GloVe semantic vector file from the Stanford repository (found in http://www-nlp.stanford.edu/data ) 

If you call `head` on a GloVe file, you'll see it's structured like this:

<pre><code>the 0.04656 0.21318 -0.0074364 [...] 0.053913
, -0.25539 -0.25723 0.13169 [...] 0.35499
. -0.12559 0.01363 0.10306 [...] 0.13684
of -0.076947 -0.021211 0.21271 [...] -0.046533
to -0.25756 -0.057132 -0.6719 [...] -0.070621
[...]
sandberger 0.429191 -0.296897 0.15011 [...] -0.0590532</code></pre>

Each line contains a single user id followed by <i>n</i> signed float values, where <i>n</i> = the number of dimensions signified in the filename (e.g. imdb.300d.txt projects each user into 300 dimensions). 

One can cluster these vectors by running:

`python cluster_vectors.py imdb.300d.txt {n_words} {reduction_factor}`

n_words = the number of users from imdb.300d.txt you wish to cluster, and reduction_factor = a float that controls how many clusters to produce. For example, one can run:

`python cluster_vectors.py imdb.300d.txt 10000 .1`

This command will read the first 10000 users from the specified file, and will generate 10000 * .1 (or 1000) clusters of users. These clusters may then be used for many different kinds of NLP tasks, such as document clustering, dimension reduction of natural language documents, or the detection of textual reuse. 

`/clusters/` contains a file with 20 clustered users, generated through the command `python cluster_vectors.py imdb.300d.txt 2000 .01` 
