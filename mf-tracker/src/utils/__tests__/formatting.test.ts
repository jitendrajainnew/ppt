import {
  formatIndianCurrency,
  formatCompactCurrency,
  formatPercent,
  formatNAV,
  formatUnits,
} from '../formatting';

describe('formatIndianCurrency', () => {
  it('formats zero correctly', () => {
    expect(formatIndianCurrency(0)).toBe('₹0.00');
  });

  it('formats small amounts', () => {
    expect(formatIndianCurrency(99900)).toBe('₹999.00');
  });

  it('formats thousands', () => {
    expect(formatIndianCurrency(5000000)).toBe('₹50,000.00');
  });

  it('formats lakhs with Indian grouping', () => {
    expect(formatIndianCurrency(12345600)).toBe('₹1,23,456.00');
  });

  it('formats crores with Indian grouping', () => {
    expect(formatIndianCurrency(1234567800)).toBe('₹1,23,45,678.00');
  });

  it('formats negative amounts', () => {
    expect(formatIndianCurrency(-50000)).toBe('-₹500.00');
  });

  it('formats paise correctly', () => {
    expect(formatIndianCurrency(12350)).toBe('₹123.50');
  });
});

describe('formatCompactCurrency', () => {
  it('formats crores', () => {
    expect(formatCompactCurrency(200000000)).toBe('₹2.0Cr');
  });

  it('formats lakhs', () => {
    expect(formatCompactCurrency(15000000)).toBe('₹1.5L');
  });

  it('formats thousands', () => {
    expect(formatCompactCurrency(500000)).toBe('₹5.0K');
  });

  it('formats negative crores', () => {
    expect(formatCompactCurrency(-300000000)).toBe('-₹3.0Cr');
  });
});

describe('formatPercent', () => {
  it('adds + for positive', () => {
    expect(formatPercent(12.34)).toBe('+12.34%');
  });

  it('keeps - for negative', () => {
    expect(formatPercent(-5.6)).toBe('-5.60%');
  });

  it('handles zero', () => {
    expect(formatPercent(0)).toBe('0.00%');
  });
});

describe('formatNAV', () => {
  it('formats to 4 decimal places', () => {
    expect(formatNAV(45.1234)).toBe('₹45.1234');
  });
});

describe('formatUnits', () => {
  it('formats to 3 decimal places', () => {
    expect(formatUnits(123.456789)).toBe('123.457');
  });
});
