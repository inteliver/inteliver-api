#!/bin/bash

# change inteliver-api to your service name
conda create --name inteliver-api python=3.11 && source activate inteliver-api

make install-deps
make install-dev-deps

export PYTHONPATH=`pwd`/src

make all

make run