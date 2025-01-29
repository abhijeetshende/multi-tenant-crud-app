# 🐍 Use an official Python base image
FROM python:3.12

# 🏠 Set the working directory inside the container
WORKDIR /app

# 📦 Copy all project files into the container
COPY . .

# 🛠 Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 🌍 Expose the Flask app port (5000)
EXPOSE 5000

# 🚀 Command to run the Flask app
CMD ["python", "main.py"]
