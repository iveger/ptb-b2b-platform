# ptb-b2b-platform

Internal monorepository for a B2B platform, including backend services, system integrations, and AI modules.

## Purpose

This repository contains the core components of the PTB B2B platform:
- Backend services and APIs
- Integrations with external systems (including 1C)
- AI-assisted modules and automation
- Technical documentation and architectural decisions

The repository is intended for internal use and structured to support long-term development and scalability.

## Repository Structure

/docs Project documentation and architectural decisions
/backend Backend services and APIs
/integrations External system integrations
/ai AI modules and assistants
/scripts Utility scripts and automation
/.github CI/CD and repository configuration


## Development Principles

- Monorepo architecture
- Clear separation of responsibilities
- Explicit architectural decisions
- Controlled access and change management
- Main branch is always stable

## Branching Model

- `main` — stable, production-ready state
- `dev` — active development
- `feature/*` — isolated feature development
- `hotfix/*` — critical fixes

Direct commits to `main` are restricted.

## Status

Project initialized. Active development has not started yet.
