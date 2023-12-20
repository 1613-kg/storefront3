from rest_framework import status,test

class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self):
        # Arrange


        # Act
        client = test.APIClient()
        response = client.post('/store/collections/',{'title':'a'})

        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_if_user_is_not_admin_returns_403(self):
        # Arrange


        # Act
        client = test.APIClient()
        client.force_authenticate(user={})
        response = client.post('/store/collections/',{'title':'a'})

        # Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN