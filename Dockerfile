# syntax=docker/dockerfile:1
FROM frostedcarbon/tfc-cli:v0.8.0 AS get-tfc-cli
FROM python:3.9.7-slim-bullseye
COPY --from=get-tfc-cli ./tfc-cli /
COPY entrypoint.py /
ENTRYPOINT ["/entrypoint.py"]
