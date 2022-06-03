import model_sum
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model_sum.init(value_a, value_b)
    result = model_sum.do_it()
    view.view_data(result, 'sum')
