import sqlite3

banco = sqlite3.connect('venda.db')

#cria tabela no sqlite
cursor = banco.cursor()
# cursor.execute("create table cliente (id_cliente  integer primary key autoincrement,nome_cliente text,telefone integer,cidade text,email text)")
# cursor.execute("create table produto (id_produto integer primary key autoincrement,nome_produto text,descricao text,categoria text,marca text,preco decimal(5,2),estoque integer)")
# cursor.execute("create table venda (id_venda integer primary key autoincrement,id_produto integer,id_cliente integer,dataHora datetime,totalVenda decimal(5,2),nome_funcionario text,FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),FOREIGN KEY (id_produto) REFERENCES cliente(id_produto))")



banco.commit()

def listar_cliente():
    cursor.execute('SELECT * FROM cliente')
    print(cursor.fetchall())

def listar_produto():
    cursor.execute('SELECT * FROM produto')
    print(cursor.fetchall())


def inserir(id_produto,nome_produto,descricao,categoria,marca,preco,estoque):
    cursor.execute("insert into produto values(?,?,?,?,?,?,?)",(id_produto,nome_produto,descricao,categoria,marca,preco,estoque))


# inserir(1,"Smartphone", "Smartphone de última geração.", "Eletrônicos", "Samsung", 1999.99, 100),
# inserir(2,"Smartwatch", "Relógio inteligente com diversas funcionalidades.", "Eletrônicos", "Apple", 1499.99, 80),
# inserir(3,"Fone de Ouvido Bluetooth", "Fone de ouvido sem fio com tecnologia Bluetooth.", "Eletrônicos", "Sony", 899.99, 120),
# inserir(4,"Tablet", "Tablet com tela de alta resolução.", "Eletrônicos", "Microsoft", 1099.99, 90),
# inserir(5,"Câmera DSLR", "Câmera digital DSLR para fotografia profissional.", "Eletrônicos", "Canon", 2599.99, 70),
# inserir(6,"Notebook", "Notebook ultrafino e potente.", "Eletrônicos", "Dell", 3499.99, 110),
# inserir(7,"TV 4K", "Televisão com resolução 4K e tecnologia HDR.", "Eletrônicos", "LG", 7999.99, 60),
# inserir(8,"Console de Video Game", "Console de última geração para jogos.", "Eletrônicos", "Sony PlayStation", 10999.99, 50),
# inserir(9,"Fone de Ouvido Gamer", "Fone de ouvido com isolamento de ruído para gamers.", "Eletrônicos", "Razer", 6499.99, 80),
# inserir(10,"Monitor Gamer", "Monitor de alta taxa de atualização para jogos.", "Eletrônicos", "Asus", 99.99, 150),
# inserir(11,"Mouse Gamer", "Mouse com sensor de alta precisão para jogadores profissionais.", "Eletrônicos", "Logitech", 5499.99, 70),
# inserir(12,"Teclado Mecânico", "Teclado mecânico com switches Cherry MX.", "Eletrônicos", "Corsair", 3799.99, 100),
# inserir(13,"HD Externo", "HD externo portátil com grande capacidade de armazenamento.", "Eletrônicos", "Seagate", 1299.99, 120),
# inserir(14,"Caixa de Som Bluetooth", "Caixa de som portátil com conexão Bluetooth.", "Eletrônicos", "JBL", 6999.99, 40),
# inserir(15,"Roteador Wi-Fi", "Roteador com tecnologia Wi-Fi 6 para alta velocidade de conexão.", "Eletrônicos", "TP-Link", 4499.99, 60),
# inserir(16,"Console Portátil", "Console portátil para jogos em movimento.", "Eletrônicos", "Nintendo", 8999.99, 80),
# inserir(17,"Câmera de Segurança", "Câmera de segurança com visão noturna e detecção de movimento.", "Eletrônicos", "Ring", 2499.99, 100),
# inserir(18,"Impressora Multifuncional", "Impressora multifuncional com conexão Wi-Fi.", "Eletrônicos", "Epson", 6999.99, 70),
# inserir(19,"Drone", "Drone com câmera HD e controle remoto.", "Eletrônicos", "DJI", 3999.99, 90),
inserir(20,"Smart TV", "Televisão inteligente com sistema operacional integrado.", "Eletrônicos", "Sony", 7499.99, 50)






# cursor.execute("delete from produto")

listar_produto()

banco.commit()