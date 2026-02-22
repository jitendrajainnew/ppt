import { FlatList, View, Text, RefreshControl, StyleSheet } from 'react-native';
import { useSIPs } from '@/hooks/useSIPs';
import { ListItemSkeleton } from '@/components/common/SkeletonLoader';
import { EmptyState } from '@/components/common/EmptyState';
import { ErrorState } from '@/components/common/ErrorState';
import { Colors } from '@/constants/colors';
import { formatIndianCurrency } from '@/utils/formatting';
import { formatDate } from '@/utils/date';
import type { SIP } from '@/types/sip';

const STATUS_COLORS: Record<string, { bg: string; text: string }> = {
  active: { bg: '#DCFCE7', text: Colors.light.positive },
  paused: { bg: '#FEF3C7', text: Colors.light.warning },
  completed: { bg: '#E0E7FF', text: Colors.light.accent },
  cancelled: { bg: '#FEE2E2', text: Colors.light.negative },
};

function SIPCard({ sip }: { sip: SIP }) {
  const status = STATUS_COLORS[sip.status] ?? STATUS_COLORS.active;

  return (
    <View style={styles.card}>
      <View style={styles.cardHeader}>
        <View style={styles.cardInfo}>
          <Text style={styles.schemeName} numberOfLines={1}>
            {sip.scheme_name ?? sip.scheme_code}
          </Text>
          <Text style={styles.fundHouse}>{sip.fund_house ?? 'Unknown AMC'}</Text>
        </View>
        <View style={[styles.statusBadge, { backgroundColor: status.bg }]}>
          <Text style={[styles.statusText, { color: status.text }]}>
            {sip.status.charAt(0).toUpperCase() + sip.status.slice(1)}
          </Text>
        </View>
      </View>

      <View style={styles.cardDetails}>
        <View>
          <Text style={styles.detailLabel}>Amount</Text>
          <Text style={styles.detailValue}>{formatIndianCurrency(sip.amount)}</Text>
        </View>
        <View>
          <Text style={styles.detailLabel}>SIP Date</Text>
          <Text style={styles.detailValue}>{sip.sip_date}th of every month</Text>
        </View>
        <View>
          <Text style={styles.detailLabel}>Next Due</Text>
          <Text style={styles.detailValue}>
            {sip.next_date ? formatDate(sip.next_date) : '—'}
          </Text>
        </View>
      </View>
    </View>
  );
}

export default function SIPsScreen() {
  const { data: sips, isLoading, isError, refetch, isRefetching } = useSIPs();

  if (isLoading) {
    return (
      <View style={styles.container}>
        {Array.from({ length: 4 }).map((_, i) => (
          <ListItemSkeleton key={i} />
        ))}
      </View>
    );
  }

  if (isError) {
    return <ErrorState onRetry={refetch} />;
  }

  if (!sips || sips.length === 0) {
    return (
      <EmptyState
        icon="repeat-outline"
        title="No SIPs Found"
        message="Your active SIPs will appear here. Start a SIP to invest regularly in mutual funds."
      />
    );
  }

  return (
    <FlatList
      style={styles.container}
      contentContainerStyle={styles.list}
      data={sips}
      keyExtractor={(item) => item.id}
      renderItem={({ item }) => <SIPCard sip={item} />}
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
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: 14,
  },
  cardInfo: {
    flex: 1,
    marginRight: 8,
  },
  schemeName: {
    fontSize: 15,
    fontWeight: '600',
    color: Colors.light.text,
    marginBottom: 2,
  },
  fundHouse: {
    fontSize: 12,
    color: Colors.light.textSecondary,
  },
  statusBadge: {
    borderRadius: 6,
    paddingHorizontal: 8,
    paddingVertical: 3,
  },
  statusText: {
    fontSize: 11,
    fontWeight: '700',
  },
  cardDetails: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  detailLabel: {
    fontSize: 11,
    color: Colors.light.textTertiary,
    marginBottom: 2,
  },
  detailValue: {
    fontSize: 13,
    fontWeight: '600',
    color: Colors.light.text,
  },
});
