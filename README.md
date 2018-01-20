#Tidying Data

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

###Column headers are values, not variable names

Problem: The columns headers are composed of the possible income values.

    |religion 	             | <$10k | $10-20k | $20-30k | $30-40k | $40-50k | $50-75k |
    |Agnostic 	             |  27 	 |   34    |  60 	   |    81   |    76 	 |   137   |
    |Atheist 	              |  12 	 |   27    |  37 	   |    52   |    35 	 |    70   |
    |Buddhist 	             |  27 	 |   21    |  30 	   |    34   |    33 	 |    58   |
    |Catholic 	             |  418  |	 617    |  732 	  |    670  |    638  |  1116   |
    |Dont know/refused      |   15  | 	 14    |   15 	  |    11   |    10 	 |     35  |
    |Evangelical Prot       |  575  |	 869    |  1064 	 |    982  |    881  |	 1486   |
    |Hindu 	                |   1 	 |    9    |    7 	  |     9   |     11  |	  34    |
    |Historically Black Prot|	228   |	 244    |   236 	 |    238  |    197  |	  223   |
    |Jehovahs Witness 	     |   20  |	  27    |   24 	  |     24  |     21  |	  30    |
    |Jewish 	               |   19  |	  19    |   25 	  |     25  |     30  |	  95    |

    
A tidy version of this dataset is one in which the income values would not be columns headers but rather values in an income column.

    |religion 	             | income    | frequency  | 
    |Agnostic 	             |  <$10k    |   27       |  
    |Agnostic 	             |  $10 -20k |   34       |  
    |Agnostic 	             |  $20 -30k |   60       |  
    |Agnostic 	             |  $30 -40k |	  81       |  
    |Agnostic               |  $40 -50k | 	 76       |  
    |Agnostic               |  $50 -75k |	  137      |  
    |Atheist 	              |  <$10k    |    12      |  
    |Atheist                |	$10 -20k  |	   27      |
    ...
