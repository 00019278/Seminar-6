def test_is_valid(test):
    if isinstance(test,int) and 1<test<3:
        return True
    else:
        return False
result = test_is_valid(2)
print(result)