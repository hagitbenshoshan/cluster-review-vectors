# read_database_reviews.py
Read reviews text data we stored in google bigquery , and create a single text file per user , concatenates its reviews from at least 30 different reviews. the output file name is review_{user_id}.txt  (for example review_858542.txt)  

# tokenize_remove_stem_pos.py

Read txt files generated by previous step , and process each text file with the following tasks 
  Tokenize , and lower tokens. 
  Remove string punctuation  ("’","‘","--","“","”","!")
  Remove stop words
  lemmatize words 
  Stemmer
  POS 
  
# cluster-review-vectors

This resource contains utilities for clustering (semantic) vectors with Python. To get started, We created vectors as used in GloVe semantic vector file from the Stanford repository (found in http://www-nlp.stanford.edu/data ) 

If you call `head` on a vector file, you'll see it's structured like this:

<pre><code>32939276 -0.019841426 0.025862843 0.003790899 -0.000359371 -0.003321933 [...]  -0.000436533
33374263 -0.004422366 -0.007749286 -0.003212388 0.000472978 -0.000795836 [...] -0.001276645</code></pre>

to generate the vector file (1000 Users , 50 features per user - representing the top 50 DVR words weights differences)  , we run the command : 
<pre><code>
SELECT
  CONCAT(CAST(user_id AS string), ' ',vec_line) asvec_line
FROM (
  SELECT
    user_id,
    ANY_VALUE(vec_line) AS vec_line
  FROM (
    SELECT
      user_id,
      STRING_AGG ( CAST(diff AS string),' ') OVER (PARTITION BY user_id ORDER BY rnk ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS vec_line
    FROM (
        SELECT user_id,round(diff,9) diff ,word , rnk
      FROM
        `imdb2.help3_NN_vectors`
      WHERE
        user_id IN (SELECT user_id  FROM `imdb2.NN_Distances` GROUP BY  1 LIMIT 1000) -- Number of users
        AND rnk< 51 -- Number of features 
      ORDER BY
        user_id,
        rnk))
  GROUP BY
    user_id)  </code></pre>
    
Each line contains a single user id followed by <i>n</i> signed float values,rounded to 9 decimal positions,  where <i>n</i> = the number of dimensions signified in the filename (e.g. vec_1000U_50P.txt projects each user into 50 dimensions). 

One can cluster these vectors by running:

`python cluster_vectors.py imdb.300d.txt {n_words} {reduction_factor}`

n_words = the number of users from imdb.300d.txt you wish to cluster, and reduction_factor = a float that controls how many clusters to produce. For example, one can run:

`python cluster_vectors.py vec_1000U_50P.txt 10000 .1`

This command will read the first 10000 users from the specified file, and will generate 10000 * .1 (or 1000) clusters of users. These clusters may then be used for many different kinds of NLP tasks, such as document clustering, dimension reduction of natural language documents, or the detection of textual reuse. 

`/clusters/` contains a file with 10 clustered users, generated through the command `python cluster_vectors.py vec_1000U_50P.txt 1000 .01` 
