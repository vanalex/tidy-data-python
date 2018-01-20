#tidy dataset example

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

    
    