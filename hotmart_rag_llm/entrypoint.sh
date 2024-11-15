#!/bin/bash

# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "🔴 Retrieving LLAMA3.2 model..."
ollama pull llama3.2
echo "🟢 Done!"

# Wait for Ollama process to finish.
wait $pid