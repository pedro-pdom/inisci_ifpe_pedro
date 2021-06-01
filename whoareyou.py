#simple who.is script to indentify the organizations that own the email domains on the dataset
#the dataset does not give me an exact number of organizations involved, so maybe this will give me a more accurate answer
import whois
w = whois.query('pythonforbeginners.com')

print(w.__dict__)