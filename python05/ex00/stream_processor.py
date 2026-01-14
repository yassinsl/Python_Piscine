from abc import ABC, abstractmethod
from typing import Any


class DataProccessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    @abstractmethod
    def format_output(self, data: Any) -> str:
        pass


class NemericProcessor(DataProccessor):
    def format_output(self, data: Any) -> str:
        return (
            f"Processed {len(data)} numeric values, "
            f"sum={sum(data)}, avg={sum(data) / len(data)}"
        )

    def validate(self, data: Any) -> bool:
        if not isinstance(data, (list, tuple)):
            return False
        return all(isinstance(x, (float, int)) for x in data)

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        if not self.validate(data):
            raise ValueError("this data have no numric number")
        print("Validation: Numirec data verifid")
        return self.format_output(data)


class TexttProcessor(DataProccessor):
    def format_output(self, data: Any) -> str:
        words = data.split()
        return f"Processed text: {len(data)} characters, {len(words)} words"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        if not self.validate(data):
            raise ValueError("this data in not a string")
        print("Validation: Text data verifid")
        return self.format_output(data)


class LogProcessor(DataProccessor):
    def format_output(self, data: Any) -> str:
        return f"[ALERT]: {data}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return ("ERROR" in data) or ("INFO" in data) or ("WARNING" in data)

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        if not self.validate(data):
            raise ValueError("this data in not a valid log entry")
        print("Valudation : log entry verified")
        return self.format_output(data)

#chat_test :)
def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    processors = [
        NemericProcessor(),
        TexttProcessor(),
        LogProcessor(),
    ]

    tests = [
        ([1, 2, 3, 4, 5], "Numeric good"),
        ([1, "x", 3], "Numeric bad"),
        ("Hello Nexus World", "Text good"),
        (12345, "Text bad"),
        ("ERROR: Connection timeout", "Log good"),
        ("random message", "Log bad"),
    ]

    for data, label in tests:
        print(f"\n--- Test: {label} ---")
        for p in processors:
            try:
                result = p.process(data)
                print("Output:", result)
            except Exception as e:
                print(f"{p.__class__.__name__} rejected -> {e}")

    print("\n=== Polymorphic Processing Demo ===")
    mixed = [
        ([1, 2, 3], NemericProcessor()),
        ("Hello Nexus", TexttProcessor()),
        ("INFO: System ready", LogProcessor()),
    ]
    for i, (data, p) in enumerate(mixed, 1):
        print(f"Result {i}: {p.process(data)}")


if __name__ == "__main__":
    main()

