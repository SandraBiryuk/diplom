import sender_stand_request

def test_order_create_and_get():
    response_create = sender_stand_request.post_new_order()
    assert response_create.status_code == 201

    track_number = response_create.json()["track"]
    response_get = sender_stand_request.get_order(track_number)
    assert response_get.status_code == 200
