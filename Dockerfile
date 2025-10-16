FROM registry.access.redhat.com/ubi9/python-39

USER 1001
WORKDIR /opt/app-root/src
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py ./

# Flask listen trên port 8080
EXPOSE 8080
CMD ["python", "app.py"]
