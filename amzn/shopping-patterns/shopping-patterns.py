"""
Amazon is trying to understand customer shopping patterns and offer items that are regularly bought together to new customers. Each item that has been bought together can be represented as an undirected graph where edges join often bundled products. A group of n products is uniquely numbered from 1 of product_nodes. A trio is defined as a group of three related products that all connected by an edge. Trios are scored by counting the number of related products outside of the trio, this is referred as a product sum.

Given product relation data, determine the minimum product sum for all trios of related products in the group. If no such trio exists, return -1.

Example
products_nodes = 6
products_edges = 6
products_from = [1,2,2,3,4,5]
products_to = [2,4,5,5,5,6]

Product	Related Products
1	| 2
2	| 1, 4, 5
3	| 5
4	| 2, 5
5	| 2, 3, 4, 6
6	| 5
A graph of n = 6 products where the only trio of related products is (2, 4, 5).

The product scores based on the graph above are:

Product	Outside Products	Which Products Are Outside
2	1	1
4	0	 
5	2	3, 6
In the diagram above, the total product score is 1 + 0 + 2 = 3 for the trio (2, 4, 5).
"""