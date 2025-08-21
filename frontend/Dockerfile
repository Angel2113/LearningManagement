FROM node:current-alpine3.22

#RUN apt-get update

# Set Working Directory
WORKDIR /src/

#Copy the app code
COPY . ./src/

ENTRYPOINT ["sh", "-c"]

# Install dependencies
CMD ["npm install && npm run dev"]

# Copy the app code
#COPY . ./app/src/

# RUN app
#CMD ["npm", "run", "dev"]