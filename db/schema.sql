DROP TABLE IF EXISTS account;

CREATE TABLE "account" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "created" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        "fullname" TEXT NOT NULL,
        "user" TEXT NOT NULL,
        "passwd" TEXT NOT NULL,
        "type" TEXT NOT NULL
);
