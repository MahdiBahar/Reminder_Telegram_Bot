# Reminder_Telegram_Bot

## Build the Docker Image
Open the terminal, navigate to the project directory (where the Dockerfile is located), and run the following command:

docker build -t todo-app .

## Verify the Image
After the build completes, you can list your images to confirm that the image was created:

docker images

## Run the Docker Container
Since your application is interactive, you can run the container in interactive mode:

docker run -it todo-app

## Save the Image to a Tar File:

Use the following command to save your image (e.g., todo-app) to a tar file named todo-app.tar:

docker save -o todo-app.tar todo-app

This command creates a file called todo-app.tar in your current directory containing your Docker image.

## Verify the Tar File:

You can check that the tar file has been created by listing the files in your directory:

ls -lh todo-app.tar

## Load the Image Later:

If you need to load the saved image on another machine or later on your current machine, use:

docker load -i todo-app.tar
