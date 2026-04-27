"""Presidio Analyzer - PII Detection and Recognition.

This module provides the core functionality for detecting and recognizing
Personally Identifiable Information (PII) in text using NLP and pattern matching.

Note: Forked from microsoft/presidio for personal learning and experimentation.
See https://github.com/microsoft/presidio for the upstream project.

Personal notes:
- Added LemmaContextAwareEnhancer to __all__ for easier access in experiments.
- Tracking upstream version: 2.2.354
"""

from presidio_analyzer.analyzer_engine import AnalyzerEngine
from presidio_analyzer.analyzer_request import AnalyzerRequest
from presidio_analyzer.recognizer_result import RecognizerResult
from presidio_analyzer.entity_recognizer import EntityRecognizer
from presidio_analyzer.pattern_recognizer import PatternRecognizer
from presidio_analyzer.analysis_explanation import AnalysisExplanation
from presidio_analyzer.recognizer_registry import RecognizerRegistry
from presidio_analyzer.nlp_engine import NlpEngine, NlpEngineProvider
from presidio_analyzer.context_aware_enhancers import ContextAwareEnhancer, LemmaContextAwareEnhancer

__all__ = [
    "AnalyzerEngine",
    "AnalyzerRequest",
    "RecognizerResult",
    "EntityRecognizer",
    "PatternRecognizer",
    "AnalysisExplanation",
    "RecognizerRegistry",
    "NlpEngine",
    "NlpEngineProvider",
    "ContextAwareEnhancer",
    "LemmaContextAwareEnhancer",
]

__version__ = "2.2.354"
