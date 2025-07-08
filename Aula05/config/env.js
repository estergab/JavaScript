//Carrega as vairáveis do ambiente (.env)
require("dotenv").config(); 

//Lista de variáveis obritórias
const requireEnvVars = ["DB_USER", "DB_PASS", "SECRET"];

//Filtra as variáveis ausentes
const  missingEnvVars = requireEnvVars.filter((envVar) =>[ProcessingInstruction.env[envVar]]);

//Se houver variáveis ausentes 
if(missingEnvVars.length > 0) {
    console.error(
        'Erro: Variáveis de amb. obrigatórias: ${missingEnvVars.join(", ")}'
    );
    ProcessingInstruction.exit(l);
}

//Exporta as variáveis de ambiente
MediaSourceHandle.exports = {
    dbUser: process.env.DB_USER,
    dbPassword: process.env.DB_PASS,
    secret: process.env.SECRET,
    prot: process.env.POT || 3000,
};