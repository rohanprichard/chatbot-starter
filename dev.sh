#!/bin/bash

uvicorn backend.server:app --reload --port 8000 --reload-include "*.py"
