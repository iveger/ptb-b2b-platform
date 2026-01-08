# System Architecture

## Architectural Overview

The PTB B2B Platform follows a layered modular architecture with clear responsibility boundaries.

## Logical Layers

### 1. Integration Layer
Responsible for:
- Communication with external systems (e.g., 1C)
- Data ingestion and export
- Protocol adaptation and data normalization

Located in:
/integrations


### 2. Core Backend Layer
Responsible for:
- Business logic
- Data validation
- Workflow orchestration
- API exposure for internal consumers

Located in:
/backend


### 3. AI Assistance Layer
Responsible for:
- Data enrichment
- Pattern detection
- Recommendation generation
- Non-authoritative decision support

Located in:
/ai


### 4. Infrastructure & Automation Layer
Responsible for:
- CI/CD
- Scripts and maintenance tasks
- Environment setup

Located in:
/.github

/scripts

## Design Constraints

- No direct coupling between AI layer and integrations
- Backend layer is the single source of truth
- Integrations are stateless where possible
- All cross-layer communication must be explicit and traceable
