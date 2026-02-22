import { View, Text, ScrollView, StyleSheet } from 'react-native';
import { useLocalSearchParams } from 'expo-router';
import { Colors } from '@/constants/colors';

export default function FundDetailScreen() {
  const { schemeCode } = useLocalSearchParams<{ schemeCode: string }>();

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <View style={styles.section}>
        <Text style={styles.label}>Scheme Code</Text>
        <Text style={styles.value}>{schemeCode}</Text>
      </View>

      <View style={styles.placeholder}>
        <Text style={styles.placeholderText}>
          Fund details, NAV chart, and transaction history will be displayed here.
        </Text>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: Colors.light.background,
  },
  content: {
    padding: 16,
  },
  section: {
    marginBottom: 24,
  },
  label: {
    fontSize: 12,
    color: Colors.light.textSecondary,
    marginBottom: 4,
  },
  value: {
    fontSize: 18,
    fontWeight: '700',
    color: Colors.light.text,
  },
  placeholder: {
    backgroundColor: Colors.light.surface,
    borderRadius: 16,
    padding: 32,
    alignItems: 'center',
  },
  placeholderText: {
    fontSize: 14,
    color: Colors.light.textSecondary,
    textAlign: 'center',
    lineHeight: 22,
  },
});
