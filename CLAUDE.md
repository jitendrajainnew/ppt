# MF Tracker — Client Portfolio App

## Project
- Android app for mutual fund clients of a SEBI-registered MFD
- Stack: React Native + Expo + TypeScript
- Backend: Supabase (auth, DB, edge functions)
- Data: MFU/BSE Star API for real transactions
- Auth: Phone + OTP via Supabase

## Architecture
- /src/screens/ — all screens
- /src/components/ — reusable UI components
- /src/services/ — API calls (Supabase, MFU, BSE Star)
- /src/hooks/ — custom React hooks (React Query)
- /src/store/ — Zustand state management
- /src/utils/ — helpers (XIRR, date, currency formatting)
- /src/navigation/ — React Navigation / Expo Router
- /src/types/ — TypeScript interfaces
- /src/constants/ — colors, config, API endpoints

## Rules
- Functional components only, no class components
- All API calls through /src/services/ — never from screens directly
- Zustand for global state, React Query for server state
- All amounts in paise internally, display in ₹ Indian formatting
- Dates in ISO internally, display DD-MMM-YYYY
- Every screen: loading skeleton + error state + empty state + pull-to-refresh

## Key Decisions
- NAV data: AMFI daily feed, cached in Supabase
- Returns: XIRR for SIP, absolute for lumpsum, CAGR for goals
- Notifications: Expo Push Notifications for SIP reminders
- Charts: react-native-chart-kit or Victory Native

## Commands
- `npm start` — start Expo dev server
- `npm run android` — run on Android
- `npx tsc --noEmit` — type check
- `npx jest` — run tests
