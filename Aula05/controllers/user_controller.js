const User = require("../models/usuarioModel");

const getUserById = async (req, res, next) => {
    try {
        const id = req.params.id;

        const user = await User.findById(id);
        if (!user) {
            return res.status(404).json({ msg: "Usuário não encontrado!"});
        }
        res.status(200).json({ user });
    } catch (error)
      next (error);

      function checktoken(req, res, next) {
        const authHeader = req.headers["authorization"]
        const token = authHeader && authHeader.split(" ")[1];
      
        if (!token) return res.status(401).json({ msg: "Acesso Negado!"});
      
        try {
          const secret = process.env.SECRET
      
          jwt.verify(token, secret);
      
          next();
        } catch (err) {
          res.status(400).json({ msg: "O token é inválido" });
        }
      }
};