# SeismicAI

**Seismic Data Interpretation & Reservoir Characterization Platform**

Oil & gas seismic data interpretation platform with horizon analysis, prospect evaluation, volumetric estimation, and risk assessment.

## Quick Start

```bash
docker compose up -d
```

- Frontend: http://localhost
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Features

- **Survey Management** — 2D/3D/4D seismic survey data management
- **Horizon Interpretation** — Amplitude analysis, bright spot detection, continuity evaluation
- **Prospect Evaluation** — Volume estimation, risk assessment, drill-ready classification
- **Volumetric Estimation** — Resource calculation based on horizon attributes
- **Risk Assessment** — Multi-factor risk analysis with adjusted probability scoring
- **Real-Time Feed** — WebSocket-powered live interpretation event stream

## Architecture

- **Backend:** FastAPI + async SQLAlchemy + PostgreSQL + WebSockets
- **Frontend:** React + TypeScript + Vite + Zustand + Axios
- **Auth:** JWT + bcrypt
- **Infrastructure:** Docker Compose

## License

MIT
