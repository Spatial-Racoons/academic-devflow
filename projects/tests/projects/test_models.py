from django.test import TestCase
from projects.models import Projeto


class ProjetoModel(TestCase):
    DESCRICAO = 'Teste do modelo projeto'
    DT_INICIO = '2010-10-10'
    DT_TERMINO = '2011-11-11'
    NOME = 'Teste'
    SITUACAO = 'Em desenvolvimento'

    def test_objeto_criado_todos_campos(self):
        """O modelo cria corretamente o objeto quando todos os atributos são fornecidos"""

        p = Projeto.objects.create(descricao=self.DESCRICAO, data_inicio=self.DT_INICIO,
                                   data_termino=self.DT_TERMINO, nome=self.NOME, situacao=self.SITUACAO)
        self.assertTrue(isinstance(p, Projeto))
        self.assertEqual(p.nome, self.NOME)
