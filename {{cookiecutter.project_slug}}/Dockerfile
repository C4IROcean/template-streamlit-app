FROM python:3.9

ENV PYTHONFAULTHANDLER=1
ENV PYTHONBUFFERED=1

RUN pip install poetry

WORKDIR /src
COPY . .

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

ENV STREAMLIT_MAPBOX_TOKEN=""
ENV DB_CONNECTION_STR=""
ENV FIGURES_PATH=/src/figures

EXPOSE 8501

CMD ["python", "-m", "odp.app.{{cookiecutter.project_slug}}"]
