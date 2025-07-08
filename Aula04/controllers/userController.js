const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const User = require('../models/User');

exports.registerUser = async (req, res) => {
    const { username, password } = req.body;
    if (!username || !password) return res.status(400).json({ error: 'Nome de usuário e senha são obrigatórios!' });
    
    const existingUser = await User.findOne({ username });
    if (existingUser) return res.status(400).json({ error: 'Nome de usuário já existe' });
    
    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = new User({ username, password: hashedPassword });
    await newUser.save();
    res.status(201).json({ message: 'Usuário registrado com sucesso' });
};

exports.loginUser = async (req, res) => {
    const { username, password } = req.body;
    if (!username || !password) return res.status(400).json({ error: 'Nome de usuário e senha são obrigatórios' });
    
    const user = await User.findOne({ username });
    if (!user || !(await bcrypt.compare(password, user.password))) return res.status(401).json({ error: 'Nome de usuário ou senha inválidos' });
    
    const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1h' });
    res.status(200).json({ access_token: token });
};

exports.getUser = async (req, res) => {
    const user = await User.findById(req.user.id).select('-password');
    if (!user) return res.status(404).json({ error: 'Usuário não encontrado' });
    res.json(user);
};

exports.updateUser = async (req, res) => {
    const { username, password } = req.body;
    if (!username && !password) return res.status(400).json({ error: 'Informe ao menos um campo para atualizar!' });
    
    const updates = {};
    if (username) updates.username = username;
    if (password) updates.password = await bcrypt.hash(password, 10);
    
    await User.findByIdAndUpdate(req.user.id, updates);
    res.json({ message: 'Usuário atualizado com sucesso' });
};

exports.deleteUser = async (req, res) => {
    await User.findByIdAndDelete(req.user.id);
    res.json({ message: 'Usuário deletado com sucesso' });
};