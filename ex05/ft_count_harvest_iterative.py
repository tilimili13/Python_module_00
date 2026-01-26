# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tnikitin <tnikitin@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/26 17:00:03 by tnikitin          #+#    #+#              #
#    Updated: 2026/01/26 17:00:03 by tnikitin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
	days = int(input("Days until harvest: "))
	i = 1
	while i <= days:
		print("Day", i)
		i += 1
	print("Harvest time!")