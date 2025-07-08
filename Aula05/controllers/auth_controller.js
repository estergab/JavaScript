const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const User = require("../models/usuarioModel");

const registerUser = async (req, res, next) => {
    try {
        const { name, email, password} = req.body
        
    }
}