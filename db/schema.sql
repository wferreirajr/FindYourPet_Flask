DROP TABLE IF EXISTS accounts;

CREATE TABLE "accounts" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "created" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        "NomeCompleto" TEXT NOT NULL,
        "Email" TEXT NOT NULL,
        "Tipo" TEXT NOT NULL,
        "Senha" TEXT NOT NULL,
        "TelCelular" TEXT,
        "TelFixo" TEXT,
        "Cep" TEXT,
        "Rua" TEXT,
        "Numero" TEXT,
        "Complemento" TEXT,
        "Bairro" TEXT,
        "Cidade" TEXT,
        "Estado" TEXT
);

CREATE TABLE "animals" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "created" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        "NomeCompleto" TEXT NOT NULL,
        "Foto" TEXT,
        "Especie" TEXT,
        "Sexo" TEXT,
        "Idade" TEXT,
        "Porte" TEXT,
        "Sobre" TEXT,
        "Cep" TEXT,
        "Rua" TEXT,
        "Numero" TEXT,
        "Complemento" TEXT,
        "Bairro" TEXT,
        "Cidade" TEXT,
        "Estado" TEXT
);
