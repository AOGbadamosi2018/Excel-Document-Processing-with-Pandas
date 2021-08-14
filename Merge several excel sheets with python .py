# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:54:01 2020

@author: AOG
"""

#importing dependencies
import pandas as pd
from pandas import DataFrame


#IMPORTATIOIN
#reading the workbook
xlsx=pd.ExcelFile('Input File.xlsx')

#creating an index based on unique sheet data
k=xlsx.sheet_names
#sheet number index iterator
n=0
#loop iterator
i=0
Sheet_container=['sheet1','sheet2','sheet3','sheet4','sheet5','sheet6','sheet7','sheet8','sheet9','sheet10']

#appending to each dataframe
while (i<10) :
    Sheet_container[n]=DataFrame()
    Sheet_container[n]=xlsx.parse(k[i])
    print(k[i]+'parsed')
    i+=1
    n+=1
    
#referencing the data in sheet 3
Sheet_container[2]


#EXPORTATION
#export names
y=('SHEET 1.csv','SHEET 2.csv','SHEET 3.csv','SHEET 4.csv','SHEET 5.csv','SHEET 6.csv','SHEET 7.csv','SHEET 8.csv','SHEET 9.csv','SHEET 10.csv')


#exporting sheet values to.csv
#iterator assignment
p=0

while (p<10) :
    Sheet_container[p].to_csv(y[p],sep=',')
    p+=1
      
print('done')





    
