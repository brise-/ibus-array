#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def array_updatedb(table_file):
	con = sqlite3.connect("array.db")
	cur = con.cursor()
	cur.execute('select * from main')
	main = cur.fetchall()

	# read from the text table
	f = open(table_file, 'r')
	z = map(lambda x:x.split('\t'), f.readlines())
	k = map(lambda y:(y[0].lower(), y[1].strip()), z)
	f.close()

	# update the database
	for i, j in k:
		cur.execute('insert into main (keys, ch) values ("' + i + '", "' + j + '");')

	con.commit()
	con.close()

# empty main table
con = sqlite3.connect("array.db")
cur = con.cursor()
cur.execute('delete from main where keys not in ("w1", "w2", "w3", "w4", "w5", "w6", "w7", "w8", "w9", "w0");')
con.commit()
con.close()

array_updatedb('array30_27489-V201509.utf8')
array_updatedb('array30_ExtB_V2016A.utf8')
array_updatedb('array30_ExtCD_V2013A.utf8')
array_updatedb('array30_ExtE_V2016A.utf8')
