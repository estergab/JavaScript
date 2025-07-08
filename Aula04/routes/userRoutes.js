const userController = require('../controllers/userController');
const express = require('express');
const { registerUser, loginUser, getUser, updateUser, deleteUser } = require('../controllers/userController');
const authenticate = require('../middleware/authMiddleware');

const router = express.Router();

router.post('/register', registerUser);
router.post('/login', loginUser);
router.get('/', authenticate, getUser);
router.put('/', authenticate, updateUser);
router.delete('/', authenticate, deleteUser);

module.exports = router;