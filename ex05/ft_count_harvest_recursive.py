# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tnikitin <tnikitin@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/26 17:08:25 by tnikitin          #+#    #+#              #
#    Updated: 2026/01/26 17:08:25 by tnikitin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(day=1, days=None):
    if days is None:
        days = int(input("Days until harvest: "))
    if day > days:
        print("Harvest time!")
        return
    print("Day", day)
    ft_count_harvest_recursive(day + 1, days)