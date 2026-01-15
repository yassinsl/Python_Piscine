from abc import ABC abstractmethod
from type import Any

class DataStreams(ABC):
    @abstractmethod
        def process_batch(self, data_batch: List[Any]) -> str:
            pass
    @abstractmethod
        def filter_data(self, data_batch: List[Any], criteria: Optioal[str] = None)-> List[Any]:
            pass
    @abstractmethid
        def get_stats(self)-> Dict[str, Union[str, int, float]]:
            pass
class SensorStream(DataStreams):

class TransactionStream(DataStreams):

class EventStreams(DataStreams):

if __name__ == "__main__":
