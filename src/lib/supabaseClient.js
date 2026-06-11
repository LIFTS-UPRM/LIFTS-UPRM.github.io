import { createClient } from '@supabase/supabase-js';

// The publishable key is safe to expose in client code; all access is
// enforced by Row Level Security policies in the database.
const SUPABASE_URL = 'https://twvcomijovmhlikgvefk.supabase.co';
const SUPABASE_PUBLISHABLE_KEY = 'sb_publishable_Osq_4R54V7777qvE92KxxA_2F55BmF1';

export const supabase = createClient(SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY);

export async function uploadImage(file, folder = 'uploads') {
  const safeName = file.name.replace(/[^a-zA-Z0-9._-]/g, '_');
  const path = `${folder}/${Date.now()}-${safeName}`;
  const { error } = await supabase.storage.from('media').upload(path, file);
  if (error) throw error;
  const { data } = supabase.storage.from('media').getPublicUrl(path);
  return data.publicUrl;
}
