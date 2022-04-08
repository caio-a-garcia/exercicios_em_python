CREATE TABLE "Proprietarios"(
    "id" INTEGER NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "data_de_nascimento" DATE NOT NULL
);
ALTER TABLE
    "Proprietarios" ADD PRIMARY KEY("id");
CREATE TABLE "Imoveis"(
    "id" INTEGER NOT NULL,
    "logradouro" VARCHAR(255) NOT NULL,
    "cep" INTEGER NOT NULL,
    "bairro" VARCHAR(255) NOT NULL,
    "cidade" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Imoveis" ADD PRIMARY KEY("id");
CREATE TABLE "Alugueis"(
    "id" INTEGER NOT NULL,
    "imovel" INTEGER NOT NULL,
    "proprietario" INTEGER NOT NULL
);
ALTER TABLE
    "Alugueis" ADD PRIMARY KEY("id");
CREATE TABLE "Inquilinos"(
    "id" INTEGER NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "data_de_nascimento" DATE NOT NULL
);
ALTER TABLE
    "Inquilinos" ADD PRIMARY KEY("id");
CREATE TABLE "Inquilino do aluguel"(
    "id" INTEGER NOT NULL,
    "id_inquilino" INTEGER NOT NULL,
    "id_aluguel" INTEGER NOT NULL
);
ALTER TABLE
    "Inquilino do aluguel" ADD PRIMARY KEY("id");
ALTER TABLE
    "Inquilino do aluguel" ADD CONSTRAINT "inquilino do aluguel_id_aluguel_foreign" FOREIGN KEY("id_aluguel") REFERENCES "Alugueis"("id");
ALTER TABLE
    "Alugueis" ADD CONSTRAINT "alugueis_imovel_foreign" FOREIGN KEY("imovel") REFERENCES "Imoveis"("id");
ALTER TABLE
    "Alugueis" ADD CONSTRAINT "alugueis_proprietario_foreign" FOREIGN KEY("proprietario") REFERENCES "Proprietarios"("id");
ALTER TABLE
    "Inquilino do aluguel" ADD CONSTRAINT "inquilino do aluguel_id_inquilino_foreign" FOREIGN KEY("id_inquilino") REFERENCES "Inquilinos"("id");