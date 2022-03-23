from main import *



def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(', 'a', ')', '(', ')']) == True

def test_parens_match_iterative2():
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False
    assert parens_match_iterative(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_iterative(['(', '(', ')']) == False
    assert parens_match_iterative(['(', 'a', ')', ')', '(']) == False
#    print(parens_match_iterative([')','('])) 
  

def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(', 'a', ')', '(', ')']) == True

def test_parens_match_scan2():
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False
    assert parens_match_scan(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_scan(['(', '(', ')']) == False
    assert parens_match_scan(['(', 'a', ')', ')', '(']) == False

def test_parens_match_dc():
    assert parens_match_dc(['(', ')']) == True
    assert parens_match_dc(['(', 'a', ')', '(', ')']) == True

def test_parens_match_df2():
    assert parens_match_dc(['(']) == False
    assert parens_match_dc([')']) == False
    assert parens_match_dc(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_dc(['(', '(', ')']) == False
    assert parens_match_dc(['(', 'a', ')', ')', '(']) == False
    assert parens_match_dc([]) == True 
test_parens_match_iterative()
test_parens_match_iterative2()
test_parens_match_scan()
test_parens_match_scan2()
test_parens_match_dc()
test_parens_match_df2()