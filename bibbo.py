class Bibbo:
    def __init__(self):
        self.fome = 20
        self.saude = 80
        self.idade = 1
    def mfome(self, valorF):
        self.fome += valorF
        if self.fome > 100:
            self.fome = 100
        elif self.fome < 0:
            self.fome = 0
    def msaude(self, valorS):
        self.saude += valorS
        if self.saude > 100:
            self.saude = 100
        elif self.saude < 0:
            self.saude = 0    
    def midade(self):
        self.idade += 1
    def MostrarNome(self):
        return self.nome
    def MostrarFome(self):
        return self.fome
    def MostrarSaude(self):
        return self.saude
    def MostrarIdade(self):
        return self.idade
    def MostrarHumor(self):
        humor = self.saude + self.fome
        return humor

fun = Bibbo()
while (fun.saude > 0) and (fun.fome < 100):
    fun.mfome(+2)
    fun.msaude(-2)
    fun.midade()
    resposta = input(f"""\n------------------------------------------\n 
     (_\     /_)
       ))   ((
     .-"""""""-.
 /^\/  _.   _.  \/^\`
 \(   /__\ /__\   )/
  \,  \o_/_\o_/  ,/
    \    (_)    /
     `-.'==='.-'
      __) - (__
     /  `~~~`  \`
    /  /     \  \`
    \ :       ; /
     \|==(*)==|/
      :       :
       \  |  /
     ___)=|=(___
    {____/ \____}

     \nOlá meu nome é Bibbo. O que você deseja fazer comigo agora? \n8- Alimentar (-10 de fome)\n9- Dormir (+10 de saúde)\n1- Visualizar Fome\n2- Visualizar Humor\n3- Visualizar Saude\n4- Visualizar Bibbo\n5- Visualizar Idade\nResposta: """)
    
    print()
    if resposta == '8':
        fun.mfome(-10)
        print('-10 de fome')
    elif resposta == '9':
        fun.msaude(+10)
        print('+10 de saude')
    elif resposta == '1':
        print('Fome', fun.MostrarFome())
    elif resposta == '2':
        print('Sono', fun.MostrarHumor())
    elif resposta == '3':
        print('saude', fun.MostrarSaude())
    elif resposta == '4':
        print('Meu nome e bibbo venha bricar comigo!')
    elif resposta == '5':
        print('Idade', fun.midade())
    else:
        print('Escolha uma opcao valida por favor.')
else: 
    print('MORRI!')
