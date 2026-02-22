---
globs: "src/**/*.test.{ts,tsx}"
---
- Test financial calculations exhaustively (edge cases matter)
- Use Jest + React Native Testing Library
- Test files colocated: Component.tsx → Component.test.tsx
- Mock Supabase client in tests
- Test XIRR with known expected values (verify against Excel)
- Test Indian number formatting with edge cases (0, negative, crores)
- Snapshot tests for UI components (catch unintended changes)
