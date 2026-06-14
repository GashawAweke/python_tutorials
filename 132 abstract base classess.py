# Abstract Base Classes(ABC)
# Used when a class should not be instantiated directly.

# Import
from abc import ABC, abstractmethod

# Example: Security Analyzer Framework


class Analyzer(ABC):

    @abstractmethod
    def analyze(self, data):
        pass


# Concrete implementation:


class MalwareAnalyzer(Analyzer):

    def analyze(self, data):
        print(f"Analyzing malware: {data}")


# Usage:

analyzer = MalwareAnalyzer()

analyzer.analyze("trojan.exe")

# invalid

analyzer = Analyzer()  # error analyzer = MalwareAnalyzer()


# Why Use ABC?

# Enforces implementation:
# Every analyzer MUST implement analyze()

# Excellent for:

# Plugin systems
# Security frameworks
# EDR agents
# SIEM integrations
