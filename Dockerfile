FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY image2css.py ./

CMD ["python", "image2css.py"]

# To build and run, enter the commands:
# docker build --no-cache -t abushaah .
# docker run --rm -v ${PWD}:/app abushaah