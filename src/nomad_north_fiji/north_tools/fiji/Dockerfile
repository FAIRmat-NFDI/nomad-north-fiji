ARG IMAGE_TAG=main
ARG BASE_IMAGE=ghcr.io/fairmat-nfdi/nomad-north-desktop-base
ARG PLUGIN_NAME=nomad-north-apmtools

FROM ${BASE_IMAGE}:${IMAGE_TAG} AS base

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

RUN apt update \
 && apt-get install -y \
        unzip \
 && rm -rf /var/lib/apt/lists/*

# Switch back to jovyan to avoid accidental container runs as root
USER ${NB_UID}
WORKDIR "${HOME}"

RUN wget https://downloads.imagej.net/fiji/archive/stable/20250808-2217/fiji-stable-linux64-jdk.zip \
 && unzip fiji-stable-linux64-jdk.zip \
 && rm -f fiji-stable-linux64-jdk.zip

COPY --chown=${NB_UID}:${NB_GID} config/Fiji.desktop ${HOME}/.config/autostart/Fiji.desktop
COPY --chown=${NB_UID}:${NB_GID} config/Fiji.desktop ${HOME}/Desktop/Fiji.desktop
