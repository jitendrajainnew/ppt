---
name: fintech-mobile-design
description: Design system for Indian fintech mobile app. Use when
  building any screen, component, or UI element for the MF tracker app.
---

# MF Tracker Design System

## Design Direction
- Style: Clean, trust-building fintech (reference: Groww, Kuvera, Zerodha Coin)
- Mood: Professional but approachable for non-tech-savvy investors
- Dark mode: Support from day 1

## Colors
- Primary: Deep blue (#1A56DB) — trust, finance
- Positive/Profit: Green (#22C55E)
- Negative/Loss: Red (#EF4444)
- Background Light: #FFFFFF / Cards: #F8FAFC
- Background Dark: #0F172A / Cards: #1E293B
- Accent: Indigo (#6366F1) for CTAs

## Typography
- Font: Inter or System default
- Portfolio value: 32px bold — biggest text on screen
- Section headers: 18px semibold
- Body: 14px regular (minimum — many users are 40+)
- Numbers: Use tabular figures for alignment in tables
- Currency: Always ₹ prefix with Indian lakh/crore formatting

## Component Patterns
- Portfolio value card: Large ₹ number + daily change badge (green/red pill)
- Fund holding row: AMC logo | Fund name + category tag | Returns % | ₹ Value
- SIP card: ₹ Amount + next date + status badge (Active/Paused/Missed)
- Goal tracker: Circular progress ring + target ₹ + time remaining
- Charts: Line chart for NAV trend, donut for asset allocation
- Empty states: Friendly illustration + action button (not just "No data")

## Mobile-Specific
- Bottom tab navigation (4-5 tabs max): Portfolio | SIPs | Goals | Alerts | Profile
- Pull to refresh on all data screens
- Skeleton loaders (shimmer effect), never spinners
- Haptic feedback on invest/redeem actions
- Touch targets: 48px minimum
- Bottom sheet modals for fund details (not new screens)
- Swipe gestures for SIP cards (pause/resume)

## Avoid
- Cluttered dashboards with 10+ numbers visible at once
- Tiny fonts below 14px
- Financial jargon without tooltip/info icons
- Generic stock illustrations
- Bright colors on large surfaces (use muted tones)
