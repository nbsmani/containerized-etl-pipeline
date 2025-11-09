FROM python:3.9-slim
WORKDIR /data_importer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./data ./src ./
ENTRYPOINT [ "python","data_importer.py" ]
CMD ["01_paris_airbnb_listings.csv","sqluser","secret","dbms","5432", "global_data","paris_airbnb" ]
