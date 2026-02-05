from abc import ABC, abstractmethod

class DatabaseClient(ABC):

    @abstractmethod
    def insert_weather(self, data):
        pass

    @abstractmethod
    def get_last_ingestion_time(self):
        pass
