1.# Description - Create a small command-line program in Python to calculate the total invoice amount for the below purchases - 
# Book - Introduction to Python Programming : Rs 499.00
# Book - Python Libraries Cookbook : Rs. 855.00
# Book - Data Science in Python : Rs. 645.00
# Taxes and additional charges are described as details - 
# GST : 12%
# Delivery Charges : Rs. 250.00

book1=int(input("Enter quantity for Introduction to Python Programming book: "));
book2 = int(input("Enter quantity for Python Libraries Cookbook book: "));
book3 = int(input("Enter quantity for Data Science in Python book: "));
b1_price=book1*499.0;
b2_price=book2*855.0;
b3_price=book3*645.0;
total = b1_price+b2_price+b3_price;
include_gst =(total) * (12/100);
del_charge=250;
total_price =total + include_gst+ del_charge;
print("Total :", total)
print("GST (12%) :",include_gst);
print("Delivery Charges : Rs. 250");
print("Total Price: ",total_price);


2.# Description: Write a program in Python to print the number of unique letters in a string. Only new letters from the string should be counted and not duplicates.

str_input=input("Enter string1 : ");
str1_lowercase=str_input.lower();
uniqueLetters=""
for each in str1_lowercase:
    if each not in uniqueLetters:
        uniqueLetters =uniqueLetters+each;
print("uniqueLetters: ",end="")
print(",".join(uniqueLetters))
