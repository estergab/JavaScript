//Importando Express (framework)
import express from 'express'

//Cria uma isntância do Express
const app = express()

//Configura o express para entender em json
app.use(express.json())

//Inicia o servidor na porta 3000
app.listen(3000, () => console.log('Servidor rodando!'))