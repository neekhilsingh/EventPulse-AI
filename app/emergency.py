def get_emergency_resources(police_station: str):

    resources = {

        "Kengeri": {
            "police": "Kengeri Police Station",
            "hospital": "BGS Global Hospital",
            "fire_station": "Kengeri Fire Station"
        },

        "Whitefield": {
            "police": "Whitefield Police Station",
            "hospital": "Manipal Hospital Whitefield",
            "fire_station": "Whitefield Fire Station"
        },

        "Electronic City": {
            "police": "Electronic City Police Station",
            "hospital": "Narayana Health City",
            "fire_station": "Electronic City Fire Station"
        },

        "Unknown": {
            "police": "Nearest Available Police Station",
            "hospital": "Nearest Government Hospital",
            "fire_station": "Nearest Fire Station"
        }

    }

    return resources.get(police_station, resources["Unknown"])