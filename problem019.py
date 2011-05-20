#!/usr/bin/python 
#Problem 019!
#9th May 2008
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
count=0
day=2
days=[31,28,31,30,31,30,31,31,30,31,30,31]
for year in range(1901,2001):
	for month in range(1,13):
		day+=days[month-1]
		if (year%4==0 and year%100!=0) or year%400==0:
			if month==2:
				day+=1
		day=day%7
		if day==0:
			count+=1
print count