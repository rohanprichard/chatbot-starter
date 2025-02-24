FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    default-mysql-client \
    bash-completion \
    ca-certificates \
    vim \
    less \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Set up Node.js repository and install Node.js + npm
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get update && apt-get install -y nodejs \
    && npm install -g npm@latest \
    && rm -rf /var/lib/apt/lists/*

# Verify installations
RUN node --version && npm --version

# Set up Python environment
RUN pip3 install --upgrade pip
RUN pip3 install setuptools

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"

COPY .bashrc /home/${USERNAME}/.bashrc
RUN chown ${USERNAME}:${USERNAME} /home/${USERNAME}/.bashrc

USER $USERNAME

WORKDIR /workspace