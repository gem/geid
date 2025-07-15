import build_rupture_plane
from shapely.geometry import Polygon
from geopandas import GeoSeries


#Define Rupture
mag = 6.50
hypocenter = {'lon': 45.86, 'lat': 34.74, 'depth': 14.8}
strike = 10
dip = 45
rake = 150
surface = build_rupture_plane.get_rupture_surface(mag, hypocenter, strike, dip, rake,'length')

def export_rupture(event,filename):
        
    top_left_lon = event['topLeft']['lon']
    top_left_lat = event['topLeft']['lat']
    top_right_lon = event['topRight']['lon']
    top_right_lat = event['topRight']['lat']
    bottom_left_lon = event['bottomLeft']['lon']
    bottom_left_lat = event['bottomLeft']['lat']
    bottom_right_lon = event['bottomRight']['lon']
    bottom_right_lat = event['bottomRight']['lat']
    geometry = Polygon([(top_left_lon, top_left_lat),
                    (bottom_left_lon, bottom_left_lat),  
                    (bottom_right_lon, bottom_right_lat),
                    (top_right_lon, top_right_lat)])

    rupture = GeoSeries([geometry])
    rupture.to_file(filename)


export_rupture(surface,'rupture_m6.5_length.shp')
