import data
import sender_stand_request

# Успешное создание заказа
def test_order_creation():
    response = sender_stand_request.order_creation(data.order_body)
    assert response.status_code == 201, 'Order not created'

# Успешное получение заказа по трек-номеру заказа, созданному в этом же тесте
# !!!Получение заказа по существующему треку может работать
def test_order_by_track():
    track = sender_stand_request.get_order_track()
    response = sender_stand_request.get_order(track)
    assert response.status_code == 200, 'Order not found'


