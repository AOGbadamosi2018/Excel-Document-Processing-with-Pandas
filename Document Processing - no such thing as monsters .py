# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 23:50:28 2021

@author: AOG
"""
# "No Such Thing As Monsters spotting list (002).xlsx"



import pandas as pd
from pandas import DataFrame


#IMPORTATIOIN
#reading the workbook
xlsx=pd.ExcelFile("No Such Thing As Monsters spotting list (002).xlsx")
Target = pd.read_excel(xlsx,'Sheet3')


# stripping off the type description and assigning
Start = Target['Start'].values


End = Target['End'].values






# creating the keys for the for loop
bool_series_start = pd.isnull(Start)

bool_series_end = pd.isnull(End)

bool_series_end[0] = 'True'
# ensuring serialization
Series_Start = pd.Series(Start)
Series_End = pd.Series(End)

# replace the value : with .

# pd.Series(Series_Start[0]).str.slice_replace(start=8, stop = 9 , repl ='.' )
# pd.Series(Series_End[0]).str.slice_replace(start=8, stop = 9 , repl ='.' )


# loops


# replacing for start series
k = 0
size = len(bool_series_start)
while size > k :
    if bool_series_start[k] == False:
        Series_Start[k] = (pd.Series(Series_Start[k]).str.slice_replace(start=8, stop = 9 , repl ='.' )).values[0]
        k=k+1
    else: k=k+1

    
# replacing for end series 
l = 0
size2 = len(bool_series_end)
while size2 > l:
    if bool_series_end[l] == False:
        Series_End[l] = (pd.Series(Series_End[l]).str.slice_replace(start=9, stop = 10 , repl ='.' )).values[0]
        Series_End[l] = (pd.Series(Series_End[l]).str.slice_replace(start=0, stop = 1 , repl ='' )).values[0]
        l=l+1
    else: l=l+1
    


# Reassigning 
Target['Start'] = Series_Start
Target['End'] = Series_End

# writing to sheet in excel file 
Target.to_excel("No Such Thing As Monsters spotting list (002).xlsx", sheet_name='Sheet 3',index = False)


print('done')





# cleaning up 
xlsx2=pd.ExcelFile("No Such Thing As Monsters spotting list.xlsx")
Target = pd.read_excel(xlsx2,'Sheet 3')


# stripping off the Duration

End = Target['End'].values

Duration = Target['Duration'].values

# ensuring serialization
Series_Duration = pd.Series(Duration)

bool_series_end = pd.isnull(End)

bool_series_end[0] = 'True'

# replacing for end series 
m = 0
size3 = len(bool_series_end)
while size3 > m:
    if bool_series_end[m] == True:
        Series_Duration[m] = ''
        m=m+1
    else: m=m+1
    

Target['Duration'] = Series_Duration

Target.to_excel("No Such Thing As Monsters spotting list.xlsx", sheet_name='Sheet 3',index = False)



