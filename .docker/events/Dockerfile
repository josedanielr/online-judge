FROM josedrm/nodesource

ENV NODE_PATH node_modules

RUN mkdir /usr/etc
COPY .docker/conf/npmrc /usr/etc
RUN npm install qu ws simplesets

COPY websocket websocket/
COPY .docker/events/config.js websocket/

CMD ["node", "websocket/daemon.js"]
