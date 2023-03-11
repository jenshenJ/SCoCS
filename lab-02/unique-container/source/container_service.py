import os 
import pickle
import re

class ContainerService:
	_container: set[str] = set()
	_username: str
	_container_filename: str

	def __init__(self, username: str):
		self._username = username
		self._container_filename = f'{username}-container.dmp'
	
	def add(self, key):
		self._container.add(key)
	
	def remove(self, key):
		self._container.remove(key)

	def list(self):
		return list(self._container)
	
	def find(self, key):
		return key in self._container
	
	def grep(self, regex):
		return list(filter(lambda key: re.match(regex, key), self._container))
	
	def save(self):
		with open(self._container_filename, 'wb') as file:
			pickle.dump(self._container, file)
	
	def is_exists(self):
		return os.path.exists(self._container_filename)
	
	def load(self):
		with open(self._container_filename, 'rb') as file:
			loaded_data = pickle.load(file)
			self._container = self._container | loaded_data

