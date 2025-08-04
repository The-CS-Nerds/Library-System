#!/bin/sh
export DB_PASS=`python dbKeyGen.py --keys db --print`
export CASBIN_LOGIN_PASS=`python dbKeyGen.py --keys auth --print`
if [ $1 = "--kill" ]; then
  docker compose down -v
  docker system prune --force
  docker volume prune --force
  exit 0
else
  docker compose down -v
  docker compose up --build $1 backend db frontend
fi
unset DB_PASS
unset CASBIN_LOGIN_PASS