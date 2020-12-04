FROM python:3

RUN mkdir -p /top_command

WORKDIR /top_command

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "./top_command.py"]
