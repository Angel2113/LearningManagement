FROM node:current-alpine3.22

# Set Working Directory
WORKDIR /app/

# Install dependencies
CMD ["npm", "install"]

# Copy the app code
COPY . ./app/src/

# RUN app
CMD ["npm", "run", "dev"]