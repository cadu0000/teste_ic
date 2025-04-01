from infra.repository.data_process import DataProcessor
from infra.repository.database_manager import DatabaseManager
from infra.repository.raw_data_loader import RawDataLoader
from infra.repository.mysql.contato_repository import ContatoRepository
from infra.repository.mysql.demonstracoes_contabeis_repository import DemonstracoesContabeisRepository
from infra.repository.mysql.localizacao_repository import LocalizacaoRepository
from infra.repository.mysql.operadora_repository import OperadoraRepository
from infra.repository.mysql.representante_repository import RepresentanteRepository

class RawDataIngestion:
    def __init__(self):
        self.data_loader = RawDataLoader()
        self.processor = DataProcessor(self.data_loader.operadora_data, self.data_loader.contabeis_data)
        self.db = DatabaseManager()

    def ingest_operadora(self):
        try:
            operadora_inserter = OperadoraRepository(self.db, self.processor.process_operadora().values.tolist())
            operadora_inserter.insert()
        except Exception as e:
            raise Exception (f"Erro ao inserir operadora: {str(e)}")

    def ingest_representante(self):
        try:
            representante_inserter = RepresentanteRepository(self.db, self.processor.process_representante().values.tolist())
            representante_inserter.insert()
        except Exception as e:
            raise Exception (f"Erro ao inserir representante: {str(e)}")

    def ingest_contato(self):
        try:
            contato_inserter = ContatoRepository(self.db, self.processor.process_contato()[['CNPJ', 'tipo', 'DDD', 'Numero']].values.tolist())
            contato_inserter.insert()
        except Exception as e:
            raise Exception (f"Erro ao inserir contato: {str(e)}")

    def ingest_localizacao(self):
        try:
            localizacao_inserter = LocalizacaoRepository(self.db, self.processor.process_localizacao().values.tolist())
            localizacao_inserter.insert()
        except Exception as e:
            raise Exception (f"Erro ao inserir localizacao: {str(e)}")

    def ingest_demonstracoes_contabeis(self):
        try:
            valid_reg_ans = self.processor.process_operadora()['Registro_ANS'].tolist()
            demonstracoes_contabeis_inserter = DemonstracoesContabeisRepository(self.db, self.processor.process_contabeis(valid_reg_ans).values.tolist())
            demonstracoes_contabeis_inserter.insert()
            
        except Exception as e:
            raise Exception (f"Erro ao inserir demonstrações contábeis: {str(e)}")

    def run(self):
        try:
            self.ingest_operadora()
            self.ingest_representante()
            self.ingest_contato()
            self.ingest_localizacao()
            self.ingest_demonstracoes_contabeis()
        except Exception as e:
            raise Exception (f"\nErro geral na ingestão de dados: {str(e)}")
        finally:
            self.db.close()

