# Use an official Python runtime as a parent image
FROM python:3.8.17

# Set the working directory to /Puilin-Bot
WORKDIR /Puilin-Bot

# Copy the current directory contents into the container at /Puilin-Bot
COPY . /Puilin-Bot/

# Install poetry
RUN pip install poetry==1.5.1

# Install project dependencies
RUN poetry install --no-root

# Set the working directory to the root directory of your project
WORKDIR /Puilin-Bot/bot/

# Run the bot script
CMD ["poetry", "run", "python", "bot.py"]
