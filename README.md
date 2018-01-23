# Tidying Data

This repository is a series of examples focusing on how to clean and tidy dataset for a later easer 
and more effective analysis.

As you maybe already know, most of the data scientist state that one of the most important task
and really frequently done is clean data. That is why it caught my attention and I wanted to to 
do some exercises.


Defining tidy data

 
A dataset defined as tidy has the following attributes:

    Each variable forms a column and contains values
    Each observation forms a row
    Each type of observational unit forms a table

As an example, imagine we have the next data set
    
    | Treatment A | Treatment A | Treatment B |
    |-----------  |-------------| ----------- |
    | John Doe    | -           | 2           |
    | Mary Joe    | 16          | 11          |
    | Joana Dill  | 3           | 1           |
    
A tidy dataset corresponding to this one could be
    
    | Name       | Treatment | Result |
    |----------- |-----------| ------ |
    | John Doe   | a         | -      |
    | Mary Joe   | a         | 16     |
    | Joana Dill | a         | 3      |
    | John Doe   | b         | 2      |
    | Mary Joe   | b         | 11     |
    | Joana Dill | b         | 1      |
    
    
This last data set looks really better than the previous one, structured, 
and for later to apply any algorithm to learn from it it is much better.

In the following examples we will see how to tidy data sets regarding the next
principles:
 
    - Column headers are values, not variable names.
    - Multiple variables are stored in one column.
    - Variables are stored in both rows and columns.
    - Multiple types of observational units are stored in the same table.
    - A single observational unit is stored in multiple tables. 

### Column headers are values, not variable names

Problem: The columns headers are composed of the possible income values.

    |religion 	             | <$10k | $10-20k | $20-30k | $30-40k | $40-50k | $50-75k |
    |Agnostic 	             |  27 	 |   34    |  60 	 |    81   |    76 	 |   137   |
    |Atheist 	             |  12 	 |   27    |  37 	 |    52   |    35 	 |    70   |
    |Buddhist 	             |  27 	 |   21    |  30 	 |    34   |    33 	 |    58   |
    |Catholic 	             |  418  |	 617   |  732 	 |    670  |    638  |  1116   |
    |Dont know/refused       |   15  | 	 14    |   15 	 |    11   |    10 	 |     35  |
    |Evangelical Prot        |  575  |	 869   |  1064 	 |    982  |    881  |	 1486  |
    |Hindu 	                 |   1 	 |    9    |    7 	 |     9   |     11  |	  34   |
    |Historically Black Prot |	228  |	 244   |   236 	 |    238  |    197  |	  223  |
    |Jehovahs Witness 	     |   20  |	  27   |   24 	 |     24  |     21  |	  30   |
    |Jewish 	             |   19  |	  19   |   25 	 |     25  |     30  |	  95   |

    
A tidy version of this dataset is one in which the income values would not be columns headers but rather values in an income column.

    |religion 	             | income    | frequency  | 
    |Agnostic 	             |  <$10k    |   27       |  
    |Agnostic 	             |  $10 -20k |   34       |  
    |Agnostic 	             |  $20 -30k |   60       |  
    |Agnostic 	             |  $30 -40k |	 81       |  
    |Agnostic                |  $40 -50k | 	 76       |  
    |Agnostic                |  $50 -75k |	 137      |  
    |Atheist 	             |  <$10k    |    12      |  
    |Atheist                 |	$10 -20k |	  27      |
    ...
    
### The columns headers are composed of values: the week number (x1st.week, …)
    
If a song is in the Top 100 for less than 75 weeks, the remaining columns are filled with 
missing values.

The data set used to follow this example is the next (you have it as well in csv format in the data 
folder in the project)

![alt text](https://github.com/vanalex/tidy-data-python/blob/master/images/billboear%20data.png)

A tidier version of the dataset is one with column name as week and the values as themselves 
values for this column as shown in the image

![alt text](https://github.com/vanalex/tidy-data-python/blob/master/images/billboard%20tidier.png)

 There is still a lot of repetition of the song details: the track name, time and genre. For this 
 reason, this dataset is still not completely tidy as we defined earlier. We will address this 
 in the next example.
 
### Multiple observational units (the song and its rank) in a single table.
On this occasion we will show you the problem of the repetition. In the billboard dataset we can see
that a song is repeated many times because it has several ranks along the time. In order to not have
these repetitions, we can do the next:

 - We firstly clean the repeated rows from the dataset. After cleaning, it is created an index for the
    song, and identifier.
    
    ![alt text](https://github.com/vanalex/tidy-data-python/blob/master/images/billboard%20repeated%20cleaned.png)
    
 - Then, we create another dataset containing the song id or index referencing the previous one created,
   the rank and date.
   
    ![alt text](https://github.com/vanalex/tidy-data-python/blob/master/images/song_rank.png)
   
   
### Multiple variables stored in one column

This dataset documents the count of confirmed tuberculosis cases by country, year, age and sex.

Problems:
 - Some columns contain multiple values: sex and age.
 - Mixture of zeros and missing values NaN. This is due to the data collection process and the distinction is 
   important for this dataset.
   
This is the initial dataset
    
   ![alt text](https://github.com/vanalex/tidy-data-python/blob/master/images/tuberculosis.png)

As we can see, we have the problems mentioned above. We need to remove the values from the header mixing age and sex
and unpivot them into rows. We’ll first need to melt the sex + age group columns into a single one. Once we have that 
single column, we’ll derive three columns from it: sex, age_lower and age_upper. With those, we’ll be able to 
properly build a tidy dataset. The result should be like this one
 
   ![alt text](https://github.com/vanalex/tidy-data-python/blob/master/images/cleaned%20tuberculosis.png)
   
### Variables are stored in both rows and columns

The problem here is that variables are stored in both rows (tmin, tmax) and columns (days).

Firstly, we show the original one
    
   ![alt text](https://github.com/vanalex/tidy-data-python/blob/master/images/weather.png) 

In order to make this dataset tidy, we want to move the three misplaced variables (tmin, tmax and days) as three 
individual columns: tmin. tmax and date.

   ![alt text](https://github.com/vanalex/tidy-data-python/blob/master/images/weather%20data%20cleaned.png)


### One type in multiple tables
   
 - The data is spread across multiple tables/files.
 - The “Year” variable is present in the file name. 

In order to load those different files into a single DataFrame, we can run a custom script that will append the 
files together. Furthermore, we’ll need to extract the “Year” variable from the file name.

The result is 
   ![alt text](https://github.com/vanalex/tidy-data-python/blob/master/images/babies%20name.png)
      
    
    