/* 
#    This program is for the automatic creation of database tables upon first start.
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
#    along with this program.  If not, see <https://www.gnu.org/licenses/>. */

CREATE TABLE IF NOT EXISTS books ( -- Needs to be updated in future
    id          UUID PRIMARY KEY,
    isbn        TEXT UNIQUE NOT NULL,
    title       TEXT NOT NULL,
    author      TEXT NOT NULL,
    published   DATE,
    description TEXT -- Will be done in markdown... Could be auto-generated in future if need be
);

CREATE TABLE IF NOT EXISTS loans ( -- Needs to be updated in future
    id            UUID PRIMARY KEY,
    isbn          TEXT      NOT NULL REFERENCES books(isbn)       ON UPDATE CASCADE,
    student_id    CHAR(4)   NOT NULL REFERENCES users(student_id) ON UPDATE CASCADE,
    borrowed_at   TIMESTAMPTZ    DEFAULT now(),
    due_at        DATE           NOT NULL,
    returned_at   TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS users (
  id UUID PRIMARY KEY,
  user_id INTEGER NOT NULL
  email TEXT NOT NULL UNIQUE,
  role TEXT NOT NULL,
);