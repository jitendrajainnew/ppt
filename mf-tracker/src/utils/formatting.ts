/**
 * Indian number formatting utilities.
 * All monetary values stored in paise internally, displayed in ₹.
 */

/** Format number in Indian lakh/crore system: ₹1,23,45,678.00 */
export function formatIndianCurrency(paise: number): string {
  const rupees = paise / 100;
  const isNegative = rupees < 0;
  const abs = Math.abs(rupees);
  const [intPart, decPart] = abs.toFixed(2).split('.');

  // Indian grouping: last 3 digits, then groups of 2
  let formatted: string;
  if (intPart.length <= 3) {
    formatted = intPart;
  } else {
    const last3 = intPart.slice(-3);
    const remaining = intPart.slice(0, -3);
    const grouped = remaining.replace(/\B(?=(\d{2})+(?!\d))/g, ',');
    formatted = `${grouped},${last3}`;
  }

  const sign = isNegative ? '-' : '';
  return `${sign}₹${formatted}.${decPart}`;
}

/** Abbreviate large amounts: ₹1.5L, ₹2.3Cr */
export function formatCompactCurrency(paise: number): string {
  const rupees = Math.abs(paise / 100);
  const sign = paise < 0 ? '-' : '';

  if (rupees >= 1_00_00_000) {
    return `${sign}₹${(rupees / 1_00_00_000).toFixed(1)}Cr`;
  }
  if (rupees >= 1_00_000) {
    return `${sign}₹${(rupees / 1_00_000).toFixed(1)}L`;
  }
  if (rupees >= 1_000) {
    return `${sign}₹${(rupees / 1_000).toFixed(1)}K`;
  }
  return formatIndianCurrency(paise);
}

/** Format percentage with 2 decimal places */
export function formatPercent(value: number): string {
  const sign = value > 0 ? '+' : '';
  return `${sign}${value.toFixed(2)}%`;
}

/** Format NAV with 4 decimal places */
export function formatNAV(nav: number): string {
  return `₹${nav.toFixed(4)}`;
}

/** Format units with 3 decimal places */
export function formatUnits(units: number): string {
  return units.toFixed(3);
}
