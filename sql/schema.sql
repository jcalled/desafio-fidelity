-- Nao havia no DER
CREATE TABLE funcionario (
    cod_funcionario SERIAL PRIMARY KEY,
    nome TEXT
);
-- Nao havia no DER
CREATE TABLE fornecedor (
    cod_fornecedor SERIAL PRIMARY KEY,
    nome TEXT
);



CREATE TABLE estado (
    cod_uf SERIAL PRIMARY KEY,
    uf VARCHAR(2) NOT NULL,
    cod_fornecedor INTEGER REFERENCES fornecedor(cod_fornecedor),
    nome TEXT
);

CREATE TABLE servico (
    cod_servico SERIAL PRIMARY KEY,
    civel BOOLEAN DEFAULT FALSE,
    criminal BOOLEAN DEFAULT FALSE
);

CREATE TABLE lote (
    cod_lote SERIAL PRIMARY KEY,
    cod_lote_prazo INTEGER,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cod_funcionario INTEGER REFERENCES funcionario(cod_funcionario),
    tipo INTEGER,
    prioridade INTEGER
);

CREATE TABLE pesquisa (
    cod_pesquisa SERIAL PRIMARY KEY,
    cod_cliente INTEGER,
    cod_uf INTEGER REFERENCES estado(cod_uf),
    cod_servico INTEGER REFERENCES servico(cod_servico),
    tipo INTEGER,
    cpf VARCHAR(20),
    cod_uf_nascimento INTEGER,
    cod_uf_rg INTEGER,
    data_entrada TIMESTAMP,
    data_conclusao TIMESTAMP,
    nome TEXT,
    nome_corrigido TEXT,
    rg VARCHAR(20),
    rg_corrigido VARCHAR(20),
    nascimento DATE,
    mae TEXT,
    mae_corrigido TEXT,
    anexo TEXT
);

CREATE TABLE lote_pesquisa (
    cod_lote_pesquisa SERIAL PRIMARY KEY,
    cod_lote INTEGER REFERENCES lote(cod_lote),
    cod_pesquisa INTEGER REFERENCES pesquisa(cod_pesquisa),
    cod_funcionario INTEGER REFERENCES funcionario(cod_funcionario),
    cod_funcionario_conclusao INTEGER REFERENCES funcionario(cod_funcionario),
    cod_fornecedor INTEGER REFERENCES fornecedor(cod_fornecedor),
    data_entrada TIMESTAMP,
    data_conclusao TIMESTAMP,
    cod_uf INTEGER REFERENCES estado(cod_uf),
    obs TEXT
);

CREATE TABLE pesquisa_spv (
    cod_pesquisa INTEGER PRIMARY KEY REFERENCES pesquisa(cod_pesquisa),
    cod_spv INTEGER,
    cod_spv_computador INTEGER,
    cod_spv_tipo INTEGER,
    cod_funcionario INTEGER REFERENCES funcionario(cod_funcionario),
    filtro INTEGER,
    website_id INTEGER,
    resultado INTEGER
);
