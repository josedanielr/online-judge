FROM josedrm/nodesource

ENV NODE_PATH node_modules

RUN npm install qu ws simplesets

COPY websocket .
COPY .docker/events/config.js websocket/

CMD ["node", "websocket/daemon.js"]
