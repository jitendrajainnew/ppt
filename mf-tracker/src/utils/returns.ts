/**
 * Financial return calculations for Indian mutual funds.
 * XIRR for SIPs, CAGR for lumpsum > 1yr, absolute for < 1yr.
 */

interface Cashflow {
  amount: number; // negative = investment, positive = redemption/current value
  date: Date;
}

/** Calculate XIRR using Newton-Raphson with bisection fallback */
export function calculateXIRR(cashflows: Cashflow[]): number | null {
  if (cashflows.length < 2) return null;

  const sorted = [...cashflows].sort(
    (a, b) => a.date.getTime() - b.date.getTime()
  );

  const daysBetween = (d1: Date, d2: Date) =>
    (d1.getTime() - d2.getTime()) / (365.25 * 24 * 60 * 60 * 1000);

  const f = (rate: number): number =>
    sorted.reduce((sum, cf) => {
      const years = daysBetween(cf.date, sorted[0].date);
      return sum + cf.amount / Math.pow(1 + rate, years);
    }, 0);

  const df = (rate: number): number =>
    sorted.reduce((sum, cf) => {
      const years = daysBetween(cf.date, sorted[0].date);
      if (years === 0) return sum;
      return sum - (years * cf.amount) / Math.pow(1 + rate, years + 1);
    }, 0);

  // Newton-Raphson
  let guess = 0.1;
  for (let i = 0; i < 100; i++) {
    const fVal = f(guess);
    const dfVal = df(guess);

    if (Math.abs(dfVal) < 1e-10) break;

    const newGuess = guess - fVal / dfVal;
    if (Math.abs(newGuess - guess) < 1e-7) {
      return newGuess;
    }
    guess = newGuess;

    if (!isFinite(guess) || isNaN(guess)) break;
  }

  // Bisection fallback
  let lo = -0.99;
  let hi = 10.0;
  for (let i = 0; i < 200; i++) {
    const mid = (lo + hi) / 2;
    const fMid = f(mid);

    if (Math.abs(fMid) < 1e-7) return mid;
    if (f(lo) * fMid < 0) {
      hi = mid;
    } else {
      lo = mid;
    }
  }

  return (lo + hi) / 2;
}

/** Absolute return: (current - invested) / invested × 100 */
export function calculateAbsoluteReturn(
  investedPaise: number,
  currentPaise: number
): number {
  if (investedPaise === 0) return 0;
  return ((currentPaise - investedPaise) / investedPaise) * 100;
}

/** CAGR: (current / invested) ^ (1/years) - 1 */
export function calculateCAGR(
  investedPaise: number,
  currentPaise: number,
  years: number
): number {
  if (investedPaise <= 0 || years <= 0) return 0;
  return (Math.pow(currentPaise / investedPaise, 1 / years) - 1) * 100;
}

/** Calculate required monthly SIP for a future goal */
export function calculateRequiredSIP(
  targetAmount: number,
  years: number,
  annualReturnRate: number
): number {
  const monthlyRate = annualReturnRate / 12 / 100;
  const months = years * 12;

  if (monthlyRate === 0) return targetAmount / months;

  return (targetAmount * monthlyRate) / (Math.pow(1 + monthlyRate, months) - 1);
}

/** Inflate a current amount to future value */
export function futureValue(
  currentAmount: number,
  years: number,
  inflationRate: number
): number {
  return currentAmount * Math.pow(1 + inflationRate / 100, years);
}
