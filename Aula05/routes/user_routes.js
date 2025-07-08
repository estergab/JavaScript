const express = require("express")
const rouyter = express.Router();
const { getUserById } = require("../controllers/user_controller");

router.get("/:id", checkToken, getUserById);

module.exports = router;




