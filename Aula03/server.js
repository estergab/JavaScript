const connectDB = require('./config/db'); // Declare uma vez
const express = require('express');
const dotenv = require('dotenv');
const userRoutes = require('./routes/userRoutes');

dotenv.config();

const app = express();
app.use(express.json());
app.use('/users', userRoutes);

connectDB(); // Chama a função para conectar ao banco

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Servidor rodando na porta ${PORT}`));

