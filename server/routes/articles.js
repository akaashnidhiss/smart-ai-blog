const express = require('express');
const path = require('path');
const router = express.Router();
// const ContactControls = require('../controllers/ContactControls');
const ArticlesControls = require('../controllers/ArticlesControls');
const ArticleInfo = require('../models/Article');


// @desc Login/Landing page
// @route GET /articles

router.get('/', async(req, res) => {
    const article = await ArticleModel.find().sort({ createdAt: 'desc' });
    res.render('home', { articles: article });
})
router.get('/home', async(req, res) => {
    const article = await ArticleModel.find().sort({ createdAt: 'desc' });
    res.render('home', { articles: article });
})

// @desc Add new article page
// @route GET /articles/add-article

router.get('/add-article', function(req, res) {
    res.render('add-article', { article: new ArticleInfo });
})

// @desc Single Article page
// @route GET /articles/slug

router.get('/:slug', async(req, res) => {
    const article = await ArticleInfo.findOne({ slug: req.params.slug });
    if (article == null) res.redirect('/');
    res.render('show', { article: article });
})

// @desc Posting articles and then going to home page
// @route POST /articles/

router.post('/', async(req, res) => {
    const Article = new ArticleInfo({
        title: req.body.title,
        description: req.body.description,
        body: req.body.body
    })
    console.log(Article);
    try {
        article = await Article.save();
        res.redirect(`/articles/${article.slug}`);
    } catch (error) {
        console.log(error);
        res.render('new', { article: article });
    }
})

// @desc Deleting articles and then going to home page
// @route POST /articles/id

router.delete('/:id', async(req, res) => {
    await ArticleInfo.findByIdAndDelete(req.params.id);
    res.redirect('/');
})

module.exports = router;