#!/usr/bin/env bash

#    This program is for the automatic movement of Docker secrets to environment variables, after on-the-fly generation.
#    Copyright (C) 2025, The CS Nerds (HippoProgrammer & SuitablyMysterious)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

set -euo pipefail

python3 dbKeyGen.py

export DB_PASS="$(< secrets/db_pass.txt)"

export DB_HOST="${DB_HOST:-localhost}"
export DB_PORT="${DB_PORT:-5432}"
export DB_NAME="${DB_NAME:-library}"
export DB_PASS=$(cat secrets/db_pass.txt)
export CASBIN_LOGIN_PASS=$(cat secrets/casbin_login_pass.txt)

#psql -v ON_ERROR_STOP=1 \
#     -v casbin_login_pass="$CASBIN_LOGIN_PASS" \
#     -f /docker-entrypoint-initdb.d/0_roles.sql

#exec /usr/local/bin/docker-entrypoint.sh "$@"


#rm secrets/db_pass.txt
#rm secrets/casbin_login_pass.txt
#rmdir secrets
