from project import check_for_paper, check_for_stone, check_for_scissor
comp_set = ["stone","paper","scissors"]

def main():
    test_check_for_stone()
    test_check_for_paper()
    test_check_for_scissor()

def test_check_for_stone():
    assert check_for_stone("stone")==True
    assert check_for_stone("scissor")==True
    assert check_for_stone("paper")==False

def test_check_for_paper():
    assert check_for_paper("paper")==True
    assert check_for_paper("stone")==True
    assert check_for_paper("scissor")==False

def test_check_for_scissor():
    assert check_for_scissor("scissor")==True
    assert check_for_scissor("paper")==True
    assert check_for_scissor("stone")==False

if __name__ == '__main__':
    main()


