states_needed = {'mt', 'wa', 'or', 'id',
                 'nv', 'ut', 'ca', 'az'}
stations = {}
stations['k_one'] = {'id', 'nv', 'ut'}
stations['k_two'] = {'wa', 'id', 'mt'}
stations['k_three'] = {'or', 'nv', 'ca'}
stations['k_four'] = {'nv', 'ut'}
stations['k_five'] = {'ca', 'az'}

final_stations = set()
while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
            final_stations.add(best_station)
            states_needed -= states_covered
print(final_stations)
