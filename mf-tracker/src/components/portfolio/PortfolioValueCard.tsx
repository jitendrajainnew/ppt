import { View, Text, StyleSheet } from 'react-native';
import { Colors } from '@/constants/colors';
import { formatIndianCurrency, formatCompactCurrency } from '@/utils/formatting';
import { ReturnsBadge } from '@/components/common/ReturnsBadge';

interface PortfolioValueCardProps {
  totalCurrent: number;
  totalInvested: number;
  totalReturns: number;
  returnsPct: number;
}

export function PortfolioValueCard({
  totalCurrent,
  totalInvested,
  totalReturns,
  returnsPct,
}: PortfolioValueCardProps) {
  const isPositive = totalReturns >= 0;

  return (
    <View style={styles.card}>
      <Text style={styles.label}>Current Value</Text>
      <Text style={styles.value}>{formatIndianCurrency(totalCurrent)}</Text>

      <View style={styles.row}>
        <View>
          <Text style={styles.subLabel}>Invested</Text>
          <Text style={styles.subValue}>{formatCompactCurrency(totalInvested)}</Text>
        </View>
        <View style={styles.returnsCol}>
          <Text style={styles.subLabel}>Returns</Text>
          <View style={styles.returnsRow}>
            <Text
              style={[
                styles.returnsValue,
                { color: isPositive ? Colors.light.positive : Colors.light.negative },
              ]}
            >
              {formatCompactCurrency(totalReturns)}
            </Text>
            <ReturnsBadge value={returnsPct} size="small" />
          </View>
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: Colors.light.primary,
    borderRadius: 20,
    padding: 24,
    marginHorizontal: 16,
    marginTop: 8,
    marginBottom: 16,
  },
  label: {
    fontSize: 14,
    color: 'rgba(255,255,255,0.7)',
    marginBottom: 4,
  },
  value: {
    fontSize: 32,
    fontWeight: '700',
    color: '#FFFFFF',
    fontVariant: ['tabular-nums'],
    marginBottom: 20,
  },
  row: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  subLabel: {
    fontSize: 12,
    color: 'rgba(255,255,255,0.6)',
    marginBottom: 2,
  },
  subValue: {
    fontSize: 16,
    fontWeight: '600',
    color: '#FFFFFF',
    fontVariant: ['tabular-nums'],
  },
  returnsCol: {
    alignItems: 'flex-end',
  },
  returnsRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  returnsValue: {
    fontSize: 16,
    fontWeight: '600',
    fontVariant: ['tabular-nums'],
  },
});
