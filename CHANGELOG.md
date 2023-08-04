# Changelog
All notable changes, fixes, and additions to the project is listed in this changelog.  
After major version v1.0.0, the project adheres to [semantic versioning](https://semver.org/).

# V0.6.0
### Changed
- [#15](https://github.com/disruptive-technologies/python-integrations/pull/15) Deprecated Python 3.7 as it is end-of-life.

# v0.5.1
### Changed
- [#13](https://github.com/disruptive-technologies/python-integrations/pull/13) SHA-1 checksum replaced with SHA-256.

### Added
- [#14](https://github.com/disruptive-technologies/python-integrations/pull/14) Added build and test for Python 3.10.

# v0.5.0
### Changed
- [#10](https://github.com/disruptive-technologies/python-integrations/pull/10) Added support for new metadata field in payload body.
- [#10](https://github.com/disruptive-technologies/python-integrations/pull/10) Rewritten modules to better align with python-client architecture.

# v0.4.0
### Changed
- [#9](https://github.com/disruptive-technologies/python-integrations/pull/9) Replaced `decode()` EmptyStringError with ConfigurationError.

### Added
- [7c97f32](https://github.com/disruptive-technologies/python-integrations/commit/7c97f32b64a0b150cc2a45747afc274c5ddae786) Added support for 2nd generation temperature sensors.

# v0.3.0
_Released on 2021-06-10._
### Added
- [#6](https://github.com/disruptive-technologies/python-integrations/pull/6) Added stricter mypy rules, resulting in better type-hinting.
- [#7](https://github.com/disruptive-technologies/python-integrations/pull/7) Added support for Django provider.

### Changed
- [#8](https://github.com/disruptive-technologies/python-integrations/pull/8) Http Push `decode_request()` functions now also returns labels.

# v0.2.0
_Released on 2021-06-04._  
### Changed
- [#5](https://github.com/disruptive-technologies/python-integrations/pull/5) Renamed `validate()` to `decode()`.


# v0.1.0
_Released on 2021-06-03._  
Initial pre-release, open-sourcing, and PyPI publication of the project.
