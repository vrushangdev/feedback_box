import bcrypt
import pytest

from feedback_box.domain.tripcode import \
    (Tripcode,
     SEPARATOR,
     TRIPCODE_OWNER_INDEX,
     TRIPCODE_PASSWORD_INDEX)


@pytest.fixture(scope='function')
def tripcode_without_code():
    return Tripcode()


@pytest.fixture(scope='function')
def tripcode_with_code():
    tripcode = Tripcode()

    tripcode.generate_code(
        owner='test_owner',
        password='dummy_password'
    )

    return tripcode


class TestTripcodeEntity:

    def test_tripcode_initialize_correctly_without_code(self, tripcode_without_code):
        assert isinstance(tripcode_without_code, Tripcode)
        assert hasattr(tripcode_without_code, 'code')
        assert tripcode_without_code.code is None

    def test__str__returns_correct_string_representation_of_tripcode(self, tripcode_with_code):
        code = tripcode_with_code.code

        assert code == str(tripcode_with_code)

    def test_tripcode_generates_correctly_code(self, monkeypatch, tripcode_without_code):
        monkeypatch.setattr(bcrypt, 'hashpw', lambda password, salt: 'hashed_password'.encode())

        tripcode = tripcode_without_code
        code = tripcode.generate_code(
            owner='test_owner',
            password='dummy_password'
        )

        assert tripcode.code == code
        assert tripcode.code.split(SEPARATOR)[TRIPCODE_OWNER_INDEX] == 'test_owner'
        assert tripcode.code.split(SEPARATOR)[TRIPCODE_PASSWORD_INDEX] == 'hashed_password'

    def test_tripcode_check_password_returns_true_when_called_with_correct_password(self, tripcode_with_code):
        assert tripcode_with_code.check_password('dummy_password')

    def test_tripcode_check_password_returns_false_when_called_with_bad_password(self, tripcode_with_code):
        assert not tripcode_with_code.check_password('wrong_password')

    def test_owner_property_returns_owner(self, tripcode_with_code):
        assert tripcode_with_code.owner == 'test_owner'
