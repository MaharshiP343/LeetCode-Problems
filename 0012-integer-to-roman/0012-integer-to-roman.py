class Solution:
    def intToRoman(self, num: int) -> str:
        out = ""
        n =num
        m = num%1000
        
        if n//1000 > 0 :
            out +=( (num //1000)*"M")
            n -=  (num //1000)*1000

        if n//900>0 :
            out+="CM"
            n -= 900
        #print(m , out, n)

        if n//500 > 0:
            out +=  "D"
            n -=500
       # print(n)
        if n//400 > 0:
            out += "CD"
            n-= 400
        
        if n//100>0:
            out += (n//100)*"C"
            n-= (n//100)*100

        if n//90 > 0 :
            out += "XC"
            n-= 90
        
        if n//50>0:
            out += "L"
            n-= 50
        
        if n//40 > 0 :
            out += "XL"
            n-= 40
        
        if n//10>0:
            out += (n//10)*"X"
            n-= (n//10)*10
        #return out


        if n//9 > 0 :
            out += "IX"
            n-= 9
        
        if n//5>0:
            out += "V"
            n-= 5
        
        if n//4> 0 :
            out += "IV"
            n-= 4
        
        if n//1>0:
            out += n*"I"
            n-= (n)*1

        return out
