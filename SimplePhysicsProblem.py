def solveit(initial_velocity, final_velocity, time):
    if initial_velocity < final_velocity:
        acceleration = (final_velocity-initial_velocity)/time
        distance = initial_velocity*time + 0.5*acceleration*(time**2)
        acceleration = float(str(round(acceleration, 2)))
        distance = float(str(round(distance, 2)))
        return [acceleration,distance]
    else:
        return []
