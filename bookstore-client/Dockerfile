# pull official base image
FROM node:13.12.0-alpine

# set working directory
WORKDIR /bookstore

# add `/app/node_modules/.bin` to $PATH
ENV PATH /bookstore/node_modules/.bin:$PATH

# install app dependencies
RUN apk add curl
COPY ./bookstore/package.json ./
RUN mkdir -p node_modules/node-sass/vendor/linux-x64-79
RUN curl -L  https://github.com/sass/node-sass/releases/download/v4.13.1/linux_musl-x64-79_binding.node -o node_modules/node-sass/vendor/linux-x64-79/binding.node

RUN npm rebuild node-sass
RUN yarn

# add app
COPY ./bookstore ./

# start app
CMD ["yarn", "start"]