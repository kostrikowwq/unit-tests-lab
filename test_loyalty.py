import pytest
from loyalty import loyalty_points

def test_loyalty_points_happy_path_guest():
    # Arrange
    amount = 20
    is_member = False
    
    # Act
    result = loyalty_points(amount, is_member)
    
    # Assert
    assert result == 1

def test_loyalty_points_member_multiplier():
    # Arrange
    amount = 40
    is_member = True
    
    # Act
    result = loyalty_points(amount, is_member)
    
    # Assert
    assert result == 4

def test_loyalty_points_boundary_nineteen_urn():
    # Arrange & Act & Assert
    assert loyalty_points(19, is_member=False) == 0

def test_loyalty_points_negative_amount_raises_error():
    # Arrange & Act & Assert
    with pytest.raises(ValueError) as exc_info:
        loyalty_points(-10, is_member=False)
    assert "не може бути від'ємною" in str(exc_info.value)

def test_loyalty_points_zero_amount():
    assert loyalty_points(0, is_member=True) == 0
