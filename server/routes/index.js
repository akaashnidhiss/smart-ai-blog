const express = require('express');
const path = require('path');
const router = express.Router();
// const ContactControls = require('../controllers/ContactControls');


// @desc Login/Landing page
// @route GET /
router.get('/', function(req, res) {
    res.render('home');
})
router.get('/home', function(req, res) {
    res.render('home');
})



module.exports = router;