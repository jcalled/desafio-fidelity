CREATE TABLE estado (
    cod_uf SERIAL PRIMARY KEY,
    uf VARCHAR(2) NOT NULL,
    cod_fornecedor INTEGER,
    nome TEXT
);


CREATE TABLE servico (
    cod_servico SERIAL PRIMARY KEY,
    civel BOOLEAN DEFAULT FALSE,
    criminal BOOLEAN DEFAULT FALSE
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


CREATE TABLE lote (
    cod_lote SERIAL PRIMARY KEY,
    cod_lote_prazo INTEGER,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cod_funcionario INTEGER,
    tipo INTEGER,
    prioridade INTEGER
);


CREATE TABLE lote_pesquisa (
    cod_lote_pesquisa SERIAL PRIMARY KEY,
    cod_lote INTEGER REFERENCES lote(cod_lote),
    cod_pesquisa INTEGER REFERENCES pesquisa(cod_pesquisa),
    cod_funcionario INTEGER,
    cod_funcionario_conclusao INTEGER,
    cod_fornecedor INTEGER,
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
    cod_funcionario INTEGER,
    filtro INTEGER,
    website_id INTEGER,
    resultado INTEGER
);



INSERT INTO estado (uf, cod_fornecedor, nome)
VALUES 
  ('SP', NULL, 'São Paulo'),
  ('RJ', NULL, 'Rio de Janeiro');


INSERT INTO servico (civel, criminal)
VALUES 
  (TRUE, FALSE),
  (FALSE, TRUE);


INSERT INTO pesquisa (
    cod_cliente, cod_uf, cod_servico, tipo,
    cpf, cod_uf_nascimento, cod_uf_rg,
    data_entrada, data_conclusao,
    nome, nome_corrigido,
    rg, rg_corrigido,
    nascimento, mae, mae_corrigido, anexo
)
VALUES 
  (1, 1, 1, 0, 
   '12345678901', 1, 1,
   CURRENT_TIMESTAMP, NULL,
   'João da Silva', NULL,
   'MG123456', NULL,
   '1985-05-20', 'Maria Silva', NULL, NULL);

INSERT INTO lote (cod_lote_prazo, data_criacao, cod_funcionario, tipo, prioridade)
VALUES 
  (NULL, CURRENT_TIMESTAMP, NULL, 1, 2);


INSERT INTO lote_pesquisa (
    cod_lote, cod_pesquisa,
    cod_funcionario, cod_funcionario_conclusao,
    cod_fornecedor, data_entrada, data_conclusao, cod_uf, obs
)
VALUES 
  (1, 1,
   NULL, NULL,
   NULL, CURRENT_TIMESTAMP, NULL, 1, 'Nenhuma observação');


-- INSERT INTO pesquisa_spv (
--     cod_pesquisa, cod_spv, cod_spv_computador,
--     cod_spv_tipo, cod_funcionario, filtro, website_id, resultado
-- )
-- VALUES 
--   (1, 1001, 2001, 1, NULL, 0, 1, 1);
