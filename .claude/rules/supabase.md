---
globs: "supabase/**/*.sql"
---
- Every table with client data MUST have RLS enabled
- Write RLS policies immediately after CREATE TABLE
- Use auth.uid() for client-scoped access
- Migrations in supabase/migrations/ with timestamps
- Edge Functions in supabase/functions/
- Never use service_role key in client app
- Use Supabase generated types: `npx supabase gen types typescript`
