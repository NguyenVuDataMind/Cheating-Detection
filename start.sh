#!/bin/bash
export LD_LIBRARY_PATH=/app/libs
exec gunicorn server:app