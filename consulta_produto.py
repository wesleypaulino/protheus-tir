from tir import Webapp
from datetime import datetime
import unittest

DataSystem = datetime.today().strftime('%d/%m/%Y')

class CONSULTA_PRODUTO(unittest.TestCase):
	
	produto = "112030"

	#Navegacao Menu Lateral 
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGACOM", DataSystem,"01","01")		
		inst.oHelper.SetLateralMenu('Atualizações > Cadastro > Produtos')
		
	#Pesquisar Browse
	def test_Browse_001(self):
		#self.oHelper.SearchBrowse('01AA1020',key='Filial+numero)
		#self.oHelper.SearchBrowse(f'D MG    {self.cliente+self.loja}', key=1, index=True)
		self.oHelper.SearchBrowse(self.produto,key='Codigo')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()    