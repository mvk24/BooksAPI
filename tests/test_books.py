import pytest

def test_create_book(client):
    book_data = {
        "title": "Unique",
        "author": "Test Author new",
        "genre": "history",
        "yop": 2022,
        "description": "Sample description",
        "price": 100
    } 
    response = client.post("/books/", json = book_data)

    print(response.status_code)
    print("Response status------333333", response.json())

    assert response.status_code == 201
    data = response.json()

    
    assert data["title"] == book_data["title"]
    assert data["author"] == book_data["author"]
    assert "id" in data
    assert "owner_id" in data


def test_get_all_books(client):
    response = client.get("/books/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)



# @pytest.mark.asyncio
# async def test_update_book(async_client):
#     create_res = await async_client.post("/books/", json = {
#         "title": "Old Title",
#         "author": "Old Author",
#         "description": "Before update"
#     })
#     book_id = create_res.json().get("id")
#     update_res = await async_client.put(f"/books/{book_id}", json = {
#         "title": "New Title",
#         "author": "new author",
#         "description": "after update"
#     })
#     assert update_res.status_code == 200
#     assert update_res.json()["title"] == "New Title"


# @pytest.mark.asyncio
# async def test_delete_book(async_client):
#     create_res = await async_client.post("/books/", json = {
#             "title": "Delete me",
#             "author": "Author X"
#             })
#     book_id = create_res.json().get("id")
#     delete_res = await async_client.delete(f"/books/{book_id}")
#     assert delete_res.status_code == 200