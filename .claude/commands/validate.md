Run full validation:
1. `npx tsc --noEmit` — TypeScript check
2. `npx jest --passWithNoTests` — Run tests
3. `npx eslint src/ --ext .ts,.tsx` — Lint check
4. Report any failures with file + line number
