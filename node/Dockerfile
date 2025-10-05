FROM node:24-alpine

WORKDIR /app

COPY . .
RUN npm install express

EXPOSE 3000

CMD [ "node", "server.js" ]
