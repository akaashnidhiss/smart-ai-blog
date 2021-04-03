# 📝 [Smart AI Blog](https://smart-ai-blog.herokuapp.com/) CMS with automatic tagging using TF-IDF NLP Algorithm

+ Live [link](https://smart-ai-blog.herokuapp.com/).

```diff
+ Sample CMS built with MEN Stack
+ Automated Tagging added (stopwords for markdown not added)
+ Search functionality added (using document similarity implemented with cosine similarity)
```
This project seeks to create a content management system (CMS) for a online publishing platform with features to enhance user retention, overall user friendliness and help admin users to perform CRUD operations on their respective articles.

The project seeks to automate the process of placing the articles under topics/tags without the need for users to add it in themselves, helping the users focus solely on the content they upload, rather than how viewers find their articles.

It uses the NLP Text Pre-Processing Alogrithm, TF-IDF, to automate this task and properly annotate each article with tags generated on how important a specific feature is to the article.

When a query is passed into the search bar, we use _cosine similarity_ to find the most similar document(article) which corresponds to the query. Thus the query can be typed in natural language, and the web application will provide the top 4 similar articles to the query made.


### 🔧 Working with the following technologies:

- Node.js and Express.js
- Mongoose and MongoDB
- Passport's authentication
- EJS's templates

### 🈯 Languages used:
- Python
- Javascript

### 👷 Working Example:
- #### Working of Search Functionality
<img src="https://user-images.githubusercontent.com/60477228/113470114-9ca15980-9470-11eb-935e-ecbf209b3695.png" width="500">
<img src="https://user-images.githubusercontent.com/60477228/113470123-af1b9300-9470-11eb-849e-b53302c7d4ad.png" width="500">


- #### Working of Automated Tagging

<img src="https://user-images.githubusercontent.com/60477228/113470170-22250980-9471-11eb-9716-3f0f2083fc9e.png" width="500">
<img src="https://user-images.githubusercontent.com/60477228/113470179-2fda8f00-9471-11eb-9831-ed6ed2ab67ad.png" width="500">
<img src="https://user-images.githubusercontent.com/60477228/113470226-9bbcf780-9471-11eb-920a-54b6c4d00874.png" width="500">


- #### Navigating to category specific pages
<img src="https://user-images.githubusercontent.com/60477228/113470277-0110e880-9472-11eb-9601-6bb4cc77ce8b.png" width="500">


