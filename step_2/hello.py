def format_position(lat, long):
    pattern = "Lat: {} - Long: {}"
    formatedPosition = pattern.format(lat, long)
    return formatedPosition

print(format_position(-52.33, 120.00))

