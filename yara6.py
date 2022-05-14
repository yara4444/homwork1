import json
q1="""x+y=? :
a.9
b.10"""
q2="""x-y=? :
a.1
b.-1"""
q3="""x+z=? :
a.9
b.10"""
q4="""x+y+z=? :
a.14
b.10"""
q5="""z+y-x=? :
a.9
b.7"""
q6="""x*y=? :
a.9
b.20"""
q7="""y//x=? :
a.1
b.10"""
q8="""x*x*y? :
a.80
b.10"""
q9="""y*y*x? :
a.1
b.100"""
q10="""z*z*x? :
a.144
b.10"""
q11="""z-y-x? :
a.-3
b.10"""
q12="""z-x? :
a.2
b.10"""
q13="""z*y/x ? :
a.7.5
b.10"""
q14="""x*z/y? :
a.1
b.3.34"""
q15="""y*y-x*x? :
a.9
b.10"""
q16="""x*x+z*y ? :
a.46
b.10"""
q17="""y*z-2x? :
a.22
b.10"""
q18="""2x+2z-y? :
a.1
b.10"""
q19="""3x-z*y? :
a.30
b.10"""
q20="""z-4y+6x? :
a.1
b.10"""
dic = {q1:"a",q2:"b",q3:"b",q4:"a",q5:"b",q6:"b",q7:"a",q8:"a",q9:"b",q10:"a",
q11:"a",q12:"a",q13:"a",q14:"b",q15:"a",q16:"a",q17:"a",q18:"b",q19:"a",q20:"b"}
q=json.dumps(dic)
with open("q.json","w")as f:
    f.write(q)
