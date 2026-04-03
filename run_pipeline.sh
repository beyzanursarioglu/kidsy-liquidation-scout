#!/bin/bash

cd /Users/beyzanur/Desktop/kidsy-liquidation-scout || exit 1

echo "=== LAUNCHD RUN START: $(date) ===" >> logs/pipeline.log

python3 app/main.py >> logs/pipeline.log 2>&1

echo "=== LAUNCHD RUN END: $(date) ===" >> logs/pipeline.log
echo "" >> logs/pipeline.log