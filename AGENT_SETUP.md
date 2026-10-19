# AI Agent Integration Guide — Deus VectorMesh

This guide provides **model-agnostic** tool schemas and code patterns to connect **Deus VectorMesh** to any modern AI agent framework (Google Gemini, Anthropic Claude, OpenAI, Ollama, LangChain, or custom agent loops).

---

## 1. Universal Tool Definition (JSON Schema)

Use this schema with any tool-calling model:

```json
{
  "name": "vector_search",
  "description": "Search local in-memory vector database for nearest semantic neighbors.",
  "parameters": {
    "type": "object",
    "properties": {
      "query_vector": {
        "type": "array",
        "items": { "type": "number" },
        "description": "Dense embedding vector representing the search query."
      },
      "top_k": {
        "type": "integer",
        "default": 3,
        "description": "Number of top similar results to return."
      }
    },
    "required": ["query_vector"]
  }
}
```

---

## 2. Model-Agnostic Implementation Examples

### Option A: Google Gemini (Python SDK)
```python
from google import genai
from google.genai import types
from module import DeusVectorMesh

mesh = DeusVectorMesh(dim=768)

def search_knowledge_base(query_vector: list[float], top_k: int = 3) -> dict:
    """Queries the local Deus VectorMesh."""
    return {"matches": mesh.query(query_vector, top_k=top_k)}

client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Find related documents for quantum theory",
    config=types.GenerateContentConfig(
        tools=[search_knowledge_base]
    )
)
```

### Option B: Anthropic Claude (Tool Calling)
```python
import anthropic
from module import DeusVectorMesh

mesh = DeusVectorMesh(dim=1536)

client = anthropic.Anthropic()
tools = [{
    "name": "vector_search",
    "description": "Search local vector memory",
    "input_schema": {
        "type": "object",
        "properties": {
            "query_vector": {"type": "array", "items": {"type": "number"}},
            "top_k": {"type": "integer", "default": 3}
        },
        "required": ["query_vector"]
    }
}]
```

### Option C: Local / Ollama / OpenAI Compatible
```python
from openai import OpenAI
from module import DeusVectorMesh

mesh = DeusVectorMesh(dim=384)
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
```
