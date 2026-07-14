import pandas as pd
from src.logger import logger


def transform_users(users):
    logger.info("Transforming user data. . .")

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

    logger.info("User data transformation completed.")

    return working_df