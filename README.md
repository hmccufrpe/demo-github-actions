# Demo: GitHub Actions com uma API de tarefas

## Rodar local
    pip install -r requirements-dev.txt
    uvicorn app.main:app --reload
    pytest && ruff check .

## Preparação (antes da apresentação)
1. Crie o repo no GitHub e suba este projeto na `main`.
2. Settings > Environments > crie `production` e ative *Required reviewers*.
3. Settings > Branches > proteja a `main` exigindo o check `test` (CI) antes do merge.
4. (Opcional) crie o secret `DEPLOY_HOOK` (ex.: deploy hook do Render). Sem ele, o deploy é simulado.

## Branches da demo
- `feature/nova-rota`: mudança válida (CI verde).
- `feature/bug`: em `app/main.py`, troque `task["done"] = True` por `task["done"] = False`.
  O teste `test_complete_task` falha e o PR fica bloqueado. Corrija no próprio PR.

## Roteiro
1. PR abre CI (matrix 3.11 e 3.12, lint, testes).
2. Commit com bug: check vermelho bloqueia merge. Fix: verde.
3. Merge na `main`: build e push no GHCR; deploy aguarda aprovação.
4. `nightly.yml`: rode manualmente via *Run workflow* (workflow_dispatch).
