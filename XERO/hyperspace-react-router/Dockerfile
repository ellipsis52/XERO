# build étape
FROM node:18-alpine AS build
WORKDIR /app
COPY . .
RUN npm install && npm run build

# serve étape
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html

