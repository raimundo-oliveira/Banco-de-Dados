from flask import Flask,render_template,request,redirect, url_for, flash
import sqlite3

app = Flask(__name__)


@app.route("/")
def principal():
	return render_template('home.html')

@app.route("/produtos")
def produtos():
	banco = sqlite3.connect('venda.db')
	cursor = banco.cursor()

	cursor.execute('SELECT * FROM produto')
	data = cursor.fetchall()
    #print(con.fetchall())

	return render_template('produtos.html', data = data)

@app.route("/clientes")
def clientes():
	banco = sqlite3.connect('venda.db')
	cursor = banco.cursor()

	cursor.execute('SELECT * FROM cliente')
	data = cursor.fetchall()
    #print(con.fetchall())

	return render_template('clientes.html', data = data)


@app.route("/add_usuario")
def add_usuario():
	return render_template("cadastro.html")

@app.route("/add_usuario2", methods = ['POST'])
def add_usuario2():
	idCliente = request.form['id']
	nome = request.form['nome']
	telefone = request.form['tel']
	cidade = request.form['cidade']
	email = request.form['email']

	banco = sqlite3.connect('venda.db')
	cursor = banco.cursor()

	cursor.execute("insert into cliente values(?,?,?,?,?)",(idCliente,nome,telefone,cidade,email))
	banco.commit()
	return redirect(url_for("clientes"))

@app.route("/add_produto")
def add_produto():
	return render_template("inserirProduto.html")

@app.route("/add_produto2", methods = ['POST'])
def add_produto2():
	idProduto = request.form['id']
	nome = request.form['nome']
	descricao = request.form['descricao']
	categoria = request.form['categoria']
	marca = request.form['marca']
	preco = request.form['preco']
	estoque = request.form['estoque']

	banco = sqlite3.connect('venda.db')
	cursor = banco.cursor()

	cursor.execute("insert into produto values(?,?,?,?,?,?,?)",(idProduto,nome,descricao,categoria,marca,preco,estoque))
	banco.commit()
	return redirect(url_for("produtos"))



@app.route("/vendas")
def vendas():
	banco = sqlite3.connect('venda.db')
	cursor = banco.cursor()

	cursor.execute("select * from venda")
	data = cursor.fetchall()
	
	return render_template("vendasRealizadas.html", data = data)

@app.route("/compra")
def compra():
	return render_template("venda.html")

@app.route("/compra2", methods = ['POST'])
def compra2():
	id_venda = request.form['id_venda']
	id_produto = request.form['id_produto']
	idCliente = request.form['id_cliente']
	dataHora = request.form['dataHora']
	totalVenda = request.form['totalVenda']
	nome_funcionario = request.form['nome_funcionario']
	

	banco = sqlite3.connect('venda.db')
	cursor = banco.cursor()

	cursor.execute("insert into venda values(?,?,?,?,?,?)", (id_venda,id_produto,idCliente,dataHora,totalVenda,nome_funcionario))
	banco.commit()

	return redirect(url_for("vendas"))

@app.route("/detalharCliente/<string:id>", methods = ['GET'])
def detalharCliente(id):
	banco = sqlite3.connect("venda.db")
	cursor = banco.cursor()

	cursor.execute("select * from cliente where id_cliente=?", (id,))
	cliente = cursor.fetchone()
	cursor.close()

	return render_template("detalharCliente.html", cliente=cliente)

@app.route("/detalharProduto/<string:id>", methods = ['GET'])
def detalharProduto(id):
	banco = sqlite3.connect("venda.db")
	cursor = banco.cursor()

	cursor.execute("select * from produto where id_produto=?", (id,))
	produto = cursor.fetchone()
	cursor.close()

	return render_template("detalharProduto.html", produto=produto)

@app.route("/editarCliente/<string:id>", methods = ['GET', 'POST'])
def editarCliente(id):
	if request.method == 'GET':
		banco = sqlite3.connect("venda.db")
		cursor = banco.cursor()
		
		cursor.execute("select * from cliente where id_cliente=?", (id,))
		cliente = cursor.fetchone()
		cursor.close()

		return render_template("editarCliente.html",cliente=cliente)
	elif request.method == 'POST':
		nome = request.form['nome']
		telefone = request.form['tel']
		cidade = request.form['cidade']
		email = request.form['email']

		banco = sqlite3.connect("venda.db")
		cursor = banco.cursor()

		cursor.execute("update cliente set nome_cliente=?,telefone=?,cidade=?,email=? where id_cliente=?", (nome,telefone,cidade,email,id,))
		cliente = cursor.fetchone()
		banco.commit()

		return redirect(url_for("clientes"))

@app.route("/excluirCliente/<string:id>",methods = ['GET'])
def excluirCliente(id):
	banco = sqlite3.connect("venda.db")
	cursor = banco.cursor()
	
	cursor.execute("delete from cliente where id_cliente=?", (id,))
	banco.commit()
	flash('dados deletados', 'warning')

	return redirect(url_for("clientes"))

@app.route("/editarProduto/<string:id>", methods = ['GET', 'POST'])
def editarProduto(id):
	if request.method == 'GET':
		banco = sqlite3.connect("venda.db")
		cursor = banco.cursor()
		
		cursor.execute("select * from produto where id_produto=?", (id,))
		produto = cursor.fetchone()
		cursor.close()

		return render_template("editarProduto.html",produto=produto)
	elif request.method == 'POST':
		nome = request.form['nome']
		descricao = request.form['descricao']
		categoria = request.form['categoria']
		marca = request.form['marca']
		preco = request.form['preco']
		estoque = request.form['estoque']
		

		banco = sqlite3.connect("venda.db")
		cursor = banco.cursor()

		cursor.execute("update produto set nome_produto=?,descricao=?,categoria=?,marca=?,preco=?,estoque=? where id_produto=?", (nome,descricao,categoria,marca,preco,estoque,id,))
		produto = cursor.fetchone()
		banco.commit()

		return redirect(url_for("produtos"))
	
@app.route("/excluirProduto/<string:id>",methods = ['GET'])
def excluirProduto(id):
	banco = sqlite3.connect("venda.db")
	cursor = banco.cursor()
	
	cursor.execute("delete from produto where id_produto=?", (id,))
	banco.commit()
	flash('dados deletados', 'warning')

	return redirect(url_for("produtos"))

@app.route("/editarVenda/<string:id>", methods = ['GET', 'POST'])
def editarVenda(id):
	if request.method == 'GET':
		banco = sqlite3.connect("venda.db")
		cursor = banco.cursor()
		
		cursor.execute("select * from venda where id_venda=?", (id,))
		venda = cursor.fetchone()
		cursor.close()

		return render_template("editarVenda.html",venda=venda)
	elif request.method == 'POST':
		dataHora = request.form['dataHora']
		totalVenda = request.form['totalVenda']
		nome_funcionario = request.form['nome_funcionario']
		

		banco = sqlite3.connect("venda.db")
		cursor = banco.cursor()

		cursor.execute("update venda set dataHora=?,totalVenda=?,nome_funcionario=? where id_venda=?", (dataHora,totalVenda,nome_funcionario,id,))
		venda = cursor.fetchone()
		banco.commit()

		return redirect(url_for("vendas"))
	
@app.route("/excluirVenda/<string:id>",methods = ['GET'])
def excluirVenda(id):
	banco = sqlite3.connect("venda.db")
	cursor = banco.cursor()
	
	cursor.execute("delete from venda where id_venda=?", (id,))
	banco.commit()
	flash('dados deletados', 'warning')

	return redirect(url_for("vendas"))


if __name__ == "__main__":
	app.secret_key = "admin123"
	app.run(debug = True)
