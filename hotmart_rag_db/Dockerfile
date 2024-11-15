FROM python:3.11-slim

# ENV variables
ENV DEBIAN_FRONTEND=noninteractive
ENV FASTAPI_PORT=$FASTAPI_PORT
ENV FASTAPI_HOST=$FASTAPI_HOST

# ChromaDB-related
ENV CHROMA_HOST=$CHROMA_HOST
ENV CHROMA_PORT=$CHROMA_PORT
ENV CHROMA_CLIENT_AUTH_CREDENTIALS=$CHROMA_CLIENT_AUTH_CREDENTIALS
ENV CHROMA_COLLECTION_NAME=$CHROMA_COLLECTION_NAME
ENV CHROMA_EMBEDDING_MODEL=$CHROMA_EMBEDDING_MODEL

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# DEBUG - print env variables

# Install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# Copy project files
COPY . /hotmart_rag_db

# Set working directory
WORKDIR /hotmart_rag_db

# Install python libraries
RUN uv sync --compile-bytecode

# Run project
CMD ["uv", "run", "main.py"]
