import requests
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.patches import Rectangle

# 1. API'den veri çek
url = "https://api.orhanaydogdu.com.tr/deprem/kandilli/live"
response = requests.get(url)
data = response.json()
deprem_list = data["result"]
df = pd.DataFrame(deprem_list)

# 2. Latitude ve Longitude çıkar
df["latitude"] = df["geojson"].apply(lambda x: x["coordinates"][1])
df["longitude"] = df["geojson"].apply(lambda x: x["coordinates"][0])

# 3. Sadece Marmara açıklarındaki depremleri seç
df = df[
    (df["longitude"] >= 28.0) & (df["longitude"] <= 29.2) &
    (df["latitude"] >= 40.7) & (df["latitude"] <= 41.2)
]

# 4. Harita çiz
plt.figure(figsize=(10, 8))
ax = plt.axes(projection=ccrs.PlateCarree())

# Siyah zemin
ax.set_facecolor('black')

# Sınırları ayarla
ax.set_extent([28.0, 29.2, 40.7, 41.2])

# Karalar gri
ax.add_feature(cfeature.LAND.with_scale('10m'), facecolor="#1a1a1a")
# Denizler siyah
ax.add_feature(cfeature.OCEAN.with_scale('10m'), facecolor="black")

# Yollar ve şehir sınırları
ax.add_feature(cfeature.COASTLINE, edgecolor='gray')
ax.add_feature(cfeature.BORDERS, linestyle=':', edgecolor='gray')

# 5. Depremleri çiz
scatter = ax.scatter(
    df["longitude"],
    df["latitude"],
    c=df["mag"].astype(float),
    cmap="autumn_r",
    s=df["mag"].astype(float)**3 * 5,
    alpha=0.8,
    edgecolor="black",
    linewidth=0.5
)

# 6. Mavi kutu
left = 28.4
bottom = 40.7
width = 0.6
height = 0.4

rect = Rectangle(
    (left, bottom),
    width,
    height,
    linewidth=3,
    edgecolor='dodgerblue',
    facecolor='none'
)
ax.add_patch(rect)

# 7. Başlık ve colorbar
plt.colorbar(scatter, label="Magnitüd", shrink=0.5)
plt.title("Marmara Denizi Deprem Aktivitesi (Kandilli API Verisi)", color='white')
plt.show()
