const MONTHS_SHORT = [
  'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
];

/** Format date as DD-MMM-YYYY (e.g., 15-Jan-2025) */
export function formatDate(isoDate: string): string {
  const d = new Date(isoDate);
  const day = String(d.getDate()).padStart(2, '0');
  const month = MONTHS_SHORT[d.getMonth()];
  const year = d.getFullYear();
  return `${day}-${month}-${year}`;
}

/** Format date as DD MMM (e.g., 15 Jan) */
export function formatDateShort(isoDate: string): string {
  const d = new Date(isoDate);
  const day = d.getDate();
  const month = MONTHS_SHORT[d.getMonth()];
  return `${day} ${month}`;
}

/** Get next SIP date from a given day of month */
export function getNextSIPDate(sipDay: number): Date {
  const now = new Date();
  const thisMonth = new Date(now.getFullYear(), now.getMonth(), sipDay);

  if (thisMonth > now) return thisMonth;

  // Next month
  return new Date(now.getFullYear(), now.getMonth() + 1, sipDay);
}

/** Days until a given date */
export function daysUntil(isoDate: string): number {
  const target = new Date(isoDate);
  const now = new Date();
  const diff = target.getTime() - now.getTime();
  return Math.ceil(diff / (1000 * 60 * 60 * 24));
}

/** Years between two dates */
export function yearsBetween(startDate: string, endDate: string): number {
  const start = new Date(startDate);
  const end = new Date(endDate);
  return (end.getTime() - start.getTime()) / (365.25 * 24 * 60 * 60 * 1000);
}
