FROM nginx:1.15.1-alpine

LABEL maintainer="corban@utos.org"

EXPOSE 80 443

COPY assets/* /usr/share/nginx
COPY config/nginx.conf /etc/nginx/nginx.conf
COPY config/default.conf /etc/nginx/conf.d/default.conf 
COPY config/snippets/* /etc/nginx/snippets/

USER nginx

CMD [ "nginx", "-g", "daemon off;" ]
