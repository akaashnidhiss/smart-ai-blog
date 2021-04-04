const express = require('express');
const path = require('path');
const router = express.Router();
const { PythonShell } = require('python-shell');
var fs = require('fs');


const ArticlesControls = require('../controllers/ArticlesControls');
const { findById } = require('../models/Article');
const ArticleInfo = require('../models/Article');
const { query } = require('express');


// @desc Login/Landing page
// @route GET /articles

router.get('/', async(req, res) => {
    const article = await ArticleInfo.find().sort({ createdAt: 'desc' });
    res.render('home', { articles: article });
})
router.get('/home', async(req, res) => {
    const article = await ArticleInfo.find().sort({ createdAt: 'desc' });
    res.render('home', { articles: article });
})

// @desc Add new article page
// @route GET /articles/add-article

router.get('/add-article', function(req, res) {
    res.render('add-article', { article: new ArticleInfo });
})



//Router to handle the incoming request.
router.get("/python", (req, res, next) => {
    //Here are the option object in which arguments can be passed for the python_test.js.
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: '', //If you are having python_test.py script in same folder, then it's optional.
        args: ['shubhamk314'] //An argument which can be accessed in the script using sys.argv[1]
    };


    PythonShell.run('trial.py', options, function(err, result) {
        if (err) console.log(err);
        // result is an array consisting of messages collected 
        //during execution of script.
        console.log('result: ', result.toString());
        res.send(result.toString())
    });
});











// @desc Single Article page
// @route GET /articles/slug

router.get('/:slug', async(req, res) => {
    const article = await ArticleInfo.findOne({ slug: req.params.slug });
    if (article == null) res.redirect('/');
    res.render('show', { article: article });
})

// @desc Posting articles and then going to home page
// @route POST /articles/


router.post('/', async(req, res, next) => {
    req.article = new ArticleInfo()
    next()
}, saveArticleAndRedirect('new'))

// @desc Deleting articles and then going to home page
// @route DELETE /articles/id

router.delete('/:id', async(req, res) => {
    await ArticleInfo.findByIdAndDelete(req.params.id);
    res.redirect('/');
})

// @desc Going to edit page for a particular article
// @route GET /articles/edit/id

router.get('/edit/:id', async(req, res) => {
    const article = await ArticleInfo.findById(req.params.id);
    res.render('edit', { article: article });
})

// @desc Putting the edited article into db
// @route PUT /articles/edit/:id

router.put('/edit/:id', async(req, res, next) => {
    req.article = await ArticleInfo.findById(req.params.id);

    let article = req.article
    article.title = req.body.title
    article.description = req.body.description
    article.body = req.body.body

    const articleAll = await ArticleInfo.find().sort({ createdAt: 'desc' });

    let arr = [];
    for (let i = 0; i < articleAll.length; i++) {

        if (article.id == articleAll.id) {
            arr.push(article.body.toString());
        } else {
            arr.push(articleAll[i].body.toString());
        }
    }



    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: 'python/',
        args: []
    };

    var file = fs.createWriteStream('python/array.txt');
    file.on('error', function(err) { console.log(err) });
    arr.forEach(function(v) { file.write(JSON.stringify(v) + "," + "/n") });
    file.end();
    PythonShell.run('Blogging.py', options, function(err, result) {
        try {
            tag_result = JSON.parse(result);
            console.log('result: ', tag_result);
            article.tags = tag_result.tags;
            Article = article.save()
        } catch (error) {
            throw err;
        }
    });
    try {
        Article = await article.save()
        res.redirect(`/articles/${Article.slug}`)
    } catch (e) {
        res.render(`${path}`, { article: article })
    }
})


// @desc Searching a paricular article from database
// @route POST /articles/search

router.post('/search', async(req, res, next) => {
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: 'python/',
        args: [req.body.query]
    };


    const articleAll = await ArticleInfo.find().sort({ createdAt: 'desc' });

    PythonShell.run('Cosine_Similarity.py', options, function(err, result) {
        try {
            cosine_result = JSON.parse(result);
            console.log('result: ', cosine_result);
            res.render('search', { query: req.body.query, article: [articleAll[cosine_result.scores[0]].toObject(), articleAll[cosine_result.scores[1]].toObject(), articleAll[cosine_result.scores[2]].toObject(), articleAll[cosine_result.scores[3]].toObject()] });

        } catch (err) {
            console.log(err);
        }
    });

})





function saveArticleAndRedirect(path) {
    return async(req, res) => {
        let article = req.article
        article.title = req.body.title
        article.description = req.body.description
        article.body = req.body.body



        const articleAll = await ArticleInfo.find().sort({ createdAt: 'desc' });
        // let arr = [articleAll.length, article.body.toString()];
        let arr = [article.body.toString()];

        for (let i = 1; i < articleAll.length; i++) {
            arr.push(articleAll[i].body.toString());
        }
        // console.log(arr);
        let options = {
            mode: 'text',
            pythonOptions: ['-u'], // get print results in real-time
            scriptPath: 'python/',
            args: []
        };
        var file = fs.createWriteStream('python/array.txt');
        file.on('error', function(err) { console.log(err) });
        arr.forEach(function(v) { file.write(JSON.stringify(v) + "," + "/n") });
        file.end();



        PythonShell.run('Blogging.py', options, function(err, result) {
            try {
                tag_result = JSON.parse(result);
                console.log('result: ', tag_result);

                article.tags = tag_result.tags;
                Article = article.save()
            } catch (error) {
                throw err;
            }
            // result is an array consisting of messages collected 
            //during execution of script.
        });


        try {
            Article = await article.save()
            res.redirect(`/articles/${Article.slug}`)
        } catch (e) {
            res.render(`${path}`, { article: article })
        }
    }
}


function cosine_similarity(query) {
    return async(req, res) => {
        let options = {
            mode: 'text',
            pythonOptions: ['-u'], // get print results in real-time
            scriptPath: 'python/', //If you are having python_test.py script in same folder, then it's optional.
            args: [] // [article.body.toString(), articlesAll.body.toString()] //An argument which can be accessed in the script using sys.argv[1]
        };




        const articleAll = await ArticleInfo.find().sort({ createdAt: 'desc' });
        // let arr = [articleAll.length, article.body.toString()];
        let arr = [query.toString()];

        for (let i = 0; i < articleAll.length; i++) {
            arr.push(articleAll[i].body.toString());
        }
        res.send('working')
            // var file = fs.createWriteStream('python/array.txt');
            // file.on('error', function(err) { /* error handling */ });
            // arr.forEach(function(v) { file.write(JSON.stringify(v) + "," + "/n") });
            // file.end();

        PythonShell.run('Cosine_Similarity.py', options, function(err, result) {
            try {
                cosine_result = JSON.parse(result);
                console.log('result: ', cosine_result);
                res.send('done')

            } catch (error) {
                console.log(error);
            }
        });
    }

}


module.exports = router;