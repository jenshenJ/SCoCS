import os 
import re


class IDbService():
    def save(self, container: set[str], container_filename: str):
        pass

    def load(self, container_filename) -> set[str]:
        pass


class ContainerService:
	_container: set[str]
	_username: str
	_container_filename: str
	_database: IDbService = None

	def __init__(self, username: str, db_service: IDbService):
		self._username = username
		self._container_filename = f'{username}-container.dmp'
		self._database = db_service
		self._container = set()
	
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
