FROM node:20.17.0-bullseye-slim

WORKDIR /appFrontend

COPY package.json .
COPY package-lock.json .
RUN npm install

COPY . .
