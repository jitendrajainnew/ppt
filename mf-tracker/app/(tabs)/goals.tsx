import { FlatList, View, Text, RefreshControl, StyleSheet } from 'react-native';
import { useGoals } from '@/hooks/useGoals';
import { ListItemSkeleton } from '@/components/common/SkeletonLoader';
import { EmptyState } from '@/components/common/EmptyState';
import { ErrorState } from '@/components/common/ErrorState';
import { Colors } from '@/constants/colors';
import { formatCompactCurrency } from '@/utils/formatting';
import { daysUntil } from '@/utils/date';
import type { Goal } from '@/types/goals';

const GOAL_ICONS: Record<string, string> = {
  child_education: '🎓',
  retirement: '🏖️',
  house: '🏠',
  car: '🚗',
  emergency_fund: '🛡️',
  wealth_creation: '💰',
  custom: '🎯',
};

function GoalCard({ goal }: { goal: Goal }) {
  const progressPct =
    goal.target_amount > 0
      ? Math.min((goal.current_value / goal.target_amount) * 100, 100)
      : 0;
  const days = daysUntil(goal.target_date);
  const years = Math.max(0, Math.floor(days / 365));
  const months = Math.max(0, Math.floor((days % 365) / 30));

  return (
    <View style={styles.card}>
      <View style={styles.cardHeader}>
        <Text style={styles.goalIcon}>{GOAL_ICONS[goal.type] ?? '🎯'}</Text>
        <View style={styles.cardInfo}>
          <Text style={styles.goalName}>{goal.name}</Text>
          <Text style={styles.timeLeft}>
            {years > 0 ? `${years}y ${months}m left` : `${months}m left`}
          </Text>
        </View>
      </View>

      <View style={styles.progressBar}>
        <View style={[styles.progressFill, { width: `${progressPct}%` }]} />
      </View>

      <View style={styles.amounts}>
        <View>
          <Text style={styles.amountLabel}>Current</Text>
          <Text style={styles.amountValue}>
            {formatCompactCurrency(goal.current_value)}
          </Text>
        </View>
        <View style={styles.amountRight}>
          <Text style={styles.amountLabel}>Target</Text>
          <Text style={styles.amountValue}>
            {formatCompactCurrency(goal.target_amount)}
          </Text>
        </View>
      </View>
    </View>
  );
}

export default function GoalsScreen() {
  const { data: goals, isLoading, isError, refetch, isRefetching } = useGoals();

  if (isLoading) {
    return (
      <View style={styles.container}>
        {Array.from({ length: 3 }).map((_, i) => (
          <ListItemSkeleton key={i} />
        ))}
      </View>
    );
  }

  if (isError) {
    return <ErrorState onRetry={refetch} />;
  }

  if (!goals || goals.length === 0) {
    return (
      <EmptyState
        icon="flag-outline"
        title="No Goals Set"
        message="Create a financial goal to plan your investments — education, retirement, house, and more."
        actionLabel="Create Goal"
        onAction={() => {}}
      />
    );
  }

  return (
    <FlatList
      style={styles.container}
      contentContainerStyle={styles.list}
      data={goals}
      keyExtractor={(item) => item.id}
      renderItem={({ item }) => <GoalCard goal={item} />}
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
  list: {
    padding: 16,
  },
  card: {
    backgroundColor: Colors.light.card,
    borderRadius: 16,
    padding: 16,
    marginBottom: 12,
    borderWidth: 1,
    borderColor: Colors.light.border,
  },
  cardHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 14,
  },
  goalIcon: {
    fontSize: 28,
    marginRight: 12,
  },
  cardInfo: {
    flex: 1,
  },
  goalName: {
    fontSize: 16,
    fontWeight: '600',
    color: Colors.light.text,
  },
  timeLeft: {
    fontSize: 12,
    color: Colors.light.textSecondary,
    marginTop: 2,
  },
  progressBar: {
    height: 6,
    backgroundColor: Colors.light.surface,
    borderRadius: 3,
    marginBottom: 14,
    overflow: 'hidden',
  },
  progressFill: {
    height: '100%',
    backgroundColor: Colors.light.primary,
    borderRadius: 3,
  },
  amounts: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  amountLabel: {
    fontSize: 11,
    color: Colors.light.textTertiary,
    marginBottom: 2,
  },
  amountValue: {
    fontSize: 15,
    fontWeight: '700',
    color: Colors.light.text,
    fontVariant: ['tabular-nums'],
  },
  amountRight: {
    alignItems: 'flex-end',
  },
});
