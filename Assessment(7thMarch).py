'Problem 1'
# class Solution:
#     def strong_passwords(self, passwords):
#         strong = []
#         ##Write your code here
#         for i in passwords:
#             if(len(i) >= 8) and any(c.isupper() for c in i) and any(c.isdigit() for c in i) and any(c in '@#$' for c in i):
#                 strong.append(i)
       
#         return strong



'Problem 2'
# class Solution:
#     def low_stock_products(self, inventory):
#         result = []
#         #Write your code here
#         for i in inventory:
#             if(inventory[i] < 10):
#                 result.append(i)
       
#         return result



'Problem 3'
# class Solution:
#     def find_duplicate_words(self, sentence):
#         words = sentence.lower().split()
#         duplicates = []
#         #Write your code here
#         for i in range(0, len(words)-1):
#             if(words[i] == words[i+1]):
#                 duplicates.append(words[i])
       
#         return duplicates



'Problem 4:'
# class Solution:
#     def unique_products(self, products):
#         result = []
#         d = {}
#         #Write your code here
#         for i in products:
#             if i in d:
#                 d[i] += 1;
#             else:
#                 d[i] = 1
#         for i in products:
#             if d[i] == 1:
#                 result.append(i)

#         return result