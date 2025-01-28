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
    && rm -rf /var/lib/apt/lists/*

# Set up Python environment
RUN pip3 install --upgrade pip
RUN pip3 install setuptools

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# Add .local/bin to PATH
ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"

# Set up bash completion and shell improvements
COPY .bashrc /home/${USERNAME}/.bashrc
RUN chown ${USERNAME}:${USERNAME} /home/${USERNAME}/.bashrc

# Switch to the user
USER $USERNAME

WORKDIR /workspace