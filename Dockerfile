FROM python:3.11

# Set the working directory in docker
WORKDIR /app

COPY . /app

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Clean up apt cache to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV OPENAI_API_KEY=your_api_key_here

# Expose the port Streamlit is running on
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "main.py"]