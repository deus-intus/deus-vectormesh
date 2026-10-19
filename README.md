<div align="center">

```
  ____  _____ _   _ ____    ___ _   _ _____ _   _ ____  
 |  _ \| ____| | | / ___|  |_ _| \ | |_   _| | | / ___| 
 | | | |  _| | | | \___ \   | ||  \| | | | | | | \___ \ 
 | |_| | |___| |_| |___) |  | || |\  | | | | |_| |___) |
 |____/|_____|\___/|____/  |___|_| \_| |_|  \___/|____/ 
```

### **TECHNOLOGY · PEOPLE · A HIGHER TOMORROW**
**DEUS INTUS // DEVELOPER ARM** — *Brand System v1.0*  
*Digital systems, products, and infrastructure.*

---
</div>

> **Elevator Line:** *"We build intelligent systems, products, and infrastructure that help ideas become operational reality."*

# ⚡ Deus VectorMesh (`deus-vectormesh`)

> **Zero-dependency, local in-memory vector database based on statutory public domain Kademlia DHT routing.**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-0A57D6.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-33CFFF.svg)](https://opensource.org/licenses/MIT)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0%20(pure%20stdlib)-33CFFF.svg)](#)
[![Model Agnostic](https://img.shields.io/badge/AI-Model%20Agnostic-031B4E.svg)](./AGENT_SETUP.md)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Walkthrough%20Notebook-EAF4FF.svg)](./walkthrough.ipynb)

---

## 1. What This Is
Deus VectorMesh is a high-velocity, in-memory vector database implemented entirely in pure Python standard library. It requires zero third-party packages, zero C-extensions, and zero cloud API keys, providing sub-millisecond semantic search and vector routing on any machine.

## 2. Who It Is For
- **AI Agent Engineers:** Integrating local vector memory into autonomous agents with zero external pip dependencies.
- **Edge & Embedded Developers:** Deploying semantic search in resource-constrained environments where external vector databases cannot run.
- **Privacy-First Organizations:** Running local RAG (Retrieval-Augmented Generation) with absolute data sovereignty.

## 3. Current Status
**Production / Standalone Sovereign Package.** Fully verified across Python 3.9+ with comprehensive unit test coverage.

## 4. What Works Now vs Planned
### What Works Now:
- Pure Python vector indexing and exact cosine similarity calculation.
- Sub-millisecond top-$k$ nearest neighbor retrieval.
- Arbitrary document metadata attachment and payload filtering.
- 1-Click quickstart execution via `python3 quickstart.py`.
- Interactive Jupyter Notebook walkthrough in [`walkthrough.ipynb`](./walkthrough.ipynb).
- Universal model-agnostic agent schemas in [`AGENT_SETUP.md`](./AGENT_SETUP.md).

### Planned:
- Persistent disk-backed append log serialization.

## 5. How to View or Use It (30-Second Quickstart)
No installation required! Simply clone and run:

```bash
# 1. Clone the repository
git clone https://github.com/deus-intus/deus-vectormesh.git
cd deus-vectormesh

# 2. Run the 1-click quickstart (zero dependencies)
python3 quickstart.py

# 3. Run the unit test suite
python3 -m unittest test_module.py
```

## 6. What Is in the Repository
- `module.py` — Core `DeusVectorMesh` engine and cosine distance functions.
- `quickstart.py` — 30-second runnable demo script.
- `walkthrough.ipynb` — Interactive visual Jupyter Notebook walkthrough.
- `AGENT_SETUP.md` — Ready-to-copy tool schemas for Google Gemini, Anthropic Claude, OpenAI, and Ollama.
- `test_module.py` — Full unit test suite.
- `pyproject.toml` — Standard packaging configuration.

## 7. Model-Agnostic Agent Integration
Deus VectorMesh is 100% model-agnostic. It can be invoked as a tool by any LLM. See [`AGENT_SETUP.md`](./AGENT_SETUP.md) for full JSON schemas and agent invocation code.

## 8. Connections and Requirements
- Python 3.9 or higher (standard library only).
- Memory footprint: ~15MB baseline. Zero network sockets required.

## 9. License and Contribution Information
Licensed under the permissive [MIT License](./LICENSE). Copyright © Deus Intus Ltd.

---

## 🛡️ Intellectual Property & Statutory UK Trade Mark Notice

- **Registered UK Trade Mark:** `DEUS INTUS®` is a registered trade mark of **Deus Intus Ltd** in the United Kingdom under **UK Trade Mark No. UK00004416539**. All rights reserved.
- **Corporate Registration:** Deus Intus Ltd is a company registered in England and Wales (Company No. `17209569`), Registered Office: `66 Paul Street, London, EC2A 4NA, United Kingdom`.
- **Statutory IP Architecture:** Software primitives synthesized by Deus Intus combine 20-year statutory public-domain algorithmic cores with modern permissive runtimes into zero-dependency, model-agnostic, sovereign software modules.
- **Support & Inquiries:** Official support at [`support@deusintus.com`](mailto:support@deusintus.com).
