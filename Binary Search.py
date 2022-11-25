# %% [markdown]
# In Linear Search algorithm, execution time is more  so we have come with new solution that is:
# BINARY SEARCH 

# %%
# BINARY SEARCH ALGORITHM
def locate_card_bs(cards, query):
    lo,hi=0, len(cards)-1
    print("lo:",lo," hi: ",hi)
    
    while lo<=hi:
        mid = (lo+hi)//2
        mid_number = cards[mid]
        print("lo: ",lo,"hi: ",hi,"mid: ",mid,"mid_number: ",mid_number)

        if mid_number == query:
            return mid
        elif mid_number > query:
            lo = mid+1
        elif mid_number < query:
            hi = mid-1

    return -1


# %%
# Ideal input
cards = [2,4,6,8,9,11,2,4,6,13,15]
cards.sort(reverse=True)
print(cards)
query = 4
result = locate_card_bs(cards,query)
print(result)


# %%
# empty input
cards = []
cards.sort(reverse=True)
print(cards)
query = 4
result = locate_card_bs(cards,query)
print(result)

# %%
# query is not present in the input
cards = [1,2,3,4,5,6]
cards.sort(reverse=True)
print(cards)
query = 7
result = locate_card_bs(cards,query)
print(result)

# %%
# query is present in the first postion of the input
cards = [1,2,3,4,5,6]
cards.sort(reverse=True)
print(cards)
query = 6
result = locate_card_bs(cards,query)
print(result)

# %%
# query is present in the last position of the input
cards = [1,2,3,44,4,5,6,55,44,33,33,66,11,668,78]
cards.sort(reverse=True)
print(cards)
query = 44
result = locate_card_bs(cards,query)
print(result)

# %% [markdown]
# 1. The above code got failed because it should pop up the first location of the number if the numbers are repetative. 
# but here it is failed
# 2. if we pass empty list, than it is getting pass
# 3. If the query number is not present than it is getting pass
# 4. Last position and first position also, it is identifying

# %%
# to over come from failure of repetative number
def test_location(cards,query, mid):
    mid_number = cards[mid]
    print("mid_number: ",mid_number)

    if mid_number == query:
        if cards[mid-1] == query and mid-1 >= 0:
            return "left"
        else:
            return "found"

    elif mid_number > query:
        return "right"
    elif mid_number < query:
        return "left"

# %%
# BINARY SEARCH ALGORITHM
def locate_card_bs(cards, query):
    lo,hi=0, len(cards)-1
    print("lo:",lo," hi: ",hi)
    
    while lo<=hi:
        mid = (lo+hi)//2
        mid_number = cards[mid]
        result = test_location(cards,query,mid)
        print("lo: ",lo,"hi: ",hi,"mid: ",mid,"mid_number: ",mid_number)

        if result == "found":
            return mid
        elif result == "right":
            lo = mid+1
        elif result == "left":
            hi = mid-1

    return -1

# %%
# repetative query numebr in input
cards = [1,1,3,3,2,3,4,5,6,44,33,66,11,668,78]
cards.sort(reverse=True)
print(cards)
query = 3
result = locate_card_bs(cards,query)
print(result)

# %%
# empty input list
cards = []
cards.sort(reverse=True)
print(cards)
query = 3
result = locate_card_bs(cards,query)
print(result)

# %%
# query is not present in list
cards = [3,4,7,8,1,99,3]
cards.sort(reverse=True)
print(cards)
query = 9
result = locate_card_bs(cards,query)
print(result)

# %% [markdown]
# The above function is able to execute all the edge condtions
# 


