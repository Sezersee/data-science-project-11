import pandas as pd
import numpy as np

# 1. CSV dosyasından karakter verilerini okur.
# Örnek input: "cyberpunk_characters.csv"
# Örnek output: DataFrame (shape: [3, 6])
def load_character_data(filepath):
    return pd.read_csv(filepath)

# 2. En yüksek strength değerine sahip ilk n karakteri döndürür.
# Örnek input: df, n=2
# Örnek output: DataFrame -> ["V", "Johnny Silverhand"]
def get_top_strength_characters(df, n=5):
    get_top= df.sort_values(by= "strength",ascending=False)
    return get_top.head(n)

# 3. Tüm karakterlerin sayısal ortalama değerlerini (strength, intelligence, agility, health) hesaplar.
# Örnek input: df
# Örnek output: {'strength': 71.66, 'intelligence': 84.33, ...}
def calculate_average_stats(df):
    return df[['strength','intelligence', 'agility','health']].mean().to_dict()

# 4. Belirli bir fraksiyona (faction) ait karakterleri filtreler.
# Örnek input: df, "Moxes"
# Örnek output: DataFrame (1 satırlık) -> "Judy Alvarez"
def filter_characters_by_faction(df, faction_name):
    return df[df['faction']==faction_name]

# 5. Health değerlerini 0-1 aralığına normalize eder.
# Örnek input: df
# Örnek output: df['health']: [1.0, 0.95, 0.85]
def normalize_health_points(df):
    min_health = df['health'].min()
    max_health = df['health'].max()
    df['health'] = (df['health'] - min_health) / (max_health - min_health)
    return df

# 6. Sayısal sütunları NumPy matrisine dönüştürür.
# Örnek input: df
# Örnek output: NumPy array -> shape (3, 4)
def convert_to_numpy_matrix(df):
    numeric_df = df.select_dtypes(include=['number'])
    return numeric_df.to_numpy()

# 7. Intelligence değeri en yüksek karakteri döndürür.
# Örnek input: df
# Örnek output: Series -> "Johnny Silverhand"
def get_character_with_max_intelligence(df):
    return df.loc[df['intelligence'].idxmax()]

# 8. Agility değerine göre karakterleri küçükten büyüğe sıralar.
# Örnek input: df
# Örnek output: DataFrame (sorted by agility)
def sort_characters_by_agility(df):
    return df.sort_values(by='agility')

# 9. Sayısal istatistikleri (mean, std, min, max...) içeren yeni bir özet DataFrame oluşturur.
# Örnek input: df
# Örnek output: df.describe() benzeri bir tablo
def create_stat_summary_dataframe(df):
    return df.describe()


# 10. DataFrame’i belirtilen bir dosya yoluna CSV olarak kaydeder.
# Örnek input: df, "output.csv"
# Örnek output: output.csv dosyası oluşur (geri döndürmeye gerek yok)
def export_dataframe_to_csv(df, output_path):
    df.to_csv(output_path)