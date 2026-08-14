# Changelog

All notable changes to this repository will be documented here.

## [Unreleased]

### Added

- Client resilience guide covering timeouts, transport errors, HTTP failures, payload parsing, retry strategy, rate limits, token handling and logging.

### Changed

- GitHub Actions quality workflow is manual-only while repository checks are run locally to control CI consumption.
- PHP example now reports malformed JSON responses explicitly instead of exposing an uncaught decode exception.

## [0.1.0] - 2026-08-07

### Added

- initial public BIBLIAAPI integration examples;
- cURL example using Bearer authentication from environment variables;
- PHP example;
- JavaScript example;
- syntax quality workflow;
- security policy, contribution guide and code of conduct;
- MIT license.
