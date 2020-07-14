#!/bin/bash
gunicorn --worker-class=gevent --worker-connections=1000 --timeout 1200 --log-level debug --workers=3 app:app --reload -b:8081