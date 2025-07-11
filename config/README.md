# Advanced Sentiment Analysis System - Configuration

## Environment Configuration

This file contains configuration settings for different deployment environments.

### Development Environment (.env.development)
```env
# Development Configuration
OPENAI_API_KEY=your_development_api_key_here
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=DEBUG

# Database (if applicable)
DATABASE_URL=sqlite:///./dev_sentiment.db

# API Configuration
API_HOST=localhost
API_PORT=8000
API_WORKERS=1

# Rate Limiting (development - more lenient)
RATE_LIMIT_REQUESTS_PER_MINUTE=100
MAX_CONCURRENT_REQUESTS=10

# Security
CORS_ORIGINS=["http://localhost:3000", "http://localhost:8080"]
ALLOWED_HOSTS=["localhost", "127.0.0.1"]

# Monitoring
ENABLE_METRICS=true
METRICS_PORT=9090
```

### Production Environment (.env.production)
```env
# Production Configuration
OPENAI_API_KEY=your_production_api_key_here
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=INFO

# Database
DATABASE_URL=postgresql://user:password@db_host:5432/sentiment_analysis

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_WORKERS=4

# Rate Limiting (production - more restrictive)
RATE_LIMIT_REQUESTS_PER_MINUTE=1000
MAX_CONCURRENT_REQUESTS=100

# Security
CORS_ORIGINS=["https://yourdomain.com"]
ALLOWED_HOSTS=["yourdomain.com", "api.yourdomain.com"]
SECRET_KEY=your_secret_key_here

# Monitoring and Logging
ENABLE_METRICS=true
METRICS_PORT=9090
LOG_FILE=/var/log/sentiment_analysis.log
SENTRY_DSN=your_sentry_dsn_here

# Caching
REDIS_URL=redis://redis:6379/0
CACHE_TTL=3600

# Performance
WORKER_TIMEOUT=30
KEEP_ALIVE=2
```

### Testing Environment (.env.test)
```env
# Testing Configuration
OPENAI_API_KEY=test_api_key
ENVIRONMENT=test
DEBUG=true
LOG_LEVEL=DEBUG

# Test Database
DATABASE_URL=sqlite:///./test_sentiment.db

# API Configuration
API_HOST=localhost
API_PORT=8001
API_WORKERS=1

# Disable external services for testing
ENABLE_EXTERNAL_APIS=false
MOCK_RESPONSES=true

# Rate Limiting (testing - very lenient)
RATE_LIMIT_REQUESTS_PER_MINUTE=10000
MAX_CONCURRENT_REQUESTS=50
```

## Configuration Management

### Loading Configuration
The application automatically loads the appropriate configuration based on the `ENVIRONMENT` variable:

1. Check for environment-specific file (`.env.{ENVIRONMENT}`)
2. Fall back to `.env` file
3. Use default values for missing configurations

### Security Best Practices
- Never commit actual API keys to version control
- Use environment-specific configuration files
- Rotate API keys regularly
- Use strong secret keys for production
- Enable proper CORS settings for web applications

### Monitoring Configuration
- Enable metrics collection in production
- Configure proper log levels for each environment
- Set up error tracking with Sentry or similar service
- Configure health check endpoints

### Performance Tuning
- Adjust worker counts based on server resources
- Configure appropriate timeouts
- Enable caching in production
- Set reasonable rate limits