# Quick Start

Ecosystem Plugin for Fantom support in Ape

## Dependencies

- [python3](https://www.python.org/downloads) version 3.8 up to 3.11.

## Installation

### via `ape`

You can install this plugin using `ape`:

```bash
ape plugins install fantom
```

or via config file:

```yaml
# ape-config.yaml
plugins:
  - name: fantom
```

### via `pip`

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install ape-fantom
```

### via `setuptools`

You can clone the repository and use [`setuptools`](https://github.com/pypa/setuptools) for the most up-to-date version:

```bash
git clone https://github.com/ApeWorX/ape-fantom.git
cd ape-fantom
python3 setup.py install
```

## Quick Usage

Installing this plugin adds support for the Fantom ecosystem:

```bash
ape console --network fantom:opera
```
