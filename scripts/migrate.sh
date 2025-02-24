#!/bin/bash
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <slug>"
  exit 1
fi

alembic revision --autogenerate -m "$1"