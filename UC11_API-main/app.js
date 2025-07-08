const express = require("express");
const app = express();
const port = 3000;

// Middleware para processar JSON
app.use(express.json());

// Array (Para não usar DB)
let produtos = [
  {
    id: 1,
    nome: "Smartphone",
    preco: 1500.0,
    descricao: "Smartphone última geração",
  },
  {
    id: 2,
    nome: "Notebook",
    preco: 3500.0,
    descricao: "Notebook para trabalho",
  },
  {
    id: 3,
    nome: "Tablet",
    preco: 900.0,
    descricao: "Tablet para entretenimento",
  },
];

// GET - Listar todos os produtos
app.get("/produtos", (req, res) => {
  res.json(produtos);
});

// GET - Buscar produto por ID
app.get("/produtos/:id", (req, res) => {
  const id = parseInt(req.params.id);
  const produto = produtos.find((p) => p.id === id);

  if (!produto) {
    return res.status(404).json({ mensagem: "Produto não encontrado" });
  }

  res.json(produto);
});

// POST - Criar novo produto
app.post("/produtos", (req, res) => {
  const novoProduto = {
    id: produtos.length + 1,
    nome: req.body.nome,
    preco: req.body.preco,
    descricao: req.body.descricao,
  };

  produtos.push(novoProduto);
  res.status(201).json(novoProduto);
});

// PUT - Atualizar produto
app.put("/produtos/:id", (req, res) => {
  const id = parseInt(req.params.id);
  const index = produtos.findIndex((p) => p.id === id);

  if (index === -1) {
    return res.status(404).json({ mensagem: "Produto não encontrado" });
  }

  const produtoAtualizado = {
    id: id,
    nome: req.body.nome,
    preco: req.body.preco,
    descricao: req.body.descricao,
  };

  produtos[index] = produtoAtualizado;
  res.json(produtoAtualizado);
});

// DELETE - Remover produto
app.delete("/produtos/:id", (req, res) => {
  const id = parseInt(req.params.id);
  const index = produtos.findIndex((p) => p.id === id);

  if (index === -1) {
    return res.status(404).json({ mensagem: "Produto não encontrado" });
  }

  produtos.splice(index, 1);
  res.status(204).send();
});

app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
