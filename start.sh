#!/bin/bash
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/app/libs

# Cài đặt ultralytics mà không cài đặt các phụ thuộc của nó
pip install ultralytics==8.0.0 --no-deps

exec gunicorn server:app