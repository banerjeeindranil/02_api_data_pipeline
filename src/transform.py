import pandas as pd


def transform_users(users):
    raw_df = pd.DataFrame(users)
    working_df = raw_df.copy()


    working_df["city"] = working_df["address"].apply(
        lambda address: address["city"]
    )
    working_df["company_name"] = working_df["company"].apply(
        lambda company: company["name"]
    )

    working_df = working_df[
        ["id",
        "name",
        "username",
        "email",
        "city", 
        "company_name"
        ]
    ]

    return working_df