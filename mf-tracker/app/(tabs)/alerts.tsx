import { View, Text, StyleSheet } from 'react-native';
import { EmptyState } from '@/components/common/EmptyState';
import { Colors } from '@/constants/colors';

export default function AlertsScreen() {
  // TODO: Wire up alerts query once backend is ready
  return (
    <View style={styles.container}>
      <EmptyState
        icon="notifications-outline"
        title="No Alerts"
        message="Set up NAV alerts and SIP reminders to stay on top of your investments."
        actionLabel="Create Alert"
        onAction={() => {}}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: Colors.light.background,
  },
});
