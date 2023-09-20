#!/usr/local/bin/python3

import shelve
import os
class ImitateDatebase:
	def __init__(self):
		self._dbm = shelve.open(os.path.join('.', '__dbm', 'persons.db'))
	def write(self, **kwargs):
		with self._dbm as file:
			for key, value in kwargs.items():
				file[key] = value
		
if __name__ == '__main__':
	persons = {'Patrich': 'Patrick', 'Pedro': 'Pedro'}
	dbm = ImitateDatebase()
	dbm.write(**persons)