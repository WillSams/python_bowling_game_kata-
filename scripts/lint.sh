#!/bin/bash
set -e
flake8 src/ specs/
python -m mypy src/
