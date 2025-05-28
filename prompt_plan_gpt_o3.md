# Prompt Plan for Career Profile Intelligence Platform

Below is a **three‑level build plan** followed by a **sequence of LLM‑ready prompts** (wrapped in `text` code‑blocks) that implement the plan step‑by‑step with test‑driven discipline.

---

## 1 High‑Level Blueprint (“What we’ll build”)

- **Phase 0 – Foundations**
  - Create monorepo (`career-intel/`) with `/backend`, `/frontend`, `/infra`, `.github/`.
  - Docker‑compose for Flask + PostgreSQL; Yarn/NPM workspace for React.
  - Pre‑commit hooks (black, isort, flake8, eslint, prettier).
  - CI pipeline (GitHub Actions) running unit tests + lint on each PR.

- **Phase 1 – Core Platform Skeleton**
  - Flask app with `/health` and `/settings/token` endpoints.
  - SQLAlchemy models for `UserConfig` (only row #1 for MVP) and Alembic migrations.
  - React app bootstrapped with Vite, routing, Tailwind, shadcn/ui.
  - Settings page to save the LinkedIn token (stored via backend API).

- **Phase 2 – Profile Data Model + CRUD**
  - Tables: `profile`, `job_history`, `education`, `tag`, `profile_tag`, `profile_version`.
  - REST endpoints for CRUD; pytest coverage.
  - Seed script to insert a sample profile (no LinkedIn call yet).

- **Phase 3 – LinkedIn Fetch Service**
  - Service class wrapping _public_ LinkedIn endpoints (token header) with rate‑limiter.
  - Worker (RQ or Celery) to populate DB from fetched JSON → structured tables.
  - Unit tests mocking LinkedIn responses.

- **Phase 4 – Batch Processing Pipeline**
  - Upload CSV/JSON list → disambiguation modal → enqueue jobs.
  - Progress tracker API (`/batch/<id>/status`).

- **Phase 5 – Dashboard MVP**
  - Timeline view (react‑timeline‑vertical) + `st_aggrid`‑like table for roles/education.
  - Tagging UI (multi‑select) & filter chips.
  - Toasts for fetch success/failure; delete profile button.

- **Phase 6 – Export + Finishing**
  - Backend routes for CSV / Excel / JSON export.
  - E2E tests (Playwright) for search → fetch → display → export.
  - Docker images published, one‑click `docker compose up` demo.

---

## 2 Milestone → Chunk Decomposition (“How we’ll build it”)

| Milestone | Iterative Chunk | Deliverable |
|-----------|-----------------|-------------|
| **M0** | C0.1 Repo skeleton<br>C0.2 Docker compose (Flask + PG)<br>C0.3 GitHub Actions CI | Linted, testable empty app boots |
| **M1** | C1.1 Flask app factory<br>C1.2 `/health` route + test<br>C1.3 SQLAlchemy base + Alembic<br>C1.4 Settings token CRUD + React form | Core API + DB + Settings UI |
| **M2** | C2.1 Profile tables & schemas<br>C2.2 CRUD endpoints + tests<br>C2.3 Insert sample profile via admin CLI | Data layer verified |
| **M3** | C3.1 LinkedIn client stub + rate‑limit<br>C3.2 Mapper JSON→ORM<br>C3.3 Worker queue + unit tests | Fetch service integrated |
| **M4** | C4.1 Upload endpoint<br>C4.2 Name→URL disambiguation modal<br>C4.3 Batch progress tracker | Batch pipeline MVP |
| **M5** | C5.1 Timeline component<br>C5.2 Table with sort/filter<br>C5.3 Tag CRUD & filter UI | Dashboard visible |
| **M6** | C6.1 Export endpoints<br>C6.2 Download buttons UI<br>C6.3 Playwright E2E flow | Feature‑complete MVP |

---

## 3 Micro‑Steps (“Right‑sizing” each chunk)

Below are the **first two milestones** exploded further; use the same pattern for later milestones.

### Milestone 0 – Foundations

| # | Step (2‑4 h each) | Tests |
|---|-------------------|-------|
| 0.1.1 | Initialise git repo with MIT LICENSE, README | N/A |
| 0.1.2 | Add `/backend` Poetry project; install Flask, pytest | `pytest -q` passes |
| 0.1.3 | Add `/frontend` Vite React template | `npm test` placeholder |
| 0.1.4 | Write `Dockerfile.backend` + `docker-compose.yml` incl. Postgres | `docker compose up` returns 200 / health |
| 0.1.5 | Add GitHub Action: lint + unit tests | Action green |
| 0.1.6 | Configure pre‑commit (black, isort, flake8) | `pre-commit run --all-files` clean |

### Milestone 1 – Core Platform Skeleton

| # | Step | Tests |
|---|------|-------|
| 1.1.1 | App factory pattern (`create_app`) | Unit test imports app |
| 1.1.2 | `/health` GET returns `{"status":"ok"}` | 200 assert |
| 1.1.3 | Set up SQLAlchemy & Alembic env | Migration generates tables |
| 1.1.4 | Create `UserConfig` model (`token`,`created_at`) | CRUD test |
| 1.1.5 | POST `/settings/token` → upsert token | Test 201 + DB row |
| 1.1.6 | React Settings page with form, Axios PUT, toast | Cypress test stub |
| 1.1.7 | Wire CORS & env var config | Integration test |

*(Continue micro‑planning for M2‑M6 similarly.)*

---

## 4 LLM Code‑Generation Prompts (one per micro‑step)

> **Contract**: write code **and matching tests only for the stated diff**, assume repo context from previous steps, do not modify unrelated files, and pass existing tests.

### Prompt 0.1.1 `init_repo`

```text
You are in an empty directory for project **career-intel**.  
Tasks:
1. `git init` and create `.gitignore` for Python, Node, Docker.  
2. Add `LICENSE` (MIT) and a minimal `README.md` with project name and one-sentence purpose.  
3. Commit with message "chore: initial repo skeleton".  
No other files. Provide the full file list and contents.
```

---

### Prompt 0.1.2 `backend_scaffold`

```text
Context: repo from Prompt 0.1.1.

Goal: create `/backend` Python package managed by Poetry.

Steps:
1. `poetry init` (non-interactive) with name `career_intel_backend`, Python ^3.11.  
2. Add dependencies: Flask==3.*, pytest, pytest-cov.  
3. Inside `backend`, create module `career_intel_back/__init__.py` with a minimal Flask app returning "placeholder".  
4. Add `tests/test_placeholder.py` asserting the route returns 200.  
5. Update `README.md` with backend run instructions.  
Output the **new/changed files only**. Ensure `pytest -q` passes.
```

---

### Prompt 0.1.3 `frontend_scaffold`

```text
Context: repo after Prompt 0.1.2.

Goal: scaffold React frontend.

Instructions:
1. Under `/frontend`, bootstrap a Vite + React + TS project called `career-intel-frontend`.
2. Add ESLint and Jest for unit testing; configure `npm test` alias to run Jest.
3. Implement a root component that renders "Career-Intel Frontend up".
4. Add a Jest test verifying the text renders.
Provide only the diff. All existing tests must still pass (`pytest`, `npm test`).
```

---

### Prompt 0.1.4 `docker_compose`

```text
Context: existing backend & frontend.

Produce:
1. `Dockerfile.backend` – multistage, poetry install, exposes 8000.  
2. `docker-compose.yml` with services:
   - `db`: postgres:16, env POSTGRES_* , volume `dbdata`
   - `backend`: build ./backend, env `DATABASE_URL`, depends_on db, ports 8000:8000
3. Modify backend entry‑point (`app.py` or gunicorn cmd) to read `DATABASE_URL`.
4. Add `make up` and `make down` targets in a root `Makefile`.

Add `tests/test_docker.py` using `subprocess` to assert `docker-compose config` exits 0 (mocked, no Docker runtime).

Return changed files only.
```

---

*(Continue prompts for **every micro‑step** 0.1.5, 0.1.6, 1.1.1 … 6.3 similarly. Each prompt: clear scope, explicit tests, no dangling TODOs.)*

---

### How to Extend the Prompt List

- Duplicate the pattern: `Prompt <milestone>.<step>_<slug>`.
- Reference prior code context explicitly.
- Each prompt produces:
  1. **Code** (implementation + tests) for that step only.
  2. **No breaking changes** – CI must stay green.
- Finish Milestone 6 with prompt 6.3 wiring export buttons & Playwright E2E, ensuring the entire flow works.

---

#### ✅ Review Checklist

- Steps granular (2‑4 h), each fully testable.  
- Prompts incremental, no orphaned code.  
- Early testing from the very first route.  
- Continuous integration wired before any “real” feature work.  
- Best practices baked in (lint, typing, migrations, rate‑limit).

Use this blueprint + prompt series to drive a code‑generation LLM (or pair‑programming) safely, with confidence in every merge.
