#    This program is for the automatic building of a Docker container from source code.
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

FROM python:3-alpine3.21

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --require-hashes --force-reinstall -r requirements.txt

RUN adduser --disabled-password --gecos '' appuser
USER appuser

ADD ./* ./

EXPOSE 8000

