from demo import views
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    app.router.add_get('/', views.index)
    app.router.add_get('/comments_detail/{post_id}', views.comments_detail,
                         name='comments_detail')
    app.router.add_post('/comments_detail/{post_id}/vote', views.vote, name='vote')
    app.router.add_get('/comments_detail/{post_id}/results', views.results, name='results')
    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path=PROJECT_ROOT / 'static',
                          name='static')
