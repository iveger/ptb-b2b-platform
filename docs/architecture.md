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

## System Boundaries

The PTB B2B Platform is explicitly NOT responsible for:

- Acting as a system of record for accounting or statutory reporting
- Replacing ERP or CRM systems
- Performing autonomous business decisions without human oversight
- Providing user-facing UI applications
- Guaranteeing real-time synchronization across external systems

The platform acts as:
- An orchestration and automation layer
- A controlled integration hub
- A data validation and enrichment component

Any functionality outside these boundaries must be implemented in external systems.

## Module Responsibilities

### Integrations Layer
- Owns communication with external systems
- Handles protocol translation and data normalization
- Does NOT contain business logic
- Does NOT make decisions

### Backend Layer
- Owns business rules and workflows
- Acts as the single source of truth
- Validates and persists data
- Coordinates interactions between modules

### AI Layer
- Provides analytical and assistive capabilities
- Generates recommendations and insights
- Does NOT initiate state changes
- Does NOT act without backend confirmation

### Infrastructure Layer
- Owns deployment, automation, and maintenance
- Provides observability and logging
- Does NOT influence business logic

