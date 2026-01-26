# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tnikitin <tnikitin@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/26 16:49:19 by tnikitin          #+#    #+#              #
#    Updated: 2026/01/26 16:49:19 by tnikitin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
	age = int(input("Enter the plant's age in days: "))
	if age < 60:
		print("Plant needs more time to grow.") 
	else:
		print("Plant is ready for harvest.")