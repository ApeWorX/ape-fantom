# Quick Start

Ecosystem Plugin for Fantom support in Ape

## Dependencies

- [Python 3](https://www.python.org/downloads) version 3.10 or greater.

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

### via source

You can clone the repository and install for development:

```bash
git clone https://github.com/ApeWorX/ape-fantom.git
cd ape-fantom
uv sync --group dev
uv run prek install
```

## Quick Usage

Installing this plugin adds support for the Fantom ecosystem:

```bash
ape console --network fantom:opera
```
