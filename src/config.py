from dataclasses import dataclass, field


@dataclass
class Settings:
    base_url: str = "https://today.line.me/webapi/portal/page/"
    tabs: list[str] = field(default_factory=list)

    listing_base_url: str = "https://today.line.me/api/v6/listings"


settings = Settings(
    tabs=[
        "top",
        "recommendation",
        "entertainment",
        # "TOPIC-Election",  # Time-specific
        # "subscription",  # Need to login
        "life",
        "video",
        "domestic",
        "global",
        "drama",
        "movie",
        "music",
        "CPBL",
        "sports",
        "finance",
        "health",
        "fun",
        "relationship",
        "horoscope",
        "parenting",
        "food",
        "travel",
        "fashion",
        "tech",
        "auto",
        "living",
        "ACG",
        "pet",
        "NBA",
        "shopping",
    ]
)
