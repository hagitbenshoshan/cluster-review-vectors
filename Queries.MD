# Preparing all combinations of NN words X all users . Results in help3_NN_comb
WITH 
subQ1 AS (SELECT  word,rnk,0 local_weight , global_weight FROM `imdb2.help2_dvr_NN` ),
subQ2 AS (SELECT user_id    FROM `imdb2.help3_NN` group by 1  )  
     SELECT * FROM subQ1
cross join         subQ2 
