# Preparing all combinations of NN words X all users . Results in help3_NN_comb
WITH 
subQ1 AS (SELECT  word,rnk,0 local_weight , global_weight FROM `imdb2.help2_dvr_NN` ),
subQ2 AS (SELECT user_id FROM `imdb2.text_of_4000_concat` group by 1) 
     SELECT * FROM subQ1
cross join         subQ2 

# Preparing vectors of NN words X all users . Results in help3_NN_vectors 
     select buid,lrnk,if(lw>0 , lw, 0 ) as local_weight, word,rnk , global_weight,user_id,diff,sorter	,rnk- lrnk    rnk_diff from      ( 
     select b.user_id buid ,  b.lrnk lrnk ,b.local_weight lw, a.*, if(b.local_weight>0 ,b.local_weight ,0) -a.global_weight   as diff , abs(if(b.local_weight>0 ,b.local_weight ,0)  -a.global_weight) as sorter 
     from (SELECT * FROM `imdb2.help3_NN_comb`  ) a  left join `imdb2.help3_NN` b   using (user_id,word) 
      ) 
