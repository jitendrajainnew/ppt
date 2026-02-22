import { useEffect, useRef } from 'react';
import { View, Animated, StyleSheet, ViewStyle } from 'react-native';
import { Colors } from '@/constants/colors';

interface SkeletonProps {
  width: number | string;
  height: number;
  borderRadius?: number;
  style?: ViewStyle;
}

export function SkeletonLoader({ width, height, borderRadius = 8, style }: SkeletonProps) {
  const opacity = useRef(new Animated.Value(0.3)).current;

  useEffect(() => {
    const animation = Animated.loop(
      Animated.sequence([
        Animated.timing(opacity, {
          toValue: 1,
          duration: 800,
          useNativeDriver: true,
        }),
        Animated.timing(opacity, {
          toValue: 0.3,
          duration: 800,
          useNativeDriver: true,
        }),
      ])
    );
    animation.start();
    return () => animation.stop();
  }, [opacity]);

  return (
    <Animated.View
      style={[
        {
          width: width as number,
          height,
          borderRadius,
          backgroundColor: Colors.light.skeleton,
          opacity,
        },
        style,
      ]}
    />
  );
}

/** Pre-built skeleton for a portfolio card */
export function PortfolioCardSkeleton() {
  return (
    <View style={skeletonStyles.card}>
      <SkeletonLoader width="40%" height={14} />
      <SkeletonLoader width="60%" height={32} style={{ marginTop: 8 }} />
      <View style={skeletonStyles.row}>
        <SkeletonLoader width="30%" height={14} />
        <SkeletonLoader width="25%" height={14} />
      </View>
    </View>
  );
}

/** Pre-built skeleton for a list item row */
export function ListItemSkeleton() {
  return (
    <View style={skeletonStyles.listItem}>
      <SkeletonLoader width={40} height={40} borderRadius={20} />
      <View style={skeletonStyles.listItemContent}>
        <SkeletonLoader width="70%" height={14} />
        <SkeletonLoader width="40%" height={12} style={{ marginTop: 6 }} />
      </View>
      <SkeletonLoader width={60} height={14} />
    </View>
  );
}

const skeletonStyles = StyleSheet.create({
  card: {
    backgroundColor: Colors.light.card,
    borderRadius: 16,
    padding: 20,
    marginBottom: 12,
  },
  row: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 12,
  },
  listItem: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 12,
    paddingHorizontal: 16,
  },
  listItemContent: {
    flex: 1,
    marginLeft: 12,
  },
});
