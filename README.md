# TwinAero: Enterprise Airline Operations & Business Digital Twin

TwinAero is a 100% open-source, Docker-enabled, AI-native digital twin platform for airline operations, fleet maintenance, crew rostering, culinary logistics, and commercial ancillary services. It integrates real-time event streaming via Apache Kafka, time-series telemetry via TimescaleDB, and multi-agent AI orchestration driven by private/public LLMs through the Model Context Protocol (MCP).

---

## 🚀 High-Level Architecture & Stack

```
## 🚀 High-Level Architecture

```mermaid
graph TD
    %% Define Styles
    classDef ui fill:#e1f5fe,stroke:#01579b,stroke-width:2px,rounded:true;
    classDef kafka fill:#fff3e0,stroke:#e65100,stroke-width:2px;
    classDef db fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#f3e5f5,stroke:#4a148c,stroke-width:2px;
    classDef ext fill:#f5f5f5,stroke:#616161,stroke-width:1px;

    %% Nodes
    UI[Live Operational Interface / Streamlit Dashboard]:::ui
    
    subgraph Ingestion ["Data Ingestion & Streaming Mesh"]
        Ext[Partner Airlines, OEM, FIDS, Banks, Rail]:::ext
        Kafka[Apache Kafka Event Mesh]:::kafka
    end

    subgraph Persistence ["Data Persistence & State Engine"]
        Timescale[TimescaleDB - Time-Series]:::db
        Redis[Redis / Valkey - Cache]:::db
    end

    subgraph Agents ["AI Agentic & Inference Layer"]
        Crew[CrewAI / LangGraph Agents]:::ai
        MCP[MCP Aviation Connectors]:::ai
        Ollama[Ollama / Local Private LLM]:::ai
    end

    %% Flow / Connections
    UI -->|API Gateway| Crew
    Ext -->|Telemetry / Events| Kafka
    Kafka -->|Stream Consumer| Timescale
    Crew -->|Tool Calls| MCP
    MCP -->|Query State| Timescale
    Crew -->|Inference| Ollama
    Timescale -.->|State Feed| UI

```

### Core Technology Stack
* **Simulation & State Engine:** TimescaleDB (PostgreSQL) + Redis (In-memory broker).
* **Streaming Event Mesh:** Apache Kafka & ZooKeeper (ACARS telemetry, SGHA ground handling, intermodal rail, payment gateways).
* **AI Orchestration & Agentic Layer:** Python 3.12, CrewAI / LangGraph, Model Context Protocol (MCP) servers.
* **Inference Layer:** Ollama / vLLM (Private Local LLMs) with GPU pass-through + Public LLM routers.
* **Orchestration:** Docker Compose.

---

## 📁 Repository Structure

```tree
twinaero/
├── docker-compose.yml             # Full containerized stack
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
├── data/                          # Enterprise IATA-aligned dataset (XLSX)
├── src/
│   ├── app.py                     # Streamlit / FastAPI control panel
│   ├── stream_worker.py           # Kafka event consumer & DB synchronizer
│   └── mcp_server.py              # Model Context Protocol aviation tools
└── snapshots/                     # Architecture diagrams & UI previews
```

---

## 🛠️ How to Install & Run

### Prerequisites
* Docker & Docker Compose
* NVIDIA Container Toolkit (optional, for local GPU LLM acceleration via Ollama)
* Python 3.12+

### Quick Start
1. Clone the repository:
   ```bash
   git clone https://github.com/roime81/twinaero.git
   cd twinaero
   ```

2. Spin up the entire infrastructure stack:
   ```bash
   docker-compose up --build -d
   ```

3. Verify container health:
   ```bash
   docker ps
   ```

---

## 💡 How to Use

1. **Trigger Real-Time Streams:** Send payload events to the Kafka broker topics (`aerovanguard.flight.telemetry`, `aerovanguard.finance.settlements`).
2. **Interact with AI Agents:** Query the multi-agent engine to analyze flight delays, evaluate IATA FTL crew legality, or simulate airport weather disruptions.
3. **Inspect State:** Connect to TimescaleDB (`localhost:5432`, user: `postgres`, password: `password`, db: `airlinetwin`) to explore operational records across Flight Operations, Fleet Maintenance (SGHA), Crew Roster (FTL), Culinary Catering, and Ancillary Business.

---

## 📸 Snapshots & Dashboards

> *High-level architectural dashboard preview showing real-time aircraft rotations, delay propagation, and agentic disruption handling.*
