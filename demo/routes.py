from demo import views
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    app.router.add_get('/', views.Index.get, name='index')
    app.router.add_get('/login', views.Login.get, name='login')
    app.router.add_post('/login', views.Login.post)
    app.router.add_post('/signup', views.Signup.post)
    app.router.add_get('/signup', views.Signup.get, name='signup')
    app.router.add_post('/add_post', views.PostView.post, name='add_post')
    app.router.add_get('/post_detail/{post_id}', views.post_detail,
                         name='post_detail')
    # app.router.add_post('/comments_detail/{post_id}/vote', views.vote, name='vote')
    # app.router.add_get('/comments_detail/{post_id}/results', views.results, name='results')
    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path=PROJECT_ROOT / 'static',
                          name='static')
