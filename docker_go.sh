#!/bin/bash
docker image build -t chi_vio .
# docker run --env-file .env -dp5000:5000 --name chi_vio_container chi_vio
docker run -dp5000:5000 --name chi_vio_container chi_vio