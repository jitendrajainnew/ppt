import { Tabs } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';
import { Colors } from '@/constants/colors';

type TabIcon = React.ComponentProps<typeof Ionicons>['name'];

const TAB_CONFIG: {
  name: string;
  title: string;
  icon: TabIcon;
  iconFocused: TabIcon;
}[] = [
  { name: 'index', title: 'Portfolio', icon: 'pie-chart-outline', iconFocused: 'pie-chart' },
  { name: 'sips', title: 'SIPs', icon: 'repeat-outline', iconFocused: 'repeat' },
  { name: 'goals', title: 'Goals', icon: 'flag-outline', iconFocused: 'flag' },
  { name: 'alerts', title: 'Alerts', icon: 'notifications-outline', iconFocused: 'notifications' },
  { name: 'profile', title: 'Profile', icon: 'person-outline', iconFocused: 'person' },
];

export default function TabLayout() {
  return (
    <Tabs
      screenOptions={{
        headerShown: true,
        tabBarActiveTintColor: Colors.light.primary,
        tabBarInactiveTintColor: Colors.light.textTertiary,
        tabBarStyle: {
          borderTopColor: Colors.light.border,
          backgroundColor: Colors.light.background,
          height: 60,
          paddingBottom: 8,
          paddingTop: 4,
        },
        tabBarLabelStyle: {
          fontSize: 11,
          fontWeight: '600',
        },
        headerStyle: {
          backgroundColor: Colors.light.background,
        },
        headerTitleStyle: {
          fontWeight: '700',
          fontSize: 18,
          color: Colors.light.text,
        },
      }}
    >
      {TAB_CONFIG.map((tab) => (
        <Tabs.Screen
          key={tab.name}
          name={tab.name}
          options={{
            title: tab.title,
            tabBarIcon: ({ focused, color, size }) => (
              <Ionicons
                name={focused ? tab.iconFocused : tab.icon}
                size={size}
                color={color}
              />
            ),
          }}
        />
      ))}
    </Tabs>
  );
}
