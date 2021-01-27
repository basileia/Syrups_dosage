from secrets import Connect


connection = Connect.get_connection()
db = connection.sirups_information

sirups = db.sirups
db.sirups.delete_many({})

entries = []

amoksiklav = {
    "Name": "AMOKSIKLAV 457 MG/5 ML",
    "Age": {"0 - 2": "Nelze určit doporučené dávkování.",  # months
            "2 - 24": {"Max": 45},
            "24 - 216": {"Min": 25, "Max": 70}},
    "Units": "na den",
    "Weight": {"40": "Zvolte lékovou formu určenou pro dospělé."},
    "Max dosage": 2800,
    "Strength": 80,
    "Strength units": "mg/ml",
    "Group": "Counting"
}
entries.append(amoksiklav)

erdomed = {
    "Name": "ERDOMED 35MG/ML POR PLV SUS",
    "Weight": {"0 - 15": "Tento přípravek není vhodný",  # kg
               "15 - 20": "2,5 ml 2krát denně",
               "21 - 30": "5 ml 2krát denně",
               "30 - 300": "5 ml 3krát denně"},
    "Group": "No Counting"
}
entries.append(erdomed)

zinnat = {
    "Name": "ZINNAT 125MG POR GRA SUS 50ML",
    "Age": {"0 - 3": "Tento přípravek není vhodný",
            "3 - 216": {"Min": 10, "Max": 15}},
    "Weight": {"40": {"Min": 250, "Max": 500}},
    "Max dosage": 500,
    "Units": "na dávku",
    "Strength": 25,
    "Strength units": "mg/ml",
    "Group": "Counting"
}
entries.append(zinnat)

sirups.insert_many(entries)
