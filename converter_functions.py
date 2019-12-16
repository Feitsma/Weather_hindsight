def meteric_to_Beaufort(wind_speed):
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

def wind_direction_to_text(wind_direction):
