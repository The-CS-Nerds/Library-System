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

FROM node:18-alpine AS build

RUN apk add --no-cache yarn

# update dependencies as needed @HippoProgrammer

WORKDIR /src/frontend

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*
COPY --from=build /src/frontend/dist /usr/share/nginx/html

EXPOSE 80

# change port if needed

CMD ["nginx", "-g", "daemon off;"]