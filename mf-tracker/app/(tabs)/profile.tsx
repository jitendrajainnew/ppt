import { View, Text, TouchableOpacity, StyleSheet, Alert } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { router } from 'expo-router';
import { useAuthStore } from '@/store/authStore';
import { Colors } from '@/constants/colors';

const MENU_ITEMS: {
  icon: React.ComponentProps<typeof Ionicons>['name'];
  label: string;
  onPress?: () => void;
}[] = [
  { icon: 'person-outline', label: 'Personal Details' },
  { icon: 'document-text-outline', label: 'Transaction History' },
  { icon: 'shield-checkmark-outline', label: 'KYC Status' },
  { icon: 'help-circle-outline', label: 'Help & Support' },
  { icon: 'information-circle-outline', label: 'About' },
];

export default function ProfileScreen() {
  const { user, signOut } = useAuthStore();

  const handleSignOut = () => {
    Alert.alert('Sign Out', 'Are you sure you want to sign out?', [
      { text: 'Cancel', style: 'cancel' },
      {
        text: 'Sign Out',
        style: 'destructive',
        onPress: async () => {
          await signOut();
          router.replace('/(auth)/login');
        },
      },
    ]);
  };

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <View style={styles.avatar}>
          <Ionicons name="person" size={32} color={Colors.light.primary} />
        </View>
        <Text style={styles.phone}>{user?.phone ?? 'Unknown'}</Text>
      </View>

      <View style={styles.menu}>
        {MENU_ITEMS.map((item) => (
          <TouchableOpacity
            key={item.label}
            style={styles.menuItem}
            onPress={item.onPress}
            activeOpacity={0.7}
          >
            <Ionicons name={item.icon} size={22} color={Colors.light.text} />
            <Text style={styles.menuLabel}>{item.label}</Text>
            <Ionicons name="chevron-forward" size={18} color={Colors.light.textTertiary} />
          </TouchableOpacity>
        ))}
      </View>

      <TouchableOpacity style={styles.signOut} onPress={handleSignOut} activeOpacity={0.7}>
        <Ionicons name="log-out-outline" size={22} color={Colors.light.negative} />
        <Text style={styles.signOutText}>Sign Out</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: Colors.light.background,
  },
  header: {
    alignItems: 'center',
    paddingVertical: 32,
    borderBottomWidth: 1,
    borderBottomColor: Colors.light.border,
  },
  avatar: {
    width: 72,
    height: 72,
    borderRadius: 36,
    backgroundColor: Colors.light.surface,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 12,
  },
  phone: {
    fontSize: 16,
    fontWeight: '600',
    color: Colors.light.text,
  },
  menu: {
    marginTop: 8,
  },
  menuItem: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 16,
    paddingHorizontal: 20,
    borderBottomWidth: 1,
    borderBottomColor: Colors.light.border,
  },
  menuLabel: {
    flex: 1,
    fontSize: 15,
    color: Colors.light.text,
    marginLeft: 14,
  },
  signOut: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 16,
    paddingHorizontal: 20,
    marginTop: 16,
  },
  signOutText: {
    fontSize: 15,
    color: Colors.light.negative,
    fontWeight: '600',
    marginLeft: 14,
  },
});
