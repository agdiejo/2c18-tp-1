FROM node:10.9.0
RUN mkdir /usr/app
WORKDIR /usr/app
COPY package.json package.json
RUN npm install
COPY app.js app.js
#ENTRYPOINT ["npm", "start", "$PUERTO_NODE"]