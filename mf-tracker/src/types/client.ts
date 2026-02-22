export interface Client {
  id: string;
  phone: string;
  name: string | null;
  pan_masked: string | null;
  can_number: string | null;
  created_at: string;
}

export type ClientInsert = Omit<Client, 'id' | 'created_at'>;
