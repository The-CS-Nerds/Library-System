#!/usr/bin/env bash
set -euo pipefail#

pyton3 dbKeyGen.py

export DB_PASS="$(< /run/secrets/db_pass)"
export CASBIN_LOGIN_PASS="$(< /run/secrets/casbin_login_pass)"

export DB_HOST="${DB_HOST:-localhost}"
export DB_PORT="${DB_PORT:-5432}"
export DB_NAME="${DB_NAME:-library-system}"

exec /usr/local/bin/docker-entrypoint.sh "$@"