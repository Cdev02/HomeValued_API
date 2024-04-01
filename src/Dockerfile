FROM python:3.11.3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV APP_USERNAME=dev_cdmr
ENV APP_WORKING_DIR=/usr/src/HomeValued1
ENV PYTHONPATH=${PYTHONPATH}:${APP_WORKING_DIR}/src/

WORKDIR ${APP_WORKING_DIR}

COPY ./requirements.txt .

# RUN groupadd ${APP_USERNAME} && \
#     useradd -g ${APP_USERNAME} ${APP_USERNAME}

# RUN chown -R ${APP_USERNAME}:${APP_USERNAME} ${APP_WORKING_DIR}
# RUN chmod -R u=rwx,g=rwx ${APP_WORKING_DIR}

# USER ${APP_USERNAME}
# ENV PATH "$PATH:/home/${APP_USERNAME}/.local/bin"
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN export PYTHONPATH=$PYTHONPATH:$(pwd)/src/
RUN export PYTHONPATH=$PYTHONPATH:$(pwd)/src/models/
RUN export PYTHONPATH=$PYTHONPATH:$(pwd)/src/db/
RUN export PYTHONPATH=$PYTHONPATH:$(pwd)/src/routes/
RUN export PYTHONPATH=$PYTHONPATH:$(pwd)/src/utils/
COPY . ./src

CMD ["python", "./src/app.py", "-e", "production", "export"]
EXPOSE 5002