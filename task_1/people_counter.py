import pandas as pd
import json


def people_count(file: str) -> json:
    country_and_people = pd.read_csv(file).values
    counted_people = {
        country[0]: {'people': [people[1] for people in country_and_people
                                if people[0] == country[0]
                                ],
                     'count': len(
                         [people[1] for people in country_and_people
                          if people[0] == country[0]
                          ]
                        )
                     }
        for country in country_and_people
    }
    return json.dumps(counted_people, indent=4)


print(people_count('data.csv'))