def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    # add/overwrite a new key-value pair
    #spacecraft["distance"] = 0.01
    #spacecraft["name"] = "Voyager 1"
    
    # add/overwrite one or more key-value pairs
    # RECEIVES A DICTIONARY AS PARAMETER
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ======== REPORT ========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ========================
    """


main()