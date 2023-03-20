import os 
import re
from db_service import DbService

class ContainerService:
	_container: set[str] = set()
	_username: str
	_container_filename: str
	_database: DbService

	def __init__(self, username: str):
		self._username = username
		self._container_filename = f'{username}-container.dmp'
		self._database = DbService()
	
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
		self._database.save(self._container, self._container_filename)
	

	def is_exists(self):
		return os.path.exists(self._container_filename)
	
	
	def load(self):
		if self.is_exists():
			loaded_data = self._database.load(self._container_filename)
			self._container = self._container | loaded_data
