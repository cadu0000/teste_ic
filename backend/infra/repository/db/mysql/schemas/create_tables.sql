CREATE DATABASE IF NOT EXISTS intuitive_care;
USE intuitive_care;
SET innodb_lock_wait_timeout = 120;

CREATE TABLE IF NOT EXISTS operadora (
    cnpj CHAR(14) PRIMARY KEY,
    reg_ans CHAR(8) UNIQUE NOT NULL,  
    razao_social VARCHAR(256),
    nome_fantasia VARCHAR(256),
    modalidade VARCHAR(64),
    endereco_eletronico VARCHAR(256),
    regiao_comercializacao VARCHAR(8),
    data_registro_ans DATE
);

CREATE TABLE IF NOT EXISTS representante (
    id_representante INT AUTO_INCREMENT PRIMARY KEY,
    cnpj_operadora CHAR(14),
    representante VARCHAR(256),
    cargo_representante VARCHAR(256),
    FOREIGN KEY (cnpj_operadora) REFERENCES operadora(cnpj) ON DELETE CASCADE
)

CREATE TABLE IF NOT EXISTS contato (
    id_contato INT AUTO_INCREMENT PRIMARY KEY,
    cnpj_operadora CHAR(14),
    tipo VARCHAR(64),
    ddd VARCHAR(64),
    numero VARCHAR(32),
    FOREIGN KEY (cnpj_operadora) REFERENCES operadora(cnpj) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS localizacao (
    id_localizacao INT AUTO_INCREMENT PRIMARY KEY,
    logradouro VARCHAR(256) NOT NULL,
    numero VARCHAR(16),
    complemento VARCHAR(128),
    bairro VARCHAR(128),
    cidade VARCHAR(128) NOT NULL,
    uf CHAR(2) NOT NULL,
    cep CHAR(8) NOT NULL,
    cnpj_operadora CHAR(14),
    FOREIGN KEY (cnpj_operadora) REFERENCES operadora(cnpj) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    id_contabil INT AUTO_INCREMENT PRIMARY KEY,
    reg_ans CHAR(8),
    data_inicio_tri DATE,
    cd_conta_contabil VARCHAR(9) NOT NULL,
    descricao VARCHAR(150),
    vl_saldo_inicial DECIMAL(20, 2),
    vl_saldo_final DECIMAL(20, 2),
    FOREIGN KEY (reg_ans) REFERENCES operadora(reg_ans)
);

CREATE INDEX idx_reg_ans_data_inicio_tri ON demonstracoes_contabeis (reg_ans, data_inicio_tri);


