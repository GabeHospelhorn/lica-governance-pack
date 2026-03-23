# LICA Governance Pack

Legal Incident & Compliance Architecture (LICA) is a decision-to-evidence governance system.

## Purpose
This repository binds:
- legal adjudication
- technical evidence
- quality management controls
- incident handling
- board-visible decision cadence
- ..

## Core structure
- `evidence/lica_crosswalk.csv` — decision-to-evidence crosswalk
- `schemas/incident_schema.json` — incident intake schema
- `templates/bv01_memo.md` — BV-01 decision memo
- `docs/regulator_packet_openai.md` — regulator-facing narrative
- `.github/workflows/pr-governance-comment.yml` — PR governance workflow
- `ci/check_lica_evidence.py` — evidence check script

## Operational principle
Every decision must have a receipt.
