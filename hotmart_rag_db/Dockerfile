FROM ubuntu:22.04

# ENV variables
ENV DEBIAN_FRONTEND=noninteractive
ENV FASTAPI_PORT=$FASTAPI_PORT
ENV FASTAPI_HOST=$FASTAPI_HOST

# ChromaDB-related
ENV CHROMA_HOST=$CHROMA_HOST
ENV CHROMA_PORT=$CHROMA_PORT
ENV CHROMA_SERVER_AUTHN_CREDENTIALS=$CHROMA_SERVER_AUTHN_CREDENTIALS
ENV CHROMA_SERVER_AUTHN_PROVIDER=$CHROMA_SERVER_AUTHN_PROVIDER
ENV CHROMA_CLIENT_AUTH_CREDENTIALS=$CHROMA_CLIENT_AUTH_CREDENTIALS
ENV CHROMA_COLLECTION_NAME=$CHROMA_COLLECTION_NAME
ENV CHROMA_EMBEDDING_MODEL=$CHROMA_EMBEDDING_MODEL

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# # Install dependencies
# RUN apt-get update && apt-get install -y \
#     curl \
#     git \
#     unzip \
#     wget \
#     zip \
#     && rm -rf /var/lib/apt/lists/*

# # Install uv
# RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Copy project files
COPY . /hotmart_rag_db

# Set working directory
WORKDIR /hotmart_rag_db

# Install dependencies
RUN uv venv --python 3.11
RUN uv sync

# Expose port
EXPOSE $FASTAPI_PORT

# Run project
CMD ["uv", "run", "main.py"]
