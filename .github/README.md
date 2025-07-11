# GitHub Actions CI/CD Pipeline

This directory contains the continuous integration and deployment workflows for the Advanced Sentiment Analysis System.

## Workflows

- `ci-cd.yml`: Main pipeline for testing, security scanning, building, and deployment
- `codeql-analysis.yml`: CodeQL security analysis
- `dependency-review.yml`: Automated dependency vulnerability scanning

## Pipeline Stages

1. **Test**: Unit tests, integration tests, coverage reporting
2. **Security**: Bandit security scanning, dependency vulnerability checks
3. **Build**: Docker image building and publishing to GitHub Container Registry
4. **Deploy**: Automated deployment to staging environment
5. **Release**: Automated versioning and GitHub releases

## Configuration

The pipeline uses the following secrets (configure in repository settings):
- `SLACK_WEBHOOK_URL`: For deployment notifications
- `GITHUB_TOKEN`: Automatically provided by GitHub

## Usage

- Push to `main` or `develop` branches triggers the full pipeline
- Pull requests trigger testing and security scanning
- Commits with `[release]` in the message trigger automated releases