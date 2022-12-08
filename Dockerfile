FROM python
COPY . /src
CMD ["python", "/src/int.py"]