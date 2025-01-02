#!/usr/bin/python3
from models import storage
from models.state import State

# Fetch all states
states = storage.all(State).values()
for state in states:
    print(f"State: {state.name}")
    # Fetch all cities linked to the state
    for city in state.cities:
        print(f"  City: {city.name}")

# Close the storage session if necessary
storage.close()
