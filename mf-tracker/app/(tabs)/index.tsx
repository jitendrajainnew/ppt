import { FlatList, RefreshControl, View, StyleSheet } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { usePortfolio } from '@/hooks/usePortfolio';
import { PortfolioValueCard } from '@/components/portfolio/PortfolioValueCard';
import { HoldingRow } from '@/components/portfolio/HoldingRow';
import { PortfolioCardSkeleton, ListItemSkeleton } from '@/components/common/SkeletonLoader';
import { EmptyState } from '@/components/common/EmptyState';
import { ErrorState } from '@/components/common/ErrorState';
import { Colors } from '@/constants/colors';

export default function PortfolioScreen() {
  const { data, isLoading, isError, refetch, isRefetching } = usePortfolio();

  if (isLoading) {
    return (
      <View style={styles.container}>
        <PortfolioCardSkeleton />
        {Array.from({ length: 5 }).map((_, i) => (
          <ListItemSkeleton key={i} />
        ))}
      </View>
    );
  }

  if (isError) {
    return <ErrorState onRetry={refetch} />;
  }

  if (!data || data.holdings.length === 0) {
    return (
      <EmptyState
        icon="pie-chart-outline"
        title="No Holdings Yet"
        message="Your mutual fund holdings will appear here once your portfolio data is synced."
      />
    );
  }

  return (
    <FlatList
      style={styles.container}
      data={data.holdings}
      keyExtractor={(item) => item.id}
      ListHeaderComponent={
        <PortfolioValueCard
          totalCurrent={data.totalCurrent}
          totalInvested={data.totalInvested}
          totalReturns={data.totalReturns}
          returnsPct={data.returnsPct}
        />
      }
      renderItem={({ item }) => <HoldingRow holding={item} />}
      refreshControl={
        <RefreshControl
          refreshing={isRefetching}
          onRefresh={refetch}
          tintColor={Colors.light.primary}
        />
      }
    />
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: Colors.light.background,
  },
});
