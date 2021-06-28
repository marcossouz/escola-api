from django.test import TestCase
from ..models import Aluno

class ModelTestCase(TestCase):
    """This class defines the test suite for the aluno model."""
    def setUp(self):
        """Define the test client and other test variables."""
        self.nome = "User Teste"
        self.rg = "123456789"
        self.cpf = "12345678910"
        self.data_nascimento = "2020-03-04"
        self.aluno = Aluno(nome=self.nome, rg=self.rg, cpf=self.cpf, data_nascimento=self.data_nascimento)

    def test_model_can_create_a_aluno(self):
        """Test the aluno model can create a aluno."""
        old_count = Aluno.objects.count()
        self.aluno.save()
        new_count = Aluno.objects.count()
        self.assertNotEqual(old_count, new_count)
