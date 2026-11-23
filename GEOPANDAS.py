
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
get_ipython().run_line_magic('matplotlib', '')
world = gpd.read_file("https://github.com/nickeubank/practicaldatascience_book/raw/refs/heads/main/notebooks/gis/example_data/world_countries/world_countries_mercator.geojson")
world.sample(5)
world.plot()
import rasterio
from rasterio.plot import show
ny = rasterio.open("https://github.com/nickeubank/practicaldatascience_book/raw/refs/heads/main/notebooks/gis/example_data//ny_raster/hdr.adf")
show(ny)
ny.read(1)
type(ny.read(1))
import geodatasets
world = gpd.read_file("https://github.com/nickeubank/practicaldatascience_book/raw/refs/heads/main/notebooks/gis/example_data/world_countries/world_countries_mercator.geojson")
world.sample(5)
world.plot()
world["country_centroids"] = world.centroid
world.sample(3)
world["country_centroids"] = world.centroid
world = world.set_geometry("country_centroids")
world.plot()
world.geometry
world["gdp_md"] = world["gdp_md"].astype("int64")

world["pop_est"] = world["pop_est"].astype("int64")

world["gdp_per_cap"] = (world["gdp_md"]*1_000_000)/world["pop_est"]
world=world[world["name"]!="Antarctica"].copy()
ax = world.plot("gdp_per_cap", cmap="Reds")
ax.set_title("World GDP Per Capita")
ax.set_axis_off()
ax
world = world.set_geometry("geometry")
ax = world.plot("gdp_per_cap", cmap="Reds")
ax.set_title("World GDP Per Capita")
ax.set_axis_off()
ax
