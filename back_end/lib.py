# class Articles(db.Module):
#     id = db.Column(db.Interger, primary_key=True)
#     title = db.Column(db.String(100))
#     body = db.Column(db.Text())
#     date = db.Column(db.DataTime, datetime.datetime.now)
#
#     def __init__(self, title, body):
#         self.title = title
#         self.body = body
#
# class ArticleSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'title', 'body', 'date')
#
# article_schema = ArticleSchema()
# articles_schema = ArticleSchema(many=True)
#
#
# @app.route('/get', method=['GET'])
# def get_articles():
#     all_articles = Articles.query.all()
#     results = articles_schema.dump(all_articles)
#     return jsonify(results)
#
#
# @app.route('/get/<id>/', method=['GET'])
# def post_details(id):
#     article = Articles.query.get(id)
#     return article_schema.jsonify(article)
#
#
# @app.route('/add', method=['POST'])
# def add_article():
#     title = request.json['title']
#     body = request.json['body']
#
#     articles = Articles(title, body)
#     db.session.add(articles)
#     db.session.commit()
#     return article_schema.jsonify(articles)
#
#
# @app.route('/update/<id>', method=['PUT'])
# def update_article(id):
#     article = Articles.query.get(id)
#     title = request.json['title']
#     body = request.json['body']
#     article.title = title
#     article.body = body
#
#     db.session.commit()
#     return article_schema.jsonify(article)
#
#
# @app.route('delete/<id>', method=['DELETE'])
# def delete_article(id):
#     article = Articles.query.get(id)
#     db.session.delete(article)
#     db.session.commit()
#
#     return article_schema.jsonify(article)


# class History(db.Model):
#     __tablename__ = 'hiatory'
#     histroy_id = db.Column(db.Interger, primary_key=True)
#     book_id = db.Column(db.Interger)
#     student_name = db.Column(db.Text())
#     date_borrow = db.Column(db.Text())
#     date_return = db.Column(db.Text())
#     status = db.Column(db.Text(), default = 'not return')
#     """
#         def __init__(self, history_id, book_id, student_name, date_borrow, date_return, status):
#         self.histroy_id = history_id
#         self.book_id = book_id
#         self.user_name = student_name
#         self.date_borrow = date_borrow
#         self.date_return = date_return
#         self.status = status
#     """