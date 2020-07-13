#!/bin/bash

gunicorn --worker-class=gevent --worker-connections=1000 --workers=3 app:app --reload -b:8081