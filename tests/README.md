# Testing Framework

## Overview
This directory contains comprehensive tests for the Advanced Sentiment Analysis System.

## Test Structure
```
tests/
├── __init__.py
├── conftest.py              # pytest configuration and fixtures
├── test_sentiment_analysis.py  # Core sentiment analysis tests
├── test_api.py              # API endpoint tests
├── test_security.py         # Security and validation tests
├── test_performance.py      # Performance and load tests
├── integration/             # Integration tests
│   ├── __init__.py
│   └── test_end_to_end.py
└── fixtures/                # Test data and fixtures
    ├── sample_texts.json
    └── expected_results.json
```

## Running Tests

### All Tests
```bash
pytest tests/
```

### With Coverage
```bash
pytest tests/ --cov=./ --cov-report=html
```

### Specific Test Categories
```bash
# Unit tests only
pytest tests/test_*.py

# Integration tests
pytest tests/integration/

# Performance tests
pytest tests/test_performance.py -v
```

## Test Categories

### Unit Tests
- Sentiment analysis accuracy
- DSPy module functionality
- Data preprocessing
- Error handling

### Integration Tests
- End-to-end workflow
- API integration
- Database operations
- External service integration

### Performance Tests
- Response time benchmarks
- Memory usage validation
- Concurrent request handling
- Scalability testing

### Security Tests
- Input validation
- API key protection
- Rate limiting
- Data sanitization

## Fixtures and Mock Data

Test fixtures are located in `tests/fixtures/` and include:
- Sample text data for various sentiment scenarios
- Expected analysis results
- Mock API responses
- Test configuration data

## Continuous Integration

Tests are automatically run on:
- Every push to main/develop branches
- Pull request creation
- Scheduled nightly runs

## Coverage Requirements

Minimum coverage thresholds:
- Overall: 85%
- Critical modules: 90%
- API endpoints: 95%