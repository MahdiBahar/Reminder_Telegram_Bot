# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the application file into the container
COPY todo_task.py .

# Define the command to run your application
CMD ["python", "todo_task.py"]
