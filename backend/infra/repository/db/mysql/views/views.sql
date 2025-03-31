CREATE VIEW maiores_despesas_trimestre_w_filtro AS
    SELECT 
        o.nome_fantasia, 
        dc.reg_ans, 
        SUM(dc.vl_saldo_final) AS total_despesas
    FROM demonstracoes_contabeis dc
    JOIN operadora o ON dc.reg_ans = o.reg_ans
    WHERE dc.descricao = 'EVENTOS/SINISTROS_CONHECIDOS'
    OR dc.descricao LIKE '%ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    AND dc.data_inicio_tri >= (
       SELECT DATE_SUB(MAX(data_inicio_tri), INTERVAL 3 MONTH) 
       FROM demonstracoes_contabeis
   )
    GROUP BY o.nome_fantasia, dc.reg_ans
    ORDER BY total_despesas DESC;

SELECT * FROM maiores_despesas_trimestre_w_filtro LIMIT 10;


CREATE VIEW maiores_despesas_ultimo_ano AS
    SELECT 
        o.nome_fantasia, 
        dc.reg_ans, 
        SUM(dc.vl_saldo_final) AS total_despesas
    FROM demonstracoes_contabeis dc
    JOIN operadora o ON dc.reg_ans = o.reg_ans
    WHERE dc.data_inicio_tri >= (
       SELECT DATE_SUB(MAX(data_inicio_tri), INTERVAL 1 YEAR) 
       FROM demonstracoes_contabeis
   )
    GROUP BY o.nome_fantasia, dc.reg_ans
    ORDER BY total_despesas DESC;


SELECT * FROM maiores_despesas_ultimo_ano LIMIT 10;

