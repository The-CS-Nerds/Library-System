#!/bin/sh
export DB_PASS=`python3 dbKeyGen.py --keys db --print`
export CASBIN_LOGIN_PASS=`python3 dbKeyGen.py --keys auth --print`
if [ $1 = "--kill" ]; then
  docker compose down
  docker system prune
  exit 0
fi
else;
  docker compose up --build $1
fi
unset DB_PASS
unset CASBIN_LOGIN_PASS