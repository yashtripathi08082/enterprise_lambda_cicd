#!/bin/bash

echo "Installing dependencies..."

pip install -r requirements.txt

echo "Running Ruff..."

ruff check .

echo "Running Black..."

black --check .

echo "Running Tests..."

pytest