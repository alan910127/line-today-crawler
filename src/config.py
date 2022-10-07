from dataclasses import dataclass, field


@dataclass
class ScraperSettings:
    base_url: str = "https://today.line.me/tw/v2/tab"
    tabs: list[str] = field(default_factory=list)


scaper_settings = ScraperSettings(
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
