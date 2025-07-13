/* 
#    This program is for the automatic creation of database roles upon first start.
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
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.*/


-- Create casbin role
CREATE ROLE casbin NOLOGIN;
CREATE ROLE casbin_login LOGIN PASSWORD :casbin_login_pass;
GRANT casbin TO casbin_login;

-- Create server admin, write and read roles
CREATE ROLE server_admin LOGIN PASSWORD 'SUBSTITUTE_PASSWORD';
CREATE ROLE server_write LOGIN PASSWORD 'SUBSTITUTE_PASSWORD';
CREATE ROLE server_read LOGIN PASSWORD 'SUBSTITUTE_PASSWORD';

CREATE ROLE zitadel LOGIN PASSWORD 'zitadel';