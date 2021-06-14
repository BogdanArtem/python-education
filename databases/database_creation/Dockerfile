FROM postgres
COPY db_init/* /docker-entrypoint-initdb.d/

ENV POSTGRES_PASSWORD=pass

EXPOSE 5432
