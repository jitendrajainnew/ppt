import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { router } from 'expo-router';
import { Colors } from '@/constants/colors';
import { formatIndianCurrency } from '@/utils/formatting';
import { ReturnsBadge } from '@/components/common/ReturnsBadge';
import type { PortfolioWithScheme } from '@/types/portfolio';

interface HoldingRowProps {
  holding: PortfolioWithScheme;
}

export function HoldingRow({ holding }: HoldingRowProps) {
  const handlePress = () => {
    router.push(`/fund/${holding.scheme_code}`);
  };

  return (
    <TouchableOpacity style={styles.row} onPress={handlePress} activeOpacity={0.7}>
      <View style={styles.iconPlaceholder}>
        <Text style={styles.iconText}>
          {holding.scheme.fund_house.charAt(0).toUpperCase()}
        </Text>
      </View>

      <View style={styles.info}>
        <Text style={styles.name} numberOfLines={1}>
          {holding.scheme.name}
        </Text>
        <Text style={styles.category}>{holding.scheme.category}</Text>
      </View>

      <View style={styles.values}>
        <Text style={styles.amount}>{formatIndianCurrency(holding.current_value)}</Text>
        <ReturnsBadge value={holding.returns_pct} size="small" />
      </View>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  row: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 14,
    paddingHorizontal: 16,
    backgroundColor: Colors.light.background,
    borderBottomWidth: 1,
    borderBottomColor: Colors.light.border,
  },
  iconPlaceholder: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: Colors.light.surface,
    justifyContent: 'center',
    alignItems: 'center',
  },
  iconText: {
    fontSize: 16,
    fontWeight: '700',
    color: Colors.light.primary,
  },
  info: {
    flex: 1,
    marginLeft: 12,
    marginRight: 8,
  },
  name: {
    fontSize: 14,
    fontWeight: '600',
    color: Colors.light.text,
    marginBottom: 2,
  },
  category: {
    fontSize: 12,
    color: Colors.light.textSecondary,
  },
  values: {
    alignItems: 'flex-end',
    gap: 4,
  },
  amount: {
    fontSize: 14,
    fontWeight: '600',
    color: Colors.light.text,
    fontVariant: ['tabular-nums'],
  },
});
