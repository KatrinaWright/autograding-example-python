import hello;

# Example Passing Test
def test_hello_pass():
    assert hello.hello_world() == "Hello!"

# Example Failed Test
# Uncomment, run once & then comment out again
#def test_hello_fail():
#    assert hello.hello_world() == "Hello World!"

#########################
#  HW Assignment Tests  #
#########################

# 4 Tests
def test_squared_sum_empty():
    assert hello.squared_sum( [] ) == 0

def test_squared_sum():
    assert hello.squared_sum([5, -2, 3]) == 38
    assert hello.squared_sum([-3, 4]) == 25
    assert hello.squared_sum([7, -1, 15, 0]) == 275

# 5 Tests
def test_mix_empty():
    assert hello.mix("", "") == ""

def test_mix():
    assert hello.mix("hello", "there") == "htehlelroe"
    assert hello.mix("1234", "abcd") == "1a2b3c4d"
    assert hello.mix("12", "abcd") == "1a2bcd"
    assert hello.mix("1234", "ab") == "1a2b34"