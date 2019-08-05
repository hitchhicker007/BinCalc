#Binary Calculator script..made by Hitch_Hicker

import os

#Code for convert float decimal to binary..
def float_bin(number):
   whole, dec = str(number).split(".")

   whole = int(whole)
   dec = int(dec)

   res = bin(whole).lstrip("0b") + "."

   for x in range(4):
      whole, dec = str((decimal_converter(dec)) * 2).split(".")  #function call of decimal_converter()..
      dec = int(dec)
      res += whole
   return res


def decimal_converter(num):
   while num > 1:
      num /= 10
   return num

#Code for check whether the number is float or integer..
def check(num):
   if "." in num:
      print("   \033[91mPlease Enter Real Number! :(")
      return False
   else:
      return True

def main():
   print("""\033[1m\033[93m
     _   _ _ _       _       _   _ _      _
    | | | (_) |_ ___| |__   | | | (_) ___| | _____ _ __
    \033[1m\033[92m| |_| | | __/ __| '_ \  | |_| | |/ __| |/ / _ \ '__|
    |  _  | | || (__| | | | |  _  | | (__|   <  __/ |
    \033[1m\033[94m|_| |_|_|\__\___|_| |_| |_| |_|_|\___|_|\_\___|_|   """)

   print("""
      \033[42m\033[1;30m===================Binery Calculator===================\033[0;m
   \033[0;m
   1. Binary Addition:   
   2. Binary Subtraction:     
   3. Binary Multiplication: 
   4. Binary Division:
   5. Convert Decimal to Binary:
   6. Convert Binary to Decimal :  
   7. Exit  """)

   #Code for user input..
   while True:
      try:
         a = int(input("   \33[104mPlease enter your choice [1-7]:\033[1;0m "))
         break
      except:
         continue

   yes = ["yes","y","Y","YES"]

   #Code for addition..
   if(a==1):
      while True:
         try:
            b = input("\n\033[1;33m   ENTER Binary NO.1 =>\033[1;0m")
            if check(b) is True:
               b=int(b,2)
               break
         except:
            continue

      while True:
         try:
            c = input("\n\033[1;33m   ENTER Binary NO.2 =>\033[1;0m")
            if check(c) is True:
               c=int(c,2)
               break
         except:
            continue

      ans = int(b) + int(c)
      print('\n\033[1m\033[95m   Answer(binary)  : '+bin(b).lstrip("0b")+" + "+bin(c).lstrip("0b")+" = " +bin(ans).lstrip("0b"))
      print('\033[1m\033[95m   Answer(Decimal)  : ',b," + ",c," = ",ans)

   #Code for subtraction..
   elif(a==2):
      while True:
         try:
            b = input("\n\033[1;33m   ENTER Binary NO.1 =>\033[1;0m")
            if check(b) is True:
               b = int(b, 2)
               break
         except:
            continue

      while True:
         try:
            c = input("\n\033[1;33m   ENTER Binary NO.2 =>\033[1;0m")
            if check(c) is True:
               c = int(c, 2)
               break
         except:
            continue

      ans = int(b) - int(c)
      print('\n\033[1m\033[95m   Answer(binary)  : ' + bin(b).lstrip("0b") + " - " + bin(c).lstrip("0b") + " = " + bin(
         ans).lstrip("0b"))
      print('\033[1m\033[95m   Answer(Decimal)  : ', b, " - ", c, " = ", ans)

   #Code for multiplication..
   elif(a==3):
      while True:
         try:
            b = input("\n\033[1;33m   ENTER Binary NO.1 =>\033[1;0m")
            if check(b) is True:
               b=int(b,2)
               break
         except:
            continue

      while True:
         try:
            c = input("\n\033[1;33m   ENTER Binary NO.2 =>\033[1;0m")
            if check(c) is True:
               c=int(c,2)
               break
         except:
            continue

      ans = int(b) * int(c)
      print('\n\033[1m\033[95m   Answer(binary)  : '+bin(b).lstrip("0b")+" * "+bin(c).lstrip("0b")+" = " +bin(ans).lstrip("0b"))
      print('\033[1m\033[95m   Answer(Decimal)  : ',b," * ",c," = ",ans)

   #Code for division..
   elif(a==4):
      while True:
         try:
            b = input("\n\033[1;33m   ENTER Binary NO.1 =>\033[1;0m")
            if check(b) is True:
               b=int(b,2)
               break
         except:
            continue

      while True:
         try:
            c = input("\n\033[1;33m   ENTER Binary NO.2 =>\033[1;0m")
            if check(c) is True:
               c=int(c,2)
               break
         except:
            continue

      ans = int(b) // int(c)
      print('\n\033[1m\033[95m   Answer(binary)  : '+bin(b).lstrip("0b")+" / "+bin(c).lstrip("0b")+" = " +bin(ans).lstrip("0b"))
      print('\033[1m\033[95m   Answer(Decimal)  : ',b," / ",c," = ",ans)

   #Code for Convert Decimal to Binary..
   elif(a==5):
      b=input("\n\033[1;33m   ENTER Decimal INPUT =>\033[1;0m")

      print('\n\033[1m\033[95m   Binary Form  : ' + bin(b))

   #Code for Convert Binary to Decimal..
   elif(a==6):
      n = input("\n\033[1;33m   ENTER Decimal INPUT =>\033[1;0m")
      if "." in n:
         print('\n\033[1m\033[95m   Binary Form  : ' + float_bin(n))
      else:
         print('\n\033[1m\033[95m   Binary Form  : ' + bin(int(n)).lstrip("0b"))

   #Code for Exit..
   elif(a==7):
      print("\033[42m\033[1;30m		Bye Bye! :)\033[1;0m")
      exit()

   #Code for wrong input..
   else:
       print("   \033[91mYou entered wrong choice! :(")

   #Code for re-run the script..
   restart = input("   \033[93mDO YOU WANT TO START AGAIN (y or n) : ")

   if restart in yes:
      os.system('clear')
      main()
   else:
      print("\033[42m\033[1;30m		Bye Bye! :)\033[1;0m")
      exit()

main()
