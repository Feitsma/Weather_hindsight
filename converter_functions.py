"""
Conversion of wind speeds and directions to compare data of KNMI with WeerPlaza
"""

def meteric_to_Beaufort(wind_speed):
    """Conversion from metric system to Beaufort"""
    if 0 <= wind_speed <= 0.2:
        Beaufort = 0
    elif 0.3 <= wind_speed <= 1.5:
        Beaufort = 1
    elif 1.6 <= wind_speed <= 3.3:
        Beaufort = 2
    elif 3.4 <= wind_speed <= 5.4:
        Beaufort = 3
    elif 5.5 <= wind_speed <= 7.9:
        Beaufort = 4
    elif 8 <= wind_speed <= 10.7:
        Beaufort = 5
    elif 10.8 <= wind_speed <= 13.8:
        Beaufort = 6
    elif 13.9 <= wind_speed <= 17.1:
        Beaufort = 7
    elif 17.2 <= wind_speed <= 20.7:
        Beaufort = 8
    elif 20.8 <= wind_speed <= 24.4:
        Beaufort = 9
    elif 24.5 <= wind_speed <= 28.4:
        Beaufort = 10
    elif 28.5 <= wind_speed <= 32.6:
        Beaufort = 11
    elif 32.7 <= wind_speed:
        Beaufort = 12

    return Beaufort

def closest_wind_direction(lst, K):
    """Determines to which direction the given direction is closest"""
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

def wind_direction_to_text(wind_direction):
    """Converts wind direction in degrees to abbreviation in text, using lookup table and function closest_wind_direction"""
    common_direcions = [0, 360, 22.5, 45, 67.5, 90, 112.5, 135, 157.5, 180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5]
    text_directions = {0:"Calm/variable", 360:"N", 22.5:"NNO", 45:"NO", 67.5:"ONO", 90:"O", 112.5:"OZO", 135:"ZO", 157.5:"ZZO", 180:"Z", 202.5:"ZZW", 225:"ZW", 247.5:"WZW", 270:"W", 292.5:"WNW", 315:"NW", 337.5:"NNW"}
    closest_common_direction = closest_wind_direction(common_direcions, wind_direction)
    direction = text_directions[closest_common_direction]
    return direction