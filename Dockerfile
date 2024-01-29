# Use an official Python runtime as a parent image
FROM python:3.11

# Copy the current directory contents into the container at /app
COPY ./fightclub fightclub

# Set the working directory in the container
WORKDIR /fightclub

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8000 for the Django app to run on
EXPOSE 5000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]