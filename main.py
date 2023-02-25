from model import Model, ModelQT
from views.view import View
from presenter import Presenter

if __name__ == '__main__':
    view = View()
    model = ModelQT()
    presenter = Presenter(view, model)
    presenter.run()
