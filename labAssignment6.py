#!/usr/bin/env python
import re

with open("input.file") as f:
	line  = f.readline().rstrip()
s = line.split(", ")

print "Here are the names that contain 5: "
for lines in s:
	if re.search("5",lines):
		print lines

print "\nHere are the names that contain the letters d or e: "
for lines in s:
	if  re.search("d",lines) or re.search("e",lines):
		print lines

print "\nHere are the names that contain d and e in that order (de): "
for lines in s:
	if re.search("de",lines):
		print lines

print "\nHere are the names that contain d and e with a single letter inbetween them: "
for lines in s:
	if re.search("d.e",lines):
		print lines

print "\nHere are the names that contain d and e in these combinations (de or ed): "
for lines in s:
	if re.search("de",lines) or re.search("ed",lines):
		print lines

print "\nHere are the names that start with x or y: "
for lines in s:
	if re.search("^x",lines) or re.search("^y",lines):
		print lines

print "\nHere are the names that start with x or y and end with an e: "
for lines in s:
	if (re.search("^x",lines) and re.search("e$",lines)) or (re.search("^y",lines) and re.search("e$",lines)):
		print lines 

print "\nHere are the names that start with an x and then is followed by any three characters and a number: "
for lines in s:
	if re.search("^x...[0123456789]",lines):
		print lines

print "\nHere are the names that contain three numbers in a row: "
for lines in s:
	if re.search("[0123456789][0123456789][0123456789]",lines):
		print lines

print "\nHere are the names that end with a d followed by either a, r or p(da,dr,dp): "
for lines in s:
	if re.search("d[arp]$",lines):
		print lines
