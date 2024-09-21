# Base image with Python 3.10
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the project files to the working directory
COPY . /app/

CMD ["python" , "manage.py", "migrate"]
CMD ["python" , "manage.py", "create_admin","vishu1132","vishu1132@gmail.com","123"]