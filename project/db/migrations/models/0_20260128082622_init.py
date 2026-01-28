from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "book" (
    "id" VARCHAR(21) NOT NULL PRIMARY KEY,
    "title" VARCHAR(255) NOT NULL,
    "author" VARCHAR(255) NOT NULL,
    "published_at" TIMESTAMP,
    "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztlm1v2jAQx79KlFdM6lDJoK2maVJgTGVaYWrZg1pVkYlNsEjsNHHaoorvPp9JYhIeBi"
    "0arcS75H939t3vLso9mQHHxI+rTc7H5kfjyWQoIPKhoB8ZJgpDrYIg0MBXjoPMYxCLCLlC"
    "akPkx0RKmMRuRENBOZMqS3wfRO5KR8o8LSWM3iXEEdwjYkQiabi5lTJlmDySOHsNx86QEh"
    "8X0qQY7la6Iyah0lojFH1VnnDdwHG5nwRMe4cTMeIsd5fZgOoRRiIkCJ4rAPJL68ykWa5S"
    "EFFC8iSxFjAZosQHDOanYcJcqN5giHGKq9kd+cNncwtMLmeAmDIRKwYBenR8wjwxkq9WbT"
    "qrVrOYeUEiv+zL1rl9WbFq7+BCLvs0a143tVjKNFVHIIFmhyjyGrWgQgZtQTsP2A3wTNDE"
    "9ZxlyDN4OyHaaGyCtNFYzRRsAFVDRIlEEW1DUUccMOYYw2Tg03hEsIPEIswvEoegAVkOtB"
    "xbworT4Gr2sAHk9NP/j4zXIO13LtpXffviByQexPGdr5jY/TZYLKVOSmrlpEQ/P8T43emf"
    "G/BqXPe6bQWMx8KL1I3ar39tQk5yWrnD+IOD8HzZmZxJhWa6EQG0z2hlMXIHjdzH1yJrwD"
    "3mT9I5eiOdTUd+bWOTED+zscXIQ2P32liVPGxgw/HcYgDCALnjBxRhZ8HCLb7Kd9EUWEFZ"
    "QQx5qivAFrJM91GbRNQdLdtUU8vaXRVpn1ezrXaY2GJZlcNVnva0YS/bVV846h7c8t6q1U"
    "/rZx9O6mfSRWWSK6drpr/T7f9j9bwnUQwpbbE2zYUc9ia9fspPY5vdc+b+NgHWjo83ACi9"
    "VgJUtiJAeaMgbMn/7NtVr7tiSdEhJZA/mSzwBlNXHBlyJRW3rxPrGopQdeGflcGrXNh/yl"
    "xb33vN8s8IDmhKxnv9vUz/AqoDb/I="
)
