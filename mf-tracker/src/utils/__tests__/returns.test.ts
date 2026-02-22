import {
  calculateXIRR,
  calculateAbsoluteReturn,
  calculateCAGR,
  calculateRequiredSIP,
  futureValue,
} from '../returns';

describe('calculateAbsoluteReturn', () => {
  it('calculates positive return', () => {
    expect(calculateAbsoluteReturn(100000, 120000)).toBeCloseTo(20.0);
  });

  it('calculates negative return', () => {
    expect(calculateAbsoluteReturn(100000, 80000)).toBeCloseTo(-20.0);
  });

  it('returns 0 for zero investment', () => {
    expect(calculateAbsoluteReturn(0, 10000)).toBe(0);
  });
});

describe('calculateCAGR', () => {
  it('calculates correct CAGR for 2x in 5 years', () => {
    // 2x in 5 years = ~14.87% CAGR
    const result = calculateCAGR(100000, 200000, 5);
    expect(result).toBeCloseTo(14.87, 1);
  });

  it('returns 0 for zero years', () => {
    expect(calculateCAGR(100000, 200000, 0)).toBe(0);
  });

  it('returns 0 for zero investment', () => {
    expect(calculateCAGR(0, 200000, 5)).toBe(0);
  });
});

describe('calculateXIRR', () => {
  it('calculates XIRR for simple investment', () => {
    const cashflows = [
      { amount: -100000, date: new Date('2024-01-01') },
      { amount: 112000, date: new Date('2025-01-01') },
    ];
    const result = calculateXIRR(cashflows);
    expect(result).not.toBeNull();
    expect(result! * 100).toBeCloseTo(12.0, 0);
  });

  it('returns null for insufficient cashflows', () => {
    expect(calculateXIRR([{ amount: -100000, date: new Date() }])).toBeNull();
  });

  it('handles SIP-like cashflows', () => {
    const cashflows = [
      { amount: -10000, date: new Date('2024-01-01') },
      { amount: -10000, date: new Date('2024-02-01') },
      { amount: -10000, date: new Date('2024-03-01') },
      { amount: -10000, date: new Date('2024-04-01') },
      { amount: -10000, date: new Date('2024-05-01') },
      { amount: -10000, date: new Date('2024-06-01') },
      { amount: 65000, date: new Date('2024-07-01') },
    ];
    const result = calculateXIRR(cashflows);
    expect(result).not.toBeNull();
    // Should be a positive return since 65000 > 60000 invested
    expect(result!).toBeGreaterThan(0);
  });
});

describe('calculateRequiredSIP', () => {
  it('calculates monthly SIP for retirement goal', () => {
    // Target: ₹1Cr in 20 years at 12% return
    const sip = calculateRequiredSIP(10000000, 20, 12);
    // Should be roughly ₹10,000/month
    expect(sip).toBeGreaterThan(5000);
    expect(sip).toBeLessThan(15000);
  });
});

describe('futureValue', () => {
  it('inflates correctly', () => {
    // ₹10L at 7% inflation for 10 years
    const fv = futureValue(1000000, 10, 7);
    expect(fv).toBeCloseTo(1967151.36, -1);
  });
});
