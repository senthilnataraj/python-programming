#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      loges
#
# Created:     20/03/2018
# Copyright:   (c) loges 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    i=(int(input()))
    i=(float(input()))
    if(1<=i<=100000):
        print('positive value')
    elif(i==0):
        print('value is zero')
    else:
        print('negative value')


if __name__ == '__main__':
    main()
