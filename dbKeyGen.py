#    This program is for the generation of long randomised database and login keys.
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

from secrets import token_urlsafe
import os

os.makedirs("secrets", exist_ok=True)

with open("secrets/db_pass.txt", "w") as f:
    f.write(token_urlsafe(512))

with open("secrets/casbin_login_pass.txt", "w") as f:
    f.write(token_urlsafe(512))