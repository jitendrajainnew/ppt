---
globs: "src/**/*.{ts,tsx}"
---
- TypeScript strict mode, no `any` types
- Path aliases: @/screens, @/components, @/services, @/hooks, @/utils, @/types
- Named exports (not default) except for screens
- Error boundaries on every screen
- No inline styles — use NativeWind classes
- No console.log in committed code (use proper logging)
- Async functions must have try-catch with user-friendly error messages
