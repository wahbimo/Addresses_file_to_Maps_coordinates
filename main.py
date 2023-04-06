import pandas as pd
from geopy import GoogleV3

AUTH_KEY = "Your Google API Key"
# you can creat your key on https://console.cloud.google.com/

geolocator = GoogleV3(api_key=AUTH_KEY)

# You might have problems with reading the file, delete the heading and leave just the Address column.
df = pd.read_excel("your_file.xlsx","sheet_name",names = ["Address"])

# Getting the correct address by autocompleting and correcting the given address.
df["loc"] = df["Address"].apply(geolocator.geocode)

# Transformation of the address to coordinates
df["point"]= df["loc"].apply(lambda loc: tuple(loc.point) if loc else None)

# Creating 3 columns for longitude, latitude and altitude.

df[['lat', 'lon', 'altitude']] = pd.DataFrame(df['point'].to_list(), index=df.index)

# Exporting the resulting data frame: you have multiple possibilities (Excel,JSON,CSV...)

df.to_excel("coordinates.xlsx","SheetName")
