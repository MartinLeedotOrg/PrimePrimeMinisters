#!/usr/bin/env python3
def is_prime(a):
    if a == 1:
        return False
    a = int(a)
    return all(a % i for i in range(2, a))


ordered_pms = ["Robert Walpole", "Spencer Compton", "Henry Pelham", "Thomas Pelham-Holles", "William Cavendish", "Thomas Pelham-Holles", "John Stuart", "George Grenville", "Charles Watson Wentworth", "William Pitt, the Elder", "Augustus Henry Fitzroy", "Frederick North", "Charles Watson Wentworth", "William Petty-Fitzmaurice", "William Henry Cavendish-Bentinck", "William Pitt, the Younger", "Henry Addington", "William Pitt, the Younger", "William Wyndham Grenville", "William Henry Cavendish-Bentinck", "Spencer Perceval", "Robert Banks Jenkinson", "George Canning", "Frederick John Robinson", "Arthur Wellesley", "Charles Grey", "William Lamb", "Arthur Wellesley", "Robert Peel", "William Lamb", "Robert Peel", "John Russell", "Edward Geoffrey Stanley", "George Hamilton-Gordon", "Henry John Temple", "Edward Geoffrey Stanley", "Henry John Temple", "John Russell", "Edward Geoffrey Stanley", "Benjamin Disraeli", "William Ewart Gladstone", "Benjamin Disraeli", "William Ewart Gladstone", "Robert Cecil", "William Ewart Gladstone", "Robert Cecil", "William Ewart Gladstone", "Archibald Philip Primrose", "Robert Cecil", "Arthur James Balfour", "Henry Campbell-Bannerman", "H.H. Asquith", "David Lloyd George", "Bonar Law", "Stanley Baldwin", "Ramsay Macdonald", "Stanley Baldwin", "Ramsay Macdonald", "Stanley Baldwin", "Neville Chamberlain", "Winston Churchill", "Clement Attlee", "Winston Churchill", "Anthony Eden", "Harold Macmillan", "Alec Douglas-Home", "Harold Wilson", "Edward Heath", "Harold Wilson", "James Callaghan", "Margaret Thatcher", "John Major", "Tony Blair", "Gordon Brown", "David Cameron", "Theresa May"]

for i, name in enumerate(ordered_pms):
    if is_prime(i + 1):
        print("{}: {}".format(i + 1, name))
