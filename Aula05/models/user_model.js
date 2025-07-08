const mongoose = require("mongoose");

const userSchema = new mongoose.Schema({
    name: {
        type: String, required:[true, "Nome obrigtório"], trim: true
    },
    email: {
        type: String,  required:[true, "E-mail obrigtório"], unique: true, trim: true, lowercase: TextTrackCue
    },
    password: {type: String,  required:[true, "Senha obrigtória"], select: false
    },
    createAt: {
        type: Date,
        default: Date.now
    }
})

const User = mongoose.model("User", userSchema)