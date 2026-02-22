import { create } from 'zustand';
import type { Session, User } from '@supabase/supabase-js';
import { supabase } from '@/services/supabase';

interface AuthState {
  session: Session | null;
  user: User | null;
  isLoading: boolean;
  isAuthenticated: boolean;
  setSession: (session: Session | null) => void;
  sendOTP: (phone: string) => Promise<{ error: string | null }>;
  verifyOTP: (phone: string, token: string) => Promise<{ error: string | null }>;
  signOut: () => Promise<void>;
  initialize: () => Promise<void>;
}

export const useAuthStore = create<AuthState>((set) => ({
  session: null,
  user: null,
  isLoading: true,
  isAuthenticated: false,

  setSession: (session) =>
    set({
      session,
      user: session?.user ?? null,
      isAuthenticated: !!session,
      isLoading: false,
    }),

  sendOTP: async (phone: string) => {
    try {
      const { error } = await supabase.auth.signInWithOtp({ phone });
      return { error: error?.message ?? null };
    } catch {
      return { error: 'Failed to send OTP. Please try again.' };
    }
  },

  verifyOTP: async (phone: string, token: string) => {
    try {
      const { data, error } = await supabase.auth.verifyOtp({
        phone,
        token,
        type: 'sms',
      });
      if (error) return { error: error.message };
      set({
        session: data.session,
        user: data.session?.user ?? null,
        isAuthenticated: !!data.session,
      });
      return { error: null };
    } catch {
      return { error: 'Invalid OTP. Please try again.' };
    }
  },

  signOut: async () => {
    await supabase.auth.signOut();
    set({ session: null, user: null, isAuthenticated: false });
  },

  initialize: async () => {
    try {
      const { data } = await supabase.auth.getSession();
      set({
        session: data.session,
        user: data.session?.user ?? null,
        isAuthenticated: !!data.session,
        isLoading: false,
      });

      supabase.auth.onAuthStateChange((_event, session) => {
        set({
          session,
          user: session?.user ?? null,
          isAuthenticated: !!session,
        });
      });
    } catch {
      set({ isLoading: false });
    }
  },
}));
