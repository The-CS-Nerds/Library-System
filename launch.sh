#!/bin/sh
export DB_PASS=`python3 dbKeyGen.py --keys db --print`
export CASBIN_LOGIN_PASS=`python3 dbKeyGen.py --keys auth --print`
docker compose up --build $1
unset DB_PASS
unset CASBIN_LOGIN_PASS