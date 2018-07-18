FROM alpine:3.8

LABEL maintainer="corban@utos.org"

WORKDIR /usr/src/app

COPY assets/* ./ 

RUN apk add --no-cache npm && \
    addgroup -g 1000 node && \
    adduser -u 1000 -G node -s /bin/sh -D node && \
    npm install

USER node

EXPOSE 8080

CMD [ "node", "app.js" ]
