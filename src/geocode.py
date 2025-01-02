import pandas as pd
from geopy import Location
from geopy.geocoders import Nominatim

df = pd.read_csv("/data/dataset.csv")

geolocator = Nominatim(user_agent="santa_catarina_geocoder")


def get_lat_lon(city: str):
    try:
        location: Location = geolocator.geocode(f"{city}, Santa Catarina, Brazil")  # type: ignore
        if location:
            return pd.Series([location.latitude, location.longitude])
    except Exception as e:
        print(f"Error fetching {city}: {e}")
    return pd.Series([None, None])


# Apply the function to each city with a delay to avoid overloading the API
df[["Latitude", "Longitude"]] = df["City"].apply(lambda x: get_lat_lon(x) if pd.notnull(x) else pd.Series([None, None]))

df.to_csv("/data/dataset_with_lat_lon.csv", index=False)
