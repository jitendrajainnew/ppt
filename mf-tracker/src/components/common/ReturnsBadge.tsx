import { View, Text, StyleSheet } from 'react-native';
import { Colors } from '@/constants/colors';
import { formatPercent } from '@/utils/formatting';

interface ReturnsBadgeProps {
  value: number;
  size?: 'small' | 'medium';
}

export function ReturnsBadge({ value, size = 'medium' }: ReturnsBadgeProps) {
  const isPositive = value >= 0;
  const bgColor = isPositive ? '#DCFCE7' : '#FEE2E2';
  const textColor = isPositive ? Colors.light.positive : Colors.light.negative;

  return (
    <View style={[styles.badge, { backgroundColor: bgColor }, size === 'small' && styles.small]}>
      <Text style={[styles.text, { color: textColor }, size === 'small' && styles.smallText]}>
        {formatPercent(value)}
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  badge: {
    borderRadius: 8,
    paddingHorizontal: 10,
    paddingVertical: 4,
  },
  small: {
    paddingHorizontal: 6,
    paddingVertical: 2,
    borderRadius: 6,
  },
  text: {
    fontSize: 14,
    fontWeight: '700',
    fontVariant: ['tabular-nums'],
  },
  smallText: {
    fontSize: 12,
  },
});
