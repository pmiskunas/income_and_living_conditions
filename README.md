# income_and_living_conditions
## Analysis on annual statistical survey on income and living conditions.

All data files downloaded from  <b>[Official statistics portal](https://osp.stat.gov.lt/viesos-duomenu-rinkmenos/-/asset_publisher/i2LnhXkrXAbl/content/metinio-pajamu-ir-gyvenimo-salygu-statistinio-tyrimo-?inheritRedirect=false&redirect=https://osp.stat.gov.lt/viesos-duomenu-rinkmenos?p_p_id=101_INSTANCE_i2LnhXkrXAbl&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_pos=1&p_p_col_count=2
)</b> also I added xlsx files in [here](https://github.com/pmiskunas/income_and_living_conditions/tree/master/data_files) (by the way there's csv files for one year data)

* Firstly if you run "ALL_to_CSV.py" the script reads xlsx files, and puts .csv files in another folder called "output_csv"
* Then the main.py reads all of the .csv files, groups it by year into dictionaries and plots some graphs. 

The main goal was to learn some of matplotlib, pandas (working with dataframes, instead of mySQL) by analysing some data.

   Different graphs for Households Income in cities and village:
![myImage](https://github.com/pmiskunas/income_and_living_conditions/blob/master/Metin%C4%97s_pajamos.png?raw=true)


   Dependence of one living condition on education:
![image](https://github.com/pmiskunas/income_and_living_conditions/blob/master/Tualet%C5%B3_su_nutekamuoju_vandeniu_skai%C4%8Dius_pagal_i%C5%A1silavinim%C4%85.png?raw=true)
