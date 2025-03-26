# Reminder_Telegram_Bot

# Build the Docker Image
## Open the terminal, navigate to the project directory (where the Dockerfile is located), and run the following command:

### docker build -t todo-app .

# Verify the Image
## After the build completes, you can list your images to confirm that the image was created:

### docker images

# Run the Docker Container
## Since your application is interactive, you can run the container in interactive mode:

### docker run -it todo-app
