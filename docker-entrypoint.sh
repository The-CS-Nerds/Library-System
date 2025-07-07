#!/usr/bin/env bash
set -euo pipefail#

python3 dbKeyGen.py

export DB_PASS="$(< /run/secrets/db_pass)"
export CASBIN_LOGIN_PASS="$(< /run/secrets/casbin_login_pass)"

export DB_HOST="${DB_HOST:-localhost}"
export DB_PORT="${DB_PORT:-5432}"
export DB_NAME="${DB_NAME:-library}"

psql -v ON_ERROR_STOP=1 \
     -v casbin_login_pass="'$CASBIN_LOGIN_PASS'" \
     -f /docker-entrypoint-initdb.d/0_roles.sql

exec /usr/local/bin/docker-entrypoint.sh "$@"