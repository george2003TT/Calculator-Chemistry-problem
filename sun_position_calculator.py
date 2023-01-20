import datetime
import math

def sun_position(date,lat,lon):

    #Convert latitude and logitde to radians
    lat = math.radians(lat)
    lon = math.radians(lon)

    #Convert date to Julian day
    julian_day = date.timetuple().tm_yday +(date.hour -12)/24 +date.minute/1440 +date.second/86400
    julian_century =(julian_day - 2451545)/36525

# Calculate solar mean anomaly
    solar_mean_anomaly = (357.52910 + 0.98560028 * julian_century) % 360
    solar_mean_anomaly = math.radians(solar_mean_anomaly)

    # Calculate ecliptic longitude
    ecliptic_longitude = (280.459 + 0.98564736 * julian_century) % 360
    ecliptic_longitude = math.radians(ecliptic_longitude)

    # Calculate declination
    sin_declination = math.sin(ecliptic_longitude) * math.sin(math.radians(23.439))
    declination = math.asin(sin_declination)

    # Calculate hour angle
    cos_hour_angle = (math.sin(-0.83) - math.sin(lat) * sin_declination) / (math.cos(lat) * math.cos(declination))
    hour_angle = math.acos(cos_hour_angle)
    hour_angle = math.degrees(hour_angle)

    # Calculate solar noon
    solar_noon = (720 - 4 * lon - hour_angle) / 1440
    solar_noon = 12 + solar_noon
    # Calculate solar elevation and azimuth
    sin_elevation = math.sin(lat) * math.sin(declination) + math.cos(lat) * math.cos(declination) * math.cos(math.radians(hour_angle))
    elevation = math.asin(sin_elevation)
    elevation = math.degrees(elevation)
    cos_azimuth = (math.sin(declination) * math.cos(lat) - math.cos(declination) * math.sin(lat) * math.cos(math.radians(hour_angle))) / math.cos(elevation)
    azimuth = math.acos(cos_azimuth)
    azimuth
    return elevation,azimuth 
date = datetime.datetime.now()
lat = 40.730610 
lon = -73.935242
elevation, azimuth = sun_position(date, lat, lon)
print("Elevation: ", elevation)
print("Azimuth: ", azimuth)
