#!/usr/local/bin/python3

import shelve
import os
class ImitateDatebase:
	def __init__(self, db_name):
		self._dbm = shelve.open(os.path.join('.', '__dbm', f'{db_name}.db'))
	def write(self, **kwargs):
		with self._dbm as file:
			for key, value in kwargs.items():
				file[key] = value
	

	def read(self):
		return self._dbm
	

if __name__ == '__main__':
	persons = {'Patrick': 'Patrick', 'Pedro': 'Pedro'}
	juices = {'Apple': 'Apple', 'Banana': 'Banana'}
	dbm = ImitateDatebase('persons')
	dbm_2 = ImitateDatebase('juices')
	dbm.write(**persons)
	dbm_2.write(**juices)
	# db = dbm.read()
	# db_2 = dbm_2.read()
	# print(db['Patrick'])
	# print(db_2['Apple'])
