# Use the official Nginx base image
FROM nginx:alpine

# Copy the HTML file to the appropriate location in the container
COPY index.html /usr/share/nginx/html/

# Expose port 80 for the Nginx server
EXPOSE 80

# Start the Nginx server
CMD ["nginx", "-g", "daemon off;"]